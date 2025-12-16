#####################################################################################################################
# Copyright(C) 2025-2026 IT4Innovations National Supercomputing Center, VSB - Technical University of Ostrava
#
# This program is free software : you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
#####################################################################################################################

from braas_hpc_renderengine_dll import enable_gpujpeg
import bpy
import os
from bpy.types import NodeTree, Node, NodeSocket, Panel
from bpy.props import (StringProperty, FloatProperty, FloatVectorProperty, IntProperty, BoolProperty, EnumProperty, PointerProperty, CollectionProperty)
import nodeitems_utils
from nodeitems_utils import NodeCategory, NodeItem

from . import utility
from . import pynari_pref

##################################
# Timer for Auto Code Generation
##################################

def auto_generate_timer():
    """Timer function to automatically generate code for selected nodes"""
    
    def order_nodes_by_connections(nodes, tree):
        """Order nodes by their connection dependencies (topological sort)"""
        visited = set()
        ordered = []
        selected_set = set(nodes)
        
        def visit(node):
            if node in visited or node not in selected_set:
                return
            visited.add(node)
            
            # Visit input nodes first (dependencies)
            for input_socket in node.inputs:
                if input_socket.is_linked:
                    for link in input_socket.links:
                        from_node = link.from_node
                        if from_node in selected_set:
                            visit(from_node)
            
            ordered.append(node)
        
        # Visit all selected nodes
        for node in nodes:
            visit(node)
        
        return ordered
    
    for area in bpy.context.screen.areas:
        if area.type == 'NODE_EDITOR':
            for space in area.spaces:
                if space.type == 'NODE_EDITOR' and space.tree_type == 'PYNARIComposerNodeTree':
                    tree = space.edit_tree
                    if tree and hasattr(tree, 'auto_generate_code') and tree.auto_generate_code:
                        # Get all selected nodes
                        selected_nodes = [node for node in tree.nodes if node.select and hasattr(node, 'generate_code')]
                        
                        if selected_nodes:
                            try:
                                # Order nodes by their connections
                                ordered_nodes = order_nodes_by_connections(selected_nodes, tree)
                                
                                # Generate code for all selected nodes in dependency order
                                code_lines = []
                                
                                for node in ordered_nodes:
                                    code_lines.append(f"# Code for node: {node.name} ({node.bl_idname})")
                                    code_lines.append("")
                                    
                                    try:
                                        node_code = node.generate_code(auto_gen_enabled=True)
                                        code_lines.extend(node_code)
                                    except:
                                        pass
                                    
                                    code_lines.append("")
                                    code_lines.append("#" * 100)
                                    code_lines.append("")
                                
                                code = "\n".join(code_lines)
                                
                                # Create or get text block
                                text_name = f"{tree.name}_code_node.py"
                                if text_name in bpy.data.texts:
                                    text = bpy.data.texts[text_name]
                                    text.clear()
                                else:
                                    text = bpy.data.texts.new(text_name)
                                
                                text.write(code)

                            except Exception as e:
                                print(f"Auto-generate error: {str(e)}")
                        
                        # Return interval based on FPS setting
                        return 1.0 / tree.auto_generate_code_fps
    
    # Check again in 0.5 seconds if no active tree found
    return 0.5

##################################
# PYNARI Composer Node Tree
##################################

class PYNARIComposerNodeTree(NodeTree):
    """PYNARI Composer Node Tree for composing PYNARI scenes"""
    bl_idname = 'PYNARIComposerNodeTree'
    bl_label = 'PYNARI Composer'
    bl_icon = 'NODETREE'

    auto_generate_code_fps: IntProperty(  # type: ignore
        name="Auto Generate Code FPS",
        min=1,
        max=30,
        default=10,
        description="Set FPS for auto-generating code when enabled"
    )

    def _update_auto_generate_code(self, context):
        """Start or stop the timer when auto-generate is toggled"""
        if self.auto_generate_code:
            # Start timer if not already running
            if not bpy.app.timers.is_registered(auto_generate_timer):
                bpy.app.timers.register(auto_generate_timer, first_interval=0.1)
        else:
            # Stop timer
            if bpy.app.timers.is_registered(auto_generate_timer):
                bpy.app.timers.unregister(auto_generate_timer)
    
    auto_generate_code: BoolProperty(  # type: ignore
        name="Auto Generate Code",
        default=False,
        description="Automatically generate code when selected node values change",
        update=_update_auto_generate_code
    )
    
    def update(self):
        """Update the node tree"""
        pass
    
    def is_valid(self, link):
        """Check if a node link is valid (sockets must have same type)"""
        return link.from_socket.bl_idname == link.to_socket.bl_idname
    
    def generate_python_code(self):
        """Generate executable Python code with pynari from the node tree"""
        code_lines = []
        code_lines.append("import pynari")
        code_lines.append("import numpy as np")
        code_lines.append("import vtk")
        code_lines.append("from vtk.util.numpy_support import vtk_to_numpy")
        code_lines.append("")
        
        # Find device node
        output_node = None
        for node in self.nodes:
            if node.bl_idname == 'PYNARIOutputPILImageNode' or node.bl_idname == 'PYNARIOutputBRAASHPCNode':
                output_node = node
                break

        if output_node is None:
            raise ValueError("No Device node found in the node tree.")
        
        code_lines.append("#" * 100)
        code_lines.append("#" * 100)        
        code_lines.append("")

        # Generate device code
        code_lines.append(f"# Device initialization")
        code_lines.append(f"device = pynari.newDevice('{output_node.lib_name}', '{output_node.dev_name}')")
        code_lines.append("")
        code_lines.append("#" * 100)
        code_lines.append("#" * 100)        
        code_lines.append("")

        # Find frame node
        frame_node = None
        for input_socket in output_node.inputs:
            if input_socket.is_linked:
                if len(input_socket.links) == 0:
                    raise ValueError("Frame input socket has no links.")
                
                if len(input_socket.links) > 1:
                    raise ValueError("Frame input socket has multiple links.")
                
                frame_node = input_socket.links[0].from_node
        
        if frame_node and frame_node.bl_idname == 'PYNARIFrameNode':
            code_lines.extend(self._generate_node_code(frame_node, set()))

            code_lines.extend(output_node.generate_code())
            code_lines.append("")

        else:
            raise ValueError("No Frame node found in the node tree (connected to Device node).")
        
        final_code = "\n".join(code_lines)
        
        ############################ Create or get text block
        text_name = f"{self.name}_code_tree.py"
        if text_name in bpy.data.texts:
            text = bpy.data.texts[text_name]
            text.clear()
        else:
            text = bpy.data.texts.new(text_name)
        
        text.write(final_code)

        return text_name
    
    def _generate_node_code(self, node, visited):
        """Recursively generate code for a node and its dependencies"""
        if node in visited or not hasattr(node, 'generate_code'):
            return []
        
        visited.add(node)
        code_lines = []
        
        # Generate code for input nodes first
        for input_socket in node.inputs:
            if input_socket.is_linked:
                for link in input_socket.links:
                    from_node = link.from_node
                    code_lines.extend(self._generate_node_code(from_node, visited))
        
        # Generate code for this node
        code_lines.extend(node.generate_code())
        code_lines.append("")
        code_lines.append("#" * 100)
        code_lines.append("#" * 100)        
        code_lines.append("")
        
        return code_lines


##################################
# Base Node Classes
##################################

class PYNARIComposerNode(Node):
    """Base class for all PYNARI nodes"""

    output_data: None
    
    @classmethod
    def poll(cls, ntree):
        return ntree.bl_idname == 'PYNARIComposerNodeTree'

    def init(self, context):
        """Create and initialize a new node.
        """
        # Node properties
        self.width = 200
    
    def get_input_value(self, input_name, default=None):
        """Get value from input socket"""
        input_socket = self.inputs.get(input_name)
        if input_socket and input_socket.is_linked:
            if len(input_socket.links) == 0:
                raise ValueError(f"Input socket '{input_name}' has no links.")
            
            if len(input_socket.links) > 1:
                raise ValueError(f"Input socket '{input_name}' has multiple links.")
            
            from_node = input_socket.links[0].from_node
            socket_varname = utility.str_to_var_name(input_name)
            return from_node.get_var_name(socket_varname)
        
        elif hasattr(input_socket, 'default_value'):
            return input_socket.default_value
        return default
    
    def get_input_value_or_linked(self, input_name, use_tuple=False):
        if not self.inputs[input_name].is_linked:
            value = self.inputs[input_name].default_value
            if use_tuple:
                return tuple(value)
            return value
        else:
            #socket_varname = utility.str_to_var_name(input_name)
            linked_values = [link.from_node.get_var_name(link.from_socket.name) for link in self.inputs[input_name].links]
            return linked_values[0]
    
    def get_var_name(self, postfix=""):
        """Get the variable name for this node's output"""
        if len(postfix) > 0:
            return f"{utility.str_to_var_name(self.name)}_{utility.str_to_var_name(postfix)}"
        
        return utility.str_to_var_name(self.name)
    
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
    
    def generate_code(self, auto_gen_enabled=False):
        """Generate Python code for this node - override in subclasses"""
        return []

    def get_file_path(self):
        if pynari_pref.preferences().braas_hpc_pynari_composer_remote:
            return str(self.file_path_remote)
        else:
            return str(bpy.path.abspath(self.file_path))
        
    def draw_file_path(self, layout):
        row = layout.column(align=True)
        if pynari_pref.preferences().braas_hpc_pynari_composer_remote:
            row.prop(self, "file_path_remote")
        else:
            row.prop(self, "file_path")

    def get_dir_path(self):
        if pynari_pref.preferences().braas_hpc_pynari_composer_remote:
            return str(self.dir_path_remote)
        else:
            return str(bpy.path.abspath(self.dir_path))
        
    def draw_dir_path(self, layout):
        row = layout.column(align=True)
        if pynari_pref.preferences().braas_hpc_pynari_composer_remote:
            row.prop(self, "dir_path_remote")
        else:
            row.prop(self, "dir_path")

##################################
# Frame Node
##################################

class PYNARIFrameNode(PYNARIComposerNode):
    """Frame node for PYNARI rendering"""
    bl_idname = 'PYNARIFrameNode'
    bl_label = 'Frame'
    bl_icon = 'RENDER_RESULT'
    
    def init(self, context):
        self.inputs.new('PYNARICameraSocket', "Camera").link_limit = 1
        self.inputs.new('PYNARIWorldSocket', "World").link_limit = 1
        self.inputs.new('PYNARIRendererSocket', "Renderer").link_limit = 1
        
        width_socket = self.inputs.new('NodeSocketInt', "Width") #.link_limit = 1
        width_socket.default_value = 1024
        
        height_socket = self.inputs.new('NodeSocketInt', "Height") #.link_limit = 1
        height_socket.default_value = 768

        self.outputs.new('PYNARIFrameSocket', "Frame")
    
    def draw_buttons(self, context, layout):
        pass
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")

        var_name = self.get_var_name("Frame")
        
        world = self.get_input_value("World")
        camera = self.get_input_value("Camera")
        renderer = self.get_input_value("Renderer")
        
        code.append(f"# Frame")
        if not auto_gen_enabled:
            code.append(f"{var_name} = device.newFrame()")
        code.append(f"{var_name}.setParameter('world', pynari.WORLD, {world})")
        code.append(f"{var_name}.setParameter('camera', pynari.CAMERA, {camera})")
        code.append(f"{var_name}.setParameter('renderer', pynari.RENDERER, {renderer})")
        
        width = self.get_input_value_or_linked("Width")
        height = self.get_input_value_or_linked("Height")
        
        code.append(f"{var_name}.setParameter('size', pynari.uint2, [int({width}), int({height})])")
        code.append(f"{var_name}.setParameter('channel.color', pynari.DATA_TYPE, pynari.UFIXED8_RGBA_SRGB)")
        code.append(f"{var_name}.commitParameters()")
        
        return code


##################################
# Camera Nodes
##################################

class PYNARICameraNode(PYNARIComposerNode):
    """Base camera node"""
    
    def init_camera_sockets(self, context):
        position_socket = self.inputs.new('NodeSocketVector', "Position") #.link_limit = 1
        position_socket.default_value = (0.0, 0.0, 0.0)
        
        direction_socket = self.inputs.new('NodeSocketVector', "Direction") #.link_limit = 1
        direction_socket.default_value = (0.0, 0.0, -1.0)
        
        up_socket = self.inputs.new('NodeSocketVector', "Up") #.link_limit = 1
        up_socket.default_value = (0.0, 1.0, 0.0)
    
    def draw_buttons(self, context, layout):
        pass


class PYNARIPerspectiveCameraNode(PYNARICameraNode):
    """Perspective camera node"""
    bl_idname = 'PYNARIPerspectiveCameraNode'
    bl_label = 'Perspective Camera'
    bl_icon = 'CAMERA_DATA'
    
    def init(self, context):
        self.init_camera_sockets(context)
        
        fovy_socket = self.inputs.new('NodeSocketFloat', "Fovy") #.link_limit = 1
        fovy_socket.default_value = 1.047
        
        aspect_socket = self.inputs.new('NodeSocketFloat', "Aspect") #.link_limit = 1
        aspect_socket.default_value = 1.333
        
        self.outputs.new('PYNARICameraSocket', "Camera")
    
    def draw_buttons(self, context, layout):
        pass
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name("Camera")
        
        position = self.get_input_value_or_linked("Position", use_tuple=True)
        direction = self.get_input_value_or_linked("Direction", use_tuple=True)
        up = self.get_input_value_or_linked("Up", use_tuple=True)
        fovy = self.get_input_value_or_linked("Fovy")
        aspect = self.get_input_value_or_linked("Aspect")
        
        code.append(f"# Perspective Camera")
        if not auto_gen_enabled:
            code.append(f"{var_name} = device.newCamera('perspective')")
        code.append(f"{var_name}.setParameter('position', pynari.FLOAT32_VEC3, {position})")
        code.append(f"{var_name}.setParameter('direction', pynari.FLOAT32_VEC3, {direction})")
        code.append(f"{var_name}.setParameter('up', pynari.FLOAT32_VEC3, {up})")
        code.append(f"{var_name}.setParameter('fovy', pynari.FLOAT32, {fovy})")
        code.append(f"{var_name}.setParameter('aspect', pynari.FLOAT32, {aspect})")
        code.append(f"{var_name}.commitParameters()")
        
        return code


class PYNARIOrthographicCameraNode(PYNARICameraNode):
    """Orthographic camera node"""
    bl_idname = 'PYNARIOrthographicCameraNode'
    bl_label = 'Orthographic Camera'
    bl_icon = 'CAMERA_DATA'
    
    def init(self, context):
        self.init_camera_sockets(context)
        
        height_socket = self.inputs.new('NodeSocketFloat', "Height") #.link_limit = 1
        height_socket.default_value = 1.0
        
        aspect_socket = self.inputs.new('NodeSocketFloat', "Aspect") #.link_limit = 1
        aspect_socket.default_value = 1.333
        
        self.outputs.new('PYNARICameraSocket', "Camera")
    
    def draw_buttons(self, context, layout):
        pass
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name("Camera")
        
        position = self.get_input_value_or_linked("Position", use_tuple=True)
        direction = self.get_input_value_or_linked("Direction", use_tuple=True)
        up = self.get_input_value_or_linked("Up", use_tuple=True)
        height = self.get_input_value_or_linked("Height")
        aspect = self.get_input_value_or_linked("Aspect")
        
        code.append(f"# Orthographic Camera")
        if not auto_gen_enabled:
            code.append(f"{var_name} = device.newCamera('orthographic')")
        code.append(f"{var_name}.setParameter('position', pynari.FLOAT32_VEC3, {position})")
        code.append(f"{var_name}.setParameter('direction', pynari.FLOAT32_VEC3, {direction})")
        code.append(f"{var_name}.setParameter('up', pynari.FLOAT32_VEC3, {up})")
        code.append(f"{var_name}.setParameter('height', pynari.FLOAT32, {height})")
        code.append(f"{var_name}.setParameter('aspect', pynari.FLOAT32, {aspect})")
        code.append(f"{var_name}.commitParameters()")
        
        return code


class PYNARIBlenderCameraNode(PYNARICameraNode):
    """Blender camera node - uses active camera from scene"""
    bl_idname = 'PYNARIBlenderCameraNode'
    bl_label = 'Blender Camera'
    bl_icon = 'CAMERA_DATA'
    
    def init(self, context):
        self.outputs.new('PYNARICameraSocket', "Camera")
    
    def draw_buttons(self, context, layout):
        pass
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name("Camera")
        
        code.append(f"# Blender Camera")
        if not auto_gen_enabled:
            code.append(f"{var_name} = device.newCamera('perspective')")
        code.append(f"{var_name}.commitParameters()")
        
        return code


##################################
# Device Node
##################################

class PYNARIOutputPILImageNode(PYNARIComposerNode):
    """Device node for PYNARI initialization"""
    bl_idname = 'PYNARIOutputPILImageNode'
    bl_label = 'PILImage'
    bl_icon = 'SETTINGS'
    
    lib_name: StringProperty(  # type: ignore
        name="Library Name",
        default="helide",
        description="PYNARI library name (e.g., helide, environment, visrtx)",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )

    dev_name: StringProperty(  # type: ignore
        name="Device Name",
        default="default",
        description="PYNARI device name",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )

    image_file_name: bpy.props.StringProperty(
        name="Name",
        default="output.png",
        subtype="FILE_NAME",
        # update = update_property
        #update=lambda self, context: self.auto_generate_node_code(context)
    ) # type: ignore

    dir_path: bpy.props.StringProperty(
        name="Path",
        default="",
        subtype="DIR_PATH",
        #update=lambda self, context: self.auto_generate_node_code(context)
    ) # type: ignore

    dir_path_remote: bpy.props.StringProperty(
        name="Path",
        default="",
        #update=lambda self, context: self.auto_generate_node_code(context)
    ) # type: ignore     
    
    def init(self, context):
        self.inputs.new('PYNARIFrameSocket', "Frame").link_limit = 1
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "lib_name")
        layout.prop(self, "dev_name")
        self.draw_dir_path(layout)
        layout.prop(self, "image_file_name")
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        frame = self.get_input_value("Frame")
        
        code.append(f"# Render")

        output_path = self.get_dir_path()

        if len(output_path) > 0:
            fullpath = f"{output_path}/{self.image_file_name}"
        else:
            fullpath = f"{self.image_file_name}"

        code.append(f"{frame}.render()")
        code.append(f"fb_color = {frame}.get('channel.color')")
        code.append("pixels = np.array(fb_color)")
        code.append("pixels = np.flipud(pixels)")
        code.append("")
        code.append(f"# Save image to file")
        code.append("from PIL import Image as PIL_Image")
        code.append(f"out_file_name = r'{fullpath}'")        
        code.append("im = PIL_Image.fromarray(pixels)")
        code.append("print(f'@pynari: done. saving to {out_file_name}')")
        code.append("im.convert('RGB').save(out_file_name)")

        return code


##################################
# Renderer Node
##################################

class PYNARIRendererNode(PYNARIComposerNode):
    """Renderer node"""
    bl_idname = 'PYNARIRendererNode'
    bl_label = 'Renderer'
    bl_icon = 'SHADING_RENDERED'
    
    renderer_subtype: StringProperty(  # type: ignore
        name="Type", 
        default="default",
        description="Renderer subtype to use (default, scivis, pathtracer, etc.)",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    background_color1: FloatVectorProperty(  # type: ignore
        name="Background1", 
        default=(0.9,0.9,0.9,1.0),
        size=4, 
        min=0.0, 
        max=1.0, 
        subtype='COLOR',
        description="The background color (RGBA)",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    background_color2: FloatVectorProperty(  # type: ignore
        name="Background2", 
        default=(0.15,0.25,0.8,1.0), 
        size=4, 
        min=0.0, 
        max=1.0, 
        subtype='COLOR',
        description="The background color (RGBA)",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    pixel_samples: IntProperty(  # type: ignore
        name="Pixel Samples", 
        default=1, 
        min=1,
        description="Number of pixel samples",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )    
    ambient_radiance: FloatProperty(  # type: ignore
        name="Ambient Radiance", 
        default=1.0, 
        min=0.0,
        description="Ambient radiance intensity",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    denoise: BoolProperty(  # type: ignore
        name="Denoise",
        default=True,
        description="Enable denoising",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    def init(self, context):
        self.outputs.new('PYNARIRendererSocket', "Renderer")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "renderer_subtype")
        layout.prop(self, "background_color1")
        layout.prop(self, "background_color2")
        layout.prop(self, "pixel_samples")
        layout.prop(self, "ambient_radiance")
        layout.prop(self, "denoise")
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name("Renderer")
        
        code.append(f"# Renderer")
        if not auto_gen_enabled:
            code.append(f"{var_name} = device.newRenderer('{self.renderer_subtype}')")
        code.append(f"{var_name}_bg_values = np.array(({tuple(self.background_color1)},{tuple(self.background_color2)}), dtype=np.float32).reshape((2,1,4))")
        code.append(f"{var_name}_bg_gradient = device.newArray2D(pynari.float4, {var_name}_bg_values)")
        code.append(f"{var_name}.setParameter('background', pynari.ARRAY2D, {var_name}_bg_gradient)")
        code.append(f"{var_name}.setParameter('pixelSamples', pynari.INT32, {self.pixel_samples})")
        code.append(f"{var_name}.setParameter('ambientRadiance', pynari.FLOAT32, {self.ambient_radiance})")
        code.append(f"{var_name}.setParameter('denoise', pynari.BOOL, {str(self.denoise)})")
        code.append(f"{var_name}.commitParameters()")
        
        return code


##################################
# World Node
##################################

class PYNARIWorldNode(PYNARIComposerNode):
    """World node"""
    bl_idname = 'PYNARIWorldNode'
    bl_label = 'World'
    bl_icon = 'WORLD'
    
    def init(self, context):
        self.inputs.new('PYNARIInstanceSocket', "Instances").link_limit = 100
        self.inputs.new('PYNARISurfaceSocket', "Surfaces").link_limit = 100
        self.inputs.new('PYNARIVolumeSocket', "Volumes").link_limit = 100
        self.inputs.new('PYNARILightSocket', "Lights").link_limit = 100

        self.outputs.new('PYNARIWorldSocket', "World")
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name("World")
        
        code.append(f"# World")
        if not auto_gen_enabled:
            code.append(f"{var_name} = device.newWorld()")
        
        # Collect instances, surfaces, volumes, lights
        instances = [link.from_node.get_var_name(link.from_socket.name) for link in self.inputs["Instances"].links]
        surfaces = [link.from_node.get_var_name(link.from_socket.name) for link in self.inputs["Surfaces"].links]
        volumes = [link.from_node.get_var_name(link.from_socket.name) for link in self.inputs["Volumes"].links]
        lights = [link.from_node.get_var_name(link.from_socket.name) for link in self.inputs["Lights"].links]
        
        if instances:
            code.append(f"{var_name}.setParameterArray1D('instance', pynari.INSTANCE, [{', '.join(instances)}])")
        if surfaces:
            code.append(f"{var_name}.setParameterArray1D('surface', pynari.SURFACE, [{', '.join(surfaces)}])")
        if volumes:
            code.append(f"{var_name}.setParameterArray1D('volume', pynari.VOLUME, [{', '.join(volumes)}])")
        if lights:
            code.append(f"{var_name}.setParameterArray1D('light', pynari.LIGHT, [{', '.join(lights)}])")
        
        code.append(f"{var_name}.commitParameters()")
        
        return code


##################################
# Group Node
##################################

class PYNARIGroupNode(PYNARIComposerNode):
    """Group node"""
    bl_idname = 'PYNARIGroupNode'
    bl_label = 'Group'
    bl_icon = 'GROUP'
    
    def init(self, context):
        self.inputs.new('PYNARIVolumeSocket', "Volumes").link_limit = 100
        self.inputs.new('PYNARILightSocket', "Lights").link_limit = 100
        self.inputs.new('PYNARISurfaceSocket', "Surfaces").link_limit = 100      

        self.outputs.new('PYNARIGroupSocket', "Group")
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name("Group")
        
        code.append(f"# Group")
        if not auto_gen_enabled:
            code.append(f"{var_name} = device.newGroup([])")
        
        surfaces = [link.from_node.get_var_name(link.from_socket.name) for link in self.inputs["Surfaces"].links]
        volumes = [link.from_node.get_var_name(link.from_socket.name) for link in self.inputs["Volumes"].links]
        lights = [link.from_node.get_var_name(link.from_socket.name) for link in self.inputs["Lights"].links]
        
        if surfaces:
            code.append(f"{var_name}.setParameterArray1D('surface', pynari.SURFACE, [{', '.join(surfaces)}])")
        if volumes:
            code.append(f"{var_name}.setParameterArray1D('volume', pynari.VOLUME, [{', '.join(volumes)}])")
        if lights:
            code.append(f"{var_name}.setParameterArray1D('light', pynari.LIGHT, [{', '.join(lights)}])")
        
        code.append(f"{var_name}.commitParameters()")
        
        return code


##################################
# Instance Node
##################################

class PYNARIInstanceNode(PYNARIComposerNode):
    """Instance node"""
    bl_idname = 'PYNARIInstanceNode'
    bl_label = 'Instance'
    bl_icon = 'OBJECT_DATA'
    
    def init(self, context):
        self.inputs.new('PYNARIGroupSocket', "Group").link_limit = 1
        
        translation_socket = self.inputs.new('NodeSocketVector', "Translation") #.link_limit = 1
        translation_socket.default_value = (0.0, 0.0, 0.0)
        
        rotation_socket = self.inputs.new('NodeSocketVector', "Rotation") #.link_limit = 1
        rotation_socket.default_value = (0.0, 0.0, 0.0)
        
        scale_socket = self.inputs.new('NodeSocketVector', "Scale") #.link_limit = 1
        scale_socket.default_value = (1.0, 1.0, 1.0)

        self.outputs.new('PYNARIInstanceSocket', "Instance")
    
    def draw_buttons(self, context, layout):
        pass
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        
        var_name = self.get_var_name("Instance")

        group = self.get_input_value("Group")
        
        translation = self.get_input_value_or_linked("Translation", use_tuple=True)
        rotation = self.get_input_value_or_linked("Rotation", use_tuple=True)
        scale = self.get_input_value_or_linked("Scale", use_tuple=True)
        
        code.append(f"# Instance")
        if not auto_gen_enabled:
            code.append(f"{var_name} = device.newInstance('transform')")
        code.append(f"{var_name}.setParameter('group', pynari.GROUP, {group})")
        
        # Create transformation matrix
        import math
        from mathutils import Matrix, Euler, Vector
        
        mat_loc = Matrix.Translation(Vector(translation))
        mat_rot = Euler(rotation, 'XYZ').to_matrix().to_4x4()
        mat_scale = Matrix.Diagonal(Vector(scale).to_4d())
        mat_scale[3][3] = 1.0
        
        transform = mat_loc @ mat_rot @ mat_scale
        transform_tuple = tuple(tuple(row) for row in transform.transposed())
        # Flatten the matrix to a single tuple of 16 floats for pynari
        transform_flat = tuple(val for row in transform_tuple for val in row)
        
        code.append(f"{var_name}.setParameter('transform', pynari.FLOAT32_MAT4, {transform_flat})")
        code.append(f"{var_name}.commitParameters()")
        
        return code


class PYNARIBlenderInstanceNode(PYNARIComposerNode):
    """Blender Instance node - uses Blender object transformation"""
    bl_idname = 'PYNARIBlenderInstanceNode'
    bl_label = 'Blender Instance'
    bl_icon = 'OBJECT_DATA'
    
    blender_object: PointerProperty(  # type: ignore
        name="Object",
        type=bpy.types.Object,
        description="Blender object to get transformation from",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    def init(self, context):
        self.inputs.new('PYNARIGroupSocket', "Group").link_limit = 1
        self.outputs.new('PYNARIInstanceSocket', "Instance")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "blender_object")
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        
        var_name = self.get_var_name("Instance")

        group = self.get_input_value("Group")
        
        code.append(f"# Blender Instance")
        if not auto_gen_enabled:
            code.append(f"{var_name} = device.newInstance('transform')")
        code.append(f"{var_name}.setParameter('group', pynari.GROUP, {group})")
        
        # Get transformation from Blender object's matrix_world
        if self.blender_object:
            from mathutils import Matrix
            
            transform = self.blender_object.matrix_world
            transform_tuple = tuple(tuple(row) for row in transform.transposed())
            # Flatten the matrix to a single tuple of 16 floats for pynari
            transform_flat = tuple(val for row in transform_tuple for val in row)
            
            code.append(f"{var_name}.setParameter('transform', pynari.FLOAT32_MAT4, {transform_flat})")
        else:
            # Use identity matrix if no object is selected
            code.append(f"# No object selected, using identity matrix")
            identity = (1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0)
            code.append(f"{var_name}.setParameter('transform', pynari.FLOAT32_MAT4, {identity})")
        
        code.append(f"{var_name}.commitParameters()")
        
        return code


##################################
# Surface Node
##################################

class PYNARISurfaceNode(PYNARIComposerNode):
    """Surface node"""
    bl_idname = 'PYNARISurfaceNode'
    bl_label = 'Surface'
    bl_icon = 'MESH_DATA'
    
    def init(self, context):
        self.inputs.new('PYNARIGeometrySocket', "Geometry").link_limit = 1
        self.inputs.new('PYNARIMaterialSocket', "Material").link_limit = 1

        self.outputs.new('PYNARISurfaceSocket', "Surface")
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        
        var_name = self.get_var_name("Surface")

        geometry = self.get_input_value("Geometry")
        material = self.get_input_value("Material")
        
        code.append(f"# Surface")
        if not auto_gen_enabled:
            code.append(f"{var_name} = device.newSurface()")
        code.append(f"{var_name}.setParameter('geometry', pynari.GEOMETRY, {geometry})")
        code.append(f"{var_name}.setParameter('material', pynari.MATERIAL, {material})")
        code.append(f"{var_name}.commitParameters()")
        
        return code


##################################
# Geometry Nodes
##################################

class PYNARITriangleGeometryNode(PYNARIComposerNode):
    """Triangle geometry node"""
    bl_idname = 'PYNARITriangleGeometryNode'
    bl_label = 'Triangle Geometry'
    bl_icon = 'MESH_DATA'
    
    def init(self, context):
        self.inputs.new('PYNARINumpyArraySocket', "NP Indices").link_limit = 1
        self.inputs.new('PYNARINumpyArraySocket', "NP Vertices").link_limit = 1
        self.inputs.new('PYNARINumpyArraySocket', "NP Normals").link_limit = 1
        self.inputs.new('PYNARINumpyArraySocket', "NP Colors").link_limit = 1

        self.outputs.new('PYNARIGeometrySocket', "Geometry")
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")

        var_name = self.get_var_name("Geometry")
        
        code.append(f"# Triangle Geometry")        
        if not auto_gen_enabled:
            code.append(f"{var_name} = device.newGeometry('triangle')")

        vertices_socket_varname =  utility.str_to_var_name("NP Vertices")
        indices_socket_varname =  utility.str_to_var_name("NP Indices")
        normals_socket_varname =  utility.str_to_var_name("NP Normals")
        colors_socket_varname =  utility.str_to_var_name("NP Colors")

        vertices = [link.from_node.get_var_name(vertices_socket_varname) for link in self.inputs["NP Vertices"].links]
        indices = [link.from_node.get_var_name(indices_socket_varname) for link in self.inputs["NP Indices"].links]
        normals = [link.from_node.get_var_name(normals_socket_varname) for link in self.inputs["NP Normals"].links]
        colors = [link.from_node.get_var_name(colors_socket_varname) for link in self.inputs["NP Colors"].links]

        if vertices:
            code.append(f"{var_name}_{vertices_socket_varname} = device.newArray1D(pynari.FLOAT32_VEC3, {vertices[0]})")
            code.append(f"{var_name}.setParameter('vertex.position', pynari.ARRAY1D, {var_name}_{vertices_socket_varname})")

        if indices:
            code.append(f"{var_name}_{indices_socket_varname} = device.newArray1D(pynari.UINT32_VEC3, {indices[0]})")
            code.append(f"{var_name}.setParameter('primitive.index', pynari.ARRAY1D, {var_name}_{indices_socket_varname})")

        if normals:
            code.append(f"{var_name}_{normals_socket_varname} = device.newArray1D(pynari.FLOAT32_VEC3, {normals[0]})")
            code.append(f"{var_name}.setParameter('vertex.normal', pynari.ARRAY1D, {var_name}_{normals_socket_varname})")
        if colors:
            code.append(f"{var_name}_{colors_socket_varname} = device.newArray1D(pynari.FLOAT32_VEC4, {colors[0]})")
            code.append(f"{var_name}.setParameter('vertex.color', pynari.ARRAY1D, {var_name}_{colors_socket_varname})")                        

        code.append(f"{var_name}.commitParameters()")
        
        return code


class PYNARISphereGeometryNode(PYNARIComposerNode):
    """Sphere geometry node"""
    bl_idname = 'PYNARISphereGeometryNode'
    bl_label = 'Sphere Geometry'
    bl_icon = 'MESH_UVSPHERE'
    
    def init(self, context):
        self.inputs.new('PYNARINumpyArraySocket', "NP Vertices").link_limit = 1
        self.inputs.new('PYNARINumpyArraySocket', "NP Indices").link_limit = 1
        self.inputs.new('PYNARINumpyArraySocket', "NP Radiuses").link_limit = 1
        self.inputs.new('PYNARINumpyArraySocket', "NP Colors").link_limit = 1
        
        radius_socket = self.inputs.new('NodeSocketFloat', "Radius") #.link_limit = 1
        radius_socket.default_value = 1.0

        self.outputs.new('PYNARIGeometrySocket', "Geometry")
    
    def draw_buttons(self, context, layout):
        pass
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")

        var_name = self.get_var_name("Geometry")
        
        code.append(f"# Sphere Geometry")
        if not auto_gen_enabled:
            code.append(f"{var_name} = device.newGeometry('sphere')")

        vertices_socket_varname =  utility.str_to_var_name("NP Vertices")
        indices_socket_varname =  utility.str_to_var_name("NP Indices")
        radiuses_socket_varname =  utility.str_to_var_name("NP Radiuses")
        colors_socket_varname =  utility.str_to_var_name("NP Colors")            

        vertices = [link.from_node.get_var_name(vertices_socket_varname) for link in self.inputs["NP Vertices"].links]
        indices = [link.from_node.get_var_name(indices_socket_varname) for link in self.inputs["NP Indices"].links]
        radiuses = [link.from_node.get_var_name(radiuses_socket_varname) for link in self.inputs["NP Radiuses"].links]
        colors = [link.from_node.get_var_name(colors_socket_varname) for link in self.inputs["NP Colors"].links]

        if vertices:
            code.append(f"{var_name}_{vertices_socket_varname} = device.newArray1D(pynari.FLOAT32_VEC3, {vertices[0]})")
            code.append(f"{var_name}.setParameter('vertex.position', pynari.ARRAY1D, {var_name}_{vertices_socket_varname})")

        if indices:
            code.append(f"{var_name}_{indices_socket_varname} = device.newArray1D(pynari.UINT32_VEC3, {indices[0]})")
            code.append(f"{var_name}.setParameter('primitive.index', pynari.ARRAY1D, {var_name}_{indices_socket_varname})")            

        if radiuses:
            code.append(f"{var_name}_{radiuses_socket_varname} = device.newArray1D(pynari.FLOAT32, {radiuses[0]})")
            code.append(f"{var_name}.setParameter('vertex.radius', pynari.ARRAY1D, {var_name}_{radiuses_socket_varname})")
        else:
            radius = self.get_input_value_or_linked("Radius")
            code.append(f"{var_name}.setParameter('radius', pynari.FLOAT32, {radius})")

        if colors:
            code.append(f"{var_name}_{colors_socket_varname} = device.newArray1D(pynari.FLOAT32_VEC4, {colors[0]})")
            code.append(f"{var_name}.setParameter('vertex.color', pynari.ARRAY1D, {var_name}_{colors_socket_varname})")

        code.append(f"{var_name}.commitParameters()")
        
        return code


class PYNARICylinderGeometryNode(PYNARIComposerNode):
    """Cylinder geometry node"""
    bl_idname = 'PYNARICylinderGeometryNode'
    bl_label = 'Cylinder Geometry'
    bl_icon = 'MESH_CYLINDER'
    
    def init(self, context):
        self.inputs.new('PYNARINumpyArraySocket', "NP Vertices").link_limit = 1
        self.inputs.new('PYNARINumpyArraySocket', "NP Indices").link_limit = 1
        self.inputs.new('PYNARINumpyArraySocket', "NP Radiuses").link_limit = 1
        self.inputs.new('PYNARINumpyArraySocket', "NP Colors").link_limit = 1
        
        radius_socket = self.inputs.new('NodeSocketFloat', "Radius") #.link_limit = 1
        radius_socket.default_value = 0.5

        self.outputs.new('PYNARIGeometrySocket', "Geometry")
    
    def draw_buttons(self, context, layout):
        pass
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")

        var_name = self.get_var_name("Geometry")
        
        code.append(f"# Cylinder Geometry")
        if not auto_gen_enabled:
            code.append(f"{var_name} = device.newGeometry('cylinder')")

        vertices_socket_varname =  utility.str_to_var_name("NP Vertices")
        indices_socket_varname =  utility.str_to_var_name("NP Indices")
        radiuses_socket_varname =  utility.str_to_var_name("NP Radiuses")
        colors_socket_varname =  utility.str_to_var_name("NP Colors")           

        vertices = [link.from_node.get_var_name(vertices_socket_varname) for link in self.inputs["NP Vertices"].links]
        indices = [link.from_node.get_var_name(indices_socket_varname) for link in self.inputs["NP Indices"].links]
        radiuses = [link.from_node.get_var_name(radiuses_socket_varname) for link in self.inputs["NP Radiuses"].links]
        colors = [link.from_node.get_var_name(colors_socket_varname) for link in self.inputs["NP Colors"].links]

        if vertices:
            code.append(f"{var_name}_{vertices_socket_varname} = device.newArray1D(pynari.FLOAT32_VEC3, {vertices[0]})")
            code.append(f"{var_name}.setParameter('vertex.position', pynari.ARRAY1D, {var_name}_{vertices_socket_varname})")

        if indices:
            code.append(f"{var_name}_{indices_socket_varname} = device.newArray1D(pynari.UINT32_VEC3, {indices[0]})")
            code.append(f"{var_name}.setParameter('primitive.index', pynari.ARRAY1D, {var_name}_{indices_socket_varname})")            

        if radiuses:
            code.append(f"{var_name}_{radiuses_socket_varname} = device.newArray1D(pynari.FLOAT32, {radiuses[0]})")
            code.append(f"{var_name}.setParameter('primitive.radius', pynari.ARRAY1D, {var_name}_{radiuses_socket_varname})")
        else:
            radius = self.get_input_value_or_linked("Radius")
            code.append(f"{var_name}.setParameter('radius', pynari.FLOAT32, {radius})")

        if colors:
            code.append(f"{var_name}_{colors_socket_varname} = device.newArray1D(pynari.FLOAT32_VEC4, {colors[0]})")
            code.append(f"{var_name}.setParameter('primitive.color', pynari.ARRAY1D, {var_name}_{colors_socket_varname})")        
        
        code.append(f"{var_name}.commitParameters()")
        
        return code


class PYNARIIsoSurfaceGeometryNode(PYNARIComposerNode):
    """IsoSurface geometry node"""
    bl_idname = 'PYNARIIsoSurfaceGeometryNode'
    bl_label = 'IsoSurface Geometry'
    bl_icon = 'MESH_DATA'
    
    def init(self, context):
        self.inputs.new('PYNARISpatialFieldSocket', "Field").link_limit = 1
        
        isovalue_socket = self.inputs.new('NodeSocketFloat', "Isovalue") #.link_limit = 1
        isovalue_socket.default_value = 0.5

        self.outputs.new('PYNARIGeometrySocket', "Geometry")
    
    def draw_buttons(self, context, layout):
        pass
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        
        var_name = self.get_var_name("Geometry")

        field = self.get_input_value("Field")
        isovalue = self.get_input_value_or_linked("Isovalue")
        
        code.append(f"# IsoSurface Geometry")
        if not auto_gen_enabled:
            code.append(f"{var_name} = device.newGeometry('isosurface')")
        code.append(f"{var_name}.setParameter('isovalue', pynari.FLOAT32, {isovalue})")
        code.append(f"{var_name}.setParameter('field', pynari.SPATIAL_FIELD, {field})")
        code.append(f"{var_name}.commitParameters()")
        
        return code


class PYNARIConeGeometryNode(PYNARIComposerNode):
    """Cone geometry node"""
    bl_idname = 'PYNARIConeGeometryNode'
    bl_label = 'Cone Geometry'
    bl_icon = 'MESH_CONE'
    
    def init(self, context):
        self.inputs.new('PYNARINumpyArraySocket', "NP Vertices").link_limit = 1
        self.inputs.new('PYNARINumpyArraySocket', "NP Indices").link_limit = 1
        self.inputs.new('PYNARINumpyArraySocket', "NP Radiuses").link_limit = 1
        self.inputs.new('PYNARINumpyArraySocket', "NP Colors").link_limit = 1

        self.outputs.new('PYNARIGeometrySocket', "Geometry")
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")

        var_name = self.get_var_name("Geometry")
        
        code.append(f"# Cone Geometry")
        if not auto_gen_enabled:
            code.append(f"{var_name} = device.newGeometry('cone')")

        vertices_socket_varname =  utility.str_to_var_name("NP Vertices")
        indices_socket_varname =  utility.str_to_var_name("NP Indices")
        radiuses_socket_varname =  utility.str_to_var_name("NP Radiuses")
        colors_socket_varname =  utility.str_to_var_name("NP Colors")         

        vertices = [link.from_node.get_var_name(vertices_socket_varname) for link in self.inputs["NP Vertices"].links]
        indices = [link.from_node.get_var_name(indices_socket_varname) for link in self.inputs["NP Indices"].links]
        radiuses = [link.from_node.get_var_name(radiuses_socket_varname) for link in self.inputs["NP Radiuses"].links]
        colors = [link.from_node.get_var_name(colors_socket_varname) for link in self.inputs["NP Colors"].links]

        if vertices:
            code.append(f"{var_name}_{vertices_socket_varname} = device.newArray1D(pynari.FLOAT32_VEC3, {vertices[0]})")
            code.append(f"{var_name}.setParameter('vertex.position', pynari.ARRAY1D, {var_name}_{vertices_socket_varname})")

        if indices:
            code.append(f"{var_name}_{indices_socket_varname} = device.newArray1D(pynari.UINT32_VEC3, {indices[0]})")
            code.append(f"{var_name}.setParameter('primitive.index', pynari.ARRAY1D, {var_name}_{indices_socket_varname})")            

        if radiuses:
            code.append(f"{var_name}_{radiuses_socket_varname} = device.newArray1D(pynari.FLOAT32, {radiuses[0]})")
            code.append(f"{var_name}.setParameter('vertex.radius', pynari.ARRAY1D, {var_name}_{radiuses_socket_varname})")

        if colors:
            code.append(f"{var_name}_{colors_socket_varname} = device.newArray1D(pynari.FLOAT32_VEC4, {colors[0]})")
            code.append(f"{var_name}.setParameter('primitive.color', pynari.ARRAY1D, {var_name}_{colors_socket_varname})")        
        
        code.append(f"{var_name}.commitParameters()")        
        
        return code


class PYNARICurveGeometryNode(PYNARIComposerNode):
    """Curve geometry node"""
    bl_idname = 'PYNARICurveGeometryNode'
    bl_label = 'Curve Geometry'
    bl_icon = 'CURVE_DATA'
    
    def init(self, context):
        self.inputs.new('PYNARINumpyArraySocket', "NP Vertices").link_limit = 1
        self.inputs.new('PYNARINumpyArraySocket', "NP Indices").link_limit = 1
        self.inputs.new('PYNARINumpyArraySocket', "NP Radiuses").link_limit = 1
        self.inputs.new('PYNARINumpyArraySocket', "NP Colors").link_limit = 1
        
        radius_socket = self.inputs.new('NodeSocketFloat', "Radius") #.link_limit = 1
        radius_socket.default_value = 0.1

        self.outputs.new('PYNARIGeometrySocket', "Geometry")
    
    def draw_buttons(self, context, layout):
        pass
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")

        var_name = self.get_var_name("Geometry")
        
        code.append(f"# Curve Geometry")
        if not auto_gen_enabled:
            code.append(f"{var_name} = device.newGeometry('curve')")

        vertices_socket_varname =  utility.str_to_var_name("NP Vertices")
        indices_socket_varname =  utility.str_to_var_name("NP Indices")
        radiuses_socket_varname =  utility.str_to_var_name("NP Radiuses")
        colors_socket_varname =  utility.str_to_var_name("NP Colors")         

        vertices = [link.from_node.get_var_name(vertices_socket_varname) for link in self.inputs["NP Vertices"].links]
        indices = [link.from_node.get_var_name(indices_socket_varname) for link in self.inputs["NP Indices"].links]
        radiuses = [link.from_node.get_var_name(radiuses_socket_varname) for link in self.inputs["NP Radiuses"].links]
        colors = [link.from_node.get_var_name(colors_socket_varname) for link in self.inputs["NP Colors"].links]        

        if vertices:
            code.append(f"{var_name}_{vertices_socket_varname} = device.newArray1D(pynari.FLOAT32_VEC3, {vertices[0]})")
            code.append(f"{var_name}.setParameter('vertex.position', pynari.ARRAY1D, {var_name}_{vertices_socket_varname})")

        if indices:
            code.append(f"{var_name}_{indices_socket_varname} = device.newArray1D(pynari.UINT32_VEC3, {indices[0]})")
            code.append(f"{var_name}.setParameter('primitive.index', pynari.ARRAY1D, {var_name}_{indices_socket_varname})            ")

        if radiuses:
            code.append(f"{var_name}_{radiuses_socket_varname} = device.newArray1D(pynari.FLOAT32, {radiuses[0]})")
            code.append(f"{var_name}.setParameter('primitive.radius', pynari.ARRAY1D, {var_name}_{radiuses_socket_varname})")
        else:
            radius = self.get_input_value_or_linked("Radius")
            code.append(f"{var_name}.setParameter('radius', pynari.FLOAT32, {radius})")

        if colors:
            code.append(f"{var_name}_{colors_socket_varname} = device.newArray1D(pynari.FLOAT32_VEC4, {colors[0]})")
            code.append(f"{var_name}.setParameter('primitive.color', pynari.ARRAY1D, {var_name}_{colors_socket_varname})")        
        
        code.append(f"{var_name}.commitParameters()")        
        
        return code


class PYNARIQuadGeometryNode(PYNARIComposerNode):
    """Quad geometry node"""
    bl_idname = 'PYNARIQuadGeometryNode'
    bl_label = 'Quad Geometry'
    bl_icon = 'MESH_PLANE'
    
    def init(self, context):
        self.inputs.new('PYNARINumpyArraySocket', "NP Indices").link_limit = 1
        self.inputs.new('PYNARINumpyArraySocket', "NP Vertices").link_limit = 1
        self.inputs.new('PYNARINumpyArraySocket', "NP Normals").link_limit = 1
        self.inputs.new('PYNARINumpyArraySocket', "NP Colors").link_limit = 1

        self.outputs.new('PYNARIGeometrySocket', "Geometry")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "position")
        layout.prop(self, "size")
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name("Geometry")
        
        code.append(f"# Quad Geometry")
        if not auto_gen_enabled:
            code.append(f"{var_name} = device.newGeometry('quad')")
        
        indices_socket_varname =  utility.str_to_var_name("NP Indices")
        vertices_socket_varname =  utility.str_to_var_name("NP Vertices")
        normals_socket_varname =  utility.str_to_var_name("NP Normals")
        colors_socket_varname =  utility.str_to_var_name("NP Colors")      

        indices = [link.from_node.get_var_name(indices_socket_varname) for link in self.inputs["NP Indices"].links]
        vertices = [link.from_node.get_var_name(vertices_socket_varname) for link in self.inputs["NP Vertices"].links]
        normals = [link.from_node.get_var_name(normals_socket_varname) for link in self.inputs["NP Normals"].links]
        colors = [link.from_node.get_var_name(colors_socket_varname) for link in self.inputs["NP Colors"].links]
        
        if vertices:
            code.append(f"{var_name}_{vertices_socket_varname} = device.newArray1D(pynari.FLOAT32_VEC3, {vertices[0]})")
            code.append(f"{var_name}.setParameter('vertex.position', pynari.ARRAY1D, {var_name}_{vertices_socket_varname})")

        if indices:
            code.append(f"{var_name}_{indices_socket_varname} = device.newArray1D(pynari.UINT32_VEC3, {indices[0]})")
            code.append(f"{var_name}.setParameter('primitive.index', pynari.ARRAY1D, {var_name}_{indices_socket_varname})")

        if normals:
            code.append(f"{var_name}_{normals_socket_varname} = device.newArray1D(pynari.FLOAT32_VEC3, {normals[0]})")
            code.append(f"{var_name}.setParameter('vertex.normal', pynari.ARRAY1D, {var_name}_{normals_socket_varname})")
        if colors:
            code.append(f"{var_name}_{colors_socket_varname} = device.newArray1D(pynari.FLOAT32_VEC4, {colors[0]})")
            code.append(f"{var_name}.setParameter('vertex.color', pynari.ARRAY1D, {var_name}_{colors_socket_varname})")                        

        code.append(f"{var_name}.commitParameters()")        
        
        return code


##################################
# Material Nodes
##################################

class PYNARIMatteMaterialNode(PYNARIComposerNode):
    """Matte material node"""
    bl_idname = 'PYNARIMatteMaterialNode'
    bl_label = 'Matte Material'
    bl_icon = 'MATERIAL'
    
    def init(self, context):
        color_socket = self.inputs.new('NodeSocketColor', "Color") #.link_limit = 1
        color_socket.default_value = (0.8, 0.8, 0.8, 1.0)
        
        opacity_socket = self.inputs.new('NodeSocketFloat', "Opacity") #.link_limit = 1
        opacity_socket.default_value = 1.0
        
        self.outputs.new('PYNARIMaterialSocket', "Material")
    
    def draw_buttons(self, context, layout):
        pass
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name("Material")
        
        color = self.get_input_value_or_linked("Color", use_tuple=True)
        if not self.inputs["Color"].is_linked:
            color = color[:3]
        opacity = self.get_input_value_or_linked("Opacity")
        
        code.append(f"# Matte Material")
        if not auto_gen_enabled:
            code.append(f"{var_name} = device.newMaterial('matte')")
        code.append(f"{var_name}.setParameter('color', pynari.float3, {color})")
        code.append(f"{var_name}.setParameter('opacity', pynari.FLOAT32, {opacity})")
        code.append(f"{var_name}.commitParameters()")
        
        return code


class PYNARIPhysicallyBasedMaterialNode(PYNARIComposerNode):
    """Physically based material node"""
    bl_idname = 'PYNARIPhysicallyBasedMaterialNode'
    bl_label = 'Physically Based Material'
    bl_icon = 'MATERIAL'
    
    def init(self, context):
        base_color_socket = self.inputs.new('NodeSocketColor', "Base Color") #.link_limit = 1
        base_color_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        
        emissive_socket = self.inputs.new('NodeSocketColor', "Emissive") #.link_limit = 1
        emissive_socket.default_value = (0.0, 0.0, 0.0, 1.0)
        
        specular_color_socket = self.inputs.new('NodeSocketColor', "Specular Color") #.link_limit = 1
        specular_color_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        
        opacity_socket = self.inputs.new('NodeSocketFloat', "Opacity") #.link_limit = 1
        opacity_socket.default_value = 1.0
        
        metallic_socket = self.inputs.new('NodeSocketFloat', "Metallic") #.link_limit = 1
        metallic_socket.default_value = 1.0
        
        roughness_socket = self.inputs.new('NodeSocketFloat', "Roughness") #.link_limit = 1
        roughness_socket.default_value = 1.0
        
        specular_socket = self.inputs.new('NodeSocketFloat', "Specular") #.link_limit = 1
        specular_socket.default_value = 0.0
        
        transmission_socket = self.inputs.new('NodeSocketFloat', "Transmission") #.link_limit = 1
        transmission_socket.default_value = 0.0
        
        ior_socket = self.inputs.new('NodeSocketFloat', "IOR") #.link_limit = 1
        ior_socket.default_value = 1.5
        
        self.outputs.new('PYNARIMaterialSocket', "Material")
    
    def draw_buttons(self, context, layout):
        pass
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name("Material")
        
        base_color = self.get_input_value_or_linked("Base Color", use_tuple=True)
        if not self.inputs["Base Color"].is_linked:
            base_color = base_color[:3]
        emissive = self.get_input_value_or_linked("Emissive", use_tuple=True)
        if not self.inputs["Emissive"].is_linked:
            emissive = emissive[:3]
        specular_color = self.get_input_value_or_linked("Specular Color", use_tuple=True)
        if not self.inputs["Specular Color"].is_linked:
            specular_color = specular_color[:3]
        opacity = self.get_input_value_or_linked("Opacity")
        metallic = self.get_input_value_or_linked("Metallic")
        roughness = self.get_input_value_or_linked("Roughness")
        specular = self.get_input_value_or_linked("Specular")
        transmission = self.get_input_value_or_linked("Transmission")
        ior = self.get_input_value_or_linked("IOR")
        
        code.append(f"# Physically Based Material")
        if not auto_gen_enabled:
            code.append(f"{var_name} = device.newMaterial('physicallyBased')")
        code.append(f"{var_name}.setParameter('baseColor', pynari.float3, {base_color})")
        code.append(f"{var_name}.setParameter('emissive', pynari.float3, {emissive})")
        code.append(f"{var_name}.setParameter('specularColor', pynari.float3, {specular_color})")
        code.append(f"{var_name}.setParameter('opacity', pynari.FLOAT32, {opacity})")
        code.append(f"{var_name}.setParameter('metallic', pynari.FLOAT32, {metallic})")
        code.append(f"{var_name}.setParameter('roughness', pynari.FLOAT32, {roughness})")
        code.append(f"{var_name}.setParameter('specular', pynari.FLOAT32, {specular})")
        code.append(f"{var_name}.setParameter('transmission', pynari.FLOAT32, {transmission})")
        code.append(f"{var_name}.setParameter('ior', pynari.FLOAT32, {ior})")
        code.append(f"{var_name}.commitParameters()")
        
        return code


class PYNARIBlenderMaterialNode(PYNARIComposerNode):
    """Blender material node - extracts values from Blender material shader"""
    bl_idname = 'PYNARIBlenderMaterialNode'
    bl_label = 'Blender Material'
    bl_icon = 'MATERIAL'
    
    blender_material: PointerProperty(  # type: ignore
        name="Material",
        type=bpy.types.Material,
        description="Blender material to extract shader properties from",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    def init(self, context):
        self.outputs.new('PYNARIMaterialSocket', "Material")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "blender_material")
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name("Material")
        
        # Extract properties from Blender material at design time
        base_color = (0.8, 0.8, 0.8)
        emissive = (0.0, 0.0, 0.0)
        specular_color = (1.0, 1.0, 1.0)
        opacity = 1.0
        metallic = 0.0
        roughness = 0.5
        specular = 0.5
        transmission = 0.0
        ior = 1.5
        
        if self.blender_material and self.blender_material.use_nodes:
            # Find Principled BSDF node
            bsdf_node = None
            for node in self.blender_material.node_tree.nodes:
                if node.type == 'BSDF_PRINCIPLED':
                    bsdf_node = node
                    break
            
            if bsdf_node:
                # Extract base color
                base_color_input = bsdf_node.inputs.get('Base Color')
                if base_color_input:
                    base_color = tuple(base_color_input.default_value[:3])
                
                # Extract emission color
                emission_input = bsdf_node.inputs.get('Emission Color') or bsdf_node.inputs.get('Emission')
                if emission_input:
                    if hasattr(emission_input.default_value, '__len__') and len(emission_input.default_value) >= 3:
                        emissive = tuple(emission_input.default_value[:3])
                    else:
                        emissive = (emission_input.default_value, emission_input.default_value, emission_input.default_value)
                
                # Extract metallic
                metallic_input = bsdf_node.inputs.get('Metallic')
                if metallic_input:
                    metallic = metallic_input.default_value
                
                # Extract roughness
                roughness_input = bsdf_node.inputs.get('Roughness')
                if roughness_input:
                    roughness = roughness_input.default_value
                
                # Extract specular
                specular_input = bsdf_node.inputs.get('Specular') or bsdf_node.inputs.get('Specular IOR Level')
                if specular_input:
                    specular = specular_input.default_value
                
                # Extract transmission
                transmission_input = bsdf_node.inputs.get('Transmission') or bsdf_node.inputs.get('Transmission Weight')
                if transmission_input:
                    transmission = transmission_input.default_value
                
                # Extract IOR
                ior_input = bsdf_node.inputs.get('IOR')
                if ior_input:
                    ior = ior_input.default_value
                
                # Extract alpha (opacity)
                alpha_input = bsdf_node.inputs.get('Alpha')
                if alpha_input:
                    opacity = alpha_input.default_value
                
                # Extract specular tint (use as specular color approximation)
                specular_tint_input = bsdf_node.inputs.get('Specular Tint')
                if specular_tint_input and base_color_input:
                    tint = specular_tint_input.default_value
                    specular_color = tuple(c * tint + 1.0 * (1.0 - tint) for c in base_color)
        
        code.append(f"# Blender Material")
        if not auto_gen_enabled:
            code.append(f"{var_name} = device.newMaterial('physicallyBased')")
        code.append(f"{var_name}.setParameter('baseColor', pynari.float3, {base_color})")
        code.append(f"{var_name}.setParameter('emissive', pynari.float3, {emissive})")
        code.append(f"{var_name}.setParameter('specularColor', pynari.float3, {specular_color})")
        code.append(f"{var_name}.setParameter('opacity', pynari.FLOAT32, {opacity})")
        code.append(f"{var_name}.setParameter('metallic', pynari.FLOAT32, {metallic})")
        code.append(f"{var_name}.setParameter('roughness', pynari.FLOAT32, {roughness})")
        code.append(f"{var_name}.setParameter('specular', pynari.FLOAT32, {specular})")
        code.append(f"{var_name}.setParameter('transmission', pynari.FLOAT32, {transmission})")
        code.append(f"{var_name}.setParameter('ior', pynari.FLOAT32, {ior})")
        code.append(f"{var_name}.commitParameters()")
        
        return code


##################################
# Light Nodes
##################################

class PYNARIDirectionalLightNode(PYNARIComposerNode):
    """Directional light node"""
    bl_idname = 'PYNARIDirectionalLightNode'
    bl_label = 'Directional Light'
    bl_icon = 'LIGHT_SUN'
    
    def init(self, context):
        direction_socket = self.inputs.new('NodeSocketVector', "Direction") #.link_limit = 1
        direction_socket.default_value = (0.0, 0.0, -1.0)
        
        color_socket = self.inputs.new('NodeSocketColor', "Color") #.link_limit = 1
        color_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        
        irradiance_socket = self.inputs.new('NodeSocketFloat', "Irradiance") #.link_limit = 1
        irradiance_socket.default_value = 1.0
        
        self.outputs.new('PYNARILightSocket', "Light")
    
    def draw_buttons(self, context, layout):
        pass
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name("Light")
        
        direction = self.get_input_value_or_linked("Direction", use_tuple=True)
        color = self.get_input_value_or_linked("Color", use_tuple=True)
        if not self.inputs["Color"].is_linked:
            color = color[:3]
        irradiance = self.get_input_value_or_linked("Irradiance")
        
        code.append(f"# Directional Light")
        if not auto_gen_enabled:
            code.append(f"{var_name} = device.newLight('directional')")
        code.append(f"{var_name}.setParameter('direction', pynari.float3, {direction})")
        code.append(f"{var_name}.setParameter('color', pynari.float3, {color})")
        code.append(f"{var_name}.setParameter('irradiance', pynari.FLOAT32, {irradiance})")
        code.append(f"{var_name}.commitParameters()")
        
        return code


class PYNARIPointLightNode(PYNARIComposerNode):
    """Point light node"""
    bl_idname = 'PYNARIPointLightNode'
    bl_label = 'Point Light'
    bl_icon = 'LIGHT_POINT'
    
    def init(self, context):
        position_socket = self.inputs.new('NodeSocketVector', "Position") #.link_limit = 1
        position_socket.default_value = (0.0, 0.0, 0.0)
        
        color_socket = self.inputs.new('NodeSocketColor', "Color") #.link_limit = 1
        color_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        
        intensity_socket = self.inputs.new('NodeSocketFloat', "Intensity") #.link_limit = 1
        intensity_socket.default_value = 1.0
        
        radius_socket = self.inputs.new('NodeSocketFloat', "Radius") #.link_limit = 1
        radius_socket.default_value = 0.0
        
        self.outputs.new('PYNARILightSocket', "Light")
    
    def draw_buttons(self, context, layout):
        pass
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name("Light")
        
        position = self.get_input_value_or_linked("Position", use_tuple=True)
        color = self.get_input_value_or_linked("Color", use_tuple=True)
        if not self.inputs["Color"].is_linked:
            color = color[:3]
        intensity = self.get_input_value_or_linked("Intensity")
        radius = self.get_input_value_or_linked("Radius")
        
        code.append(f"# Point Light")
        if not auto_gen_enabled:
            code.append(f"{var_name} = device.newLight('point')")
        code.append(f"{var_name}.setParameter('position', pynari.FLOAT32_VEC3, {position})")
        code.append(f"{var_name}.setParameter('color', pynari.float3, {color})")
        code.append(f"{var_name}.setParameter('intensity', pynari.FLOAT32, {intensity})")
        code.append(f"{var_name}.setParameter('radius', pynari.FLOAT32, {radius})")
        code.append(f"{var_name}.commitParameters()")
        
        return code


class PYNARIQuadLightNode(PYNARIComposerNode):
    """Quad light node"""
    bl_idname = 'PYNARIQuadLightNode'
    bl_label = 'Quad Light'
    bl_icon = 'LIGHT_AREA'
    
    def init(self, context):
        position_socket = self.inputs.new('NodeSocketVector', "Position") #.link_limit = 1
        position_socket.default_value = (0.0, 0.0, 0.0)
        
        edge1_socket = self.inputs.new('NodeSocketVector', "Edge 1") #.link_limit = 1
        edge1_socket.default_value = (1.0, 0.0, 0.0)
        
        edge2_socket = self.inputs.new('NodeSocketVector', "Edge 2") #.link_limit = 1
        edge2_socket.default_value = (0.0, 1.0, 0.0)
        
        color_socket = self.inputs.new('NodeSocketColor', "Color") #.link_limit = 1
        color_socket.default_value = (1.0, 1.0, 1.0, 1.0)
        
        intensity_socket = self.inputs.new('NodeSocketFloat', "Intensity") #.link_limit = 1
        intensity_socket.default_value = 1.0
        
        self.outputs.new('PYNARILightSocket', "Light")
    
    def draw_buttons(self, context, layout):
        pass
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name("Light")
        
        position = self.get_input_value_or_linked("Position", use_tuple=True)
        edge1 = self.get_input_value_or_linked("Edge 1", use_tuple=True)
        edge2 = self.get_input_value_or_linked("Edge 2", use_tuple=True)
        color = self.get_input_value_or_linked("Color", use_tuple=True)
        if not self.inputs["Color"].is_linked:
            color = color[:3]
        intensity = self.get_input_value_or_linked("Intensity")
        
        code.append(f"# Quad Light")
        if not auto_gen_enabled:
            code.append(f"{var_name} = device.newLight('quad')")
        code.append(f"{var_name}.setParameter('position', pynari.FLOAT32_VEC3, {position})")
        code.append(f"{var_name}.setParameter('edge1', pynari.FLOAT32_VEC3, {edge1})")
        code.append(f"{var_name}.setParameter('edge2', pynari.FLOAT32_VEC3, {edge2})")
        code.append(f"{var_name}.setParameter('color', pynari.float3, {color})")
        code.append(f"{var_name}.setParameter('intensity', pynari.FLOAT32, {intensity})")
        code.append(f"{var_name}.commitParameters()")
        
        return code


##################################
# Value Nodes
##################################

class PYNARIStringValueNode(PYNARIComposerNode):
    """String value node"""
    bl_idname = 'PYNARIStringValueNode'
    bl_label = 'String Value'
    bl_icon = 'DRIVER'
    
    value: StringProperty(  # type: ignore
        name="Value",
        default="",
        description="String value",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    def init(self, context):
        self.outputs.new('NodeSocketString', "Value")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "value")
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name("Value")
        code.append(f"# String Value")
        code.append(f"{var_name} = '{self.value}'")
        return code


class PYNARIFloatValueNode(PYNARIComposerNode):
    """Float value node"""
    bl_idname = 'PYNARIFloatValueNode'
    bl_label = 'Float Value'
    bl_icon = 'DRIVER'
    
    value: FloatProperty(  # type: ignore
        name="Value",
        default=0.0,
        description="Float value",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    def init(self, context):
        self.outputs.new('NodeSocketFloat', "Value")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "value")
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name("Value")
        code.append(f"# Float Value")
        code.append(f"{var_name} = {self.value}")
        return code


class PYNARIFloatVector3DValueNode(PYNARIComposerNode):
    """Float vector value node"""
    bl_idname = 'PYNARIFloatVector3DValueNode'
    bl_label = 'Float Vector 3D Value'
    bl_icon = 'ORIENTATION_GLOBAL'
    
    value: FloatVectorProperty(  # type: ignore
        name="Value",
        default=(0.0, 0.0, 0.0),
        size=3,
        description="Float vector value",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    def init(self, context):
        self.outputs.new('NodeSocketVector', "Value")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "value")
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name("Value")
        code.append(f"# Float Vector Value")
        code.append(f"{var_name} = {tuple(self.value)}")
        return code

class PYNARIFloatVector2DValueNode(PYNARIComposerNode):
    """Float vector value node"""
    bl_idname = 'PYNARIFloatVector2DValueNode'
    bl_label = 'Float Vector 2D Value'
    bl_icon = 'ORIENTATION_GLOBAL'
    
    value: FloatVectorProperty(  # type: ignore
        name="Value",
        default=(0.0, 0.0),
        size=2,
        description="Float vector value",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    def init(self, context):
        self.outputs.new('NodeSocketVector2D', "Value")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "value")
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name("Value")
        code.append(f"# Float Vector Value")
        code.append(f"{var_name} = {tuple(self.value)}")
        return code

class PYNARIIntValueNode(PYNARIComposerNode):
    """Int value node"""
    bl_idname = 'PYNARIIntValueNode'
    bl_label = 'Int Value'
    bl_icon = 'LINENUMBERS_ON'
    
    value: IntProperty(  # type: ignore
        name="Value",
        default=0,
        description="Integer value",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    def init(self, context):
        self.outputs.new('NodeSocketInt', "Value")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "value")
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name("Value")
        code.append(f"# Int Value")
        code.append(f"{var_name} = {self.value}")
        return code


##################################
# Math Nodes
##################################

class PYNARIIntMathNode(PYNARIComposerNode):
    """Int math operations node"""
    bl_idname = 'PYNARIIntMathNode'
    bl_label = 'Int Math'
    bl_icon = 'LINENUMBERS_ON'
    
    operation: EnumProperty(  # type: ignore
        name="Operation",
        items=[
            ('ADD', "Add", "A + B"),
            ('SUBTRACT', "Subtract", "A - B"),
            ('MULTIPLY', "Multiply", "A * B"),
            ('DIVIDE', "Divide", "A / B"),
        ],
        default='ADD',
        description="Math operation to perform",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    def init(self, context):
        a_socket = self.inputs.new('NodeSocketInt', "A") #.link_limit = 1
        a_socket.default_value = 0
        
        b_socket = self.inputs.new('NodeSocketInt', "B") #.link_limit = 1
        b_socket.default_value = 0
        
        self.outputs.new('NodeSocketInt', "Result")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "operation", text="")
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name("Result")
        
        if not self.inputs["A"].is_linked:
            a = self.inputs["A"].default_value
        else:
            a_socket_varname = utility.str_to_var_name("A")
            a = [link.from_node.get_var_name(a_socket_varname) for link in self.inputs["A"].links]
            a = a[0]
        
        if not self.inputs["B"].is_linked:
            b = self.inputs["B"].default_value
        else:
            b_socket_varname = utility.str_to_var_name("B")
            b = [link.from_node.get_var_name(b_socket_varname) for link in self.inputs["B"].links]
            b = b[0]
        
        ops = {
            'ADD': '+',
            'SUBTRACT': '-',
            'MULTIPLY': '*',
            'DIVIDE': '//'
        }
        op = ops[self.operation]
        
        code.append(f"# Int Math ({self.operation})")
        code.append(f"{var_name} = int({a} {op} {b})")
        
        return code


class PYNARIFloatMathNode(PYNARIComposerNode):
    """Float math operations node"""
    bl_idname = 'PYNARIFloatMathNode'
    bl_label = 'Float Math'
    bl_icon = 'DRIVER'
    
    operation: EnumProperty(  # type: ignore
        name="Operation",
        items=[
            ('ADD', "Add", "A + B"),
            ('SUBTRACT', "Subtract", "A - B"),
            ('MULTIPLY', "Multiply", "A * B"),
            ('DIVIDE', "Divide", "A / B"),
        ],
        default='ADD',
        description="Math operation to perform",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    def init(self, context):
        a_socket = self.inputs.new('NodeSocketFloat', "A") #.link_limit = 1
        a_socket.default_value = 0.0
        
        b_socket = self.inputs.new('NodeSocketFloat', "B") #.link_limit = 1
        b_socket.default_value = 0.0
        
        self.outputs.new('NodeSocketFloat', "Result")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "operation", text="")
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name("Result")
        
        a = self.get_input_value_or_linked("A")
        b = self.get_input_value_or_linked("B")
        
        ops = {
            'ADD': '+',
            'SUBTRACT': '-',
            'MULTIPLY': '*',
            'DIVIDE': '/'
        }
        op = ops[self.operation]
        
        code.append(f"# Float Math ({self.operation})")
        code.append(f"{var_name} = {a} {op} {b}")
        
        return code


class PYNARIVectorMathNode(PYNARIComposerNode):
    """Vector math operations node"""
    bl_idname = 'PYNARIVectorMathNode'
    bl_label = 'Vector Math'
    bl_icon = 'ORIENTATION_GIMBAL'
    
    operation: EnumProperty(  # type: ignore
        name="Operation",
        items=[
            ('ADD', "Add", "A + B"),
            ('SUBTRACT', "Subtract", "A - B"),
            ('MULTIPLY', "Multiply", "A * B (component-wise)"),
            ('DIVIDE', "Divide", "A / B (component-wise)"),
        ],
        default='ADD',
        description="Math operation to perform",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    def init(self, context):
        a_socket = self.inputs.new('NodeSocketVector', "A") #.link_limit = 1
        a_socket.default_value = (0.0, 0.0, 0.0)
        
        b_socket = self.inputs.new('NodeSocketVector', "B") #.link_limit = 1
        b_socket.default_value = (0.0, 0.0, 0.0)
        
        self.outputs.new('NodeSocketVector', "Result")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "operation", text="")
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name("Result")
        
        if not self.inputs["A"].is_linked:
            a = tuple(self.inputs["A"].default_value)
        else:
            a_socket_varname = utility.str_to_var_name("A")
            a = [link.from_node.get_var_name(a_socket_varname) for link in self.inputs["A"].links]
            a = a[0]
        
        if not self.inputs["B"].is_linked:
            b = tuple(self.inputs["B"].default_value)
        else:
            b_socket_varname = utility.str_to_var_name("B")
            b = [link.from_node.get_var_name(b_socket_varname) for link in self.inputs["B"].links]
            b = b[0]
        
        code.append(f"# Vector Math ({self.operation})")
        
        if self.operation == 'ADD':
            code.append(f"{var_name} = tuple(a + b for a, b in zip({a}, {b}))")
        elif self.operation == 'SUBTRACT':
            code.append(f"{var_name} = tuple(a - b for a, b in zip({a}, {b}))")
        elif self.operation == 'MULTIPLY':
            code.append(f"{var_name} = tuple(a * b for a, b in zip({a}, {b}))")
        elif self.operation == 'DIVIDE':
            code.append(f"{var_name} = tuple(a / b if b != 0 else 0 for a, b in zip({a}, {b}))")
        
        return code


class PYNARIDimensionToSpacingNode(PYNARIComposerNode):
    """Dimension to spacing conversion node"""
    bl_idname = 'PYNARIDimensionToSpacingNode'
    bl_label = 'Dimension to Spacing'
    bl_icon = 'DRIVER_TRANSFORM'
    
    def init(self, context):
        resolution_socket = self.inputs.new('NodeSocketVector', "Dimension") #.link_limit = 1
        resolution_socket.default_value = (0.0, 0.0, 0.0)
        
        self.outputs.new('NodeSocketVector', "Spacing")
    
    def draw_buttons(self, context, layout):
        pass
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name("Spacing")
        
        if not self.inputs["Dimension"].is_linked:
            resolution = tuple(self.inputs["Dimension"].default_value)
        else:
            resolution_socket_varname = utility.str_to_var_name("Dimension")
            resolution = [link.from_node.get_var_name(resolution_socket_varname) for link in self.inputs["Dimension"].links]
            resolution = resolution[0]
        
        code.append(f"# Dimension to Spacing Conversion")
        code.append(f"{var_name} = tuple(2/(r-1) if r > 1 else 1.0 for r in {resolution})")
        
        return code


class PYNARIFindMinMaxNode(PYNARIComposerNode):
    """Find min and max value from numpy array"""
    bl_idname = 'PYNARIFindMinMaxNode'
    bl_label = 'Find Min Max'
    bl_icon = 'SORTSIZE'
    
    def init(self, context):
        self.inputs.new('PYNARINumpyArraySocket', "NP Data").link_limit = 1
        
        self.outputs.new('NodeSocketVector2D', "Range")
    
    def draw_buttons(self, context, layout):
        pass
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name("Range")
        
        # data_socket_varname = utility.str_to_var_name("NP Data")
        data = [link.from_node.get_var_name(link.from_socket.name) for link in self.inputs["NP Data"].links]
        
        code.append(f"# Find Min Max")
        if data:
            code.append(f"{var_name} = (float(np.min({data[0]})), float(np.max({data[0]})))")
        else:
            code.append(f"{var_name} = (0.0, 1.0)")
        
        return code


##################################
# Volume Nodes
##################################
#TODO
class PYNARITransferFunction1DVolumeNode(PYNARIComposerNode):
    """Transfer function 1D volume node"""
    bl_idname = 'PYNARITransferFunction1DVolumeNode'
    bl_label = 'Transfer Function 1D Volume'
    bl_icon = 'VOLUME_DATA'
    
    def init(self, context):
        self.inputs.new('PYNARISpatialFieldSocket', "Field").link_limit = 1
        self.inputs.new('PYNARINumpyArraySocket', "NP Colors").link_limit = 1
        
        # Create input sockets for properties
        opacity_socket = self.inputs.new('NodeSocketFloat', "Opacity") #.link_limit = 1
        opacity_socket.default_value = 1.0
        # opacity_socket.min_value = 0.0
        # opacity_socket.max_value = 1.0
        
        unit_distance_socket = self.inputs.new('NodeSocketFloat', "Unit Distance") #.link_limit = 1
        unit_distance_socket.default_value = 1.0
        # unit_distance_socket.min_value = 0.001
        
        value_range_socket = self.inputs.new('NodeSocketVector2D', "Range") #.link_limit = 1
        value_range_socket.default_value = (0.0, 1.0)

        self.outputs.new('PYNARIVolumeSocket', "Volume")
    
    def draw_buttons(self, context, layout):
        # Properties are now shown as input sockets
        pass
    
    def generate_code(self, auto_gen_enabled=False):
        code = []

        if auto_gen_enabled:
            for link in self.inputs["NP Colors"].links:
                code.extend(link.from_node.generate_code(auto_gen_enabled))

        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name("Volume")
        field = self.get_input_value("Field")
        
        # Get values from input sockets
        opacity = self.get_input_value_or_linked("Opacity")
        unit_distance = self.get_input_value_or_linked("Unit Distance")
        value_range = self.get_input_value_or_linked("Range", use_tuple=True)
        if not self.inputs["Range"].is_linked:
            value_range = (value_range[0], value_range[1])
        
        code.append(f"# Transfer Function Volume")
        if not auto_gen_enabled:
            code.append(f"{var_name} = device.newVolume('transferFunction1D')")
        code.append(f"{var_name}.setParameter('value', pynari.SPATIAL_FIELD, {field})")
        code.append(f"{var_name}.setParameter('opacity', pynari.FLOAT32, {opacity})")
        code.append(f"{var_name}.setParameter('unitDistance', pynari.FLOAT32, {unit_distance})")
        code.append(f"{var_name}.setParameter('valueRange', pynari.FLOAT32_BOX1, {value_range})")
        
        colors = [link.from_node.get_var_name(link.from_socket.name) for link in self.inputs["NP Colors"].links]

        colors_socket_varname =  utility.str_to_var_name("NP Colors")
        if colors:
            code.append(f"{var_name}_{colors_socket_varname} = device.newArray1D(pynari.float4, {colors[0]})")
            code.append(f"{var_name}.setParameter('color', pynari.ARRAY1D, {var_name}_{colors_socket_varname})")                        
        
        
        code.append(f"{var_name}.commitParameters()")
        
        return code


##################################
# Transfer Function Utility Nodes
##################################

class PYNARIColorRampNode(PYNARIComposerNode):
    """Color ramp node for creating transfer function colors"""
    bl_idname = 'PYNARIColorRampNode'
    bl_label = 'Color Ramp'
    bl_icon = 'COLOR'
    
    num_samples: IntProperty(  # type: ignore
        name="Samples",
        default=256,
        min=2,
        max=4096,
        description="Number of color samples to generate",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    # Color stop 1
    position_0: FloatProperty(  # type: ignore
        name="Position 0",
        default=0.0,
        min=0.0,
        max=1.0,
        description="Position of color stop (0-1)",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    color_0: FloatVectorProperty(  # type: ignore
        name="Color 0",
        default=(0.0, 0.0, 0.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        subtype='COLOR',
        description="RGBA color at this stop",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    # Color stop 2
    position_1: FloatProperty(  # type: ignore
        name="Position 1",
        default=0.25,
        min=0.0,
        max=1.0,
        description="Position of color stop (0-1)",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    color_1: FloatVectorProperty(  # type: ignore
        name="Color 1",
        default=(0.0, 0.0, 1.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        subtype='COLOR',
        description="RGBA color at this stop",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    # Color stop 3
    position_2: FloatProperty(  # type: ignore
        name="Position 2",
        default=0.5,
        min=0.0,
        max=1.0,
        description="Position of color stop (0-1)",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    color_2: FloatVectorProperty(  # type: ignore
        name="Color 2",
        default=(0.0, 1.0, 0.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        subtype='COLOR',
        description="RGBA color at this stop",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    # Color stop 4
    position_3: FloatProperty(  # type: ignore
        name="Position 3",
        default=0.75,
        min=0.0,
        max=1.0,
        description="Position of color stop (0-1)",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    color_3: FloatVectorProperty(  # type: ignore
        name="Color 3",
        default=(1.0, 1.0, 0.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        subtype='COLOR',
        description="RGBA color at this stop",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    # Color stop 5
    position_4: FloatProperty(  # type: ignore
        name="Position 4",
        default=1.0,
        min=0.0,
        max=1.0,
        description="Position of color stop (0-1)",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    color_4: FloatVectorProperty(  # type: ignore
        name="Color 4",
        default=(1.0, 0.0, 0.0, 1.0),
        size=4,
        min=0.0,
        max=1.0,
        subtype='COLOR',
        description="RGBA color at this stop",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    interpolation: EnumProperty(  # type: ignore
        name="Interpolation",
        items=[
            ('linear', "Linear", "Linear interpolation between color stops"),
            ('constant', "Constant", "No interpolation, constant color regions"),
        ],
        default='linear',
        description="Interpolation method between color stops",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    def init(self, context):
        self.outputs.new('PYNARINumpyArraySocket', "NP Colors")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "num_samples")
        layout.prop(self, "interpolation")
        layout.separator()
        
        box = layout.box()
        box.label(text="Color Stops:")
        
        for i in range(5):
            row = box.row(align=True)
            row.prop(self, f"position_{i}", text=f"Stop {i}")
            row.prop(self, f"color_{i}", text="")
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name("NP Colors")

        # colors_socket_varname =  utility.str_to_var_name("NP Colors")
        
        code.append(f"# Color Ramp")
        code.append(f"")
        
        code.append(f"{var_name} = np.array([")
        for i in range(5):
            color = getattr(self, f"color_{i}")
            code.append(f"    [{color[0]}, {color[1]}, {color[2]}, {color[3]}],")
        code.append(f"], dtype=np.float32)")
        code.append(f"")        

        return code


class PYNARIBlenderColorRampNode(PYNARIComposerNode):
    """Blender Color Ramp node - extracts color ramp from Blender material shader"""
    bl_idname = 'PYNARIBlenderColorRampNode'
    bl_label = 'Blender Color Ramp'
    bl_icon = 'COLOR'
    
    blender_material: PointerProperty(  # type: ignore
        name="Material",
        type=bpy.types.Material,
        description="Blender material to extract color ramp from",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    num_samples: IntProperty(  # type: ignore
        name="Samples",
        default=256,
        min=2,
        max=4096,
        description="Number of color samples to evaluate from the color ramp",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    def init(self, context):
        self.outputs.new('PYNARINumpyArraySocket', "NP Colors")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "blender_material")
        layout.prop(self, "num_samples")
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name("NP Colors")
        #colors_socket_varname = utility.str_to_var_name("NP Colors")
        
        # Extract color ramp from Blender material at design time
        colors_list = []
        
        if self.blender_material and self.blender_material.use_nodes:
            # Find ColorRamp node in shader tree
            color_ramp_node = None
            for node in self.blender_material.node_tree.nodes:
                if node.type == 'VALTORGB':  # ColorRamp node type
                    color_ramp_node = node
                    break
            
            if color_ramp_node:
                # Evaluate color ramp at N evenly spaced positions
                for i in range(self.num_samples):
                    position = i / (self.num_samples - 1) if self.num_samples > 1 else 0.0
                    color = color_ramp_node.color_ramp.evaluate(position)
                    colors_list.append([color[0], color[1], color[2], color[3]])
        
        if not colors_list:
            for i in range(self.num_samples):
                position = i / (self.num_samples - 1) if self.num_samples > 1 else 0.0
                # Simple default gradient from black to white
                colors_list.append([position, position, position, 1.0])
        
        code.append(f"# Blender Color Ramp")
        code.append(f"{var_name} = np.array([")
        for color in colors_list:
            code.append(f"    [{color[0]}, {color[1]}, {color[2]}, {color[3]}],")
        code.append(f"], dtype=np.float32)")
        code.append(f"")
        
        return code


##################################
# Spatial Field Nodes
##################################

class PYNARIUnstructuredFieldNode(PYNARIComposerNode):
    """Unstructured spatial field node"""
    bl_idname = 'PYNARIUnstructuredFieldNode'
    bl_label = 'Unstructured Field'
    bl_icon = 'SNAP_VOLUME'
    
    use_vertex_data: BoolProperty(  # type: ignore
        name="Use Vertex Data",
        default=True,
        description="Use vertex (point) data instead of cell data",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    def init(self, context):
        self.inputs.new('PYNARINumpyArraySocket', "NP Vertices").link_limit = 1
        self.inputs.new('PYNARINumpyArraySocket', "NP Cells Indexes").link_limit = 1
        self.inputs.new('PYNARINumpyArraySocket', "NP Cells Index First").link_limit = 1
        self.inputs.new('PYNARINumpyArraySocket', "NP Cell Types").link_limit = 1
        self.inputs.new('PYNARINumpyArraySocket', "NP Vertex Data").link_limit = 1
        self.inputs.new('PYNARINumpyArraySocket', "NP Cell Data").link_limit = 1

        self.outputs.new('PYNARISpatialFieldSocket', "Field")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "use_vertex_data")
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name("Field")
        
        code.append(f"# Unstructured Field")
        if not auto_gen_enabled:
            code.append(f"{var_name} = device.newSpatialField('unstructured')")

        # vertices_socket_varname = utility.str_to_var_name("NP Vertices")
        # cells_indexes_socket_varname = utility.str_to_var_name("NP Cells Indexes")
        # cells_index_first_socket_varname = utility.str_to_var_name("NP Cells Index First")
        # cell_types_socket_varname = utility.str_to_var_name("NP Cell Types")
        # vertex_data_socket_varname = utility.str_to_var_name("NP Vertex Data")
        # cell_data_socket_varname = utility.str_to_var_name("NP Cell Data")

        vertices = [link.from_node.get_var_name(link.from_socket.name) for link in self.inputs["NP Vertices"].links]
        cells_indexes = [link.from_node.get_var_name(link.from_socket.name) for link in self.inputs["NP Cells Indexes"].links]
        cells_index_first = [link.from_node.get_var_name(link.from_socket.name) for link in self.inputs["NP Cells Index First"].links]
        cell_types = [link.from_node.get_var_name(link.from_socket.name) for link in self.inputs["NP Cell Types"].links]
        vertex_data = [link.from_node.get_var_name(link.from_socket.name) for link in self.inputs["NP Vertex Data"].links]
        cell_data = [link.from_node.get_var_name(link.from_socket.name) for link in self.inputs["NP Cell Data"].links]

        if vertices:
            code.append(f"{var_name}_array_vertex = device.newArray(pynari.FLOAT32_VEC3, {vertices[0]})")
            code.append(f"{var_name}.setParameter('vertex.position', pynari.ARRAY, {var_name}_array_vertex)")

        if vertex_data and self.use_vertex_data:
            code.append(f"{var_name}_array_vertex_data = device.newArray(pynari.FLOAT32, {vertex_data[0]})")
            code.append(f"{var_name}.setParameter('vertex.data', pynari.float, {var_name}_array_vertex_data)")
        
        if cell_data and not self.use_vertex_data:
            code.append(f"{var_name}_array_cell_data = device.newArray(pynari.FLOAT32, {cell_data[0]})")
            code.append(f"{var_name}.setParameter('cell.data', pynari.ARRAY, {var_name}_array_cell_data)")

        if cells_indexes:
            code.append(f"{var_name}_array_cells_indexes = device.newArray(pynari.UINT32, {cells_indexes[0]})")
            code.append(f"{var_name}.setParameter('index', pynari.ARRAY, {var_name}_array_cells_indexes)")

        if cell_types:
            code.append(f"{var_name}_array_cell_types = device.newArray(pynari.UINT8, {cell_types[0]})")
            code.append(f"{var_name}.setParameter('cell.type', pynari.ARRAY, {var_name}_array_cell_types)")

        if cells_index_first:
            code.append(f"{var_name}_array_cells_index_first = device.newArray(pynari.UINT32, {cells_index_first[0]})")
            code.append(f"{var_name}.setParameter('cell.index', pynari.ARRAY, {var_name}_array_cells_index_first)")
        
        code.append(f"{var_name}.commitParameters()")
        
        return code


class PYNARIStructuredRegularFieldNode(PYNARIComposerNode):
    """Structured regular spatial field node"""
    bl_idname = 'PYNARIStructuredRegularFieldNode'
    bl_label = 'Structured Regular Field'
    bl_icon = 'SNAP_VOLUME'
    
    filter_type: EnumProperty(  # type: ignore
        name="Filter",
        items=[
            ('nearest', "Nearest", "Nearest neighbor filtering"),
            ('linear', "Linear", "Linear interpolation filtering"),
        ],
        default='linear',
        description="Filter used for reconstructing the field",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    def init(self, context):
        self.inputs.new('PYNARINumpyArraySocket', "NP Volume Data").link_limit = 1
        
        origin_socket = self.inputs.new('NodeSocketVector', "Origin") #.link_limit = 1
        origin_socket.default_value = (0.0, 0.0, 0.0)
        
        spacing_socket = self.inputs.new('NodeSocketVector', "Spacing") #.link_limit = 1
        spacing_socket.default_value = (1.0, 1.0, 1.0)

        self.outputs.new('PYNARISpatialFieldSocket', "Field")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "filter_type")
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name("Field")
        
        if not self.inputs["Origin"].is_linked:
            origin = tuple(self.inputs["Origin"].default_value)
        else:
            # origin_socket_varname = utility.str_to_var_name("Origin")
            origin = [link.from_node.get_var_name(link.from_socket.name) for link in self.inputs["Origin"].links]
            origin = origin[0]
        
        if not self.inputs["Spacing"].is_linked:
            spacing = tuple(self.inputs["Spacing"].default_value)
        else:
            # spacing_socket_varname = utility.str_to_var_name("Spacing")
            spacing = [link.from_node.get_var_name(link.from_socket.name) for link in self.inputs["Spacing"].links]
            spacing = spacing[0]
        
        code.append(f"# Structured Regular Field")
        if not auto_gen_enabled:
            code.append(f"{var_name} = device.newSpatialField('structuredRegular')")

        code.append(f"{var_name}.setParameter('origin', pynari.float3, {origin})")
        code.append(f"{var_name}.setParameter('spacing', pynari.float3, {spacing})")
        code.append(f"{var_name}.setParameter('filter', pynari.STRING, '{self.filter_type}')")
        
        data = [link.from_node.get_var_name(link.from_socket.name) for link in self.inputs["NP Volume Data"].links]

        volume_data_socket_varname =  utility.str_to_var_name("NP Volume Data")
        if data:
            code.append(f"{var_name}_{volume_data_socket_varname} = device.newArray3D(pynari.float, {data[0]})")
            code.append(f"{var_name}.setParameter('data', pynari.ARRAY3D, {var_name}_{volume_data_socket_varname})")
        
        code.append(f"{var_name}.commitParameters()")
        
        return code
##################################
# Sampler Nodes
##################################

class PYNARIImage2DSamplerNode(PYNARIComposerNode):
    """Image 2D sampler node"""
    bl_idname = 'PYNARIImage2DSamplerNode'
    bl_label = 'Image2D Sampler'
    bl_icon = 'TEXTURE'
    
    filter_type: EnumProperty(  # type: ignore
        name="Filter",
        items=[
            ('nearest', "Nearest", "Nearest neighbor filtering"),
            ('linear', "Linear", "Linear interpolation filtering"),
        ],
        default='linear',
        description="Filter of the sampler",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    wrap_mode: EnumProperty(  # type: ignore
        name="Wrap Mode",
        items=[
            ('clampToEdge', "Clamp To Edge", "Clamp coordinates to edge"),
            ('repeat', "Repeat", "Repeat texture coordinates"),
            ('mirrorRepeat', "Mirror Repeat", "Mirror and repeat texture coordinates"),
        ],
        default='clampToEdge',
        description="Wrap mode of the sampler for both dimensions",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    def init(self, context):
        self.outputs.new('PYNARISamplerSocket', "Sampler")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "filter_type")
        layout.prop(self, "wrap_mode")
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name("Sampler")
        
        code.append(f"# Image2D Sampler")
        if not auto_gen_enabled:
            code.append(f"{var_name} = device.newSampler('image2D')")
        code.append(f"# Example: create a simple texture")
        code.append(f"texture_data = np.random.rand(256, 256, 4).astype(np.float32)")
        code.append(f"{var_name}.setParameter('image', texture_data)")
        code.append(f"{var_name}.setParameter('filter', '{self.filter_type}')")
        code.append(f"{var_name}.setParameter('wrapMode1', '{self.wrap_mode}')")
        code.append(f"{var_name}.setParameter('wrapMode2', '{self.wrap_mode}')")
        code.append(f"{var_name}.commitParameters()")
        
        return code


##################################
# PyVista Data Reader Nodes
##################################

class PYNARIReadPyVistaPolyDataNode(PYNARIComposerNode):
    """Read PolyData from file (e.g., OBJ, STL, VTK) and output numpy arrays"""
    bl_idname = 'PYNARIReadPyVistaPolyDataNode'
    bl_label = 'Read PolyData (PyVista)'
    bl_icon = 'FILE_FOLDER'
    
    file_path: bpy.props.StringProperty(
        name="File",
        default="",
        description="Path to the mesh file (OBJ, STL, VTK, etc.)",
        subtype="FILE_PATH",
        #update=lambda self, context: self.auto_generate_node_code(context)
    ) # type: ignore

    file_path_remote: bpy.props.StringProperty(
        name="File",
        default="",
        description="Path to the mesh file (OBJ, STL, VTK, etc.)",
        #update=lambda self, context: self.auto_generate_node_code(context)
    ) # type: ignore     
    
    compute_normals: BoolProperty(  # type: ignore
        name="Compute Normals",
        default=False,
        description="Automatically compute normals if not present in the file",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )

    triangulate: BoolProperty(  # type: ignore
        name="Triangulate",
        default=True,
        description="Automatically triangulate the mesh if not already triangulated",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    def init(self, context):
        self.outputs.new('PYNARINumpyArraySocket', "NP Indices")
        self.outputs.new('PYNARINumpyArraySocket', "NP Vertices")
        self.outputs.new('PYNARINumpyArraySocket', "NP Normals")
        self.outputs.new('PYNARINumpyArraySocket', "NP Colors")
    
    def draw_buttons(self, context, layout):
        self.draw_file_path(layout)
        layout.prop(self, "compute_normals")
        layout.prop(self, "triangulate")
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name()

        indices_socket_varname =  utility.str_to_var_name("NP Indices")
        vertices_socket_varname =  utility.str_to_var_name("NP Vertices")        
        normals_socket_varname =  utility.str_to_var_name("NP Normals")
        colors_socket_varname =  utility.str_to_var_name("NP Colors")
        
        code.append(f"# Read PolyData: {self.get_file_path()}")
        code.append(f"import pyvista as pv")
        code.append(f"{var_name}_mesh = pv.read(r'{self.get_file_path()}')")
        if self.triangulate:
            code.append(f"{var_name}_mesh = {var_name}_mesh.triangulate()")
        code.append(f"")
        
        # Vertices
        code.append(f"# Extract vertices")
        code.append(f"{var_name}_{vertices_socket_varname} = np.asarray({var_name}_mesh.points, dtype=np.float32)")
        code.append(f"")      
        
        # Indices
        code.append(f"# Extract indices (triangular faces)")
        code.append(f"{var_name}_faces = np.asarray({var_name}_mesh.faces)")
        code.append(f"{var_name}_faces_reshaped = {var_name}_faces.reshape(-1, 4)")
        code.append(f"{var_name}_{indices_socket_varname} = {var_name}_faces_reshaped[:, 1:4].astype(np.uint32)")
        code.append(f"")
        
        # Normals
        if self.compute_normals:
            code.append(f"# Compute or extract normals")
            code.append(f"if {var_name}_mesh.point_normals is None or len({var_name}_mesh.point_normals) == 0:")
            code.append(f"    {var_name}_mesh.compute_normals(inplace=True)")
            code.append(f"{var_name}_{normals_socket_varname} = np.asarray({var_name}_mesh.point_normals, dtype=np.float32)")
        else:
            code.append(f"# Extract normals if available")
            code.append(f"if {var_name}_mesh.point_normals is not None and len({var_name}_mesh.point_normals) > 0:")
            code.append(f"    {var_name}_{normals_socket_varname} = np.asarray({var_name}_mesh.point_normals, dtype=np.float32)")
            code.append(f"else:")
            code.append(f"    {var_name}_{normals_socket_varname} = None")
        code.append(f"")
        
        # Colors
        code.append(f"# Extract colors if available")
        code.append(f"{var_name}_{colors_socket_varname} = None")
        code.append(f"if 'RGBA' in {var_name}_mesh.point_data:")
        code.append(f"    {var_name}_{colors_socket_varname} = np.asarray({var_name}_mesh.point_data['RGBA'], dtype=np.float32) / 255.0")
        code.append(f"elif 'RGB' in {var_name}_mesh.point_data:")
        code.append(f"    rgb = np.asarray({var_name}_mesh.point_data['RGB'], dtype=np.float32) / 255.0")
        code.append(f"    {var_name}_{colors_socket_varname} = np.c_[rgb, np.ones(rgb.shape[0], dtype=np.float32)]")
        code.append(f"elif {var_name}_mesh.active_scalars is not None:")
        code.append(f"    {var_name}_{colors_socket_varname} = np.asarray({var_name}_mesh.active_scalars, dtype=np.float32)")
        
        return code


class PYNARIReadPyVistaUnstructuredDataNode(PYNARIComposerNode):
    """Read unstructured mesh data from file (e.g., VTU) and output numpy arrays for vertices, cells, and data"""
    bl_idname = 'PYNARIReadPyVistaUnstructuredDataNode'
    bl_label = 'Read Unstructured Data (PyVista)'
    bl_icon = 'FILE_FOLDER'
    
    file_path: bpy.props.StringProperty(
        name="File",
        default="",
        description="Path to the unstructured mesh file (VTU, VTK, etc.)",
        subtype="FILE_PATH",
        #update=lambda self, context: self.auto_generate_node_code(context)
    ) # type: ignore

    file_path_remote: bpy.props.StringProperty(
        name="File",
        default="",
        description="Path to the unstructured mesh file (VTU, VTK, etc.)",
        #update=lambda self, context: self.auto_generate_node_code(context)
    ) # type: ignore
    
    scalar_field: StringProperty(  # type: ignore
        name="Scalar Field",
        default="temperature",
        description="Name of the scalar field to extract (leave empty for active scalars)",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    use_vertex_data: BoolProperty(  # type: ignore
        name="Use Vertex Data",
        default=True,
        description="Use vertex (point) data instead of cell data",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    def init(self, context):
        self.outputs.new('PYNARINumpyArraySocket', "NP Vertices")
        self.outputs.new('PYNARINumpyArraySocket', "NP Cells Indexes")
        self.outputs.new('PYNARINumpyArraySocket', "NP Cells Index First")
        self.outputs.new('PYNARINumpyArraySocket', "NP Cell Types")
        self.outputs.new('PYNARINumpyArraySocket', "NP Vertex Data")
        self.outputs.new('PYNARINumpyArraySocket', "NP Cell Data")
    
    def draw_buttons(self, context, layout):
        self.draw_file_path(layout)
        layout.prop(self, "scalar_field")
        layout.prop(self, "use_vertex_data")
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name()

        vertices_socket_varname = utility.str_to_var_name("NP Vertices")
        cells_indexes_socket_varname = utility.str_to_var_name("NP Cells Indexes")
        cells_index_first_socket_varname = utility.str_to_var_name("NP Cells Index First")
        cell_types_socket_varname = utility.str_to_var_name("NP Cell Types")
        vertex_data_socket_varname = utility.str_to_var_name("NP Vertex Data")
        cell_data_socket_varname = utility.str_to_var_name("NP Cell Data")
        
        code.append(f"# Read Unstructured Data: {self.get_file_path()}")
        code.append(f"import pyvista as pv")
        code.append(f"import sys")
        code.append(f"{var_name}_reader = pv.get_reader(r'{self.get_file_path()}')")
        code.append(f"{var_name}_mesh = {var_name}_reader.read()")
        code.append(f"")
        
        # Extract vertices
        code.append(f"# Extract vertices")
        code.append(f"{var_name}_{vertices_socket_varname} = {var_name}_mesh.points")
        code.append(f"")
        
        # Extract cell types
        code.append(f"# Extract cell types")
        code.append(f"{var_name}_{cell_types_socket_varname} = {var_name}_mesh.celltypes")
        code.append(f"")
        
        # Extract cells and process for PYNARI unstructured format
        code.append(f"# Process cells for PYNARI unstructured format")
        code.append(f"{var_name}_cells = {var_name}_mesh.cells")
        code.append(f"{var_name}_cells_indexes = []")
        code.append(f"{var_name}_cells_index_first = []")
        code.append(f"{var_name}_idx = 0")
        code.append(f"{var_name}_idx_newcells = 0")
        code.append(f"{var_name}_lencells = len({var_name}_cells)")
        code.append(f"while {var_name}_idx < {var_name}_lencells:")
        code.append(f"    {var_name}_cells_index_first.append({var_name}_idx_newcells)")
        code.append(f"    N = {var_name}_cells[{var_name}_idx]")
        code.append(f"    i1 = {var_name}_idx + 1")
        code.append(f"    i2 = i1 + N")
        code.append(f"    {var_name}_cells_indexes.append(list({var_name}_cells[i1:i2]))")
        code.append(f"    {var_name}_idx = i2")
        code.append(f"    {var_name}_idx_newcells = {var_name}_idx_newcells + N")
        code.append(f"")
        code.append(f"# Convert to NumPy arrays")
        code.append(f"{var_name}_{cells_indexes_socket_varname} = np.hstack(np.array({var_name}_cells_indexes))")
        code.append(f"{var_name}_{cells_index_first_socket_varname} = np.array({var_name}_cells_index_first)")
        code.append(f"")
        
        # Extract scalar data
        if self.scalar_field:
            code.append(f"# Extract scalar field: {self.scalar_field}")
            code.append(f"if '{self.scalar_field}' in {var_name}_mesh.point_data:")
            code.append(f"    {var_name}_{vertex_data_socket_varname} = np.asarray({var_name}_mesh.point_data['{self.scalar_field}'], dtype=np.float32)")
            code.append(f"else:")
            code.append(f"    {var_name}_{vertex_data_socket_varname} = None")
            code.append(f"")
            code.append(f"if '{self.scalar_field}' in {var_name}_mesh.cell_data:")
            code.append(f"    {var_name}_{cell_data_socket_varname} = np.asarray({var_name}_mesh.cell_data['{self.scalar_field}'], dtype=np.float32)")
            code.append(f"else:")
            code.append(f"    {var_name}_{cell_data_socket_varname} = None")
        else:
            code.append(f"# Extract active scalars")
            code.append(f"if {var_name}_mesh.active_scalars is not None:")
            code.append(f"    {var_name}_{vertex_data_socket_varname} = np.asarray({var_name}_mesh.active_scalars, dtype=np.float32)")
            code.append(f"else:")
            code.append(f"    {var_name}_{vertex_data_socket_varname} = None")
            code.append(f"{var_name}_{cell_data_socket_varname} = None")
        
        return code


class PYNARIReadPyVistaVolumeDataNode(PYNARIComposerNode):
    """Read volume data from file (e.g., VTU, VTI) and output numpy arrays"""
    bl_idname = 'PYNARIReadPyVistaVolumeDataNode'
    bl_label = 'Read Volume Data (PyVista)'
    bl_icon = 'FILE_FOLDER'
    
    # filename: StringProperty(  # type: ignore
    #     name="File Path",
    #     default="",
    #     description="Path to the volume file (VTU, VTI, VTK, etc.)",
    #     subtype='FILE_PATH'
    # )

    file_path: bpy.props.StringProperty(
        name="File",
        default="",
        description="Path to the volume file (VTU, VTI, VTK, etc.)",
        subtype="FILE_PATH",        
        # update = update_property
        #update=lambda self, context: self.auto_generate_node_code(context)
    ) # type: ignore

    file_path_remote: bpy.props.StringProperty(
        name="File",
        default="",
        description="Path to the volume file (VTU, VTI, VTK, etc.)",
        # update = update_property
        #update=lambda self, context: self.auto_generate_node_code(context)
    ) # type: ignore      
    
    scalar_field: StringProperty(  # type: ignore
        name="Scalar Field",
        default="",
        description="Name of the scalar field to extract (leave empty for active scalars)",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    def init(self, context):        
        self.outputs.new('PYNARINumpyArraySocket', "NP Volume Data")
        self.outputs.new('NodeSocketVector', "Dimension")
    
    def draw_buttons(self, context, layout):
        # layout.prop(self, "filename")
        self.draw_file_path(layout)
        layout.prop(self, "scalar_field")
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name()

        volume_data_socket_varname =  self.get_var_name("NP Volume Data")
        dimension_socket_varname =  self.get_var_name("Dimension")        
        # origin_socket_varname =  utility.str_to_var_name("NP Origin")
        # spacing_socket_varname =  utility.str_to_var_name("NP Spacing")        
        
        code.append(f"# Read Volume Data: {self.get_file_path()}")
        code.append(f"import pyvista as pv")
        code.append(f"{var_name}_volume = pv.read(r'{self.get_file_path()}')")
        code.append(f"")
        
        # Extract scalar data
        if self.scalar_field:
            code.append(f"# Extract specified scalar field")
            code.append(f"if '{self.scalar_field}' in {var_name}_volume.point_data:")
            code.append(f"    {var_name}_scalars = np.asarray({var_name}_volume.point_data['{self.scalar_field}'], dtype=np.float32)")
            code.append(f"else:")
            code.append(f"    raise ValueError(f\"Scalar field '{self.scalar_field}' not found in volume data\")")
        else:
            code.append(f"# Extract active scalars")
            code.append(f"if {var_name}_volume.active_scalars is not None:")
            code.append(f"    {var_name}_scalars = np.asarray({var_name}_volume.active_scalars, dtype=np.float32)")
            code.append(f"else:")
            code.append(f"    raise ValueError(\"No active scalar field found in volume data\")")
        code.append(f"")
        
        # Try to extract structured grid information
        code.append(f"# Extract volume dimensions, origin, and spacing")
        code.append(f"if hasattr({var_name}_volume, 'dimensions'):")
        code.append(f"    {dimension_socket_varname} = np.array({var_name}_volume.dimensions, dtype=np.int32)")
        code.append(f"    {volume_data_socket_varname} = {var_name}_scalars.reshape({var_name}_volume.dimensions, order='F')")
        code.append(f"else:")
        code.append(f"    # For unstructured grids, estimate dimensions")
        code.append(f"    n_points = len({var_name}_scalars)")
        code.append(f"    dim = int(np.ceil(n_points ** (1/3)))")
        code.append(f"    {dimension_socket_varname} = np.array([dim, dim, dim], dtype=np.int32)")
        code.append(f"    {volume_data_socket_varname} = {var_name}_scalars")
        # code.append(f"")
        # code.append(f"if hasattr({var_name}_volume, 'origin'):")
        # code.append(f"    {var_name}_{origin_socket_varname} = np.array({var_name}_volume.origin, dtype=np.float32)")
        # code.append(f"else:")
        # code.append(f"    {var_name}_{origin_socket_varname} = np.array([0.0, 0.0, 0.0], dtype=np.float32)")
        # code.append(f"")
        # code.append(f"if hasattr({var_name}_volume, 'spacing'):")
        # code.append(f"    {var_name}_{spacing_socket_varname} = np.array({var_name}_volume.spacing, dtype=np.float32)")
        # code.append(f"else:")
        # code.append(f"    {var_name}_{spacing_socket_varname} = np.array([1.0, 1.0, 1.0], dtype=np.float32)")
        
        return code


class PYNARIReadCZIVolumeDataNode(PYNARIComposerNode):
    """Read CZI volume data from file using czifile package"""
    bl_idname = 'PYNARIReadCZIVolumeDataNode'
    bl_label = 'Read CZI Volume (czifile)'
    bl_icon = 'FILE_FOLDER'
    
    # filename: StringProperty(  # type: ignore
    #     name="File Path",
    #     default="",
    #     description="Path to the CZI file",
    #     subtype='FILE_PATH'
    # )

    file_path: bpy.props.StringProperty(
        name="File",
        default="",
        description="Path to the CZI file",
        subtype="FILE_PATH",        
        # update = update_property
        #update=lambda self, context: self.auto_generate_node_code(context)
    ) # type: ignore

    file_path_remote: bpy.props.StringProperty(
        name="File",
        default="",
        description="Path to the CZI file",
        #update=lambda self, context: self.auto_generate_node_code(context)
    ) # type: ignore     
    
    def init(self, context):        
        self.outputs.new('PYNARINumpyArraySocket', "NP Volume Data")
        self.outputs.new('NodeSocketVector', "Dimension")
    
    def draw_buttons(self, context, layout):
        self.draw_file_path(layout)
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name()

        volume_data_socket_varname =  self.get_var_name("NP Volume Data")
        dimension_socket_varname =  self.get_var_name("Dimension")          
        
        code.append(f"# Read CZI Volume Data: {self.get_file_path()}")
        code.append(f"import czifile")
        code.append(f"")
        code.append(f"with czifile.CziFile(r'{self.get_file_path()}') as czi:")
        code.append(f"    # Access the image data as a 5D array (dimensions order: T, Z, C, Y, X)")
        code.append(f"    {volume_data_socket_varname} = czi.asarray().astype(np.float32)")
        code.append(f"")
        code.append(f"{dimension_socket_varname} = np.array({volume_data_socket_varname}.shape, dtype=np.int32)")
        # code.append(f"{var_name}_origin = np.array([0.0, 0.0, 0.0], dtype=np.float32)")
        # code.append(f"{var_name}_spacing = np.array([1.0, 1.0, 1.0], dtype=np.float32)")
        
        return code


class PYNARIReadSKImageVolumeDataNode(PYNARIComposerNode):
    """Read volume data from file using scikit-image package"""
    bl_idname = 'PYNARIReadSKImageVolumeDataNode'
    bl_label = 'Read Volume (scikit-image)'
    bl_icon = 'FILE_FOLDER'
    
    # filename: StringProperty(  # type: ignore
    #     name="File Path",
    #     default="",
    #     description="Path to the image file (TIFF, PNG, etc.)",
    #     subtype='FILE_PATH'
    # )

    file_path: bpy.props.StringProperty(
        name="File",
        default="",
        description="Path to the image file (TIFF, PNG, etc.)",
        subtype="FILE_PATH",        
        # update = update_property
        #update=lambda self, context: self.auto_generate_node_code(context)
    ) # type: ignore

    file_path_remote: bpy.props.StringProperty(
        name="File",
        default="",
        description="Path to the image file (TIFF, PNG, etc.)",
        # update = update_property
        #update=lambda self, context: self.auto_generate_node_code(context)
    ) # type: ignore      
    
    def init(self, context):       
        self.outputs.new('PYNARINumpyArraySocket', "NP Volume Data")
        self.outputs.new('NodeSocketVector', "Dimension")
    
    def draw_buttons(self, context, layout):
        # layout.prop(self, "filename")
        self.draw_file_path(layout)
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name()

        volume_data_socket_varname =  self.get_var_name("NP Volume Data")
        dimension_socket_varname =  self.get_var_name("Dimension")          
        
        code.append(f"# Read Volume Data (scikit-image): {self.get_file_path()}")
        code.append(f"from skimage import io")
        code.append(f"")
        code.append(f"{volume_data_socket_varname} = io.imread(r'{self.get_file_path()}').astype(np.float32)")
        code.append(f"")
        code.append(f"{dimension_socket_varname} = np.array({volume_data_socket_varname}.shape, dtype=np.int32)")
        # code.append(f"# {var_name}_origin = np.array([0.0, 0.0, 0.0], dtype=np.float32)")
        # code.append(f"# {var_name}_spacing = np.array([1.0, 1.0, 1.0], dtype=np.float32)")
        
        return code


class PYNARIReadPILVolumeDataNode(PYNARIComposerNode):
    """Read volume data from file using PIL (Python Imaging Library)"""
    bl_idname = 'PYNARIReadPILVolumeDataNode'
    bl_label = 'Read Volume (PIL)'
    bl_icon = 'FILE_FOLDER'
    
    # filename: StringProperty(  # type: ignore
    #     name="File Path",
    #     default="",
    #     description="Path to the image file (supports multi-frame TIFF)",
    #     subtype='FILE_PATH'
    # )

    file_path: bpy.props.StringProperty(
        name="File",
        default="",
        description="Path to the image file (supports multi-frame TIFF)",
        subtype="FILE_PATH",        
        #update=lambda self, context: self.auto_generate_node_code(context)
    ) # type: ignore

    file_path_remote: bpy.props.StringProperty(
        name="File",
        default="",
        description="Path to the image file (supports multi-frame TIFF)",
        # update = update_property
        #update=lambda self, context: self.auto_generate_node_code(context)
    ) # type: ignore        
    
    def init(self, context):        
        self.outputs.new('PYNARINumpyArraySocket', "NP Volume Data")
        self.outputs.new('NodeSocketVector', "Dimension")
    
    def draw_buttons(self, context, layout):
        # layout.prop(self, "filename")
        self.draw_file_path(layout)
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name()

        volume_data_socket_varname =  self.get_var_name("NP Volume Data")
        dimension_socket_varname =  self.get_var_name("Dimension") 
        
        code.append(f"# Read Volume Data (PIL): {self.get_file_path()}")
        code.append(f"from PIL import Image")
        code.append(f"")
        code.append(f"{var_name}_dataset = Image.open(r'{self.get_file_path()}')")
        code.append(f"{var_name}_h, {var_name}_w = np.shape({var_name}_dataset)")
        code.append(f"")
        code.append(f"# Determine dtype based on image mode")
        code.append(f"{var_name}_dtype = np.float32")
        code.append(f"if {var_name}_dataset.mode == 'I;16':")
        code.append(f"    {var_name}_dtype = np.uint16")
        code.append(f"elif {var_name}_dataset.mode == 'I':")
        code.append(f"    {var_name}_dtype = np.int32")
        code.append(f"")
        code.append(f"# Read all frames from the image")
        code.append(f"{volume_data_socket_varname} = np.zeros(({var_name}_h, {var_name}_w, {var_name}_dataset.n_frames), dtype={var_name}_dtype)")
        code.append(f"for i in range({var_name}_dataset.n_frames):")
        code.append(f"    {var_name}_dataset.seek(i)")
        code.append(f"    {volume_data_socket_varname}[:, :, i] = np.array({var_name}_dataset)")
        code.append(f"")
        code.append(f"{volume_data_socket_varname} = {volume_data_socket_varname}.astype(np.float32)")
        code.append(f"")
        code.append(f"{dimension_socket_varname} = np.array({volume_data_socket_varname}.shape, dtype=np.int32)")
        # code.append(f"{var_name}_origin = np.array([0.0, 0.0, 0.0], dtype=np.float32)")
        # code.append(f"{var_name}_spacing = np.array([1.0, 1.0, 1.0], dtype=np.float32)")
        
        return code


class PYNARIReadSimpleITKVolumeDataNode(PYNARIComposerNode):
    """Read volume data from file using SimpleITK (supports DICOM and medical imaging formats)"""
    bl_idname = 'PYNARIReadSimpleITKVolumeDataNode'
    bl_label = 'Read Volume (SimpleITK)'
    bl_icon = 'FILE_FOLDER'
    
    # filename: StringProperty(  # type: ignore
    #     name="File Path",
    #     default="",
    #     description="Path to the image file (DICOM, NIfTI, etc.)",
    #     subtype='FILE_PATH'
    # )

    file_path: bpy.props.StringProperty(
        name="File",
        default="",
        description="Path to the image file (DICOM, NIfTI, etc.)",
        subtype="FILE_PATH",        
        #update=lambda self, context: self.auto_generate_node_code(context)
    ) # type: ignore

    file_path_remote: bpy.props.StringProperty(
        name="File",
        default="",
        description="Path to the image file (DICOM, NIfTI, etc.)",
        #update=lambda self, context: self.auto_generate_node_code(context)
    ) # type: ignore         
    
    def init(self, context):        
        self.outputs.new('PYNARINumpyArraySocket', "NP Volume Data")
        self.outputs.new('NodeSocketVector', "Dimension")
    
    def draw_buttons(self, context, layout):
        # layout.prop(self, "filename")
        self.draw_file_path(layout)
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name()

        volume_data_socket_varname =  self.get_var_name("NP Volume Data")
        dimension_socket_varname =  self.get_var_name("Dimension")        
        
        code.append(f"# Read Volume Data (SimpleITK): {self.get_file_path()}")
        code.append(f"import SimpleITK as sitk")
        code.append(f"")
        code.append(f"{var_name}_reader = sitk.ImageFileReader()")
        code.append(f"{var_name}_reader.SetFileName(r'{self.get_file_path()}')")
        code.append(f"{var_name}_sitk_image = {var_name}_reader.Execute()")
        code.append(f"")
        code.append(f"{volume_data_socket_varname} = sitk.GetArrayFromImage({var_name}_sitk_image).astype(np.float32)")
        code.append(f"")
        code.append(f"{dimension_socket_varname} = np.array({volume_data_socket_varname}.shape, dtype=np.int32)")
        # code.append(f"{var_name}_origin = np.array({var_name}_sitk_image.GetOrigin(), dtype=np.float32)")
        # code.append(f"{var_name}_spacing = np.array({var_name}_sitk_image.GetSpacing(), dtype=np.float32)")
        
        return code


class PYNARIReadRAWVolumeDataNode(PYNARIComposerNode):
    """Read raw volume data from binary file with configurable resolution and data type"""
    bl_idname = 'PYNARIReadRAWVolumeDataNode'
    bl_label = 'Read RAW Volume'
    bl_icon = 'FILE_FOLDER'
    
    file_path: bpy.props.StringProperty(
        name="File",
        default="",
        description="Path to the raw volume file",
        subtype="FILE_PATH",        
        #update=lambda self, context: self.auto_generate_node_code(context)
    ) # type: ignore

    file_path_remote: bpy.props.StringProperty(
        name="File",
        default="",
        description="Path to the raw volume file",
        #update=lambda self, context: self.auto_generate_node_code(context)
    ) # type: ignore
    
    data_type: EnumProperty(  # type: ignore
        name="Data Type",
        items=[
            ('int8', "int8", "8-bit signed integer"),
            ('uint8', "uint8", "8-bit unsigned integer"),
            ('int16', "int16", "16-bit signed integer"),
            ('uint16', "uint16", "16-bit unsigned integer"),
            ('int32', "int32", "32-bit signed integer"),
            ('uint32', "uint32", "32-bit unsigned integer"),
            ('float32', "float32", "32-bit floating point"),
            ('float64', "float64/double", "64-bit floating point (double)"),
        ],
        default='uint16',
        description="Data type of the raw volume data",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    endianness: EnumProperty(  # type: ignore
        name="Endianness",
        items=[
            ('little', "Little Endian", "Little endian byte order"),
            ('big', "Big Endian", "Big endian byte order"),
        ],
        default='little',
        description="Byte order of the raw data",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    def init(self, context):
        dimension_socket = self.inputs.new('NodeSocketVector', "Dimension") #.link_limit = 1
        dimension_socket.default_value = (0.0, 0.0, 0.0)
        
        self.outputs.new('PYNARINumpyArraySocket', "NP Volume Data")
        self.outputs.new('NodeSocketVector', "Dimension")
    
    def draw_buttons(self, context, layout):
        self.draw_file_path(layout)
        layout.prop(self, "data_type")
        layout.prop(self, "endianness")
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name()
        
        volume_data_socket_varname =  self.get_var_name("NP Volume Data")
        dimension_socket_varname =  self.get_var_name("Dimension")
        
        code.append(f"# Read RAW Volume Data: {self.get_file_path()}")
        code.append(f"")
        
        # Map data type to numpy dtype
        dtype_map = {
            'int8': 'np.int8',
            'uint8': 'np.uint8',
            'int16': 'np.int16',
            'uint16': 'np.uint16',
            'int32': 'np.int32',
            'uint32': 'np.uint32',
            'float32': 'np.float32',
            'float64': 'np.float64'
        }
        
        dtype_str = dtype_map[self.data_type]
        
        # Get resolution from input sockets
        dimension = self.get_input_value_or_linked("Dimension", use_tuple=True)
        code.append(f"{dimension_socket_varname} = ({int(dimension[2])}, {int(dimension[1])}, {int(dimension[0])})  # Z, Y, X order")
        code.append(f"")
        
        code.append(f"# Read raw binary file")
        code.append(f"with open(r'{self.get_file_path()}', 'rb') as f:")
        code.append(f"    {var_name}_raw_data = np.fromfile(f, dtype={dtype_str})")
        code.append(f"")
        
        code.append(f"# Handle endianness")
        if self.endianness == 'big':
            code.append(f"{var_name}_raw_data = {var_name}_raw_data.byteswap().newbyteorder()")
        code.append(f"")
        
        code.append(f"# Reshape to 3D volume")
        code.append(f"{volume_data_socket_varname} = {var_name}_raw_data.reshape({dimension_socket_varname}, order='F').astype(np.float32)")
        code.append(f"")
        code.append(f"print(f'Loaded RAW volume: {{len({var_name}_raw_data)}} values, shape: {{{volume_data_socket_varname}.shape}}')")
        
        return code


class PYNARIReadOpenVDBVolumeDataNode(PYNARIComposerNode):
    """Read OpenVDB volume data from file using pyopenvdb"""
    bl_idname = 'PYNARIReadOpenVDBVolumeDataNode'
    bl_label = 'Read Volume (OpenVDB)'
    bl_icon = 'FILE_FOLDER'
    
    file_path: bpy.props.StringProperty(
        name="File",
        default="",
        description="Path to the OpenVDB file (.vdb)",
        subtype="FILE_PATH",
        #update=lambda self, context: self.auto_generate_node_code(context)
    ) # type: ignore

    file_path_remote: bpy.props.StringProperty(
        name="File",
        default="",
        description="Path to the OpenVDB file (.vdb)",
        #update=lambda self, context: self.auto_generate_node_code(context)
    ) # type: ignore
    
    grid_name: StringProperty(  # type: ignore
        name="Grid Name",
        default="",
        description="Name of the grid to extract (leave empty for first grid)",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    def init(self, context):
        self.outputs.new('PYNARINumpyArraySocket', "NP Volume Data")
        self.outputs.new('NodeSocketVector', "Dimension")
        self.outputs.new('NodeSocketVector', "Origin")
        self.outputs.new('NodeSocketVector', "Spacing")
    
    def draw_buttons(self, context, layout):
        self.draw_file_path(layout)
        layout.prop(self, "grid_name")
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        var_name = self.get_var_name()

        volume_data_socket_varname = self.get_var_name("NP Volume Data")
        dimension_socket_varname = self.get_var_name("Dimension")
        origin_socket_varname = self.get_var_name("Origin")
        spacing_socket_varname = self.get_var_name("Spacing")
        
        code.append(f"# Read OpenVDB Volume Data: {self.get_file_path()}")
        code.append(f"import openvdb as vdb")
        code.append(f"")
        code.append(f"{var_name}_vdb = vdb.readAllGridMetadata(r'{self.get_file_path()}')")
        code.append(f"")
        
        # Select grid
        if self.grid_name:
            code.append(f"# Extract specified grid")
            code.append(f"for grid in {var_name}_vdb:")
            code.append(f"    if '{self.grid_name}' == grid.name:")
            code.append(f"        {var_name}_grid = grid")
            code.append(f"    else:")
            code.append(f"        raise ValueError(f\"Grid '{self.grid_name}' not found in OpenVDB file.\")")
        else:
            code.append(f"# Extract first grid")
            code.append(f"if len({var_name}_vdb) > 0:")
            code.append(f"    {var_name}_grid = {var_name}_vdb[0]")
            code.append(f"    print(f\"Using grid: {var_name}_grid.name\")")
            code.append(f"else:")
            code.append(f"    raise ValueError(\"No grids found in OpenVDB file\")")
        code.append(f"")
        
        # Get grid properties
        code.append(f"# Get grid properties")
        code.append(f"{var_name}_bbox = {var_name}_grid.evalActiveVoxelBoundingBox()")
        code.append(f"{var_name}_dim = {var_name}_bbox[1] - {var_name}_bbox[0] + vdb.Vec3i(1, 1, 1)")
        code.append(f"{dimension_socket_varname} = np.array([{var_name}_dim.x, {var_name}_dim.y, {var_name}_dim.z], dtype=np.int32)")
        code.append(f"")
        
        # Get transform information
        code.append(f"# Get transform information")
        code.append(f"{var_name}_transform = {var_name}_grid.transform")
        code.append(f"{var_name}_voxel_size = {var_name}_transform.voxelSize()")
        code.append(f"{spacing_socket_varname} = np.array([{var_name}_voxel_size[0], {var_name}_voxel_size[1], {var_name}_voxel_size[2]], dtype=np.float32)")
        code.append(f"")
        code.append(f"# Calculate origin from bounding box and transform")
        code.append(f"{var_name}_world_min = {var_name}_transform.indexToWorld({var_name}_bbox[0])")
        code.append(f"{origin_socket_varname} = np.array([{var_name}_world_min.x, {var_name}_world_min.y, {var_name}_world_min.z], dtype=np.float32)")
        code.append(f"")
        
        # Convert to numpy array
        code.append(f"# Convert grid to numpy array")
        code.append(f"{volume_data_socket_varname} = np.zeros(({var_name}_dim.z, {var_name}_dim.y, {var_name}_dim.x), dtype=np.float32)")
        code.append(f"{var_name}_grid.copyToArray({volume_data_socket_varname})")
        code.append(f"")
        code.append(f"print(f'Loaded OpenVDB volume: shape={{{volume_data_socket_varname}.shape}}, origin={{{origin_socket_varname}}}, spacing={{{spacing_socket_varname}}}')")
        
        return code


class PYNARIObjectScriptNode(PYNARIComposerNode):
    """Script node for custom Python code"""
    bl_idname = 'PYNARIObjectScriptNode'
    bl_label = 'Object Script'
    bl_icon = 'TEXT'
    
    script: PointerProperty(  # type: ignore
        name="Script",
        type=bpy.types.Text,
        description="Python script text block",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    def init(self, context):
        #self.inputs.new('PYNARIObjectSocket', "Input").link_limit = 1
        self.outputs.new('PYNARIObjectSocket', "Output")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "script")
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        
        if self.script:
            code.append(f"# Script: {self.script.name}")
            code.append(self.script.as_string())
        else:
            code.append("# No script selected")
        
        return code

class PYNARINumpyArrayScriptNode(PYNARIComposerNode):
    """Script node for custom Python code"""
    bl_idname = 'PYNARINumpyArrayScriptNode'
    bl_label = 'Numpy Array Script'
    bl_icon = 'TEXT'
    
    script: PointerProperty(  # type: ignore
        name="Script",
        type=bpy.types.Text,
        description="Python script text block",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    
    def init(self, context):
        self.outputs.new('PYNARINumpyArraySocket', "NP")
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "script")

    def get_var_name(self, postfix=""):
        """Get the function name for this node's output"""
        #return f"{utility.str_to_var_name(self.name)}_{postfix}()"

        if len(postfix) > 0:
            return f"{utility.str_to_var_name(self.name)}_{postfix}()"
        
        return f"{utility.str_to_var_name(self.name)}()"
    
    def generate_code(self, auto_gen_enabled=False):
        code = []
        code.append(f"# Label: {self.label}")
        
        if self.script:
            code.append(f"# Script: {self.script.name}")
            
            postfix = ""
            if self.outputs["NP"].is_linked:
                postfix = utility.str_to_var_name(self.outputs["NP"].links[0].to_socket.name)

            func_name = self.get_var_name(postfix)

            code.append(f"def {func_name}:")
            # Add indentation to each line of the script
            for line in self.script.as_string().split('\n'):
                code.append(f"    {line}")
        else:
            code.append("# No script selected")
        
        return code        

##################################
# BRAAS HPC Output Node
##################################

class PYNARIOutputBRAASHPCNode(PYNARIComposerNode):
    """BRAAS HPC rendering output node"""
    bl_idname = 'PYNARIOutputBRAASHPCNode'
    bl_label = 'BRAAS HPC Output'
    bl_icon = 'NETWORK_DRIVE'
    
    lib_name: StringProperty(  # type: ignore
        name="Library Name",
        default="helide",
        description="PYNARI library name (e.g., helide, environment, visrtx)",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    dev_name: StringProperty(  # type: ignore
        name="Device Name",
        default="default",
        description="PYNARI device name",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    hostname: StringProperty(  # type: ignore
        name="Hostname",
        default="localhost",
        description="Server hostname or IP address",
        #update=lambda self, context: self.auto_generate_node_code(context)
    )
    port: IntProperty(  # type: ignore
        name="Port",
        default=7000,
        min=1,
        max=65535,
        description="Server port number",
        # update=lambda self, context: self.auto_generate_node_code(context)
    )

    use_gpujpeg: BoolProperty(  # type: ignore
        name="Use GPUJPEG",
        default=False,
        description="Use GPUJPEG compression for image transmission",
    )

    use_mpi: BoolProperty(  # type: ignore
        name="Use MPI",
        default=False,
        description="Use MPI for distributed rendering",
    )    
    
    def init(self, context):
        self.inputs.new('PYNARIFrameSocket', "Frame").link_limit = 1
    
    def draw_buttons(self, context, layout):
        layout.prop(self, "lib_name")
        layout.prop(self, "dev_name")
        layout.prop(self, "use_gpujpeg")
        layout.prop(self, "use_mpi")
        #layout.prop(self, "port")
    
    def generate_code(self, auto_gen_enabled=False):
        """Generate BRAAS HPC render loop code"""
        code = []
        code.append(f"# Label: {self.label}")
        
        # Get the frame node
        frame_node = None
        if self.inputs["Frame"].is_linked:
            fl = self.inputs["Frame"].links[0]
            frame_node = fl.from_node
            # Name of the frame node
            frame_node_name = frame_node.get_var_name(fl.from_socket.name)

        
        if not frame_node or frame_node.bl_idname != 'PYNARIFrameNode':
            raise ValueError("BRAAS HPC node requires a Frame node connection")
        
        # Get frame dimensions
        width = frame_node.width
        height = frame_node.height

        # Port
        port = self.port

        # GPUJPEG
        # enable_gpujpeg = 1 if self.use_gpujpeg else 0

        if hasattr(bpy.context.scene, "braas_hpc_renderengine"):
            server_settings = bpy.context.scene.braas_hpc_renderengine.server_settings
            port = server_settings.braas_hpc_renderengine_port    
        
        # Find the perspective camera from the frame's camera input
        camera_var_name = "perspective_camera"
        if frame_node.inputs["Camera"].is_linked:
            cl = frame_node.inputs["Camera"].links[0]
            camera_node = cl.from_node
            camera_var_name = camera_node.get_var_name(cl.from_socket.name)
        
        # Find the world from the frame's world input
        world_var_name = "world"
        if frame_node.inputs["World"].is_linked:
            wl = frame_node.inputs["World"].links[0]
            world_node = wl.from_node
            world_var_name = world_node.get_var_name(wl.from_socket.name)
        
        # Generate the BRAAS HPC rendering code
        code.append("# BRAAS HPC Rendering Output")
        code.append("#" * 100)
        code.append("import time")
        code.append("import ctypes")
        code.append("import os")
        code.append("from ctypes import Array, cdll, c_void_p, c_char, c_char_p, c_int, c_int32, c_uint32, c_float, c_bool, c_ulong, POINTER")
        code.append("")
        code.append("import braas_hpc_renderengine_dll as _renderengine_dll")
        code.append("")
        code.append("#" * 100)
       
        code.append("#" * 100)
        code.append("# Matrix/Vector transformation utilities")
        code.append("")
        code.append("def mul_vec(mat, vec):")
        code.append("    \"\"\"Multiply 4x4 matrix with vector (direction/normal transformation)\"\"\"")
        code.append("    x, y, z = vec[0], vec[1], vec[2]")
        code.append("    return np.array([")
        code.append("        x * mat[0] + y * mat[1] + z * mat[2],")
        code.append("        x * mat[4] + y * mat[5] + z * mat[6],")
        code.append("        x * mat[8] + y * mat[9] + z * mat[10]")
        code.append("    ], dtype=np.float32)")
        code.append("")
        code.append("def mul_point(mat, vec):")
        code.append("    \"\"\"Multiply 4x4 matrix with point (position transformation)\"\"\"")
        code.append("    x, y, z = vec[0], vec[1], vec[2]")
        code.append("    return np.array([")
        code.append("        x * mat[0] + y * mat[1] + z * mat[2] + mat[3],")
        code.append("        x * mat[4] + y * mat[5] + z * mat[6] + mat[7],")
        code.append("        x * mat[8] + y * mat[9] + z * mat[10] + mat[11]")
        code.append("    ], dtype=np.float32)")
        code.append("")
        code.append("#" * 100)
        code.append("# BRAAS HPC Render Loop")
        code.append("")
        code.append("def render_loop(server_host='localhost', server_port=7000, width=1024, height=768):")
        code.append("    \"\"\"Main rendering loop for BRAAS HPC\"\"\"")
        code.append("")
        code.append("    # Initialize render state")
        code.append("    render_time = 0.0")
        code.append("    acc_render_time = 0.0")
        code.append("    acc_samples = 0")
        code.append("")

        code.append("    # Initialize MPI")
        if self.use_mpi:
            code.append("    import mpi4py.MPI as MPI")
            code.append("    mpi_name = MPI.COMM_WORLD.Get_name()")
            code.append("    mpi_addr = MPI._addressof(MPI.COMM_WORLD)")
            code.append("    device.setParameter('pointer_to_mpi_communicator', anari.UINT64, mpi_addr)")
            code.append("    device.commitParameters()")
            code.append("    mpi_rank, mpi_size = (MPI.COMM_WORLD.Get_rank(), MPI.COMM_WORLD.Get_size())")
        else:
            code.append("    mpi_comm = None")
            code.append("    mpi_rank = 0")
            code.append("    mpi_size = 1")
        
        code.append("    # Initialize renderengine_dll")
        if self.use_gpujpeg:
            code.append(f"    {frame_node_name}.setParameter('channel.color', pynari.DATA_TYPE, pynari.UFIXED8_RGBA_SRGB)")
            code.append(f"    {frame_node_name}.commitParameters()")

            code.append(f"    if mpi_rank == 0:")
            code.append(f"        _renderengine_dll.enable_gpujpeg(1)")
            code.append(f"        _renderengine_dll.set_pixsize(8) #pynari.UFIXED8_RGBA_SRGB")
        else:
            code.append(f"    {frame_node_name}.setParameter('channel.color', pynari.DATA_TYPE, pynari.FLOAT32_VEC4)")
            code.append(f"    {frame_node_name}.commitParameters()")

            code.append(f"    if mpi_rank == 0:")
            code.append(f"        _renderengine_dll.enable_gpujpeg(0)")
            code.append(f"        _renderengine_dll.set_pixsize(32) #pynari.FLOAT32_VEC4")

        code.append("")
        code.append("    # Initialize server connection")
        code.append("    if mpi_rank == 0:")
        code.append("        server_address = server_host.encode('utf-8')")
        code.append("        _renderengine_dll.server_init(server_address, server_port, int(width), int(height))")
        code.append("")
        code.append("        # Check for connection errors")
        code.append("        if _renderengine_dll.com_error() != 0:")
        code.append("            print(f\"Failed to connect to server at {server_host}:{server_port}\")")
        code.append("            return 1")
        code.append("")
        code.append("    print(\"Start rendering...\")")
        code.append("")
        code.append("    # Camera state storage")
        code.append("    view_matrix = (ctypes.c_float * 16)()")
        code.append("    lens = ctypes.c_float()")
        code.append("    nearclip = ctypes.c_float()")
        code.append("    farclip = ctypes.c_float()")
        code.append("    sensor_width = ctypes.c_float()")
        code.append("    sensor_height = ctypes.c_float()")
        code.append("    sensor_fit = ctypes.c_int32()")
        code.append("    view_camera_zoom = ctypes.c_float()")
        code.append("    view_camera_offset0 = ctypes.c_float()")
        code.append("    view_camera_offset1 = ctypes.c_float()")
        code.append("    use_view_camera = ctypes.c_int32()")
        code.append("    shift_x = ctypes.c_float()")
        code.append("    shift_y = ctypes.c_float()")
        code.append("    view_perspective = ctypes.c_int32()")
        code.append("")
        code.append("    # Initial camera vectors (in camera/local space)")
        code.append("    camera_pos_local = np.array([0.0, 0.0, 0.0], dtype=np.float32)")
        code.append("    camera_dir_local = np.array([0.0, 0.0, -1.0], dtype=np.float32)")
        code.append("    camera_up_local = np.array([0.0, 1.0, 0.0], dtype=np.float32)")
        code.append("")
        code.append("    # Get world bounds for scene information")
        code.append(f"    bbox = {world_var_name}.getBounds()")
        code.append("    world_bounds_lower = np.array([bbox[0], bbox[1], bbox[2]], dtype=np.float32)")
        code.append("    world_bounds_upper = np.array([bbox[3], bbox[4], bbox[5]], dtype=np.float32)")
        code.append("    scalars_range = np.array([0.0, 1.0], dtype=np.float32)")
        code.append("")
        code.append("    current_width = int(width)")
        code.append("    current_height = int(height)")
        code.append("")
        code.append("    render_running = True")
        code.append("    last_loop_time = 1.0/25.0  # Initial estimate: 40ms (25 FPS)")
        code.append("")
        code.append("    # Main render loop")
        code.append("    while render_running:")
        code.append("        loop_start = time.time()")
        code.append("")
        code.append("        # Receive camera data from client")
        code.append("        receive_start = time.time()")
        code.append("        if mpi_rank == 0:")
        code.append("            result_recv_cam_data = _renderengine_dll.recv_cam_data()")
        code.append("")
        code.append("            if _renderengine_dll.com_error() != 0:")
        code.append("                print(\"TCP Error or connection closed\")")
        code.append("                break")
        code.append("")
        code.append("            # Check for resolution changes")
        code.append("            current_width = _renderengine_dll.get_width()")
        code.append("            current_height = _renderengine_dll.get_height()")
        code.append("")
        code.append("            # Get camera parameters from client")
        code.append("            _renderengine_dll.get_camera(")
        code.append("                ctypes.cast(view_matrix, ctypes.c_void_p),")
        code.append("                ctypes.byref(lens),")
        code.append("                ctypes.byref(nearclip),")
        code.append("                ctypes.byref(farclip),")
        code.append("                ctypes.byref(sensor_width),")
        code.append("                ctypes.byref(sensor_height),")
        code.append("                ctypes.byref(sensor_fit),")
        code.append("                ctypes.byref(view_camera_zoom),")
        code.append("                ctypes.byref(view_camera_offset0),")
        code.append("                ctypes.byref(view_camera_offset1),")
        code.append("                ctypes.byref(use_view_camera),")
        code.append("                ctypes.byref(shift_x),")
        code.append("                ctypes.byref(shift_y),")
        code.append("                ctypes.byref(view_perspective)")
        code.append("            )")
        code.append("")
        code.append("        if current_width != width or current_height != height:")
        code.append("            width = current_width")
        code.append("            height = current_height")
        code.append("            print(f\"Resizing to {width}x{height}\")")
        code.append(f"            {frame_node_name}.setParameter('size', pynari.uint2, [int(width), int(height)])")
        code.append(f"            {frame_node_name}.commitParameters()")
        code.append("            acc_samples = 0")
        code.append("            acc_render_time = 0.0")        
        code.append("")
        code.append("        # Validate resolution")
        code.append("        if current_width == 0 or current_height == 0:")
        code.append("            print(\"Width or height is 0!\")")
        code.append("            break")
        code.append("")
        code.append("        if result_recv_cam_data != 0: # Camera changed")
        code.append("            # Calculate aspect ratio")
        code.append("            camera_aspect = float(current_width) / float(current_height)")
        code.append("")
        code.append("            # Update camera in PYNARI - transform to world space using inverse view matrix")
        code.append("            view_matrix_np = np.array(view_matrix, dtype=np.float32)")
        code.append("            camera_pos_world = mul_point(view_matrix_np, camera_pos_local)")
        code.append("            camera_dir_world = mul_vec(view_matrix_np, camera_dir_local)")
        code.append("            camera_up_world = mul_vec(view_matrix_np, camera_up_local)")
        code.append("")
        code.append("            # Update perspective camera with transformed parameters")
        code.append(f"            {camera_var_name}.setParameter('aspect', pynari.FLOAT32, camera_aspect)")
        code.append(f"            {camera_var_name}.setParameter('position', pynari.FLOAT32_VEC3, tuple(camera_pos_world))")
        code.append(f"            {camera_var_name}.setParameter('direction', pynari.FLOAT32_VEC3, tuple(camera_dir_world))")
        code.append(f"            {camera_var_name}.setParameter('up', pynari.FLOAT32_VEC3, tuple(camera_up_world))")
        code.append(f"            {camera_var_name}.setParameter('fovy', pynari.FLOAT32, float(lens.value))")
        code.append(f"            {camera_var_name}.commitParameters()")
        code.append("")
        code.append("            acc_samples = 0")
        code.append("            acc_render_time = 0.0")
        code.append("")        
        code.append("        # Receive custom BRAAS HPC data")
        code.append("        if mpi_rank == 0:")
        code.append("            data_buffer = (ctypes.c_char * 4)()")
        code.append("            _renderengine_dll.recv_braas_hpc_renderengine_data(data_buffer, 4)")
        code.append("")
        code.append("            # Get data size")
        code.append("            cyclesphiDataRenderSize = ctypes.cast(data_buffer, POINTER(c_int32))[0]")        
        code.append("")
        code.append("            if cyclesphiDataRenderSize > 0:")
        code.append("                # Receive cyclesphiDataRender")        
        code.append("                data_buffer = (ctypes.c_char * cyclesphiDataRenderSize)()")
        code.append("                _renderengine_dll.recv_braas_hpc_renderengine_data(data_buffer, cyclesphiDataRenderSize)")
        code.append("                cyclesphiDataRender = bytes(data_buffer).decode('utf-8')")
        code.append("                if len(cyclesphiDataRender) > 0:")
        code.append("                    acc_samples = 0")
        code.append("                    acc_render_time = 0.0")
        code.append("                    try:")
        code.append("                        exec(cyclesphiDataRender)")
        code.append("                    except Exception as e:")
        code.append("                        print(f\"Error executing BRAAS HPC data: {e}\")")

        code.append("")
        code.append("        # Render multiple samples based on previous loop time")
        code.append("        # Adaptive time budget: use time of previous iteration (TCP + render)")
        code.append("        fps_loop_time = 1.0 / last_loop_time")
        code.append("        fps_budget = max(25.0, fps_loop_time * 0.8)  # Use 80% of last loop time, max 1/25ms")
        code.append("        render_batch_start = time.time()")
        code.append("        samples_this_batch = 0")
        code.append("")
        code.append("        while True:")
        code.append("            # Render one sample")
        code.append("            render_start = time.time()")
        code.append(f"            {frame_node_name}.render()")
        code.append("            render_time = time.time() - render_start")
        code.append("            ")
        code.append("            acc_samples += 1")
        code.append("            acc_render_time += render_time")
        code.append("            samples_this_batch += 1")
        code.append("            ")
        code.append("            # Check if we've exceeded the time budget")
        code.append("            fps_elapsed = 1.0 / (time.time() - render_batch_start)")
        code.append("            if fps_elapsed <= fps_budget:")
        code.append("                break")
        code.append("            ")
        code.append("            # Stop if single render takes longer than budget (avoid getting stuck)")
        code.append("            fps_render = 1.0 / render_time")
        code.append("            if fps_render < fps_budget or acc_samples < 3:")
        code.append("                break")

        # TODO
        # code.append("            break")

        code.append("")
        code.append("        acc_fps = float(acc_samples) / acc_render_time if acc_render_time > 0.0 else 0.0")
        code.append("")
        code.append("        # Map frame buffer and send pixels to client")
        code.append(f"        fb_color = {frame_node_name}.map('channel.color')")
        code.append("        if mpi_rank == 0:")
        code.append("            _renderengine_dll.set_pixels(fb_color, False)")
        code.append(f"        {frame_node_name}.unmap('channel.color')")
        code.append("")
        code.append("        # Send scene metadata (bounds, ranges, FPS)")
        code.append("        if mpi_rank == 0:")
        code.append("            _renderengine_dll.set_braas_hpc_renderengine_range(")
        code.append("                world_bounds_lower.ctypes.data_as(c_void_p),")
        code.append("                world_bounds_upper.ctypes.data_as(c_void_p),")
        code.append("                scalars_range.ctypes.data_as(c_void_p),")
        code.append("                acc_samples,")
        code.append("                acc_fps")
        code.append("            )")
        code.append("")
        code.append("        # Send pixel data to client")
        code.append("        if mpi_rank == 0:")
        code.append("            result_send_pixels = _renderengine_dll.send_pixels_data()")
        code.append("")
        code.append("            if _renderengine_dll.com_error() != 0:")
        code.append("                print(\"TCP Error during send\")")
        code.append("                break")
        code.append("")
        code.append("        # Update last loop time for next iteration's time budget")
        code.append("        last_loop_time = time.time() - loop_start")
        code.append("")
        code.append("    # Cleanup")
        code.append("    if mpi_rank == 0:")
        code.append("        _renderengine_dll.server_close_connection()")
        code.append("")
        
        if self.use_mpi:
            code.append("    MPI.Finalize()")

        code.append("")
        code.append("    print(\"Rendering stopped.\")")
        code.append("")
        code.append("# Start BRAAS HPC render loop")        
        code.append(f"render_loop('{self.hostname}', {port}, {width}, {height})")
        
        return code


##################################
# Socket Types
##################################
class PYNARIBaseSocket(NodeSocket):
    bl_idname = 'PYNARIBaseSocket'
    bl_label = 'Base Socket'

    def is_valid_color(self, r, g, b, a):
        for l in self.links:
            if l.from_socket.bl_idname != l.to_socket.bl_idname:
                return (1.0, 0.0, 0.0, 1.0)
            
        return (r, g, b, a)

class PYNARIFrameSocket(PYNARIBaseSocket):
    bl_idname = 'PYNARIFrameSocket'
    bl_label = 'Frame Socket'
    
    def draw(self, context, layout, node, text):
        layout.label(text=text)
    
    def draw_color(self, context, node):
        return self.is_valid_color(1.0, 0.4, 0.216, 1.0)


class PYNARIWorldSocket(PYNARIBaseSocket):
    bl_idname = 'PYNARIWorldSocket'
    bl_label = 'World Socket'
    
    def draw(self, context, layout, node, text):
        layout.label(text=text)
    
    def draw_color(self, context, node):
        return self.is_valid_color(0.2, 0.6, 1.0, 1.0)


class PYNARICameraSocket(PYNARIBaseSocket):
    bl_idname = 'PYNARICameraSocket'
    bl_label = 'Camera Socket'
    
    def draw(self, context, layout, node, text):
        layout.label(text=text)
    
    def draw_color(self, context, node):
        return self.is_valid_color(0.8, 0.8, 0.2, 1.0)


class PYNARIRendererSocket(PYNARIBaseSocket):
    bl_idname = 'PYNARIRendererSocket'
    bl_label = 'Renderer Socket'
    
    def draw(self, context, layout, node, text):
        layout.label(text=text)
    
    def draw_color(self, context, node):
        return self.is_valid_color(1.0, 0.5, 0.0, 1.0)


class PYNARIGroupSocket(PYNARIBaseSocket):
    bl_idname = 'PYNARIGroupSocket'
    bl_label = 'Group Socket'
    
    def draw(self, context, layout, node, text):
        layout.label(text=text)
    
    def draw_color(self, context, node):
        return self.is_valid_color(0.4, 0.8, 0.4, 1.0)


class PYNARIInstanceSocket(PYNARIBaseSocket):
    bl_idname = 'PYNARIInstanceSocket'
    bl_label = 'Instance Socket'
    
    def draw(self, context, layout, node, text):
        layout.label(text=text)
    
    def draw_color(self, context, node):
        return self.is_valid_color(0.6, 0.4, 0.8, 1.0)


class PYNARISurfaceSocket(PYNARIBaseSocket):
    bl_idname = 'PYNARISurfaceSocket'
    bl_label = 'Surface Socket'
    
    def draw(self, context, layout, node, text):
        layout.label(text=text)
    
    def draw_color(self, context, node):
        return self.is_valid_color(0.2, 0.8, 0.8, 1.0)


class PYNARIGeometrySocket(PYNARIBaseSocket):
    bl_idname = 'PYNARIGeometrySocket'
    bl_label = 'Geometry Socket'
    
    def draw(self, context, layout, node, text):
        layout.label(text=text)
    
    def draw_color(self, context, node):
        return self.is_valid_color(0.1, 0.6, 0.9, 1.0)


class PYNARIMaterialSocket(PYNARIBaseSocket):
    bl_idname = 'PYNARIMaterialSocket'
    bl_label = 'Material Socket'
    
    def draw(self, context, layout, node, text):
        layout.label(text=text)
    
    def draw_color(self, context, node):
        return self.is_valid_color(0.9, 0.3, 0.5, 1.0)


class PYNARILightSocket(PYNARIBaseSocket):
    bl_idname = 'PYNARILightSocket'
    bl_label = 'Light Socket'
    
    def draw(self, context, layout, node, text):
        layout.label(text=text)
    
    def draw_color(self, context, node):
        return self.is_valid_color(1.0, 1.0, 0.4, 1.0)


class PYNARIVolumeSocket(PYNARIBaseSocket):
    bl_idname = 'PYNARIVolumeSocket'
    bl_label = 'Volume Socket'
    
    def draw(self, context, layout, node, text):
        layout.label(text=text)
    
    def draw_color(self, context, node):
        return self.is_valid_color(0.5, 0.3, 0.9, 1.0)


class PYNARISpatialFieldSocket(PYNARIBaseSocket):
    bl_idname = 'PYNARISpatialFieldSocket'
    bl_label = 'Spatial Field Socket'
    
    def draw(self, context, layout, node, text):
        layout.label(text=text)
    
    def draw_color(self, context, node):
        return self.is_valid_color(0.3, 0.9, 0.5, 1.0)


class PYNARISamplerSocket(PYNARIBaseSocket):
    bl_idname = 'PYNARISamplerSocket'
    bl_label = 'Sampler Socket'
    
    def draw(self, context, layout, node, text):
        layout.label(text=text)
    
    def draw_color(self, context, node):
        return self.is_valid_color(0.8, 0.5, 0.9, 1.0)


class PYNARINumpyArraySocket(PYNARIBaseSocket):
    bl_idname = 'PYNARINumpyArraySocket'
    bl_label = 'Numpy Array Socket'
    
    def draw(self, context, layout, node, text):
        layout.label(text=text)
    
    def draw_color(self, context, node):
        return self.is_valid_color(0.9, 0.6, 0.2, 1.0)


class PYNARIObjectSocket(PYNARIBaseSocket):
    bl_idname = 'PYNARIObjectSocket'
    bl_label = 'Object Socket'
    
    def draw(self, context, layout, node, text):
        layout.label(text=text)
    
    def draw_color(self, context, node):
        # Always valid - compatible with any PYNARI socket
        return (0.7, 0.7, 0.7, 1.0)

##################################
# Node Categories
##################################

class PYNARIComposerNodeCategory(NodeCategory):
    @classmethod
    def poll(cls, context):
        return context.space_data.tree_type == 'PYNARIComposerNodeTree'


node_categories = [
    PYNARIComposerNodeCategory('PYNARI_OUTPUT', "Output", items=[
        NodeItem('PYNARIOutputPILImageNode'),
        NodeItem('PYNARIOutputBRAASHPCNode'),
    ]),
    PYNARIComposerNodeCategory('PYNARI_FRAME', "Frame", items=[
        NodeItem('PYNARIFrameNode'),
    ]),    
    PYNARIComposerNodeCategory('PYNARI_SCENE', "Scene", items=[
        NodeItem('PYNARIWorldNode'),
        NodeItem('PYNARIGroupNode'),
        NodeItem('PYNARIInstanceNode'),
        NodeItem('PYNARIBlenderInstanceNode'),
        NodeItem('PYNARISurfaceNode'),
    ]),
    PYNARIComposerNodeCategory('PYNARI_CAMERA', "Cameras", items=[
        NodeItem('PYNARIPerspectiveCameraNode'),
        NodeItem('PYNARIOrthographicCameraNode'),
        NodeItem('PYNARIBlenderCameraNode'),
    ]),
    PYNARIComposerNodeCategory('PYNARI_RENDER', "Render", items=[
        NodeItem('PYNARIRendererNode'),
    ]),
    PYNARIComposerNodeCategory('PYNARI_GEOMETRY', "Geometry", items=[
        NodeItem('PYNARITriangleGeometryNode'),
        NodeItem('PYNARISphereGeometryNode'),
        NodeItem('PYNARICylinderGeometryNode'),
        NodeItem('PYNARIIsoSurfaceGeometryNode'),
        NodeItem('PYNARIConeGeometryNode'),
        NodeItem('PYNARICurveGeometryNode'),
        NodeItem('PYNARIQuadGeometryNode'),
    ]),
    PYNARIComposerNodeCategory('PYNARI_MATERIAL', "Materials", items=[
        NodeItem('PYNARIMatteMaterialNode'),
        NodeItem('PYNARIPhysicallyBasedMaterialNode'),
    ]),
    PYNARIComposerNodeCategory('PYNARI_LIGHT', "Lights", items=[
        NodeItem('PYNARIDirectionalLightNode'),
        NodeItem('PYNARIPointLightNode'),
        NodeItem('PYNARIQuadLightNode'),
    ]),
    PYNARIComposerNodeCategory('PYNARI_VOLUME', "Volumes", items=[
        NodeItem('PYNARITransferFunction1DVolumeNode'),
        NodeItem('PYNARIColorRampNode'),
        NodeItem('PYNARIBlenderColorRampNode'),
        NodeItem('PYNARIStructuredRegularFieldNode'),
        NodeItem('PYNARIUnstructuredFieldNode'),
    ]),
    PYNARIComposerNodeCategory('PYNARI_SAMPLER', "Samplers", items=[
        NodeItem('PYNARIImage2DSamplerNode'),
    ]),
    PYNARIComposerNodeCategory('PYNARI_READ', "Read Input", items=[
        NodeItem('PYNARIReadPyVistaPolyDataNode'),
        NodeItem('PYNARIReadPyVistaVolumeDataNode'),
        NodeItem('PYNARIReadPyVistaUnstructuredDataNode'),
        NodeItem('PYNARIReadCZIVolumeDataNode'),
        NodeItem('PYNARIReadSKImageVolumeDataNode'),
        NodeItem('PYNARIReadPILVolumeDataNode'),
        NodeItem('PYNARIReadSimpleITKVolumeDataNode'),
        NodeItem('PYNARIReadRAWVolumeDataNode'),
        NodeItem('PYNARIReadOpenVDBVolumeDataNode'),
    ]),
    PYNARIComposerNodeCategory('PYNARI_UTILITY', "Utility", items=[
        NodeItem('PYNARIObjectScriptNode'),
        NodeItem('PYNARINumpyArrayScriptNode'),
    ]),
    PYNARIComposerNodeCategory('PYNARI_INPUT', "Input", items=[
        NodeItem('PYNARIStringValueNode'),
        NodeItem('PYNARIFloatValueNode'),
        NodeItem('PYNARIFloatVector2DValueNode'),
        NodeItem('PYNARIFloatVector3DValueNode'),
        NodeItem('PYNARIIntValueNode'),
    ]),
    PYNARIComposerNodeCategory('PYNARI_MATH', "Math", items=[
        NodeItem('PYNARIIntMathNode'),
        NodeItem('PYNARIFloatMathNode'),
        NodeItem('PYNARIVectorMathNode'),
        NodeItem('PYNARIDimensionToSpacingNode'),
        NodeItem('PYNARIFindMinMaxNode'),
    ]),

  
]


##################################
# Operators
##################################

class PYNARICOMPOSER_OT_GenerateCodeTree(bpy.types.Operator):
    """Generate Python code from PYNARI node tree"""
    bl_idname = "pynari_composer.generate_code_tree"
    bl_label = "Generate Tree Code"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space.type == 'NODE_EDITOR' and space.tree_type == 'PYNARIComposerNodeTree'
    
    def execute(self, context):
        tree = context.space_data.edit_tree
        if not tree:
            self.report({'ERROR'}, "No active node tree")
            return {'CANCELLED'}
        
        text_name = tree.generate_python_code()
        self.report({'INFO'}, f"Generated code in text block '{text_name}'")
        
        return {'FINISHED'}


class PYNARICOMPOSER_OT_GenerateCodeNode(bpy.types.Operator):
    """Generate Python code for selected node only"""
    bl_idname = "pynari_composer.generate_code_node"
    bl_label = "Generate Node Code"
    bl_options = {'REGISTER', 'UNDO'}
    
    @classmethod
    def poll(cls, context):
        space = context.space_data
        if space.type != 'NODE_EDITOR' or space.tree_type != 'PYNARIComposerNodeTree':
            return False
        tree = space.edit_tree
        return tree and tree.nodes.active is not None
    
    def execute(self, context):
        tree = context.space_data.edit_tree
        if not tree:
            self.report({'ERROR'}, "No active node tree")
            return {'CANCELLED'}
        
        node = tree.nodes.active
        if not node:
            self.report({'ERROR'}, "No active node selected")
            return {'CANCELLED'}
        
        # Check if node has generate_code method
        if not hasattr(node, 'generate_code'):
            self.report({'ERROR'}, f"Node '{node.name}' does not support code generation")
            return {'CANCELLED'}
        
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
        
        self.report({'INFO'}, f"Generated code for node '{node.name}' in text block '{text_name}'")
        return {'FINISHED'}


##################################
# Remote File Management
##################################

class PYNARICOMPOSER_OT_update_remote_files(bpy.types.Operator):
    bl_idname = 'pynari_composer.update_remote_files'
    bl_label = 'Update remote files'

    name: bpy.props.StringProperty(        
        default="/"
    )  # type: ignore
    
    is_directory: bpy.props.BoolProperty(
        default=True
    )  # type: ignore

    active_node: None     

    def execute(self, context):
        pref = pynari_pref.preferences()

        if self.is_directory:
            context.scene.braas_hpc_pynari_composer_remote_list.clear()
            context.scene.braas_hpc_pynari_composer_remote_list_index = -1

            if self.name == "..":
                if context.scene.braas_hpc_pynari_composer_remote_path[len(context.scene.braas_hpc_pynari_composer_remote_path) - 1] == "/":
                    context.scene.braas_hpc_pynari_composer_remote_path = os.path.dirname(context.scene.braas_hpc_pynari_composer_remote_path)

                context.scene.braas_hpc_pynari_composer_remote_path = os.path.dirname(context.scene.braas_hpc_pynari_composer_remote_path)
                context.scene.braas_hpc_pynari_composer_remote_path = str(context.scene.braas_hpc_pynari_composer_remote_path) + "/"
            else:
                divider = "/"
                if context.scene.braas_hpc_pynari_composer_remote_path[len(context.scene.braas_hpc_pynari_composer_remote_path) - 1] == "/":
                    divider = ""

                context.scene.braas_hpc_pynari_composer_remote_path = str(context.scene.braas_hpc_pynari_composer_remote_path) + divider + str(self.name)

            item = context.scene.braas_hpc_pynari_composer_remote_list.add()
            item.Name = ".."
            item.is_directory = True

            # Check BRaaS HPC addon
            try:
                import braas_hpc

                pref = braas_hpc.raas_pref.preferences()
                preset = pref.cluster_presets[bpy.context.scene.raas_cluster_presets_index]
                ssh_server_name = braas_hpc.raas_config.GetServerFromType(preset.cluster_name.upper())    

            except ImportError:
                self.report({'ERROR'}, "BRAAS HPC addon not found. Please install and enable it.")
                return {'CANCELLED'}         

            # Folders
            try:
                remote_file_list = braas_hpc.raas_connection.ssh_command_sync(ssh_server_name, " ls -p " + context.scene.braas_hpc_pynari_composer_remote_path + " | grep -e /", preset)
                lines = remote_file_list.split('\n')

                for line in lines:
                    if len(line) > 0:
                        item = context.scene.braas_hpc_pynari_composer_remote_list.add()
                        item.Name = line
                        item.is_directory = True
            except:
                pass

            # Files
            try:
                remote_file_list = braas_hpc.raas_connection.ssh_command_sync(ssh_server_name, " ls -p " + context.scene.braas_hpc_pynari_composer_remote_path + " | grep -v /", preset)
                lines = remote_file_list.split('\n')

                for line in lines:
                    if len(line) > 0:
                        item = context.scene.braas_hpc_pynari_composer_remote_list.add()
                        item.Name = line
                        item.is_directory = False

            except:
                pass

            try:
                if context.active_node is not None and isinstance(context.active_node, PYNARIComposerNode) and pref.braas_hpc_pynari_composer_remote:
                    context.active_node.dir_path_remote = str(context.scene.braas_hpc_pynari_composer_remote_path)
            except:
                pass 

        else:
            try:
                if context.active_node is not None and isinstance(context.active_node, PYNARIComposerNode) and pref.braas_hpc_pynari_composer_remote:
                    context.active_node.file_path_remote = str(context.scene.braas_hpc_pynari_composer_remote_path) + str(self.name)
            except:
                pass           

        return {"FINISHED"}
    

class PYNARICOMPOSER_PG_remote_files(bpy.types.PropertyGroup):
    Name: bpy.props.StringProperty(
        name="Name"
    )  # type: ignore
    
    is_directory: bpy.props.BoolProperty(
        default=False
    )  # type: ignore    
    

class PYNARICOMPOSER_UL_remote_files(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        op = layout.operator("pynari_composer.update_remote_files", text=item.Name, icon='FILE_FOLDER' if item.is_directory else 'FILE_BLEND')
        op.name = item.Name
        op.is_directory = item.is_directory


class PYNARICOMPOSER_PT_remote_file_path_node(Panel):
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "PYNARI"
    bl_label = "Remote"   

    @classmethod
    def poll(cls, context):
        pref = pynari_pref.preferences()        
        return context.active_node is not None and isinstance(context.active_node, PYNARIComposerNode) and pref.braas_hpc_pynari_composer_remote

    def draw(self, context):
        layout = self.layout

        col = layout.column()
        col.prop(context.scene, "braas_hpc_pynari_composer_remote_path")
        col.operator("pynari_composer.update_remote_files")
        col.template_list("PYNARICOMPOSER_UL_remote_files", "", context.scene, "braas_hpc_pynari_composer_remote_list", context.scene, "braas_hpc_pynari_composer_remote_list_index")        


##################################
# UI Panel
##################################

class PYNARICOMPOSER_PT_ComposerPanel(bpy.types.Panel):
    """PYNARI Composer panel in Node Editor"""
    bl_label = "PYNARI Composer"
    bl_idname = "PYNARICOMPOSER_PT_composer_panel"
    bl_space_type = 'NODE_EDITOR'
    bl_region_type = 'UI'
    bl_category = "PYNARI"
    
    @classmethod
    def poll(cls, context):
        space = context.space_data
        return space.type == 'NODE_EDITOR' and space.tree_type == 'PYNARIComposerNodeTree'
    
    def draw(self, context):
        layout = self.layout
        tree = context.space_data.edit_tree
        
        # Code generation buttons
        layout.operator(PYNARICOMPOSER_OT_GenerateCodeTree.bl_idname, icon='FILE_SCRIPT')

        box = layout.box()
        
        active_node = tree.nodes.active if tree else None

        if active_node:
            box.label(text=f"Active Node: {active_node.name}")
        else:
            box.label(text="No Active Node")

        col = box.column()
        # Auto-generate checkbox
        if tree:
            #box.separator()            
            col.prop(tree, "auto_generate_code_fps", text="Auto Generate Node Code FPS")
            col.prop(tree, "auto_generate_code", text="Auto Generate Node Code")

        col.separator()
        col.operator(PYNARICOMPOSER_OT_GenerateCodeNode.bl_idname, icon='NODE')


##################################
# Registration
##################################

classes = (
    # Sockets
    PYNARIFrameSocket,
    PYNARIWorldSocket,
    PYNARICameraSocket,
    PYNARIRendererSocket,
    PYNARIGroupSocket,
    PYNARIInstanceSocket,
    PYNARISurfaceSocket,
    PYNARIGeometrySocket,
    PYNARIMaterialSocket,
    PYNARILightSocket,
    PYNARIVolumeSocket,
    PYNARISpatialFieldSocket,
    PYNARISamplerSocket,
    PYNARINumpyArraySocket,
    PYNARIObjectSocket,
    
    # Node Tree
    PYNARIComposerNodeTree,
    
    # Nodes
    PYNARIFrameNode,
    PYNARIOutputPILImageNode,
    PYNARIOutputBRAASHPCNode,
    PYNARIPerspectiveCameraNode,
    PYNARIOrthographicCameraNode,
    PYNARIBlenderCameraNode,
    PYNARIRendererNode,
    PYNARIWorldNode,
    PYNARIGroupNode,
    PYNARIInstanceNode,
    PYNARIBlenderInstanceNode,
    PYNARISurfaceNode,
    PYNARITriangleGeometryNode,
    PYNARISphereGeometryNode,
    PYNARICylinderGeometryNode,
    PYNARIIsoSurfaceGeometryNode,
    PYNARIConeGeometryNode,
    PYNARICurveGeometryNode,
    PYNARIQuadGeometryNode,
    PYNARIMatteMaterialNode,
    PYNARIPhysicallyBasedMaterialNode,
    PYNARIDirectionalLightNode,
    PYNARIPointLightNode,
    PYNARIQuadLightNode,
    PYNARITransferFunction1DVolumeNode,
    PYNARIColorRampNode,
    PYNARIBlenderColorRampNode,
    PYNARIStructuredRegularFieldNode,
    PYNARIImage2DSamplerNode,
    PYNARIReadPyVistaPolyDataNode,
    PYNARIReadPyVistaVolumeDataNode,
    PYNARIReadCZIVolumeDataNode,
    PYNARIReadSKImageVolumeDataNode,
    PYNARIReadPILVolumeDataNode,
    PYNARIReadSimpleITKVolumeDataNode,
    PYNARIObjectScriptNode,
    PYNARINumpyArrayScriptNode,
    PYNARIReadPyVistaUnstructuredDataNode,
    PYNARIUnstructuredFieldNode,
    PYNARIReadRAWVolumeDataNode,
    PYNARIReadOpenVDBVolumeDataNode,

    PYNARIStringValueNode,
    PYNARIFloatValueNode,
    PYNARIFloatVector2DValueNode,
    PYNARIFloatVector3DValueNode,
    PYNARIIntValueNode,
    
    PYNARIIntMathNode,
    PYNARIFloatMathNode,
    PYNARIVectorMathNode,
    PYNARIDimensionToSpacingNode,
    PYNARIFindMinMaxNode,
    
    # Operators
    PYNARICOMPOSER_OT_GenerateCodeTree,
    PYNARICOMPOSER_OT_GenerateCodeNode,
    PYNARICOMPOSER_OT_update_remote_files,
    
    # Property Groups
    PYNARICOMPOSER_PG_remote_files,
    
    # UI Lists
    PYNARICOMPOSER_UL_remote_files,
    
    # Panels
    PYNARICOMPOSER_PT_ComposerPanel,
    PYNARICOMPOSER_PT_remote_file_path_node,
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    
    # Register scene properties
    bpy.types.Scene.braas_hpc_pynari_composer_remote_path = StringProperty(
        name="Remote Path",
        description="Current remote file path",
        default="/"
    )
    bpy.types.Scene.braas_hpc_pynari_composer_remote_list = CollectionProperty(
        type=PYNARICOMPOSER_PG_remote_files
    )
    bpy.types.Scene.braas_hpc_pynari_composer_remote_list_index = IntProperty(
        name="Remote File List Index",
        default=-1
    )
    
    try:
        nodeitems_utils.register_node_categories('PYNARICOMPOSER_NODES', node_categories)
    except:
        pass


def unregister():
    # Unregister timer if running
    if bpy.app.timers.is_registered(auto_generate_timer):
        bpy.app.timers.unregister(auto_generate_timer)
    
    try:
        nodeitems_utils.unregister_node_categories('PYNARICOMPOSER_NODES')
    except:
        pass
    
    # Unregister scene properties
    del bpy.types.Scene.braas_hpc_pynari_composer_remote_path
    del bpy.types.Scene.braas_hpc_pynari_composer_remote_list
    del bpy.types.Scene.braas_hpc_pynari_composer_remote_list_index
    
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
