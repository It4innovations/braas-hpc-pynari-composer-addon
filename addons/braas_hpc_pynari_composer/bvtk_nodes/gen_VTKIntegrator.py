# Generated definitions for VTK class group: Integrator
# VTK version: 9.5.2

from .core import *    
TYPENAMES = []

#--------------------------------------------------------------
class VTKRungeKutta2(Node, PBVTK_Node):

    bl_idname = 'VTKRungeKutta2Type'
    bl_label  = 'vtkRungeKutta2'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return []
    def m_connections( self ):
        return ([], [], ['FunctionSet'], ['self']) 
    
add_class( VTKRungeKutta2 )        
TYPENAMES.append('VTKRungeKutta2Type' )

#--------------------------------------------------------------
class VTKRungeKutta4(Node, PBVTK_Node):

    bl_idname = 'VTKRungeKutta4Type'
    bl_label  = 'vtkRungeKutta4'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return []
    def m_connections( self ):
        return ([], [], ['FunctionSet'], ['self']) 
    
add_class( VTKRungeKutta4 )        
TYPENAMES.append('VTKRungeKutta4Type' )

#--------------------------------------------------------------
class VTKRungeKutta45(Node, PBVTK_Node):

    bl_idname = 'VTKRungeKutta45Type'
    bl_label  = 'vtkRungeKutta45'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return []
    def m_connections( self ):
        return ([], [], ['FunctionSet'], ['self']) 
    
add_class( VTKRungeKutta45 )        
TYPENAMES.append('VTKRungeKutta45Type' )

#--------------------------------------------------------------
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( PBVTK_NodeCategory( 'Integrator', 'Integrator', items=menu_items) )