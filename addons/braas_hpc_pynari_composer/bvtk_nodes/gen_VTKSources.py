# Generated definitions for VTK class group: Source
# VTK version: 9.5.2

from .core import *    
TYPENAMES = []

#--------------------------------------------------------------
class VTKAMRGaussianPulseSource(Node, PBVTK_Node):

    bl_idname = 'VTKAMRGaussianPulseSourceType'
    bl_label  = 'vtkAMRGaussianPulseSource'
    
    m_PulseAmplitude: bpy.props.FloatProperty(name='PulseAmplitude', default=0.0001) #type: ignore
    m_PulseOrigin: bpy.props.FloatVectorProperty(name='PulseOrigin', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    m_PulseWidth: bpy.props.FloatVectorProperty(name='PulseWidth', default=[0.5, 0.5, 0.5], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_PulseAmplitude','m_PulseOrigin','m_PulseWidth',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKAMRGaussianPulseSource )        
TYPENAMES.append('VTKAMRGaussianPulseSourceType' )

#--------------------------------------------------------------
class VTKArcSource(Node, PBVTK_Node):

    bl_idname = 'VTKArcSourceType'
    bl_label  = 'vtkArcSource'
    
    m_Negative: bpy.props.BoolProperty(name='Negative', default=False) #type: ignore
    m_UseNormalAndAngle: bpy.props.BoolProperty(name='UseNormalAndAngle', default=False) #type: ignore
    m_Resolution: bpy.props.IntProperty(name='Resolution', default=1) #type: ignore
    m_Angle: bpy.props.FloatProperty(name='Angle', default=90.0) #type: ignore
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    m_Normal: bpy.props.FloatVectorProperty(name='Normal', default=[0.0, 0.0, 1.0], size=3) #type: ignore
    m_Point1: bpy.props.FloatVectorProperty(name='Point1', default=[0.0, 0.5, 0.0], size=3) #type: ignore
    m_Point2: bpy.props.FloatVectorProperty(name='Point2', default=[0.5, 0.0, 0.0], size=3) #type: ignore
    m_PolarVector: bpy.props.FloatVectorProperty(name='PolarVector', default=[1.0, 0.0, 0.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Negative','m_UseNormalAndAngle','m_Resolution','m_Angle','m_Center','m_Normal','m_Point1','m_Point2','m_PolarVector',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKArcSource )        
TYPENAMES.append('VTKArcSourceType' )

#--------------------------------------------------------------
class VTKArrowSource(Node, PBVTK_Node):

    bl_idname = 'VTKArrowSourceType'
    bl_label  = 'vtkArrowSource'
    
    m_Invert: bpy.props.BoolProperty(name='Invert', default=False) #type: ignore
    m_ShaftResolution: bpy.props.IntProperty(name='ShaftResolution', default=6) #type: ignore
    m_TipResolution: bpy.props.IntProperty(name='TipResolution', default=6) #type: ignore
    m_ShaftRadius: bpy.props.FloatProperty(name='ShaftRadius', default=0.03) #type: ignore
    m_TipLength: bpy.props.FloatProperty(name='TipLength', default=0.35) #type: ignore
    m_TipRadius: bpy.props.FloatProperty(name='TipRadius', default=0.1) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Invert','m_ShaftResolution','m_TipResolution','m_ShaftRadius','m_TipLength','m_TipRadius',]
    def m_connections( self ):
        return ([], ['VTK Output'], ['ArrowOrigin'], []) 
    
add_class( VTKArrowSource )        
TYPENAMES.append('VTKArrowSourceType' )

#--------------------------------------------------------------
class VTKAxes(Node, PBVTK_Node):

    bl_idname = 'VTKAxesType'
    bl_label  = 'vtkAxes'
    
    m_ComputeNormals: bpy.props.BoolProperty(name='ComputeNormals', default=True) #type: ignore
    m_Symmetric: bpy.props.BoolProperty(name='Symmetric', default=True) #type: ignore
    m_ScaleFactor: bpy.props.FloatProperty(name='ScaleFactor', default=1.0) #type: ignore
    m_Origin: bpy.props.FloatVectorProperty(name='Origin', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_ComputeNormals','m_Symmetric','m_ScaleFactor','m_Origin',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKAxes )        
TYPENAMES.append('VTKAxesType' )

#--------------------------------------------------------------
class VTKBooleanTexture(Node, PBVTK_Node):

    bl_idname = 'VTKBooleanTextureType'
    bl_label  = 'vtkBooleanTexture'
    
    m_Thickness: bpy.props.IntProperty(name='Thickness', default=0) #type: ignore
    m_XSize: bpy.props.IntProperty(name='XSize', default=12) #type: ignore
    m_YSize: bpy.props.IntProperty(name='YSize', default=12) #type: ignore
    m_InIn: bpy.props.IntVectorProperty(name='InIn', default=[255, 255], size=2) #type: ignore
    m_InOn: bpy.props.IntVectorProperty(name='InOn', default=[255, 255], size=2) #type: ignore
    m_InOut: bpy.props.IntVectorProperty(name='InOut', default=[255, 255], size=2) #type: ignore
    m_OnIn: bpy.props.IntVectorProperty(name='OnIn', default=[255, 255], size=2) #type: ignore
    m_OnOn: bpy.props.IntVectorProperty(name='OnOn', default=[255, 255], size=2) #type: ignore
    m_OnOut: bpy.props.IntVectorProperty(name='OnOut', default=[255, 255], size=2) #type: ignore
    m_OutIn: bpy.props.IntVectorProperty(name='OutIn', default=[255, 255], size=2) #type: ignore
    m_OutOn: bpy.props.IntVectorProperty(name='OutOn', default=[255, 255], size=2) #type: ignore
    m_OutOut: bpy.props.IntVectorProperty(name='OutOut', default=[255, 255], size=2) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Thickness','m_XSize','m_YSize','m_InIn','m_InOn','m_InOut','m_OnIn','m_OnOn','m_OnOut','m_OutIn','m_OutOn','m_OutOut',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKBooleanTexture )        
TYPENAMES.append('VTKBooleanTextureType' )

#--------------------------------------------------------------
class VTKBoundedPointSource(Node, PBVTK_Node):

    bl_idname = 'VTKBoundedPointSourceType'
    bl_label  = 'vtkBoundedPointSource'
    
    m_ProduceCellOutput: bpy.props.BoolProperty(name='ProduceCellOutput', default=False) #type: ignore
    m_ProduceRandomScalars: bpy.props.BoolProperty(name='ProduceRandomScalars', default=False) #type: ignore
    m_NumberOfPoints: bpy.props.IntProperty(name='NumberOfPoints', default=100) #type: ignore
    m_Bounds: bpy.props.FloatVectorProperty(name='Bounds', default=[-1.0, 1.0, -1.0, 1.0, -1.0, 1.0], size=6) #type: ignore
    m_ScalarRange: bpy.props.FloatVectorProperty(name='ScalarRange', default=[0.0, 1.0], size=2) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_ProduceCellOutput','m_ProduceRandomScalars','m_NumberOfPoints','m_Bounds','m_ScalarRange',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKBoundedPointSource )        
TYPENAMES.append('VTKBoundedPointSourceType' )

#--------------------------------------------------------------
class VTKCameraHandleSource(Node, PBVTK_Node):

    bl_idname = 'VTKCameraHandleSourceType'
    bl_label  = 'vtkCameraHandleSource'
    
    m_Directional: bpy.props.BoolProperty(name='Directional', default=False) #type: ignore
    m_Size: bpy.props.FloatProperty(name='Size', default=0.5) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Directional','m_Size',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKCameraHandleSource )        
TYPENAMES.append('VTKCameraHandleSourceType' )

#--------------------------------------------------------------
class VTKCellGridCellSource(Node, PBVTK_Node):

    bl_idname = 'VTKCellGridCellSourceType'
    bl_label  = 'vtkCellGridCellSource'
    
    m_CellType: bpy.props.StringProperty(name='CellType', default="") #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_CellType',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKCellGridCellSource )        
TYPENAMES.append('VTKCellGridCellSourceType' )

#--------------------------------------------------------------
class VTKCellTypeSource(Node, PBVTK_Node):

    bl_idname = 'VTKCellTypeSourceType'
    bl_label  = 'vtkCellTypeSource'
    
    m_CompleteQuadraticSimplicialElements: bpy.props.BoolProperty(name='CompleteQuadraticSimplicialElements', default=False) #type: ignore
    m_CellOrder: bpy.props.IntProperty(name='CellOrder', default=3) #type: ignore
    m_CellType: bpy.props.IntProperty(name='CellType', default=12) #type: ignore
    m_OutputPrecision: bpy.props.IntProperty(name='OutputPrecision', default=0) #type: ignore
    m_PolynomialFieldOrder: bpy.props.IntProperty(name='PolynomialFieldOrder', default=1) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_CompleteQuadraticSimplicialElements','m_CellOrder','m_CellType','m_OutputPrecision','m_PolynomialFieldOrder',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKCellTypeSource )        
TYPENAMES.append('VTKCellTypeSourceType' )

#--------------------------------------------------------------
class VTKConeSource(Node, PBVTK_Node):

    bl_idname = 'VTKConeSourceType'
    bl_label  = 'vtkConeSource'
    
    m_Capping: bpy.props.BoolProperty(name='Capping', default=True) #type: ignore
    m_Resolution: bpy.props.IntProperty(name='Resolution', default=6) #type: ignore
    m_Angle: bpy.props.FloatProperty(name='Angle', default=26.56505117707799) #type: ignore
    m_Height: bpy.props.FloatProperty(name='Height', default=1.0) #type: ignore
    m_Radius: bpy.props.FloatProperty(name='Radius', default=0.5) #type: ignore
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    m_Direction: bpy.props.FloatVectorProperty(name='Direction', default=[1.0, 0.0, 0.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Capping','m_Resolution','m_Angle','m_Height','m_Radius','m_Center','m_Direction',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKConeSource )        
TYPENAMES.append('VTKConeSourceType' )

#--------------------------------------------------------------
class VTKCubeSource(Node, PBVTK_Node):

    bl_idname = 'VTKCubeSourceType'
    bl_label  = 'vtkCubeSource'
    
    m_XLength: bpy.props.FloatProperty(name='XLength', default=1.0) #type: ignore
    m_YLength: bpy.props.FloatProperty(name='YLength', default=1.0) #type: ignore
    m_ZLength: bpy.props.FloatProperty(name='ZLength', default=1.0) #type: ignore
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_XLength','m_YLength','m_ZLength','m_Center',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKCubeSource )        
TYPENAMES.append('VTKCubeSourceType' )

#--------------------------------------------------------------
class VTKCursor2D(Node, PBVTK_Node):

    bl_idname = 'VTKCursor2DType'
    bl_label  = 'vtkCursor2D'
    
    m_Axes: bpy.props.BoolProperty(name='Axes', default=True) #type: ignore
    m_Outline: bpy.props.BoolProperty(name='Outline', default=True) #type: ignore
    m_Point: bpy.props.BoolProperty(name='Point', default=True) #type: ignore
    m_TranslationMode: bpy.props.BoolProperty(name='TranslationMode', default=True) #type: ignore
    m_Wrap: bpy.props.BoolProperty(name='Wrap', default=True) #type: ignore
    m_Radius: bpy.props.FloatProperty(name='Radius', default=2.0) #type: ignore
    m_ModelBounds: bpy.props.FloatVectorProperty(name='ModelBounds', default=[-10.0, 10.0, -10.0, 10.0, 0.0, 0.0], size=6) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Axes','m_Outline','m_Point','m_TranslationMode','m_Wrap','m_Radius','m_ModelBounds',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKCursor2D )        
TYPENAMES.append('VTKCursor2DType' )

#--------------------------------------------------------------
class VTKCursor3D(Node, PBVTK_Node):

    bl_idname = 'VTKCursor3DType'
    bl_label  = 'vtkCursor3D'
    
    m_Axes: bpy.props.BoolProperty(name='Axes', default=True) #type: ignore
    m_Outline: bpy.props.BoolProperty(name='Outline', default=True) #type: ignore
    m_TranslationMode: bpy.props.BoolProperty(name='TranslationMode', default=True) #type: ignore
    m_Wrap: bpy.props.BoolProperty(name='Wrap', default=True) #type: ignore
    m_XShadows: bpy.props.BoolProperty(name='XShadows', default=True) #type: ignore
    m_YShadows: bpy.props.BoolProperty(name='YShadows', default=True) #type: ignore
    m_ZShadows: bpy.props.BoolProperty(name='ZShadows', default=True) #type: ignore
    m_ModelBounds: bpy.props.FloatVectorProperty(name='ModelBounds', default=[-1.0, 1.0, -1.0, 1.0, -1.0, 1.0], size=6) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Axes','m_Outline','m_TranslationMode','m_Wrap','m_XShadows','m_YShadows','m_ZShadows','m_ModelBounds',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKCursor3D )        
TYPENAMES.append('VTKCursor3DType' )

#--------------------------------------------------------------
class VTKCylinderSource(Node, PBVTK_Node):

    bl_idname = 'VTKCylinderSourceType'
    bl_label  = 'vtkCylinderSource'
    
    m_Capping: bpy.props.BoolProperty(name='Capping', default=True) #type: ignore
    m_CapsuleCap: bpy.props.BoolProperty(name='CapsuleCap', default=True) #type: ignore
    m_LatLongTessellation: bpy.props.BoolProperty(name='LatLongTessellation', default=True) #type: ignore
    m_Resolution: bpy.props.IntProperty(name='Resolution', default=6) #type: ignore
    m_Height: bpy.props.FloatProperty(name='Height', default=1.0) #type: ignore
    m_Radius: bpy.props.FloatProperty(name='Radius', default=0.5) #type: ignore
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Capping','m_CapsuleCap','m_LatLongTessellation','m_Resolution','m_Height','m_Radius','m_Center',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKCylinderSource )        
TYPENAMES.append('VTKCylinderSourceType' )

#--------------------------------------------------------------
class VTKDataObjectGenerator(Node, PBVTK_Node):

    bl_idname = 'VTKDataObjectGeneratorType'
    bl_label  = 'vtkDataObjectGenerator'
    
    m_Program: bpy.props.StringProperty(name='Program', default="ID1") #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Program',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKDataObjectGenerator )        
TYPENAMES.append('VTKDataObjectGeneratorType' )

#--------------------------------------------------------------
class VTKDiagonalMatrixSource(Node, PBVTK_Node):

    bl_idname = 'VTKDiagonalMatrixSourceType'
    bl_label  = 'vtkDiagonalMatrixSource'
    
    m_ColumnLabel: bpy.props.StringProperty(name='ColumnLabel', default="columns") #type: ignore
    m_RowLabel: bpy.props.StringProperty(name='RowLabel', default="rows") #type: ignore
    m_ArrayType: bpy.props.IntProperty(name='ArrayType', default=0) #type: ignore
    m_Extents: bpy.props.IntProperty(name='Extents', default=3) #type: ignore
    m_Diagonal: bpy.props.FloatProperty(name='Diagonal', default=1.0) #type: ignore
    m_SubDiagonal: bpy.props.FloatProperty(name='SubDiagonal', default=0.0) #type: ignore
    m_SuperDiagonal: bpy.props.FloatProperty(name='SuperDiagonal', default=0.0) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_ColumnLabel','m_RowLabel','m_ArrayType','m_Extents','m_Diagonal','m_SubDiagonal','m_SuperDiagonal',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKDiagonalMatrixSource )        
TYPENAMES.append('VTKDiagonalMatrixSourceType' )

#--------------------------------------------------------------
class VTKDiskSource(Node, PBVTK_Node):

    bl_idname = 'VTKDiskSourceType'
    bl_label  = 'vtkDiskSource'
    
    m_CircumferentialResolution: bpy.props.IntProperty(name='CircumferentialResolution', default=6) #type: ignore
    m_RadialResolution: bpy.props.IntProperty(name='RadialResolution', default=1) #type: ignore
    m_InnerRadius: bpy.props.FloatProperty(name='InnerRadius', default=0.25) #type: ignore
    m_OuterRadius: bpy.props.FloatProperty(name='OuterRadius', default=0.5) #type: ignore
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    m_Normal: bpy.props.FloatVectorProperty(name='Normal', default=[0.0, 0.0, 1.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_CircumferentialResolution','m_RadialResolution','m_InnerRadius','m_OuterRadius','m_Center','m_Normal',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKDiskSource )        
TYPENAMES.append('VTKDiskSourceType' )

#--------------------------------------------------------------
class VTKEarthSource(Node, PBVTK_Node):

    bl_idname = 'VTKEarthSourceType'
    bl_label  = 'vtkEarthSource'
    
    m_Outline: bpy.props.BoolProperty(name='Outline', default=True) #type: ignore
    m_OnRatio: bpy.props.IntProperty(name='OnRatio', default=10) #type: ignore
    m_Radius: bpy.props.FloatProperty(name='Radius', default=1.0) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Outline','m_OnRatio','m_Radius',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKEarthSource )        
TYPENAMES.append('VTKEarthSourceType' )

#--------------------------------------------------------------
class VTKEllipseArcSource(Node, PBVTK_Node):

    bl_idname = 'VTKEllipseArcSourceType'
    bl_label  = 'vtkEllipseArcSource'
    
    m_Close: bpy.props.BoolProperty(name='Close', default=False) #type: ignore
    m_Resolution: bpy.props.IntProperty(name='Resolution', default=100) #type: ignore
    m_Ratio: bpy.props.FloatProperty(name='Ratio', default=1.0) #type: ignore
    m_SegmentAngle: bpy.props.FloatProperty(name='SegmentAngle', default=90.0) #type: ignore
    m_StartAngle: bpy.props.FloatProperty(name='StartAngle', default=0.0) #type: ignore
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    m_MajorRadiusVector: bpy.props.FloatVectorProperty(name='MajorRadiusVector', default=[1.0, 0.0, 0.0], size=3) #type: ignore
    m_Normal: bpy.props.FloatVectorProperty(name='Normal', default=[0.0, 0.0, 1.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Close','m_Resolution','m_Ratio','m_SegmentAngle','m_StartAngle','m_Center','m_MajorRadiusVector','m_Normal',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKEllipseArcSource )        
TYPENAMES.append('VTKEllipseArcSourceType' )

#--------------------------------------------------------------
class VTKEllipticalButtonSource(Node, PBVTK_Node):

    bl_idname = 'VTKEllipticalButtonSourceType'
    bl_label  = 'vtkEllipticalButtonSource'
    e_TextureStyle_items=[ (x,x,x) for x in ['FitImage', 'Proportional']]
    
    m_TwoSided: bpy.props.BoolProperty(name='TwoSided', default=True) #type: ignore
    m_CircumferentialResolution: bpy.props.IntProperty(name='CircumferentialResolution', default=4) #type: ignore
    m_ShoulderResolution: bpy.props.IntProperty(name='ShoulderResolution', default=2) #type: ignore
    m_TextureResolution: bpy.props.IntProperty(name='TextureResolution', default=2) #type: ignore
    m_Depth: bpy.props.FloatProperty(name='Depth', default=0.05) #type: ignore
    m_Height: bpy.props.FloatProperty(name='Height', default=0.5) #type: ignore
    m_RadialRatio: bpy.props.FloatProperty(name='RadialRatio', default=1.1) #type: ignore
    m_Width: bpy.props.FloatProperty(name='Width', default=0.5) #type: ignore
    e_TextureStyle: bpy.props.EnumProperty(name='TextureStyle', default="Proportional", items=e_TextureStyle_items) #type: ignore
    m_TextureDimensions: bpy.props.IntVectorProperty(name='TextureDimensions', default=[100, 100], size=2) #type: ignore
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    m_ShoulderTextureCoordinate: bpy.props.FloatVectorProperty(name='ShoulderTextureCoordinate', default=[0.0, 0.0], size=2) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_TwoSided','m_CircumferentialResolution','m_ShoulderResolution','m_TextureResolution','m_Depth','m_Height','m_RadialRatio','m_Width','e_TextureStyle','m_TextureDimensions','m_Center','m_ShoulderTextureCoordinate',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKEllipticalButtonSource )        
TYPENAMES.append('VTKEllipticalButtonSourceType' )

#--------------------------------------------------------------
class VTKEnsembleSource(Node, PBVTK_Node):

    bl_idname = 'VTKEnsembleSourceType'
    bl_label  = 'vtkEnsembleSource'
    
    m_CurrentMember: bpy.props.IntProperty(name='CurrentMember', default=0) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_CurrentMember',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKEnsembleSource )        
TYPENAMES.append('VTKEnsembleSourceType' )

#--------------------------------------------------------------
class VTKFrustumSource(Node, PBVTK_Node):

    bl_idname = 'VTKFrustumSourceType'
    bl_label  = 'vtkFrustumSource'
    
    m_ShowLines: bpy.props.BoolProperty(name='ShowLines', default=True) #type: ignore
    m_LinesLength: bpy.props.FloatProperty(name='LinesLength', default=1.0) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_ShowLines','m_LinesLength',]
    def m_connections( self ):
        return ([], ['VTK Output'], ['Planes'], []) 
    
add_class( VTKFrustumSource )        
TYPENAMES.append('VTKFrustumSourceType' )

#--------------------------------------------------------------
class VTKGlyphSource2D(Node, PBVTK_Node):

    bl_idname = 'VTKGlyphSource2DType'
    bl_label  = 'vtkGlyphSource2D'
    e_GlyphType_items=[ (x,x,x) for x in ['None', 'Vertex', 'Dash', 'Cross', 'ThickCross', 'Triangle', 'Square', 'Circle', 'Diamond', 'Arrow', 'ThickArrow', 'HookedArrow', 'EdgeArrow']]
    
    m_Cross: bpy.props.BoolProperty(name='Cross', default=True) #type: ignore
    m_Dash: bpy.props.BoolProperty(name='Dash', default=True) #type: ignore
    m_DoublePointed: bpy.props.BoolProperty(name='DoublePointed', default=False) #type: ignore
    m_Filled: bpy.props.BoolProperty(name='Filled', default=True) #type: ignore
    m_PointInwards: bpy.props.BoolProperty(name='PointInwards', default=False) #type: ignore
    m_Resolution: bpy.props.IntProperty(name='Resolution', default=8) #type: ignore
    m_RotationAngle: bpy.props.FloatProperty(name='RotationAngle', default=0.0) #type: ignore
    m_Scale: bpy.props.FloatProperty(name='Scale', default=1.0) #type: ignore
    m_Scale2: bpy.props.FloatProperty(name='Scale2', default=1.5) #type: ignore
    m_TipLength: bpy.props.FloatProperty(name='TipLength', default=0.3) #type: ignore
    e_GlyphType: bpy.props.EnumProperty(name='GlyphType', default="Vertex", items=e_GlyphType_items) #type: ignore
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    m_Color: bpy.props.FloatVectorProperty(name='Color', default=[1.0, 1.0, 1.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Cross','m_Dash','m_DoublePointed','m_Filled','m_PointInwards','m_Resolution','m_RotationAngle','m_Scale','m_Scale2','m_TipLength','e_GlyphType','m_Center','m_Color',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKGlyphSource2D )        
TYPENAMES.append('VTKGlyphSource2DType' )

#--------------------------------------------------------------
class VTKGoldenBallSource(Node, PBVTK_Node):

    bl_idname = 'VTKGoldenBallSourceType'
    bl_label  = 'vtkGoldenBallSource'
    
    m_GenerateNormals: bpy.props.BoolProperty(name='GenerateNormals', default=True) #type: ignore
    m_IncludeCenterPoint: bpy.props.BoolProperty(name='IncludeCenterPoint', default=True) #type: ignore
    m_Resolution: bpy.props.IntProperty(name='Resolution', default=20) #type: ignore
    m_Radius: bpy.props.FloatProperty(name='Radius', default=0.5) #type: ignore
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_GenerateNormals','m_IncludeCenterPoint','m_Resolution','m_Radius','m_Center',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKGoldenBallSource )        
TYPENAMES.append('VTKGoldenBallSourceType' )

#--------------------------------------------------------------
class VTKHyperTreeGridPreConfiguredSource(Node, PBVTK_Node):

    bl_idname = 'VTKHyperTreeGridPreConfiguredSourceType'
    bl_label  = 'vtkHyperTreeGridPreConfiguredSource'
    
    m_CustomDepth: bpy.props.IntProperty(name='CustomDepth', default=2) #type: ignore
    m_CustomDim: bpy.props.IntProperty(name='CustomDim', default=2) #type: ignore
    m_CustomFactor: bpy.props.IntProperty(name='CustomFactor', default=2) #type: ignore
    m_CustomSubdivisions: bpy.props.IntVectorProperty(name='CustomSubdivisions', default=[2, 2, 2], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_CustomDepth','m_CustomDim','m_CustomFactor','m_CustomSubdivisions',]
    def m_connections( self ):
        return ([], ['VTK Output'], ['CustomArchitecture', 'HTGMode'], []) 
    
add_class( VTKHyperTreeGridPreConfiguredSource )        
TYPENAMES.append('VTKHyperTreeGridPreConfiguredSourceType' )

#--------------------------------------------------------------
class VTKHyperTreeGridSource(Node, PBVTK_Node):

    bl_idname = 'VTKHyperTreeGridSourceType'
    bl_label  = 'vtkHyperTreeGridSource'
    
    m_GenerateInterfaceFields: bpy.props.BoolProperty(name='GenerateInterfaceFields', default=False) #type: ignore
    m_TransposedRootIndexing: bpy.props.BoolProperty(name='TransposedRootIndexing', default=False) #type: ignore
    m_UseDescriptor: bpy.props.BoolProperty(name='UseDescriptor', default=True) #type: ignore
    m_UseMask: bpy.props.BoolProperty(name='UseMask', default=False) #type: ignore
    m_Descriptor: bpy.props.StringProperty(name='Descriptor', default=".") #type: ignore
    m_Mask: bpy.props.StringProperty(name='Mask', default="0") #type: ignore
    m_BranchFactor: bpy.props.IntProperty(name='BranchFactor', default=2) #type: ignore
    m_MaxDepth: bpy.props.IntProperty(name='MaxDepth', default=1) #type: ignore
    m_GridScale: bpy.props.FloatVectorProperty(name='GridScale', default=[1.0, 1.0, 1.0], size=3) #type: ignore
    m_Origin: bpy.props.FloatVectorProperty(name='Origin', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_GenerateInterfaceFields','m_TransposedRootIndexing','m_UseDescriptor','m_UseMask','m_Descriptor','m_Mask','m_BranchFactor','m_MaxDepth','m_GridScale','m_Origin',]
    def m_connections( self ):
        return ([], ['VTK Output'], ['Quadric', 'DescriptorBits', 'MaskBits'], []) 
    
add_class( VTKHyperTreeGridSource )        
TYPENAMES.append('VTKHyperTreeGridSourceType' )

#--------------------------------------------------------------
class VTKImageCanvasSource2D(Node, PBVTK_Node):

    bl_idname = 'VTKImageCanvasSource2DType'
    bl_label  = 'vtkImageCanvasSource2D'
    e_ScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Long', 'UnsignedLong', 'Float', 'Double']]
    
    m_DefaultZ: bpy.props.IntProperty(name='DefaultZ', default=0) #type: ignore
    m_NumberOfScalarComponents: bpy.props.IntProperty(name='NumberOfScalarComponents', default=1) #type: ignore
    e_ScalarType: bpy.props.EnumProperty(name='ScalarType', default="Double", items=e_ScalarType_items) #type: ignore
    m_DrawColor: bpy.props.FloatVectorProperty(name='DrawColor', default=[0.0, 0.0, 0.0, 0.0], size=4) #type: ignore
    m_Ratio: bpy.props.FloatVectorProperty(name='Ratio', default=[1.0, 1.0, 1.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_DefaultZ','m_NumberOfScalarComponents','e_ScalarType','m_DrawColor','m_Ratio',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKImageCanvasSource2D )        
TYPENAMES.append('VTKImageCanvasSource2DType' )

#--------------------------------------------------------------
class VTKImageEllipsoidSource(Node, PBVTK_Node):

    bl_idname = 'VTKImageEllipsoidSourceType'
    bl_label  = 'vtkImageEllipsoidSource'
    e_OutputScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Long', 'UnsignedLong', 'Float', 'Double']]
    
    m_InValue: bpy.props.FloatProperty(name='InValue', default=255.0) #type: ignore
    m_OutValue: bpy.props.FloatProperty(name='OutValue', default=0.0) #type: ignore
    e_OutputScalarType: bpy.props.EnumProperty(name='OutputScalarType', default="UnsignedChar", items=e_OutputScalarType_items) #type: ignore
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[128.0, 128.0, 0.0], size=3) #type: ignore
    m_Radius: bpy.props.FloatVectorProperty(name='Radius', default=[70.0, 70.0, 70.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_InValue','m_OutValue','e_OutputScalarType','m_Center','m_Radius',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKImageEllipsoidSource )        
TYPENAMES.append('VTKImageEllipsoidSourceType' )

#--------------------------------------------------------------
class VTKImageGaussianSource(Node, PBVTK_Node):

    bl_idname = 'VTKImageGaussianSourceType'
    bl_label  = 'vtkImageGaussianSource'
    
    m_Maximum: bpy.props.FloatProperty(name='Maximum', default=1.0) #type: ignore
    m_StandardDeviation: bpy.props.FloatProperty(name='StandardDeviation', default=100.0) #type: ignore
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Maximum','m_StandardDeviation','m_Center',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKImageGaussianSource )        
TYPENAMES.append('VTKImageGaussianSourceType' )

#--------------------------------------------------------------
class VTKImageGridSource(Node, PBVTK_Node):

    bl_idname = 'VTKImageGridSourceType'
    bl_label  = 'vtkImageGridSource'
    e_DataScalarType_items=[ (x,x,x) for x in ['UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'Double']]
    
    m_FillValue: bpy.props.FloatProperty(name='FillValue', default=0.0) #type: ignore
    m_LineValue: bpy.props.FloatProperty(name='LineValue', default=1.0) #type: ignore
    e_DataScalarType: bpy.props.EnumProperty(name='DataScalarType', default="Double", items=e_DataScalarType_items) #type: ignore
    m_GridOrigin: bpy.props.IntVectorProperty(name='GridOrigin', default=[0, 0, 0], size=3) #type: ignore
    m_GridSpacing: bpy.props.IntVectorProperty(name='GridSpacing', default=[10, 10, 0], size=3) #type: ignore
    m_DataOrigin: bpy.props.FloatVectorProperty(name='DataOrigin', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    m_DataSpacing: bpy.props.FloatVectorProperty(name='DataSpacing', default=[1.0, 1.0, 1.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_FillValue','m_LineValue','e_DataScalarType','m_GridOrigin','m_GridSpacing','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKImageGridSource )        
TYPENAMES.append('VTKImageGridSourceType' )

#--------------------------------------------------------------
class VTKImageImport(Node, PBVTK_Node):

    bl_idname = 'VTKImageImportType'
    bl_label  = 'vtkImageImport'
    e_DataScalarType_items=[ (x,x,x) for x in ['UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'Float', 'Double']]
    
    m_ScalarArrayName: bpy.props.StringProperty(name='ScalarArrayName', default="scalars") #type: ignore
    m_NumberOfScalarComponents: bpy.props.IntProperty(name='NumberOfScalarComponents', default=1) #type: ignore
    e_DataScalarType: bpy.props.EnumProperty(name='DataScalarType', default="Short", items=e_DataScalarType_items) #type: ignore
    m_DataOrigin: bpy.props.FloatVectorProperty(name='DataOrigin', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    m_DataSpacing: bpy.props.FloatVectorProperty(name='DataSpacing', default=[1.0, 1.0, 1.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_ScalarArrayName','m_NumberOfScalarComponents','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['VTK Output'], ['CallbackUserData', 'ImportVoidPointer'], []) 
    
add_class( VTKImageImport )        
TYPENAMES.append('VTKImageImportType' )

#--------------------------------------------------------------
class VTKImageMandelbrotSource(Node, PBVTK_Node):

    bl_idname = 'VTKImageMandelbrotSourceType'
    bl_label  = 'vtkImageMandelbrotSource'
    
    m_ConstantSize: bpy.props.BoolProperty(name='ConstantSize', default=True) #type: ignore
    m_MaximumNumberOfIterations: bpy.props.IntProperty(name='MaximumNumberOfIterations', default=100) #type: ignore
    m_SubsampleRate: bpy.props.IntProperty(name='SubsampleRate', default=1) #type: ignore
    m_ProjectionAxes: bpy.props.IntVectorProperty(name='ProjectionAxes', default=[0, 1, 2], size=3) #type: ignore
    m_OriginCX: bpy.props.FloatVectorProperty(name='OriginCX', default=[-1.75, -1.25, 0.0, 0.0], size=4) #type: ignore
    m_SampleCX: bpy.props.FloatVectorProperty(name='SampleCX', default=[0.01, 0.01, 0.01, 0.01], size=4) #type: ignore
    m_SizeCX: bpy.props.FloatVectorProperty(name='SizeCX', default=[2.5, 2.5, 2.0, 1.5], size=4) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_ConstantSize','m_MaximumNumberOfIterations','m_SubsampleRate','m_ProjectionAxes','m_OriginCX','m_SampleCX','m_SizeCX',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKImageMandelbrotSource )        
TYPENAMES.append('VTKImageMandelbrotSourceType' )

#--------------------------------------------------------------
class VTKImageNoiseSource(Node, PBVTK_Node):

    bl_idname = 'VTKImageNoiseSourceType'
    bl_label  = 'vtkImageNoiseSource'
    
    m_Maximum: bpy.props.FloatProperty(name='Maximum', default=10.0) #type: ignore
    m_Minimum: bpy.props.FloatProperty(name='Minimum', default=0.0) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Maximum','m_Minimum',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKImageNoiseSource )        
TYPENAMES.append('VTKImageNoiseSourceType' )

#--------------------------------------------------------------
class VTKImageSinusoidSource(Node, PBVTK_Node):

    bl_idname = 'VTKImageSinusoidSourceType'
    bl_label  = 'vtkImageSinusoidSource'
    
    m_Amplitude: bpy.props.FloatProperty(name='Amplitude', default=255.0) #type: ignore
    m_Period: bpy.props.FloatProperty(name='Period', default=20.0) #type: ignore
    m_Phase: bpy.props.FloatProperty(name='Phase', default=0.0) #type: ignore
    m_Direction: bpy.props.FloatVectorProperty(name='Direction', default=[1.0, 0.0, 0.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Amplitude','m_Period','m_Phase','m_Direction',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKImageSinusoidSource )        
TYPENAMES.append('VTKImageSinusoidSourceType' )

#--------------------------------------------------------------
class VTKImplicitFunctionToImageStencil(Node, PBVTK_Node):

    bl_idname = 'VTKImplicitFunctionToImageStencilType'
    bl_label  = 'vtkImplicitFunctionToImageStencil'
    
    m_Threshold: bpy.props.FloatProperty(name='Threshold', default=0.0) #type: ignore
    m_OutputWholeExtent: bpy.props.IntVectorProperty(name='OutputWholeExtent', default=[0, -1, 0, -1, 0, -1], size=6) #type: ignore
    m_OutputOrigin: bpy.props.FloatVectorProperty(name='OutputOrigin', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    m_OutputSpacing: bpy.props.FloatVectorProperty(name='OutputSpacing', default=[1.0, 1.0, 1.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Threshold','m_OutputWholeExtent','m_OutputOrigin','m_OutputSpacing',]
    def m_connections( self ):
        return ([], ['VTK Output'], ['Input'], []) 
    
add_class( VTKImplicitFunctionToImageStencil )        
TYPENAMES.append('VTKImplicitFunctionToImageStencilType' )

#--------------------------------------------------------------
class VTKLassoStencilSource(Node, PBVTK_Node):

    bl_idname = 'VTKLassoStencilSourceType'
    bl_label  = 'vtkLassoStencilSource'
    e_Shape_items=[ (x,x,x) for x in ['Polygon', 'Spline']]
    
    m_SliceOrientation: bpy.props.IntProperty(name='SliceOrientation', default=2) #type: ignore
    e_Shape: bpy.props.EnumProperty(name='Shape', default="Polygon", items=e_Shape_items) #type: ignore
    m_OutputWholeExtent: bpy.props.IntVectorProperty(name='OutputWholeExtent', default=[0, -1, 0, -1, 0, -1], size=6) #type: ignore
    m_OutputOrigin: bpy.props.FloatVectorProperty(name='OutputOrigin', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    m_OutputSpacing: bpy.props.FloatVectorProperty(name='OutputSpacing', default=[1.0, 1.0, 1.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_SliceOrientation','e_Shape','m_OutputWholeExtent','m_OutputOrigin','m_OutputSpacing',]
    def m_connections( self ):
        return ([], ['VTK Output'], ['Points'], []) 
    
add_class( VTKLassoStencilSource )        
TYPENAMES.append('VTKLassoStencilSourceType' )

#--------------------------------------------------------------
class VTKLineSource(Node, PBVTK_Node):

    bl_idname = 'VTKLineSourceType'
    bl_label  = 'vtkLineSource'
    
    m_UseRegularRefinement: bpy.props.BoolProperty(name='UseRegularRefinement', default=True) #type: ignore
    m_NumberOfRefinementRatios: bpy.props.IntProperty(name='NumberOfRefinementRatios', default=0) #type: ignore
    m_Resolution: bpy.props.IntProperty(name='Resolution', default=1) #type: ignore
    m_Point1: bpy.props.FloatVectorProperty(name='Point1', default=[-0.5, 0.0, 0.0], size=3) #type: ignore
    m_Point2: bpy.props.FloatVectorProperty(name='Point2', default=[0.5, 0.0, 0.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_UseRegularRefinement','m_NumberOfRefinementRatios','m_Resolution','m_Point1','m_Point2',]
    def m_connections( self ):
        return ([], ['VTK Output'], ['Points'], []) 
    
add_class( VTKLineSource )        
TYPENAMES.append('VTKLineSourceType' )

#--------------------------------------------------------------
class VTKOutlineCornerSource(Node, PBVTK_Node):

    bl_idname = 'VTKOutlineCornerSourceType'
    bl_label  = 'vtkOutlineCornerSource'
    e_BoxType_items=[ (x,x,x) for x in ['AxisAligned', 'Oriented']]
    
    m_GenerateFaces: bpy.props.BoolProperty(name='GenerateFaces', default=True) #type: ignore
    m_CornerFactor: bpy.props.FloatProperty(name='CornerFactor', default=0.2) #type: ignore
    e_BoxType: bpy.props.EnumProperty(name='BoxType', default="AxisAligned", items=e_BoxType_items) #type: ignore
    m_Bounds: bpy.props.FloatVectorProperty(name='Bounds', default=[-1.0, 1.0, -1.0, 1.0, -1.0, 1.0], size=6) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_GenerateFaces','m_CornerFactor','e_BoxType','m_Bounds',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKOutlineCornerSource )        
TYPENAMES.append('VTKOutlineCornerSourceType' )

#--------------------------------------------------------------
class VTKOutlineSource(Node, PBVTK_Node):

    bl_idname = 'VTKOutlineSourceType'
    bl_label  = 'vtkOutlineSource'
    e_BoxType_items=[ (x,x,x) for x in ['AxisAligned', 'Oriented']]
    
    m_GenerateFaces: bpy.props.BoolProperty(name='GenerateFaces', default=True) #type: ignore
    e_BoxType: bpy.props.EnumProperty(name='BoxType', default="AxisAligned", items=e_BoxType_items) #type: ignore
    m_Bounds: bpy.props.FloatVectorProperty(name='Bounds', default=[-1.0, 1.0, -1.0, 1.0, -1.0, 1.0], size=6) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_GenerateFaces','e_BoxType','m_Bounds',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKOutlineSource )        
TYPENAMES.append('VTKOutlineSourceType' )

#--------------------------------------------------------------
class VTKPSphereSource(Node, PBVTK_Node):

    bl_idname = 'VTKPSphereSourceType'
    bl_label  = 'vtkPSphereSource'
    
    m_GenerateNormals: bpy.props.BoolProperty(name='GenerateNormals', default=True) #type: ignore
    m_LatLongTessellation: bpy.props.BoolProperty(name='LatLongTessellation', default=True) #type: ignore
    m_PhiResolution: bpy.props.IntProperty(name='PhiResolution', default=8) #type: ignore
    m_ThetaResolution: bpy.props.IntProperty(name='ThetaResolution', default=8) #type: ignore
    m_EndPhi: bpy.props.FloatProperty(name='EndPhi', default=180.0) #type: ignore
    m_EndTheta: bpy.props.FloatProperty(name='EndTheta', default=360.0) #type: ignore
    m_Radius: bpy.props.FloatProperty(name='Radius', default=0.5) #type: ignore
    m_StartPhi: bpy.props.FloatProperty(name='StartPhi', default=0.0) #type: ignore
    m_StartTheta: bpy.props.FloatProperty(name='StartTheta', default=0.0) #type: ignore
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_GenerateNormals','m_LatLongTessellation','m_PhiResolution','m_ThetaResolution','m_EndPhi','m_EndTheta','m_Radius','m_StartPhi','m_StartTheta','m_Center',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKPSphereSource )        
TYPENAMES.append('VTKPSphereSourceType' )

#--------------------------------------------------------------
class VTKParametricFunctionSource(Node, PBVTK_Node):

    bl_idname = 'VTKParametricFunctionSourceType'
    bl_label  = 'vtkParametricFunctionSource'
    e_ScalarMode_items=[ (x,x,x) for x in ['None', 'U', 'V', 'U0', 'V0', 'U0V0', 'Modulus', 'Phase', 'Quadrant', 'X', 'Y', 'Z', 'Distance', 'FunctionDefined']]
    
    m_GenerateNormals: bpy.props.BoolProperty(name='GenerateNormals', default=True) #type: ignore
    m_GenerateTextureCoordinates: bpy.props.BoolProperty(name='GenerateTextureCoordinates', default=True) #type: ignore
    m_UResolution: bpy.props.IntProperty(name='UResolution', default=50) #type: ignore
    m_VResolution: bpy.props.IntProperty(name='VResolution', default=50) #type: ignore
    m_WResolution: bpy.props.IntProperty(name='WResolution', default=50) #type: ignore
    e_ScalarMode: bpy.props.EnumProperty(name='ScalarMode', default="None", items=e_ScalarMode_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_GenerateNormals','m_GenerateTextureCoordinates','m_UResolution','m_VResolution','m_WResolution','e_ScalarMode',]
    def m_connections( self ):
        return ([], ['VTK Output'], ['ParametricFunction'], []) 
    
add_class( VTKParametricFunctionSource )        
TYPENAMES.append('VTKParametricFunctionSourceType' )

#--------------------------------------------------------------
class VTKPartitionedDataSetCollectionSource(Node, PBVTK_Node):

    bl_idname = 'VTKPartitionedDataSetCollectionSourceType'
    bl_label  = 'vtkPartitionedDataSetCollectionSource'
    
    m_NumberOfShapes: bpy.props.IntProperty(name='NumberOfShapes', default=7) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_NumberOfShapes',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKPartitionedDataSetCollectionSource )        
TYPENAMES.append('VTKPartitionedDataSetCollectionSourceType' )

#--------------------------------------------------------------
class VTKPartitionedDataSetSource(Node, PBVTK_Node):

    bl_idname = 'VTKPartitionedDataSetSourceType'
    bl_label  = 'vtkPartitionedDataSetSource'
    
    m_NumberOfPartitions: bpy.props.IntProperty(name='NumberOfPartitions', default=0) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_NumberOfPartitions',]
    def m_connections( self ):
        return ([], ['VTK Output'], ['ParametricFunction'], []) 
    
add_class( VTKPartitionedDataSetSource )        
TYPENAMES.append('VTKPartitionedDataSetSourceType' )

#--------------------------------------------------------------
class VTKPlaneSource(Node, PBVTK_Node):

    bl_idname = 'VTKPlaneSourceType'
    bl_label  = 'vtkPlaneSource'
    
    m_XResolution: bpy.props.IntProperty(name='XResolution', default=1) #type: ignore
    m_YResolution: bpy.props.IntProperty(name='YResolution', default=1) #type: ignore
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    m_Normal: bpy.props.FloatVectorProperty(name='Normal', default=[0.0, 0.0, 1.0], size=3) #type: ignore
    m_Origin: bpy.props.FloatVectorProperty(name='Origin', default=[-0.5, -0.5, 0.0], size=3) #type: ignore
    m_Point1: bpy.props.FloatVectorProperty(name='Point1', default=[0.5, -0.5, 0.0], size=3) #type: ignore
    m_Point2: bpy.props.FloatVectorProperty(name='Point2', default=[-0.5, 0.5, 0.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_XResolution','m_YResolution','m_Center','m_Normal','m_Origin','m_Point1','m_Point2',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKPlaneSource )        
TYPENAMES.append('VTKPlaneSourceType' )

#--------------------------------------------------------------
class VTKPlatonicSolidSource(Node, PBVTK_Node):

    bl_idname = 'VTKPlatonicSolidSourceType'
    bl_label  = 'vtkPlatonicSolidSource'
    e_SolidType_items=[ (x,x,x) for x in ['Tetrahedron', 'Cube', 'Octahedron', 'Icosahedron', 'Dodecahedron']]
    
    e_SolidType: bpy.props.EnumProperty(name='SolidType', default="Tetrahedron", items=e_SolidType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['e_SolidType',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKPlatonicSolidSource )        
TYPENAMES.append('VTKPlatonicSolidSourceType' )

#--------------------------------------------------------------
class VTKPointHandleSource(Node, PBVTK_Node):

    bl_idname = 'VTKPointHandleSourceType'
    bl_label  = 'vtkPointHandleSource'
    
    m_Directional: bpy.props.BoolProperty(name='Directional', default=False) #type: ignore
    m_Size: bpy.props.FloatProperty(name='Size', default=0.5) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Directional','m_Size',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKPointHandleSource )        
TYPENAMES.append('VTKPointHandleSourceType' )

#--------------------------------------------------------------
class VTKPointLoad(Node, PBVTK_Node):

    bl_idname = 'VTKPointLoadType'
    bl_label  = 'vtkPointLoad'
    
    m_ComputeEffectiveStress: bpy.props.BoolProperty(name='ComputeEffectiveStress', default=True) #type: ignore
    m_LoadValue: bpy.props.FloatProperty(name='LoadValue', default=1.0) #type: ignore
    m_PoissonsRatio: bpy.props.FloatProperty(name='PoissonsRatio', default=0.3) #type: ignore
    m_ModelBounds: bpy.props.FloatVectorProperty(name='ModelBounds', default=[-1.0, 1.0, -1.0, 1.0, -1.0, 1.0], size=6) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_ComputeEffectiveStress','m_LoadValue','m_PoissonsRatio','m_ModelBounds',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKPointLoad )        
TYPENAMES.append('VTKPointLoadType' )

#--------------------------------------------------------------
class VTKPointSource(Node, PBVTK_Node):

    bl_idname = 'VTKPointSourceType'
    bl_label  = 'vtkPointSource'
    e_Distribution_items=[ (x,x,x) for x in ['Shell', 'Uniform', 'Exponential']]
    
    m_NumberOfPoints: bpy.props.IntProperty(name='NumberOfPoints', default=10) #type: ignore
    m_Lambda: bpy.props.FloatProperty(name='Lambda', default=1.3646668159164e-311) #type: ignore
    m_Radius: bpy.props.FloatProperty(name='Radius', default=0.5) #type: ignore
    e_Distribution: bpy.props.EnumProperty(name='Distribution', default="Uniform", items=e_Distribution_items) #type: ignore
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_NumberOfPoints','m_Lambda','m_Radius','e_Distribution','m_Center',]
    def m_connections( self ):
        return ([], ['VTK Output'], ['RandomSequence'], []) 
    
add_class( VTKPointSource )        
TYPENAMES.append('VTKPointSourceType' )

#--------------------------------------------------------------
class VTKPolyLineSource(Node, PBVTK_Node):

    bl_idname = 'VTKPolyLineSourceType'
    bl_label  = 'vtkPolyLineSource'
    
    m_Closed: bpy.props.BoolProperty(name='Closed', default=True) #type: ignore
    m_NumberOfPoints: bpy.props.IntProperty(name='NumberOfPoints', default=0) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Closed','m_NumberOfPoints',]
    def m_connections( self ):
        return ([], ['VTK Output'], ['Points'], []) 
    
add_class( VTKPolyLineSource )        
TYPENAMES.append('VTKPolyLineSourceType' )

#--------------------------------------------------------------
class VTKPolyPointSource(Node, PBVTK_Node):

    bl_idname = 'VTKPolyPointSourceType'
    bl_label  = 'vtkPolyPointSource'
    
    m_NumberOfPoints: bpy.props.IntProperty(name='NumberOfPoints', default=0) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_NumberOfPoints',]
    def m_connections( self ):
        return ([], ['VTK Output'], ['Points'], []) 
    
add_class( VTKPolyPointSource )        
TYPENAMES.append('VTKPolyPointSourceType' )

#--------------------------------------------------------------
class VTKProgrammableDataObjectSource(Node, PBVTK_Node):

    bl_idname = 'VTKProgrammableDataObjectSourceType'
    bl_label  = 'vtkProgrammableDataObjectSource'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return []
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKProgrammableDataObjectSource )        
TYPENAMES.append('VTKProgrammableDataObjectSourceType' )

#--------------------------------------------------------------
class VTKROIStencilSource(Node, PBVTK_Node):

    bl_idname = 'VTKROIStencilSourceType'
    bl_label  = 'vtkROIStencilSource'
    e_Shape_items=[ (x,x,x) for x in ['Box', 'Ellipsoid', 'CylinderX', 'CylinderY', 'CylinderZ']]
    
    e_Shape: bpy.props.EnumProperty(name='Shape', default="Box", items=e_Shape_items) #type: ignore
    m_OutputWholeExtent: bpy.props.IntVectorProperty(name='OutputWholeExtent', default=[0, -1, 0, -1, 0, -1], size=6) #type: ignore
    m_Bounds: bpy.props.FloatVectorProperty(name='Bounds', default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6) #type: ignore
    m_OutputOrigin: bpy.props.FloatVectorProperty(name='OutputOrigin', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    m_OutputSpacing: bpy.props.FloatVectorProperty(name='OutputSpacing', default=[1.0, 1.0, 1.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['e_Shape','m_OutputWholeExtent','m_Bounds','m_OutputOrigin','m_OutputSpacing',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKROIStencilSource )        
TYPENAMES.append('VTKROIStencilSourceType' )

#--------------------------------------------------------------
class VTKRTAnalyticSource(Node, PBVTK_Node):

    bl_idname = 'VTKRTAnalyticSourceType'
    bl_label  = 'vtkRTAnalyticSource'
    
    m_SubsampleRate: bpy.props.IntProperty(name='SubsampleRate', default=1) #type: ignore
    m_Maximum: bpy.props.FloatProperty(name='Maximum', default=255.0) #type: ignore
    m_StandardDeviation: bpy.props.FloatProperty(name='StandardDeviation', default=0.5) #type: ignore
    m_XFreq: bpy.props.FloatProperty(name='XFreq', default=60.0) #type: ignore
    m_XMag: bpy.props.FloatProperty(name='XMag', default=10.0) #type: ignore
    m_YFreq: bpy.props.FloatProperty(name='YFreq', default=30.0) #type: ignore
    m_YMag: bpy.props.FloatProperty(name='YMag', default=18.0) #type: ignore
    m_ZFreq: bpy.props.FloatProperty(name='ZFreq', default=40.0) #type: ignore
    m_ZMag: bpy.props.FloatProperty(name='ZMag', default=5.0) #type: ignore
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_SubsampleRate','m_Maximum','m_StandardDeviation','m_XFreq','m_XMag','m_YFreq','m_YMag','m_ZFreq','m_ZMag','m_Center',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKRTAnalyticSource )        
TYPENAMES.append('VTKRTAnalyticSourceType' )

#--------------------------------------------------------------
class VTKRandomHyperTreeGridSource(Node, PBVTK_Node):

    bl_idname = 'VTKRandomHyperTreeGridSourceType'
    bl_label  = 'vtkRandomHyperTreeGridSource'
    
    m_MaxDepth: bpy.props.IntProperty(name='MaxDepth', default=5) #type: ignore
    m_Seed: bpy.props.IntProperty(name='Seed', default=0) #type: ignore
    m_MaskedFraction: bpy.props.FloatProperty(name='MaskedFraction', default=0.0) #type: ignore
    m_SplitFraction: bpy.props.FloatProperty(name='SplitFraction', default=0.5) #type: ignore
    m_Dimensions: bpy.props.IntVectorProperty(name='Dimensions', default=[6, 6, 3], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_MaxDepth','m_Seed','m_MaskedFraction','m_SplitFraction','m_Dimensions',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKRandomHyperTreeGridSource )        
TYPENAMES.append('VTKRandomHyperTreeGridSourceType' )

#--------------------------------------------------------------
class VTKRectangularButtonSource(Node, PBVTK_Node):

    bl_idname = 'VTKRectangularButtonSourceType'
    bl_label  = 'vtkRectangularButtonSource'
    e_TextureStyle_items=[ (x,x,x) for x in ['FitImage', 'Proportional']]
    
    m_TwoSided: bpy.props.BoolProperty(name='TwoSided', default=True) #type: ignore
    m_BoxRatio: bpy.props.FloatProperty(name='BoxRatio', default=1.1) #type: ignore
    m_Depth: bpy.props.FloatProperty(name='Depth', default=0.05) #type: ignore
    m_Height: bpy.props.FloatProperty(name='Height', default=0.5) #type: ignore
    m_TextureHeightRatio: bpy.props.FloatProperty(name='TextureHeightRatio', default=0.95) #type: ignore
    m_TextureRatio: bpy.props.FloatProperty(name='TextureRatio', default=0.9) #type: ignore
    m_Width: bpy.props.FloatProperty(name='Width', default=0.5) #type: ignore
    e_TextureStyle: bpy.props.EnumProperty(name='TextureStyle', default="Proportional", items=e_TextureStyle_items) #type: ignore
    m_TextureDimensions: bpy.props.IntVectorProperty(name='TextureDimensions', default=[100, 100], size=2) #type: ignore
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    m_ShoulderTextureCoordinate: bpy.props.FloatVectorProperty(name='ShoulderTextureCoordinate', default=[0.0, 0.0], size=2) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_TwoSided','m_BoxRatio','m_Depth','m_Height','m_TextureHeightRatio','m_TextureRatio','m_Width','e_TextureStyle','m_TextureDimensions','m_Center','m_ShoulderTextureCoordinate',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKRectangularButtonSource )        
TYPENAMES.append('VTKRectangularButtonSourceType' )

#--------------------------------------------------------------
class VTKRegularPolygonSource(Node, PBVTK_Node):

    bl_idname = 'VTKRegularPolygonSourceType'
    bl_label  = 'vtkRegularPolygonSource'
    
    m_GeneratePolygon: bpy.props.BoolProperty(name='GeneratePolygon', default=True) #type: ignore
    m_GeneratePolyline: bpy.props.BoolProperty(name='GeneratePolyline', default=True) #type: ignore
    m_NumberOfSides: bpy.props.IntProperty(name='NumberOfSides', default=6) #type: ignore
    m_Radius: bpy.props.FloatProperty(name='Radius', default=0.5) #type: ignore
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    m_Normal: bpy.props.FloatVectorProperty(name='Normal', default=[0.0, 0.0, 1.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_GeneratePolygon','m_GeneratePolyline','m_NumberOfSides','m_Radius','m_Center','m_Normal',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKRegularPolygonSource )        
TYPENAMES.append('VTKRegularPolygonSourceType' )

#--------------------------------------------------------------
class VTKResizingWindowToImageFilter(Node, PBVTK_Node):

    bl_idname = 'VTKResizingWindowToImageFilterType'
    bl_label  = 'vtkResizingWindowToImageFilter'
    e_InputBufferType_items=[ (x,x,x) for x in ['RGB', 'RGBA', 'ZBuffer']]
    
    m_SizeLimit: bpy.props.IntProperty(name='SizeLimit', default=4000) #type: ignore
    e_InputBufferType: bpy.props.EnumProperty(name='InputBufferType', default="RGB", items=e_InputBufferType_items) #type: ignore
    m_Size: bpy.props.IntVectorProperty(name='Size', default=[0, 0], size=2) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_SizeLimit','e_InputBufferType','m_Size',]
    def m_connections( self ):
        return ([], ['VTK Output'], ['Input'], []) 
    
add_class( VTKResizingWindowToImageFilter )        
TYPENAMES.append('VTKResizingWindowToImageFilterType' )

#--------------------------------------------------------------
class VTKRowQueryToTable(Node, PBVTK_Node):

    bl_idname = 'VTKRowQueryToTableType'
    bl_label  = 'vtkRowQueryToTable'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return []
    def m_connections( self ):
        return ([], ['VTK Output'], ['Query'], []) 
    
add_class( VTKRowQueryToTable )        
TYPENAMES.append('VTKRowQueryToTableType' )

#--------------------------------------------------------------
class VTKSQLDatabaseTableSource(Node, PBVTK_Node):

    bl_idname = 'VTKSQLDatabaseTableSourceType'
    bl_label  = 'vtkSQLDatabaseTableSource'
    
    m_GeneratePedigreeIds: bpy.props.BoolProperty(name='GeneratePedigreeIds', default=True) #type: ignore
    m_PedigreeIdArrayName: bpy.props.StringProperty(name='PedigreeIdArrayName', default="id") #type: ignore
    m_Query: bpy.props.StringProperty(name='Query', default="") #type: ignore
    m_URL: bpy.props.StringProperty(name='URL', default="") #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_GeneratePedigreeIds','m_PedigreeIdArrayName','m_Query','m_URL',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKSQLDatabaseTableSource )        
TYPENAMES.append('VTKSQLDatabaseTableSourceType' )

#--------------------------------------------------------------
class VTKSampleFunction(Node, PBVTK_Node):

    bl_idname = 'VTKSampleFunctionType'
    bl_label  = 'vtkSampleFunction'
    e_OutputScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Long', 'UnsignedLong', 'Float', 'Double']]
    
    m_Capping: bpy.props.BoolProperty(name='Capping', default=True) #type: ignore
    m_ComputeNormals: bpy.props.BoolProperty(name='ComputeNormals', default=True) #type: ignore
    m_NormalArrayName: bpy.props.StringProperty(name='NormalArrayName', default="normals") #type: ignore
    m_ScalarArrayName: bpy.props.StringProperty(name='ScalarArrayName', default="scalars") #type: ignore
    m_CapValue: bpy.props.FloatProperty(name='CapValue', default=1e+30) #type: ignore
    e_OutputScalarType: bpy.props.EnumProperty(name='OutputScalarType', default="Double", items=e_OutputScalarType_items) #type: ignore
    m_SampleDimensions: bpy.props.IntVectorProperty(name='SampleDimensions', default=[50, 50, 50], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Capping','m_ComputeNormals','m_NormalArrayName','m_ScalarArrayName','m_CapValue','e_OutputScalarType','m_SampleDimensions',]
    def m_connections( self ):
        return ([], ['VTK Output'], ['ImplicitFunction'], []) 
    
add_class( VTKSampleFunction )        
TYPENAMES.append('VTKSampleFunctionType' )

#--------------------------------------------------------------
class VTKSectorSource(Node, PBVTK_Node):

    bl_idname = 'VTKSectorSourceType'
    bl_label  = 'vtkSectorSource'
    
    m_CircumferentialResolution: bpy.props.IntProperty(name='CircumferentialResolution', default=6) #type: ignore
    m_RadialResolution: bpy.props.IntProperty(name='RadialResolution', default=1) #type: ignore
    m_EndAngle: bpy.props.FloatProperty(name='EndAngle', default=90.0) #type: ignore
    m_InnerRadius: bpy.props.FloatProperty(name='InnerRadius', default=1.0) #type: ignore
    m_OuterRadius: bpy.props.FloatProperty(name='OuterRadius', default=2.0) #type: ignore
    m_StartAngle: bpy.props.FloatProperty(name='StartAngle', default=0.0) #type: ignore
    m_ZCoord: bpy.props.FloatProperty(name='ZCoord', default=0.0) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_CircumferentialResolution','m_RadialResolution','m_EndAngle','m_InnerRadius','m_OuterRadius','m_StartAngle','m_ZCoord',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKSectorSource )        
TYPENAMES.append('VTKSectorSourceType' )

#--------------------------------------------------------------
class VTKSelectionSource(Node, PBVTK_Node):

    bl_idname = 'VTKSelectionSourceType'
    bl_label  = 'vtkSelectionSource'
    e_FieldTypeOption_items=[ (x,x,x) for x in ['FieldType', 'ElementType']]
    
    m_Expression: bpy.props.StringProperty(name='Expression', default="") #type: ignore
    m_ElementType: bpy.props.IntProperty(name='ElementType', default=1) #type: ignore
    m_FieldType: bpy.props.IntProperty(name='FieldType', default=0) #type: ignore
    m_NumberOfNodes: bpy.props.IntProperty(name='NumberOfNodes', default=1) #type: ignore
    m_ProcessID: bpy.props.IntProperty(name='ProcessID', default=-1) #type: ignore
    e_FieldTypeOption: bpy.props.EnumProperty(name='FieldTypeOption', default="FieldType", items=e_FieldTypeOption_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Expression','m_ElementType','m_FieldType','m_NumberOfNodes','m_ProcessID','e_FieldTypeOption',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKSelectionSource )        
TYPENAMES.append('VTKSelectionSourceType' )

#--------------------------------------------------------------
class VTKSpatioTemporalHarmonicsSource(Node, PBVTK_Node):

    bl_idname = 'VTKSpatioTemporalHarmonicsSourceType'
    bl_label  = 'vtkSpatioTemporalHarmonicsSource'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return []
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKSpatioTemporalHarmonicsSource )        
TYPENAMES.append('VTKSpatioTemporalHarmonicsSourceType' )

#--------------------------------------------------------------
class VTKSpherePuzzle(Node, PBVTK_Node):

    bl_idname = 'VTKSpherePuzzleType'
    bl_label  = 'vtkSpherePuzzle'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return []
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKSpherePuzzle )        
TYPENAMES.append('VTKSpherePuzzleType' )

#--------------------------------------------------------------
class VTKSpherePuzzleArrows(Node, PBVTK_Node):

    bl_idname = 'VTKSpherePuzzleArrowsType'
    bl_label  = 'vtkSpherePuzzleArrows'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return []
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKSpherePuzzleArrows )        
TYPENAMES.append('VTKSpherePuzzleArrowsType' )

#--------------------------------------------------------------
class VTKSphereSource(Node, PBVTK_Node):

    bl_idname = 'VTKSphereSourceType'
    bl_label  = 'vtkSphereSource'
    
    m_GenerateNormals: bpy.props.BoolProperty(name='GenerateNormals', default=True) #type: ignore
    m_LatLongTessellation: bpy.props.BoolProperty(name='LatLongTessellation', default=True) #type: ignore
    m_PhiResolution: bpy.props.IntProperty(name='PhiResolution', default=8) #type: ignore
    m_ThetaResolution: bpy.props.IntProperty(name='ThetaResolution', default=8) #type: ignore
    m_EndPhi: bpy.props.FloatProperty(name='EndPhi', default=180.0) #type: ignore
    m_EndTheta: bpy.props.FloatProperty(name='EndTheta', default=360.0) #type: ignore
    m_Radius: bpy.props.FloatProperty(name='Radius', default=0.5) #type: ignore
    m_StartPhi: bpy.props.FloatProperty(name='StartPhi', default=0.0) #type: ignore
    m_StartTheta: bpy.props.FloatProperty(name='StartTheta', default=0.0) #type: ignore
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_GenerateNormals','m_LatLongTessellation','m_PhiResolution','m_ThetaResolution','m_EndPhi','m_EndTheta','m_Radius','m_StartPhi','m_StartTheta','m_Center',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKSphereSource )        
TYPENAMES.append('VTKSphereSourceType' )

#--------------------------------------------------------------
class VTKSuperquadricSource(Node, PBVTK_Node):

    bl_idname = 'VTKSuperquadricSourceType'
    bl_label  = 'vtkSuperquadricSource'
    
    m_Toroidal: bpy.props.BoolProperty(name='Toroidal', default=True) #type: ignore
    m_AxisOfSymmetry: bpy.props.IntProperty(name='AxisOfSymmetry', default=1) #type: ignore
    m_PhiResolution: bpy.props.IntProperty(name='PhiResolution', default=16) #type: ignore
    m_ThetaResolution: bpy.props.IntProperty(name='ThetaResolution', default=16) #type: ignore
    m_PhiRoundness: bpy.props.FloatProperty(name='PhiRoundness', default=1.0) #type: ignore
    m_Size: bpy.props.FloatProperty(name='Size', default=0.5) #type: ignore
    m_ThetaRoundness: bpy.props.FloatProperty(name='ThetaRoundness', default=1.0) #type: ignore
    m_Thickness: bpy.props.FloatProperty(name='Thickness', default=0.3333) #type: ignore
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    m_Scale: bpy.props.FloatVectorProperty(name='Scale', default=[1.0, 1.0, 1.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Toroidal','m_AxisOfSymmetry','m_PhiResolution','m_ThetaResolution','m_PhiRoundness','m_Size','m_ThetaRoundness','m_Thickness','m_Center','m_Scale',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKSuperquadricSource )        
TYPENAMES.append('VTKSuperquadricSourceType' )

#--------------------------------------------------------------
class VTKTemporalFractal(Node, PBVTK_Node):

    bl_idname = 'VTKTemporalFractalType'
    bl_label  = 'vtkTemporalFractal'
    
    m_AdaptiveSubdivision: bpy.props.BoolProperty(name='AdaptiveSubdivision', default=True) #type: ignore
    m_DiscreteTimeSteps: bpy.props.BoolProperty(name='DiscreteTimeSteps', default=True) #type: ignore
    m_GenerateRectilinearGrids: bpy.props.BoolProperty(name='GenerateRectilinearGrids', default=True) #type: ignore
    m_GhostLevels: bpy.props.BoolProperty(name='GhostLevels', default=True) #type: ignore
    m_TwoDimensional: bpy.props.BoolProperty(name='TwoDimensional', default=True) #type: ignore
    m_Asymmetric: bpy.props.IntProperty(name='Asymmetric', default=1) #type: ignore
    m_Dimensions: bpy.props.IntProperty(name='Dimensions', default=10) #type: ignore
    m_MaximumLevel: bpy.props.IntProperty(name='MaximumLevel', default=6) #type: ignore
    m_FractalValue: bpy.props.FloatProperty(name='FractalValue', default=9.5) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AdaptiveSubdivision','m_DiscreteTimeSteps','m_GenerateRectilinearGrids','m_GhostLevels','m_TwoDimensional','m_Asymmetric','m_Dimensions','m_MaximumLevel','m_FractalValue',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKTemporalFractal )        
TYPENAMES.append('VTKTemporalFractalType' )

#--------------------------------------------------------------
class VTKTessellatedBoxSource(Node, PBVTK_Node):

    bl_idname = 'VTKTessellatedBoxSourceType'
    bl_label  = 'vtkTessellatedBoxSource'
    
    m_DuplicateSharedPoints: bpy.props.BoolProperty(name='DuplicateSharedPoints', default=True) #type: ignore
    m_Quads: bpy.props.BoolProperty(name='Quads', default=True) #type: ignore
    m_Level: bpy.props.IntProperty(name='Level', default=0) #type: ignore
    m_Bounds: bpy.props.FloatVectorProperty(name='Bounds', default=[-0.5, 0.5, -0.5, 0.5, -0.5, 0.5], size=6) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_DuplicateSharedPoints','m_Quads','m_Level','m_Bounds',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKTessellatedBoxSource )        
TYPENAMES.append('VTKTessellatedBoxSourceType' )

#--------------------------------------------------------------
class VTKTextSource(Node, PBVTK_Node):

    bl_idname = 'VTKTextSourceType'
    bl_label  = 'vtkTextSource'
    
    m_Backing: bpy.props.BoolProperty(name='Backing', default=True) #type: ignore
    m_Text: bpy.props.StringProperty(name='Text', default="") #type: ignore
    m_BackgroundColor: bpy.props.FloatVectorProperty(name='BackgroundColor', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    m_ForegroundColor: bpy.props.FloatVectorProperty(name='ForegroundColor', default=[1.0, 1.0, 1.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Backing','m_Text','m_BackgroundColor','m_ForegroundColor',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKTextSource )        
TYPENAMES.append('VTKTextSourceType' )

#--------------------------------------------------------------
class VTKTexturedSphereSource(Node, PBVTK_Node):

    bl_idname = 'VTKTexturedSphereSourceType'
    bl_label  = 'vtkTexturedSphereSource'
    
    m_PhiResolution: bpy.props.IntProperty(name='PhiResolution', default=8) #type: ignore
    m_ThetaResolution: bpy.props.IntProperty(name='ThetaResolution', default=8) #type: ignore
    m_Phi: bpy.props.FloatProperty(name='Phi', default=0.0) #type: ignore
    m_Radius: bpy.props.FloatProperty(name='Radius', default=0.5) #type: ignore
    m_Theta: bpy.props.FloatProperty(name='Theta', default=0.0) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_PhiResolution','m_ThetaResolution','m_Phi','m_Radius','m_Theta',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKTexturedSphereSource )        
TYPENAMES.append('VTKTexturedSphereSourceType' )

#--------------------------------------------------------------
class VTKTimeSourceExample(Node, PBVTK_Node):

    bl_idname = 'VTKTimeSourceExampleType'
    bl_label  = 'vtkTimeSourceExample'
    
    m_Analytic: bpy.props.BoolProperty(name='Analytic', default=True) #type: ignore
    m_Growing: bpy.props.BoolProperty(name='Growing', default=True) #type: ignore
    m_XAmplitude: bpy.props.FloatProperty(name='XAmplitude', default=0.0) #type: ignore
    m_YAmplitude: bpy.props.FloatProperty(name='YAmplitude', default=0.0) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Analytic','m_Growing','m_XAmplitude','m_YAmplitude',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKTimeSourceExample )        
TYPENAMES.append('VTKTimeSourceExampleType' )

#--------------------------------------------------------------
class VTKTransformToGrid(Node, PBVTK_Node):

    bl_idname = 'VTKTransformToGridType'
    bl_label  = 'vtkTransformToGrid'
    e_GridScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Float', 'Double']]
    
    e_GridScalarType: bpy.props.EnumProperty(name='GridScalarType', default="Float", items=e_GridScalarType_items) #type: ignore
    m_GridExtent: bpy.props.IntVectorProperty(name='GridExtent', default=[0, 0, 0, 0, 0, 0], size=6) #type: ignore
    m_GridOrigin: bpy.props.FloatVectorProperty(name='GridOrigin', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    m_GridSpacing: bpy.props.FloatVectorProperty(name='GridSpacing', default=[1.0, 1.0, 1.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['e_GridScalarType','m_GridExtent','m_GridOrigin','m_GridSpacing',]
    def m_connections( self ):
        return ([], ['VTK Output'], ['Input'], []) 
    
add_class( VTKTransformToGrid )        
TYPENAMES.append('VTKTransformToGridType' )

#--------------------------------------------------------------
class VTKTriangularTexture(Node, PBVTK_Node):

    bl_idname = 'VTKTriangularTextureType'
    bl_label  = 'vtkTriangularTexture'
    
    m_TexturePattern: bpy.props.IntProperty(name='TexturePattern', default=1) #type: ignore
    m_XSize: bpy.props.IntProperty(name='XSize', default=64) #type: ignore
    m_YSize: bpy.props.IntProperty(name='YSize', default=64) #type: ignore
    m_ScaleFactor: bpy.props.FloatProperty(name='ScaleFactor', default=1.0) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_TexturePattern','m_XSize','m_YSize','m_ScaleFactor',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKTriangularTexture )        
TYPENAMES.append('VTKTriangularTextureType' )

#--------------------------------------------------------------
class VTKTrivialProducer(Node, PBVTK_Node):

    bl_idname = 'VTKTrivialProducerType'
    bl_label  = 'vtkTrivialProducer'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return []
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKTrivialProducer )        
TYPENAMES.append('VTKTrivialProducerType' )

#--------------------------------------------------------------
class VTKUniformHyperTreeGridSource(Node, PBVTK_Node):

    bl_idname = 'VTKUniformHyperTreeGridSourceType'
    bl_label  = 'vtkUniformHyperTreeGridSource'
    
    m_GenerateInterfaceFields: bpy.props.BoolProperty(name='GenerateInterfaceFields', default=False) #type: ignore
    m_TransposedRootIndexing: bpy.props.BoolProperty(name='TransposedRootIndexing', default=False) #type: ignore
    m_UseDescriptor: bpy.props.BoolProperty(name='UseDescriptor', default=True) #type: ignore
    m_UseMask: bpy.props.BoolProperty(name='UseMask', default=False) #type: ignore
    m_Descriptor: bpy.props.StringProperty(name='Descriptor', default=".") #type: ignore
    m_Mask: bpy.props.StringProperty(name='Mask', default="0") #type: ignore
    m_BranchFactor: bpy.props.IntProperty(name='BranchFactor', default=2) #type: ignore
    m_MaxDepth: bpy.props.IntProperty(name='MaxDepth', default=1) #type: ignore
    m_GridScale: bpy.props.FloatVectorProperty(name='GridScale', default=[1.0, 1.0, 1.0], size=3) #type: ignore
    m_Origin: bpy.props.FloatVectorProperty(name='Origin', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_GenerateInterfaceFields','m_TransposedRootIndexing','m_UseDescriptor','m_UseMask','m_Descriptor','m_Mask','m_BranchFactor','m_MaxDepth','m_GridScale','m_Origin',]
    def m_connections( self ):
        return ([], ['VTK Output'], ['Quadric', 'DescriptorBits', 'MaskBits'], []) 
    
add_class( VTKUniformHyperTreeGridSource )        
TYPENAMES.append('VTKUniformHyperTreeGridSourceType' )

#--------------------------------------------------------------
class VTKVectorText(Node, PBVTK_Node):

    bl_idname = 'VTKVectorTextType'
    bl_label  = 'vtkVectorText'
    
    m_Text: bpy.props.StringProperty(name='Text', default="") #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Text',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKVectorText )        
TYPENAMES.append('VTKVectorTextType' )

#--------------------------------------------------------------
class VTKVideoSource(Node, PBVTK_Node):

    bl_idname = 'VTKVideoSourceType'
    bl_label  = 'vtkVideoSource'
    e_OutputFormat_items=[ (x,x,x) for x in ['Luminance', 'RGB', 'RGBA']]
    
    m_AutoAdvance: bpy.props.BoolProperty(name='AutoAdvance', default=True) #type: ignore
    m_FrameBufferSize: bpy.props.IntProperty(name='FrameBufferSize', default=1) #type: ignore
    m_FrameCount: bpy.props.IntProperty(name='FrameCount', default=0) #type: ignore
    m_NumberOfOutputFrames: bpy.props.IntProperty(name='NumberOfOutputFrames', default=1) #type: ignore
    m_FrameRate: bpy.props.FloatProperty(name='FrameRate', default=30.0) #type: ignore
    m_Opacity: bpy.props.FloatProperty(name='Opacity', default=1.0) #type: ignore
    m_StartTimeStamp: bpy.props.FloatProperty(name='StartTimeStamp', default=0.0) #type: ignore
    e_OutputFormat: bpy.props.EnumProperty(name='OutputFormat', default="Luminance", items=e_OutputFormat_items) #type: ignore
    m_FrameSize: bpy.props.IntVectorProperty(name='FrameSize', default=[320, 240, 1], size=3) #type: ignore
    m_OutputWholeExtent: bpy.props.IntVectorProperty(name='OutputWholeExtent', default=[0, -1, 0, -1, 0, -1], size=6) #type: ignore
    m_DataOrigin: bpy.props.FloatVectorProperty(name='DataOrigin', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    m_DataSpacing: bpy.props.FloatVectorProperty(name='DataSpacing', default=[1.0, 1.0, 1.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AutoAdvance','m_FrameBufferSize','m_FrameCount','m_NumberOfOutputFrames','m_FrameRate','m_Opacity','m_StartTimeStamp','e_OutputFormat','m_FrameSize','m_OutputWholeExtent','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKVideoSource )        
TYPENAMES.append('VTKVideoSourceType' )

#--------------------------------------------------------------
class VTKWindowToImageFilter(Node, PBVTK_Node):

    bl_idname = 'VTKWindowToImageFilterType'
    bl_label  = 'vtkWindowToImageFilter'
    e_InputBufferType_items=[ (x,x,x) for x in ['RGB', 'RGBA', 'ZBuffer']]
    
    m_FixBoundary: bpy.props.BoolProperty(name='FixBoundary', default=False) #type: ignore
    m_ReadFrontBuffer: bpy.props.BoolProperty(name='ReadFrontBuffer', default=True) #type: ignore
    m_ShouldRerender: bpy.props.BoolProperty(name='ShouldRerender', default=True) #type: ignore
    e_InputBufferType: bpy.props.EnumProperty(name='InputBufferType', default="RGB", items=e_InputBufferType_items) #type: ignore
    m_Scale: bpy.props.IntVectorProperty(name='Scale', default=[1, 1], size=2) #type: ignore
    m_Viewport: bpy.props.FloatVectorProperty(name='Viewport', default=[0.0, 0.0, 1.0, 1.0], size=4) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_FixBoundary','m_ReadFrontBuffer','m_ShouldRerender','e_InputBufferType','m_Scale','m_Viewport',]
    def m_connections( self ):
        return ([], ['VTK Output'], ['Input'], []) 
    
add_class( VTKWindowToImageFilter )        
TYPENAMES.append('VTKWindowToImageFilterType' )

#--------------------------------------------------------------
class VTKWordCloud(Node, PBVTK_Node):

    bl_idname = 'VTKWordCloudType'
    bl_label  = 'vtkWordCloud'
    
    m_BWMask: bpy.props.BoolProperty(name='BWMask', default=False) #type: ignore
    m_BackgroundColorName: bpy.props.StringProperty(name='BackgroundColorName', default="MidnightBlue") #type: ignore
    m_ColorSchemeName: bpy.props.StringProperty(name='ColorSchemeName', default="") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_FontFileName: bpy.props.StringProperty(name='FontFileName', default="", subtype='FILE_PATH') #type: ignore
    m_MaskColorName: bpy.props.StringProperty(name='MaskColorName', default="black") #type: ignore
    m_MaskFileName: bpy.props.StringProperty(name='MaskFileName', default="", subtype='FILE_PATH') #type: ignore
    m_StopListFileName: bpy.props.StringProperty(name='StopListFileName', default="", subtype='FILE_PATH') #type: ignore
    m_Title: bpy.props.StringProperty(name='Title', default="") #type: ignore
    m_WordColorName: bpy.props.StringProperty(name='WordColorName', default="") #type: ignore
    m_DPI: bpy.props.IntProperty(name='DPI', default=200) #type: ignore
    m_FontMultiplier: bpy.props.IntProperty(name='FontMultiplier', default=6) #type: ignore
    m_Gap: bpy.props.IntProperty(name='Gap', default=2) #type: ignore
    m_MaxFontSize: bpy.props.IntProperty(name='MaxFontSize', default=48) #type: ignore
    m_MinFontSize: bpy.props.IntProperty(name='MinFontSize', default=12) #type: ignore
    m_MinFrequency: bpy.props.IntProperty(name='MinFrequency', default=1) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_BWMask','m_BackgroundColorName','m_ColorSchemeName','m_FileName','m_FontFileName','m_MaskColorName','m_MaskFileName','m_StopListFileName','m_Title','m_WordColorName','m_DPI','m_FontMultiplier','m_Gap','m_MaxFontSize','m_MinFontSize','m_MinFrequency',]
    def m_connections( self ):
        return ([], ['VTK Output'], [], []) 
    
add_class( VTKWordCloud )        
TYPENAMES.append('VTKWordCloudType' )

#--------------------------------------------------------------
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( PBVTK_NodeCategory( 'Source', 'Source', items=menu_items) )