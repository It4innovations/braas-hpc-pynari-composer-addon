# -----------------------------------------------------------------------------
# BVTK Node Tree Core Classes
# Based on BVTK by Simon Boden
# Modified by Timo Keskitalo
# References:
#   https://github.com/simboden/BVtkNodes
#   https://github.com/tkeskita/BVtkNodes
# -----------------------------------------------------------------------------
# Modified by Milan Jaros, IT4Innovations, 2025-2026

import logging

l = logging.getLogger(__name__)

import bpy
from bpy.types import NodeTree, Node, NodeSocket
from nodeitems_utils import NodeCategory, NodeItem
import nodeitems_utils
import os
import vtk
import functools  # for decorators

from math import nan

# from . import b_properties  # Boolean properties

# b_path = b_properties.__file__  # Boolean properties config file path
# from .cache import BVTKCache

ENUM_ICON = "DOT"  # Default icon for enumeration lists
debug_mode = False  # Set true to see more information in nodes

# -----------------------------------------------------------------------------
# PBVTK_NodeTree
# -----------------------------------------------------------------------------


# class PBVTK_NodeTree(NodeTree):
#     """PBVTK Node Tree"""

#     bl_idname = "PYNARIComposerNodeTree"
#     bl_label = "PBVTK Node Tree"
#     bl_icon = "COLOR_BLUE"


# -----------------------------------------------------------------------------
# Custom socket type
# -----------------------------------------------------------------------------


class PBVTK_NodeSocket(NodeSocket):
    """PBVTK Node Socket"""

    bl_idname = "PBVTK_NodeSocketType"
    bl_label = "PBVTK Node Socket"

    def is_valid_color(self, r, g, b, a):
        for l in self.links:
            if l.from_socket.bl_idname != l.to_socket.bl_idname:
                return (1.0, 0.0, 0.0, 1.0)
            
        return (r, g, b, a)    

    def draw(self, context, layout, node, txt):
        layout.label(text=txt)

    def draw_color(self, context, node):
        return self.is_valid_color(0.4, 1.0, 0.216, 1.0)    

# -----------------------------------------------------------------------------
# Custom Code decorators
# -----------------------------------------------------------------------------


# def show_custom_code(func):
#     """Decorator to show custom code in nodes. Used in draw_buttons()."""

#     @functools.wraps(func)
#     def show_custom_code_wrapper(self, context, layout):
#         # Call function first
#         value = func(self, context, layout)
#         # Then show Custom Code
#         row = layout.row()
#         if self.expanded:
#             row.label(text="Custom Code:")
#         elif len(self.custom_code) > 0:
#             pseudo_code = self.custom_code[: self.custom_code.find("(")]
#             row.label(text="Custom Code: " + pseudo_code + "...")
#         else:
#             row.label(text="Custom Code: None")
#         # Expand button
#         # TODO: Make proper expandable menu with triangle icon and text
#         row.prop(
#             self,
#             "expanded",
#             icon="HIDE_OFF" if self.expanded else "HIDE_ON",
#             icon_only=True,
#             emboss=False,
#             expand=True,
#         )

#         if self.expanded:
#             col = layout.column(align=True)
#             row = col.row()
#             # Only show edit and save buttons in node if cache is up-to-date,
#             # otherwise get_tree() fails for the operator.
#             if self.get_vtk_obj():
#                 op = row.operator(
#                     "node.bvtk_custom_code_edit", text="Edit", icon="TEXT"
#                 )
#                 op.node_id = self.node_id  # Set node id in operator
#                 op = row.operator(
#                     "node.bvtk_custom_code_save", text="Save", icon="FILE_TICK"
#                 )
#                 op.node_id = self.node_id  # Set node id in operator
#             if len(self.custom_code) > 0:
#                 box = layout.box()
#                 col = box.column()
#                 for text in self.custom_code.splitlines():
#                     row = col.row()
#                     row.label(text=text)
#         return value

#     return show_custom_code_wrapper


# def run_custom_code(func):
#     """Decorator to run custom code. Used in apply_properties()."""

#     @functools.wraps(func)
#     def run_custom_code_wrapper(self):
#         # Run optional validation routine, which can update values in
#         # node before running the actual function.
#         if hasattr(self, "validate_and_update_values_special"):
#             value = self.validate_and_update_values_special()
#             if value:
#                 self.ui_message = value
#                 return "error"

#         # Call the actual function
#         value = func(self)

#         # Then run Custom Code
#         vtk_obj = self.get_vtk_obj()
#         if vtk_obj and len(self.custom_code) > 0:
#             for x in self.custom_code.splitlines():
#                 if x.startswith("#"):
#                     continue
#                 cmd = "vtk_obj." + x
#                 l.debug("%s run %r" % (self.name, cmd))
#                 # TODO: Error handling
#                 exec(cmd, globals(), locals())

#         # Call custom apply function if such is specified (special
#         # node). Otherwise call Update(), but only if setting of
#         # properties was succesful.
#         if hasattr(self, "apply_properties_special"):
#             value = self.apply_properties_special()
#         else:
#             if hasattr(vtk_obj, "Update") and value == "up-to-date":
#                 try:
#                     vtk_obj.Update()
#                 except:
#                     self.ui_message = "Failed to run Update() for VTK object"
#                     value = "error"
#         return value

#     return run_custom_code_wrapper


# -----------------------------------------------------------------------------
# base class for all PBVTK_Nodes
#
# General implementation for VTK nodes below. Special nodes may
# need to provide own versions of following methods:
# - m_properties() - names of node properties
# - m_connections() - names of node connections
# - init_special() - special function to run when node is created
# - draw_buttons_special() - special node UI contents
# - init_vtk() - creation and initialization of VTK object
# - apply_inputs() - update input connections to VTK object
# - validate_and_update_values_special() - optional node value
#       validation and update routine
# - apply_properties_special() - special function to run for setting
#       properties and update VTK object for special nodes
# - get_vtk_output_object_special() - special function to provide
#       VTK output object for special nodes
# -----------------------------------------------------------------------------


class PBVTK_Node:
    """Base class for VTK nodes and special nodes"""

    node_id: bpy.props.IntProperty(
        name="Node ID Number",
        description="Node ID Number for mapping VTK objects in PBVTKCache",
        default=0,
    ) # type: ignore
    connected_input_names: bpy.props.StringProperty(
        name="Names of Connected Input Nodes",
        description="Names of connected input nodes, used for triggering status change in update()",
        default="",
    ) # type: ignore
    # ui_message: bpy.props.StringProperty(
    #     name="Result Message",
    #     description="Latest Result Message from Node Update, Information for User",
    #     default="",
    # ) # type: ignore
    # vtk_status: bpy.props.EnumProperty(
    #     name="VTK Status",
    #     description="Status of PBVTK node",
    #     items={
    #         # No status information. This should never be a state for
    #         # nodes that are initialized and work correctly.
    #         ("none", "none", "none", 0),
    #         # VTK object exists but no values / commands for it has been run yet.
    #         # This is state reserved for a possible future where running only
    #         # initialization without updating is required.
    #         ("initialized", "initialized", "initialized", 1),
    #         # Setting a value/running a command has failed, execution has been stopped
    #         ("error", "error", "error", 2),
    #         # A change has been made to an upstream node, may need to update
    #         ("upstream-changed", "upstream-changed", "upstream-changed", 3),
    #         # A change has been made to this node, may need to run update
    #         ("out-of-date", "out-of-date", "out-of-date", 4),
    #         # Input node(s) are running an update.
    #         # Reserved for modal operators that visualize node tree updates.
    #         ("waiting-for-upstream", "waiting-for-upstream", "waiting-for-upstream", 5),
    #         # Setting values / running commands for this node
    #         ("updating", "updating", "updating", 6),
    #         # Successfully finished running update commands for this node
    #         ("up-to-date", "up-to-date", "up-to-date", 7),
    #     },
    #     default="none",
    # ) # type: ignore
    # custom_code: bpy.props.StringProperty(
    #     name="Custom Code",
    #     description="Custom Python Code to Run for This Node's VTK Object",
    #     default="",
    #     maxlen=0,
    # ) # type: ignore
    # expanded: bpy.props.BoolProperty(
    #     name="Show Code",
    #     description="Boolean to Show/Hide Custom Code Panel",
    #     default=False,
    # ) # type: ignore

    @classmethod
    def poll(cls, ntree):
        return ntree.bl_idname == "PYNARIComposerNodeTree"
    
    def get_var_name(self, postfix=""):
        """Get the variable name for this node's output.
        This follows the pattern used in PYNARIComposerNode.
        """
        from .. import utility
        if len(postfix) > 0:
            return f"{utility.str_to_var_name(self.name)}_{utility.str_to_var_name(postfix)}"
        
        return utility.str_to_var_name(self.name)
    
    def generate_code(self, auto_gen_enabled=False):
        """Generate Python code for this node.
        This method should be overridden in child classes.
        Returns a list of code lines (strings).
        
        Default implementation generates basic VTK object creation and property setting.
        """
        code = []
        code.append(f"# Label: {self.label if hasattr(self, 'label') and self.label else self.name}")
        
        var_name = self.get_var_name()
        vtk_class_name = self.bl_label if hasattr(self, 'bl_label') else self.__class__.__name__
        
        # Create VTK object
        code.append(f"# VTK Node: {vtk_class_name}")
        if not auto_gen_enabled:
            # code.append(f"import vtk")
            code.append(f"{var_name} = vtk.{vtk_class_name}()")
        
        # Set input connections
        if hasattr(self, 'm_connections'):
            inputs, outputs, extra_inputs, extra_outputs = self.m_connections()
            for i, input_socket_name in enumerate(inputs):
                input_node, from_socket_name = self.get_input_node_and_socketname(input_socket_name)
                if input_node:
                    input_var_name = input_node.get_var_name()
                    code.append(f"{var_name}.SetInputConnection({input_var_name}.GetOutputPort())")
        
        # Set properties from m_properties
        if hasattr(self, 'm_properties') and hasattr(self, 'b_properties'):
            m_properties = self.m_properties()
            for i, prop_name in enumerate(m_properties):
                # Only process visible properties
                if self.b_properties[i]:
                    inputval = getattr(self, prop_name, None)
                    if inputval is None or len(str(inputval)) == 0:
                        continue
                    
                    # SetXFileName(Y) only if attribute is a string
                    if "FileName" in prop_name and isinstance(inputval, str):
                        value = os.path.realpath(bpy.path.abspath(inputval))
                        code.append(f"{var_name}.Set{prop_name[2:]}(r'{value}')")
                    # SetXToY()
                    elif prop_name.startswith("e_"):
                        code.append(f"{var_name}.Set{prop_name[2:]}To{inputval}()")
                    # SetX(value)
                    else:
                        # Convert Blender property arrays to lists
                        if hasattr(inputval, '__len__') and not isinstance(inputval, str):
                            try:
                                inputval = list(inputval)
                            except:
                                pass
                        # Get the property value
                        code.append(f"{var_name}.Set{prop_name[2:]}({repr(inputval)})")
        
        # Add custom code if present
        if hasattr(self, 'custom_code') and len(self.custom_code) > 0:
            code.append(f"# Custom Code")
            for line in self.custom_code.splitlines():
                if not line.startswith("#"):
                    code.append(f"{var_name}.{line}")
        
        # Call Update() if available and not in auto-gen mode
        #if not auto_gen_enabled:
        code.append(f"{var_name}.Update()")
        
        return code
    
    def auto_generate_node_code(self, context):
        """Callback to auto-generate code when properties change"""
        # Get the node tree
        if not hasattr(self, 'id_data'):
            return
        
        tree = self.id_data
        if not tree or not hasattr(tree, 'auto_generate_code'):
            return
        
        # Only proceed if auto-generate is enabled and this node is active
        if not tree.auto_generate_code:
            return
        
        # Check if this node is the active node in any node editor
        for area in context.screen.areas:
            if area.type == 'NODE_EDITOR':
                for space in area.spaces:
                    if space.type == 'NODE_EDITOR' and space.tree_type == 'PYNARIComposerNodeTree':
                        if space.edit_tree == tree and space.edit_tree.nodes.active == self:
                            node = self

                            # Generate code for the selected node
                            code_lines = []
                            # code_lines.append("import pynari")
                            # code_lines.append("")
                            code_lines.append(f"# Code for node: {node.name} ({node.bl_idname})")
                            code_lines.append("")
                            
                            try:
                                node_code = node.generate_code(auto_gen_enabled=True)
                                code_lines.extend(node_code)
                            except Exception as e:
                                self.report({'ERROR'}, f"Error generating code: {str(e)}")
                                return {'CANCELLED'}
                            
                            code = "\n".join(code_lines)
                            
                            # Create or get text block
                            text_name = f"{tree.name}_code_node.py"
                            if text_name in bpy.data.texts:
                                text = bpy.data.texts[text_name]
                                text.clear()
                            else:
                                text = bpy.data.texts.new(text_name)
                            
                            text.write(code)                            

                            return    

    def m_properties(self):
        """Return list of node specific property names.
        Implement this for each node class.
        """
        return []

    def m_connections(self):
        """Return lists of node specific connection names:
        input socket names, output socket names, extra inputs, and extra outputs.
        Implement this for each node class.
        """
        return ([], [], [], [])

    # def get_input_socket_names(self):
    #     """Return input socket names from m_connections.
    #     """
    #     m_connections = self.m_connections()
    #     return m_connections[0]

    # def get_output_socket_names(self):
    #     """Return output socket names from m_connections.
    #     """
    #     m_connections = self.m_connections()
    #     return m_connections[1]

    def init(self, context):
        """Create and initialize a new PBVTK node.
        """
        # Node properties
        self.width = 200
        # self.use_custom_color = True
        # self.color = 0.5, 0.5, 0.5

        # Create sockets to node
        inputs, outputs, extra_inputs, extra_outputs = self.m_connections()
        inputs.extend(extra_inputs)
        outputs.extend(extra_outputs)
        for x in inputs:
            self.inputs.new("PBVTK_NodeSocketType", x)
        for x in outputs:
            self.outputs.new("PBVTK_NodeSocketType", x)

        # if hasattr(self, "init_special"):
        #     self.init_special(context)

    # def set_vtk_status(self, new_status="none"):
    #     """Set node's VTK status to new status value and change node color.
    #     Note: Does not trigger any updates.
    #     """

    #     def status_to_color(vtk_status="none"):
    #         """Return color for argument VTK status"""
    #         colors = {
    #             "none": (0.1, 0.1, 0.1),
    #             "initialized": (0.5, 0.5, 0.5),
    #             "error": (0.6, 0.1, 0.1),
    #             "upstream-changed": (0.6, 0.5, 0),
    #             "out-of-date": (0.3, 0.5, 0.1),
    #             "waiting-for-upstream": (0.1, 0.6, 0.6),
    #             "updating": (0.1, 0.1, 0.6),
    #             "up-to-date": (0.3, 0.3, 0.3),
    #         }
    #         return colors[vtk_status]

    #     self.vtk_status = new_status
    #     self.color = status_to_color(new_status)

    # def init_vtk(self):
    #     """Initialize and return a VTK object for the node.
    #     This is a general implementation for VTK nodes.
    #     Special nodes need to implement their own initialization.
    #     If special node has no VTK objects, it's OK to return None.
    #     """
    #     vtk_class = getattr(vtk, self.bl_label, None)
    #     if vtk_class is None:
    #         raise Exception("Bad VTK class name " + self.bl_label)
    #     vtk_obj = vtk_class()
    #     if not vtk_obj:
    #         raise Exception("Could not create " + self.bl_label)
    #     self.set_vtk_status("initialized")
    #     l.debug("Init VTK done for node: %s, id #%d" % (self.name, self.node_id))
    #     return vtk_obj

    # def free(self):
    #     """Clean up node information upon node removal.
    #     """
    #     # PBVTKCache removed - no cleanup needed
    #     pass

    # @show_custom_code
    def draw_buttons(self, context, layout):
        """Show properties in the node. General implementation for both VTK
        and special nodes. Special nodes may provide draw_buttons_special()
        to show custom content in node.
        """

        # # Show node ID number and status in debug mode
        # global debug_mode
        # if debug_mode:
        #     row = layout.row()
        #     row.label(text="node_id #%d: %r" % (self.node_id, str(self.vtk_status)))

        # # Show message if any
        # if len(self.ui_message) > 0:
        #     box = layout.box()
        #     for line in self.ui_message.split("\n"):
        #         row = box.row()
        #         row.label(text=line)

        # Main content
        if hasattr(self, "draw_buttons_special"):
            self.draw_buttons_special(context, layout)
        else:
            # Get properties and show visible ones
            m_properties = self.m_properties()
            for i in range(len(m_properties)):
                if not hasattr(self, "b_properties") or self.b_properties[i]:
                    layout.prop(self, m_properties[i])

        #     # Write button for writer nodes
        #     if self.bl_idname.endswith("WriterType"):
        #         layout.operator("node.bvtk_node_write").node_path = node_path(self)

        # # Update button is shown when there is something to update
        # if self.vtk_status != "up-to-date":
        #     row = layout.row()
        #     row.operator("node.bvtk_node_update").node_path = node_path(self)

        # pass

    # @run_custom_code
    # def apply_properties(self):
    #     """Set properties from node to VTK object, and update the VTK object.
    #     Return appropriate vtk_status according to success of update.
    #     General implementation for both VTK and special nodes.
    #     """

    #     # Do nothing if inputs are not connected
    #     namelist = [
    #         link.to_socket.name for socket in self.inputs for link in socket.links
    #     ]
    #     missing_inputs = ""
    #     for input in self.get_input_socket_names():
    #         # Only require connections named "VTK Input" are connected
    #         if not input.startswith("VTK Input"):
    #             continue
    #         if input not in namelist:
    #             missing_inputs += input + " "
    #     if len(missing_inputs) > 0:
    #         self.ui_message = "Missing input connection(s): " + missing_inputs
    #         return "error"

    #     # Stop here if there is a custom apply routine, meaning this is a special node
    #     if hasattr(self, "apply_properties_special"):
    #         return "up-to-date"

    #     # Require an object exists in cache
    #     vtk_obj = self.get_vtk_obj()
    #     if not vtk_obj:
    #         self.ui_message = "Internal Error: No VTK object found in cache"
    #         return "error"

    #     m_properties = self.m_properties()
    #     for x in [
    #         m_properties[i] for i in range(len(m_properties)) if self.b_properties[i]
    #     ]:
    #         # Skip setting any empty values
    #         inputval = getattr(self, x)
    #         if len(str(inputval)) == 0:
    #             continue
    #         # SetXFileName(Y) only if attribute is a string
    #         if "FileName" in x and isinstance(inputval, str):
    #             value = os.path.realpath(bpy.path.abspath(inputval))
    #             cmd = "vtk_obj.Set" + x[2:] + "(value)"
    #         # SetXToY()
    #         elif x.startswith("e_"):
    #             cmd = "vtk_obj.Set" + x[2:] + "To" + inputval + "()"
    #         # SetX(self.Y)
    #         else:
    #             cmd = "vtk_obj.Set" + x[2:] + "(self." + x + ")"

    #         # Run the command and stop if error occurs
    #         try:
    #             exec(cmd, globals(), locals())
    #         except:
    #             # TODO: How to get error message and put it to ui_message?
    #             self.ui_message = "Error when running: " + cmd
    #             return "error"

    #     # Everything was set successfully
    #     return "up-to-date"

    # def get_vtk_obj(self):
    #     """Return the VTK object of this node from cache.
    #     """
    #     # PBVTKCache removed - return None
    #     return None

    # def vtk_obj_in_cache(self):
    #     """Return True if an object (or None) is in cache.
    #     True means that node has been initialized correctly.
    #     """
    #     # PBVTKCache removed - return False
    #     return False

    # def get_output_connection(self, socketname="VTK Output"):
    #     """Return VTK output connection object for argument output socket name
    #     of this node. Return None if no connection is provided.
    #     """

    #     # VTK Nodes are derived from vtkAlgorithm, which implements VTK connections
    #     vtk_obj = self.get_vtk_obj()
    #     if not isinstance(vtk_obj, vtk.vtkAlgorithm):
    #         return None
    #     if socketname == "VTK Output" or socketname == "output 0":
    #         return vtk_obj.GetOutputPort()
    #     elif socketname == "output 1":
    #         return vtk_obj.GetOutputPort(1)
    #     else:
    #         raise Exception(
    #             "Not implemented connection for #"
    #             + str(self.node_id)
    #             + ": "
    #             + socketname
    #         )

    # def get_vtk_output_object(self, socketname="VTK Output"):
    #     """Return VTK output data object for argument output socket name of
    #     this node.
    #     """

    #     # Special nodes may provide custom function
    #     if hasattr(self, "get_vtk_output_object_special"):
    #         return self.get_vtk_output_object_special(socketname)

    #     # Normal VTK algorithm provides output data object via producer
    #     vtk_connection = self.get_output_connection(socketname)
    #     if hasattr(vtk_connection, "IsA") and vtk_connection.IsA("vtkAlgorithmOutput"):
    #         producer = vtk_connection.GetProducer()
    #         return producer.GetOutputDataObject(vtk_connection.GetIndex())

    #     # Final option is to return node's cached VTK object (may be None)
    #     return self.get_vtk_obj()

    # def get_vtk_output_obj_and_connection(self, socketname="VTK Output"):
    #     """Return both the output VTK data object and VTK connection for the
    #     argument output socket name of this node.
    #     """
    #     vtk_output_obj = self.get_vtk_output_object(socketname)
    #     vtk_connection = self.get_output_connection(socketname)
    #     return vtk_output_obj, vtk_connection

    # def apply_inputs(self):
    #     """Set/update node input connections to this node's VTK object.
    #     This is called from update_vtk() during update.
    #     General implementation for VTK nodes.
    #     """
    #     inputs, dummy1, extra_inputs, dummy2 = self.m_connections()
    #     vtk_obj = self.get_vtk_obj()
    #     if not vtk_obj:
    #         return None

    #     # Normal connections
    #     for i, socketname in enumerate(inputs):
    #         (
    #             input_node,
    #             vtk_output_obj,
    #             vtk_connection,
    #         ) = self.get_input_node_and_output_vtk_objects(socketname)
    #         # Remove unconnected connection
    #         if not input_node and hasattr(vtk_obj, "RemoveInputConnection"):
    #             vtk_obj.RemoveInputConnection(i, i)
    #             continue

    #         # Normal vtkAlgorithms use SetInputConnection
    #         if vtk_connection and vtk_connection.IsA("vtkAlgorithmOutput"):
    #             vtk_obj.SetInputConnection(i, vtk_connection)

    #         # Special nodes can provide a VTK data object as output
    #         elif hasattr(vtk_output_obj, "IsA") and vtk_output_obj.IsA("vtkDataObject"):
    #             vtk_obj.SetInputData(i, vtk_output_obj)

    #     # Extra connections (call method SetX(vtk_output_obj) for vtk_obj)
    #     # See e.g. vtkClipPolyData in the clip example tree.
    #     for socketname in extra_inputs:
    #         (
    #             input_node,
    #             vtk_output_obj,
    #             dummy,
    #         ) = self.get_input_node_and_output_vtk_objects(socketname)
    #         if not input_node:
    #             continue
    #         if not vtk_output_obj:
    #             raise Exception("Failed to get output from" + socketname)
    #         cmd = "vtk_obj.Set" + socketname + "(vtk_output_obj)"
    #         # TODO: Error handling
    #         exec(cmd, globals(), locals())

    # def get_input_node_and_output_vtk_objects(self, input_socket_name="VTK Input"):
    #     """Return input node, VTK output object it produces, and the VTK
    #     output connection of the input node which is connected to this
    #     node's argument input socket name.
    #     """
    #     input_node, from_socket_name = self.get_input_node_and_socketname(
    #         input_socket_name
    #     )
    #     if not input_node:
    #         return None, None, None
    #     vtk_obj, vtk_connection = input_node.get_vtk_output_obj_and_connection(
    #         from_socket_name
    #     )
    #     return input_node, vtk_obj, vtk_connection

    def get_input_node_and_socketname(self, input_socket_name="VTK Input"):
        """Get one input node and it's output socket name using this nodes'
        input socket name.
        """
        (
            nodes,
            from_socket_names,
            to_socket_names,
        ) = self.get_input_nodes_and_socketnames()
        for node, from_socket_name, to_socket_name in zip(
            nodes, from_socket_names, to_socket_names
        ):
            if to_socket_name == input_socket_name:
                return node, from_socket_name
        return None, None

    def get_input_nodes(self):
        """Return list of all input nodes.
        """
        nodes, dummy1, dummy2 = self.get_input_nodes_and_socketnames()
        return nodes

    def get_input_nodes_and_socketnames(self):
        """Return list of all input nodes of this node, node socket names in
        this node, and node socket names in input node.
        """
        nodes = []
        from_socket_names = []
        to_socket_names = []
        # Get all input nodes
        for socket in self.inputs:
            for link in socket.links:
                nodes.append(link.from_node)
                from_socket_names.append(link.from_socket.name)
                to_socket_names.append(link.to_socket.name)
        return nodes, from_socket_names, to_socket_names

    def get_output_nodes(self):
        """Return list of all output nodes from this node.
        """
        output_nodes = []
        for socket in self.outputs:
            for link in socket.links:
                output_nodes.append(link.to_node)
        return output_nodes

    # def copy(self, node):
    #     """Copy setup from another node to self.
    #     """
    #     self.node_id = 0
    #     vtk_obj = self.init_vtk()
    #     # PBVTKCache removed - vtk_obj not cached
    #     if hasattr(self, "copy_special"):
    #         # some nodes need to set properties (such as color ramp elements)
    #         # after being copied
    #         self.copy_special(node)
    #     l.debug("Copy done for node: %s, id #%d" % (self.name, self.node_id))

    def get_b(self):
        """Get list of booleans to show/hide boolean properties.
        """
        # b_properties removed - return all True (show all properties by default)
        if hasattr(self, 'b_properties'):
            return [True] * len(self.b_properties)
        return []

    def set_b(self, value):
        """Set boolean property list and update boolean properties file.
        """
        # b_properties removed - no-op
        pass

    # def outdate_vtk_status(self, context):
    #     """Set node VTK status to out-of-date and notify downstream when a
    #     property value is changed in UI.
    #     """
    #     # PBVTKCache removed - simplified update logic
    #     l.debug(self.name + ": Setting VTK status out-of-date")
    #     self.set_vtk_status("out-of-date")
    #     self.notify_downstream(vtk_status="out-of-date")

    # def update(self):
    #     """Update routine triggered on node UI topology changes (adding or
    #     removing nodes and links).
    #     """
    #     # PBVTKCache removed - simplified update logic
    #     namelist = [
    #         link.from_node.name for socket in self.inputs for link in socket.links
    #     ]
    #     names = str(namelist)
    #     if self.connected_input_names != names:
    #         self.set_vtk_status("out-of-date")
    #         self.notify_downstream(vtk_status="out-of-date")

    # def outdate_upstream(self):
    #     """Set all upstream nodes to out-of-date status (to force update on
    #     them when they are updated next time).
    #     """
    #     for node in self.get_input_nodes():
    #         node.outdate_upstream()
    #         node.set_vtk_status("out-of-date")

    # def notify_downstream(self, vtk_status="out-of-date", origin_node=True):
    #     """Make status changes in downstream nodes, to advertise update made
    #     in this node.
    #     """
    #     # Recursively call for downstream nodes
    #     for node in self.get_output_nodes():
    #         node.notify_downstream(vtk_status="out-of-date", origin_node=False)
    #     # For downstream nodes, out-of-date supercedes upstream-changed
    #     if self.vtk_status != "out-of-date":
    #         self.set_vtk_status("upstream-changed")
    #     if origin_node:
    #         self.set_vtk_status(vtk_status)

    # def update_vtk(self):
    #     """Recursively update upstream nodes and this node if not up-to-date.
    #     """
    #     # Recursively call for upstream nodes
    #     for node in self.get_input_nodes():
    #         if node.vtk_status != "up-to-date":
    #             node.update_vtk()

    #     # Do nothing if upstream was not successfully updated
    #     for node in self.get_input_nodes():
    #         if node.vtk_status != "up-to-date":
    #             self.ui_message = "Can't update, upstream update failed."
    #             return "out-of-date"

    #     # Remove old messages
    #     self.ui_message = ""

    #     # Allocate VTK object if it doesn't exist already
    #     if not self.vtk_obj_in_cache():
    #         vtk_obj = self.init_vtk()
    #         # PBVTKCache removed - vtk_obj not cached
    #         l.debug("Init done for node: %s, id #%d" % (self.name, self.node_id))

    #     # Update this node's properties to VTK object only if needed
    #     if self.vtk_status != "up-to-date":
    #         self.set_vtk_status("updating")
    #         l.debug("Updating " + self.name)

    #         # Update VTK connections if node connections have changed
    #         namelist = [
    #             link.from_node.name for socket in self.inputs for link in socket.links
    #         ]
    #         names = str(namelist)
    #         if self.connected_input_names != names:
    #             self.connected_input_names = names
    #             self.apply_inputs()

    #         # Special nodes: Update VTK connections always, because
    #         # provided VTK data object might have changed.
    #         elif not str(self.__class__).startswith("vtk"):
    #             self.apply_inputs()

    #         # This is the only point where apply_properties() should be called
    #         new_status = self.apply_properties()

    #         if new_status not in (
    #             "none",
    #             "initialized",
    #             "error",
    #             "upstream-changed",
    #             "out-of-date",
    #             "waiting-for-upstream",
    #             "updating",
    #             "up-to-date",
    #         ):
    #             self.ui_message = "Internal error:\napply_properties() does not return a valid status string"
    #             new_status = "error"
    #         self.notify_downstream(vtk_status=new_status)


# -----------------------------------------------------------------------------
# Node Update Operators
# -----------------------------------------------------------------------------


# class PBVTK_OT_NodeUpdate(bpy.types.Operator):
#     """Node Update Operator"""

#     bl_idname = "node.bvtk_node_update"
#     bl_label = "Update Node"

#     node_path: bpy.props.StringProperty() # type: ignore

#     def execute(self, context):
#         # node = eval(self.node_path)
#         # node.update_vtk()
#         return {"FINISHED"}


# class PBVTK_OT_NodeForceUpdateUpstream(bpy.types.Operator):
#     """Force All Upstream Nodes and This Node to be Updated"""

#     bl_idname = "node.bvtk_node_force_update_upstream"
#     bl_label = "Force Update Upstream"

#     node_path: bpy.props.StringProperty() # type: ignore

#     def execute(self, context):
#         # node = eval(self.node_path)
#         # node.outdate_upstream()
#         # node.update_vtk()
#         return {"FINISHED"}


# -----------------------------------------------------------------------------
# VTK Writer Nodes' Write Operator
# -----------------------------------------------------------------------------
# class PBVTK_OT_NodeWrite(bpy.types.Operator):
#     """Operator to call VTK Write() for a writer node"""

#     bl_idname = "node.bvtk_node_write"
#     bl_label = "Write Data"

#     node_path: bpy.props.StringProperty() # type: ignore

#     def execute(self, context):
#         # node = eval(self.node_path)
#         # if node:
#         #     node.update_vtk()
#         #     node.get_vtk_obj().Write()

#         return {"FINISHED"}


# -----------------------------------------------------------------------------
# Registering
# -----------------------------------------------------------------------------

CLASSES = {}  # dictionary of classes is used to allow class overriding
UI_CLASSES = []


def add_class(obj):
    CLASSES[obj.bl_idname] = obj

def add_ui_class(obj):
    UI_CLASSES.append(obj)


# b_properties and check_b_properties removed


# Register classes
# add_class(PBVTK_NodeTree)
# add_class(PBVTK_NodeSocket)
# Operator classes commented out - not defined in this file
# add_ui_class(PBVTK_OT_NodeUpdate)
# add_ui_class(PBVTK_OT_NodeForceUpdateUpstream)
# add_ui_class(PBVTK_OT_NodeWrite)

# -----------------------------------------------------------------------------
# VTK Node Category
# -----------------------------------------------------------------------------


class PBVTK_NodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == "PYNARIComposerNodeTree"


CATEGORIES = []


# -----------------------------------------------------------------------------
# Debug utilities
# -----------------------------------------------------------------------------


# def ls(o):
#     l.debug("\n".join(sorted(dir(o))))


# def print_cls(obj):
#     l.debug("------------------------------")
#     l.debug("Class = " + obj.__class__.__name__)
#     l.debug("------------------------------")
#     for m in sorted(dir(obj)):
#         if not m.startswith("__"):
#             attr = getattr(obj, m)
#             rep = str(attr)
#             if len(rep) > 100:
#                 rep = rep[:100] + "  [...]"
#             l.debug(m.ljust(30) + "=" + rep)


# def print_nodes():
#     l.debug("maxid = " + str(NodesMaxId))
#     for nt in bpy.data.node_groups:
#         if nt.bl_idname == "PYNARIComposerNodeTree":
#             l.debug("tree " + nt.name)
#             for n in nt.nodes:
#                 if get_vtkobj(n) is None:
#                     x = ""
#                 else:
#                     x = "VTK object"
#                 l.debug("node " + str(n.node_id) + ": " + n.name.ljust(30, " ") + x)


# -----------------------------------------------------------------------------
# Useful help functions
# -----------------------------------------------------------------------------


# def update_3d_view():
#     """Force update of 3D View"""
#     return  # No need for this in Blender 2.8? Remove function when certain.
#     screen = bpy.context.screen
#     if screen:
#         for area in screen.areas:
#             if area.type == "VIEW_3D":
#                 for space in area.spaces:
#                     if space.type == "VIEW_3D":
#                         # This updates viewport in Blender 2.79, not sure why
#                         # space.viewport_shade = space.viewport_shade
#                         continue


# def node_path(node):
#     """Return node path of a node"""
#     return (
#         "bpy.data.node_groups["
#         + repr(node.id_data.name)
#         + "].nodes["
#         + repr(node.name)
#         + "]"
#     )


# def node_prop_path(node, propname):
#     """Return node property path"""
#     return node_path(node) + "." + propname


# def assert_bvtk(condition, message):
#     if not condition:
#         raise (AssertionError(message))


# def first_elements(list_of_lists):
#     """Return first elements in argument list of lists (like an enum list)
#     """
#     if not isinstance(list_of_lists, list):
#         return None
#     elem_list = [x[0] for x in list_of_lists]
#     return elem_list


# def string_to_floats(input_string: str):
#     """Return a list of floats from a comma separated text string.
#     """
#     vals = input_string.split(",")
#     floats = []
#     for val in vals:
#         try:
#             floats.append(float(val))
#         except:
#             return None
#     return floats


# def get_all_bvtk_nodes():
#     """Return list of PBVTK Nodes from all node trees/groups"""
#     bvtk_nodes = []
#     for node_group in bpy.data.node_groups:
#         if node_group.bl_idname != "PYNARIComposerNodeTree":
#             continue
#         for node in node_group.nodes:
#             bvtk_nodes.append(node)
#     return bvtk_nodes

# -----------------------------------------------------------------------------
# VTK Extended Filters
# -----------------------------------------------------------------------------
from .gen_VTKFilters1 import VTKContourFilter

class PBVTK_PG_ValueSettings(bpy.types.PropertyGroup):
    """Property Group for float array of variable size"""

    value: bpy.props.FloatProperty(default=0) # type: ignore

add_ui_class(PBVTK_PG_ValueSettings)

class VTKContourFilterExtend(VTKContourFilter):
    """Manually modified version of VTK Contour Filter"""

    m_Values: bpy.props.CollectionProperty(type=PBVTK_PG_ValueSettings) # type: ignore

    def update_values_count(self, context):
        """Update m_Values collection size based on m_NumberOfContours"""
        current_count = len(self.m_Values)
        target_count = self.m_NumberOfContours
        
        # Add items if we need more
        while len(self.m_Values) < target_count:
            self.m_Values.add()
        
        # Remove items if we have too many
        while len(self.m_Values) > target_count:
            self.m_Values.remove(len(self.m_Values) - 1)
    
    m_NumberOfContours: bpy.props.IntProperty(
        name='NumberOfContours', 
        default=1, 
        min=0,
        update=update_values_count
    ) # type: ignore

    def init(self, context):
        """Initialize node and ensure m_Values has correct size"""
        # Call parent init
        super().init(context)
        # Initialize values collection
        self.update_values_count(context)

    def draw_buttons_special(self, context, layout):

        # Get properties and show visible ones
        m_properties = self.m_properties()
        for i in range(len(m_properties)):
            if not hasattr(self, "b_properties") or self.b_properties[i]:
                layout.prop(self, m_properties[i])
        
        # Display value inputs (only if collection is properly sized)
        if self.m_NumberOfContours > 0 and len(self.m_Values) == self.m_NumberOfContours:
            box = layout.box()
            box.label(text="Contour Values:")
            for i, item in enumerate(self.m_Values):
                row = box.row(align=True)
                row.prop(item, "value", text=f"Value {i}")
        elif len(self.m_Values) != self.m_NumberOfContours:
            # Show a message if collection size doesn't match
            box = layout.box()
            box.label(text="Note: Click on another node and back to refresh values", icon='INFO')
    
    def generate_code(self, auto_gen_enabled=False):
        """Generate code for VTKContourFilter with dynamic values"""
        # Get base code from parent
        code = super().generate_code(auto_gen_enabled)
        
        var_name = self.get_var_name()
        
        # Remove the Update() call if it's at the end (we'll add it back after SetValue calls)
        if code and code[-1] == f"{var_name}.Update()":
            code.pop()
        
        # Add SetValue calls for each contour value (before Update)
        if self.m_NumberOfContours > 0 and len(self.m_Values) > 0:
            code.append(f"# Set contour values")
            for i, item in enumerate(self.m_Values):
                if i < self.m_NumberOfContours:
                    code.append(f"{var_name}.SetValue({i}, {item.value})")
        
        # Add Update() back at the end
        #if not auto_gen_enabled:
        code.append(f"{var_name}.Update()")
        
        return code

# -----------------------------------------------------------------------------
# VTK to Numpy Converter Nodes
# -----------------------------------------------------------------------------

class VTKPolyDataToNumpyNode(Node, PBVTK_Node):
    """Convert VTK PolyData to Numpy arrays"""
    bl_idname = "VTKPolyDataToNumpyType"
    bl_label = "VTK PolyData to Numpy"
    bl_icon = "MESH_DATA"

    def m_properties(self):
        return []

    def m_connections(self):
        return (["VTK Input"], [], [], [])

    def init(self, context):
        # Call parent init
        PBVTK_Node.init(self, context)
        # Add numpy output sockets
        self.outputs.new("PYNARINumpyArraySocket", "NP Vertices")
        self.outputs.new("PYNARINumpyArraySocket", "NP Indices")
        self.outputs.new("PYNARINumpyArraySocket", "NP Normals")

    def generate_code(self, auto_gen_enabled=False):
        """Generate code to convert VTK PolyData to numpy arrays"""
        code = []
        code.append(f"# Label: {self.label if hasattr(self, 'label') and self.label else self.name}")
        
        var_name = self.get_var_name()
        
        # Get input VTK object variable name
        input_node, from_socket_name = self.get_input_node_and_socketname("VTK Input")
        if not input_node:
            code.append(f"# No input connected")
            return code
        
        vtk_var = input_node.get_var_name()
        
        code.append(f"# Convert VTK PolyData to Numpy")
        # code.append(f"import numpy as np")
        # code.append(f"from vtk.util.numpy_support import vtk_to_numpy")
        # code.append(f"")
        
        # Get the output from VTK pipeline
        code.append(f"{vtk_var}.Update()")
        code.append(f"{var_name}_polydata = {vtk_var}.GetOutput()")
        code.append(f"")
        
        # Get socket variable names
        vertices_socket_varname = self.get_var_name("NP Vertices")
        indices_socket_varname = self.get_var_name("NP Indices")
        normals_socket_varname = self.get_var_name("NP Normals")
        
        # Extract vertices
        code.append(f"# Extract vertices")
        code.append(f"{vertices_socket_varname} = vtk_to_numpy({var_name}_polydata.GetPoints().GetData()).astype(np.float32)")
        code.append(f"")
        
        # Extract indices (faces)
        code.append(f"# Extract indices")
        code.append(f"{var_name}_polys = {var_name}_polydata.GetPolys()")
        code.append(f"{var_name}_polys_data = vtk_to_numpy({var_name}_polys.GetData())")
        code.append(f"# Reshape assuming triangles (n, 4) where first value is count")
        code.append(f"{indices_socket_varname} = {var_name}_polys_data.reshape(-1, 4)[:, 1:].astype(np.uint32)")
        code.append(f"")
        
        # Extract normals if available
        code.append(f"# Extract normals if available")
        code.append(f"if {var_name}_polydata.GetPointData().GetNormals():")
        code.append(f"    {normals_socket_varname} = vtk_to_numpy({var_name}_polydata.GetPointData().GetNormals()).astype(np.float32)")
        code.append(f"else:")
        code.append(f"    {normals_socket_varname} = None")
        
        return code


class VTKStructuredGridToNumpyNode(Node, PBVTK_Node):
    """Convert VTK Structured Grid to Numpy arrays"""
    bl_idname = "VTKStructuredGridToNumpyType"
    bl_label = "VTK Structured Grid to Numpy"
    bl_icon = "MESH_GRID"

    def m_properties(self):
        return []

    def m_connections(self):
        return (["VTK Input"], [], [], [])

    def init(self, context):
        PBVTK_Node.init(self, context)
        self.outputs.new("PYNARINumpyArraySocket", "NP Points")
        self.outputs.new("PYNARINumpyArraySocket", "NP Dimensions")
        self.outputs.new("PYNARINumpyArraySocket", "NP Scalars")

    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label if hasattr(self, 'label') and self.label else self.name}")
        
        var_name = self.get_var_name()
        input_node, from_socket_name = self.get_input_node_and_socketname("VTK Input")
        if not input_node:
            code.append(f"# No input connected")
            return code
        
        vtk_var = input_node.get_var_name()
        
        code.append(f"# Convert VTK Structured Grid to Numpy")
        # code.append(f"import numpy as np")
        # code.append(f"from vtk.util.numpy_support import vtk_to_numpy")
        # code.append(f"")
        
        code.append(f"{vtk_var}.Update()")
        code.append(f"{var_name}_grid = {vtk_var}.GetOutput()")
        code.append(f"")
        
        # Get socket variable names
        points_socket_varname = self.get_var_name("NP Points")
        dimensions_socket_varname = self.get_var_name("NP Dimensions")
        scalars_socket_varname = self.get_var_name("NP Scalars")
        
        # Extract points
        code.append(f"# Extract points")
        code.append(f"{points_socket_varname} = vtk_to_numpy({var_name}_grid.GetPoints().GetData()).astype(np.float32)")
        code.append(f"")
        
        # Extract dimensions
        code.append(f"# Extract dimensions")
        code.append(f"{dimensions_socket_varname} = np.array({var_name}_grid.GetDimensions(), dtype=np.int32)")
        code.append(f"")
        
        # Extract scalars if available
        code.append(f"# Extract scalars if available")
        code.append(f"if {var_name}_grid.GetPointData().GetScalars():")
        code.append(f"    {scalars_socket_varname} = vtk_to_numpy({var_name}_grid.GetPointData().GetScalars()).astype(np.float32)")
        code.append(f"else:")
        code.append(f"    {scalars_socket_varname} = None")
        
        return code


class VTKUnstructuredGridToNumpyNode(Node, PBVTK_Node):
    """Convert VTK Unstructured Grid to Numpy arrays"""
    bl_idname = "VTKUnstructuredGridToNumpyType"
    bl_label = "VTK Unstructured Grid to Numpy"
    bl_icon = "MESH_DATA"

    def m_properties(self):
        return []

    def m_connections(self):
        return (["VTK Input"], [], [], [])

    def init(self, context):
        PBVTK_Node.init(self, context)
        self.outputs.new("PYNARINumpyArraySocket", "NP Points")
        self.outputs.new("PYNARINumpyArraySocket", "NP Cells")
        self.outputs.new("PYNARINumpyArraySocket", "NP Cell Types")
        self.outputs.new("PYNARINumpyArraySocket", "NP Scalars")

    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label if hasattr(self, 'label') and self.label else self.name}")
        
        var_name = self.get_var_name()
        input_node, from_socket_name = self.get_input_node_and_socketname("VTK Input")
        if not input_node:
            code.append(f"# No input connected")
            return code
        
        vtk_var = input_node.get_var_name()
        
        code.append(f"# Convert VTK Unstructured Grid to Numpy")
        # code.append(f"import numpy as np")
        # code.append(f"from vtk.util.numpy_support import vtk_to_numpy")
        # code.append(f"")
        
        code.append(f"{vtk_var}.Update()")
        code.append(f"{var_name}_ugrid = {vtk_var}.GetOutput()")
        code.append(f"")
        
        # Get socket variable names
        points_socket_varname = self.get_var_name("NP Points")
        cells_socket_varname = self.get_var_name("NP Cells")
        cell_types_socket_varname = self.get_var_name("NP Cell Types")
        scalars_socket_varname = self.get_var_name("NP Scalars")
        
        # Extract points
        code.append(f"# Extract points")
        code.append(f"{points_socket_varname} = vtk_to_numpy({var_name}_ugrid.GetPoints().GetData()).astype(np.float32)")
        code.append(f"")
        
        # Extract cells
        code.append(f"# Extract cells")
        code.append(f"{cells_socket_varname} = vtk_to_numpy({var_name}_ugrid.GetCells().GetData())")
        code.append(f"")
        
        # Extract cell types
        code.append(f"# Extract cell types")
        code.append(f"{cell_types_socket_varname} = vtk_to_numpy({var_name}_ugrid.GetCellTypesArray())")
        code.append(f"")
        
        # Extract scalars if available
        code.append(f"# Extract scalars if available")
        code.append(f"if {var_name}_ugrid.GetPointData().GetScalars():")
        code.append(f"    {scalars_socket_varname} = vtk_to_numpy({var_name}_ugrid.GetPointData().GetScalars()).astype(np.float32)")
        code.append(f"else:")
        code.append(f"    {scalars_socket_varname} = None")
        
        return code


class VTKImageDataToNumpyNode(Node, PBVTK_Node):
    """Convert VTK Image Data (Volume) to Numpy array"""
    bl_idname = "VTKImageDataToNumpyType"
    bl_label = "VTK Image Data to Numpy"
    bl_icon = "VOLUME_DATA"

    def m_properties(self):
        return []

    def m_connections(self):
        return (["VTK Input"], [], [], [])

    def init(self, context):
        PBVTK_Node.init(self, context)
        self.outputs.new("PYNARINumpyArraySocket", "NP Volume")
        self.outputs.new("PYNARINumpyArraySocket", "NP Dimensions")
        self.outputs.new("PYNARINumpyArraySocket", "NP Spacing")
        self.outputs.new("PYNARINumpyArraySocket", "NP Origin")

    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label if hasattr(self, 'label') and self.label else self.name}")
        
        var_name = self.get_var_name()
        input_node, from_socket_name = self.get_input_node_and_socketname("VTK Input")
        if not input_node:
            code.append(f"# No input connected")
            return code
        
        vtk_var = input_node.get_var_name()
        
        code.append(f"# Convert VTK Image Data to Numpy")
        # code.append(f"import numpy as np")
        # code.append(f"from vtk.util.numpy_support import vtk_to_numpy")
        # code.append(f"")
        
        code.append(f"{vtk_var}.Update()")
        code.append(f"{var_name}_imagedata = {vtk_var}.GetOutput()")
        code.append(f"")
        
        # Get socket variable names
        volume_socket_varname = self.get_var_name("NP Volume")
        dimensions_socket_varname = self.get_var_name("NP Dimensions")
        spacing_socket_varname = self.get_var_name("NP Spacing")
        origin_socket_varname = self.get_var_name("NP Origin")
        
        # Extract volume data
        code.append(f"# Extract volume data")
        code.append(f"{var_name}_dims = {var_name}_imagedata.GetDimensions()")
        code.append(f"{var_name}_scalars = {var_name}_imagedata.GetPointData().GetScalars()")
        code.append(f"{volume_socket_varname} = vtk_to_numpy({var_name}_scalars).reshape({var_name}_dims, order='F').astype(np.float32)")
        code.append(f"")
        
        # Extract metadata
        code.append(f"# Extract metadata")
        code.append(f"{dimensions_socket_varname} = np.array({var_name}_dims, dtype=np.int32)")
        code.append(f"{spacing_socket_varname} = np.array({var_name}_imagedata.GetSpacing(), dtype=np.float32)")
        code.append(f"{origin_socket_varname} = np.array({var_name}_imagedata.GetOrigin(), dtype=np.float32)")
        
        return code


# Add converter nodes to CLASSES
add_class(VTKPolyDataToNumpyNode)
add_class(VTKStructuredGridToNumpyNode)
add_class(VTKUnstructuredGridToNumpyNode)
add_class(VTKImageDataToNumpyNode)

# -----------------------------------------------------------------------------
# Registration Functions
# -----------------------------------------------------------------------------


def register():
    """Register all VTK nodes and create VTK category"""

    from . import gen_VTKFilters
    from . import gen_VTKFilters1
    from . import gen_VTKFilters2
    from . import gen_VTKImplicitFunc
    from . import gen_VTKIntegrator
    from . import gen_VTKParametricFunc
    from . import gen_VTKReaders
    from . import gen_VTKSources
    from . import gen_VTKTransform
    from . import gen_VTKWriters

    bpy.utils.register_class(PBVTK_NodeSocket)

    # Register UI classes if any
    for cls in UI_CLASSES:
        bpy.utils.register_class(cls)

    # Extend
    add_class(VTKContourFilterExtend)

    # Register socket and converter nodes
    for cls in CLASSES.values():
        bpy.utils.register_class(cls)
    
    node_categories_items = []
    for cls in CLASSES.values():
        node_categories_items.append(nodeitems_utils.NodeItem(cls.bl_idname))

    node_categories = [
        PBVTK_NodeCategory('VTK', "VTK", items=node_categories_items),
    ]

    try:
        nodeitems_utils.register_node_categories('PBVTK_NODES', node_categories)
    except:
        pass        

def unregister():
    """Unregister all VTK nodes and category"""

    from . import gen_VTKFilters
    from . import gen_VTKFilters1
    from . import gen_VTKFilters2
    from . import gen_VTKImplicitFunc
    from . import gen_VTKIntegrator
    from . import gen_VTKParametricFunc
    from . import gen_VTKReaders
    from . import gen_VTKSources
    from . import gen_VTKTransform
    from . import gen_VTKWriters

    try:
        nodeitems_utils.unregister_node_categories('PBVTK_NODES')
    except:
        pass

    bpy.utils.unregister_class(PBVTK_NodeSocket)  

    # Unregister socket and converter nodes
    for cls in CLASSES.values():
        bpy.utils.unregister_class(cls)
    
    # Unregister UI classes if any
    for cls in UI_CLASSES:
        bpy.utils.unregister_class(cls)