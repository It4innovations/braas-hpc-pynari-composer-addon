# Generated definitions for VTK class group: Writer
# VTK version: 9.5.2

from .core import *    
TYPENAMES = []

#--------------------------------------------------------------
class VTKArrayDataWriter(Node, PBVTK_Node):

    bl_idname = 'VTKArrayDataWriterType'
    bl_label  = 'vtkArrayDataWriter'
    
    m_Binary: bpy.props.BoolProperty(name='Binary', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Binary','m_WriteToOutputString','m_FileName',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKArrayDataWriter )        
TYPENAMES.append('VTKArrayDataWriterType' )

#--------------------------------------------------------------
class VTKArrayWriter(Node, PBVTK_Node):

    bl_idname = 'VTKArrayWriterType'
    bl_label  = 'vtkArrayWriter'
    
    m_Binary: bpy.props.BoolProperty(name='Binary', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Binary','m_WriteToOutputString','m_FileName',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKArrayWriter )        
TYPENAMES.append('VTKArrayWriterType' )

#--------------------------------------------------------------
class VTKBMPWriter(Node, PBVTK_Node):

    bl_idname = 'VTKBMPWriterType'
    bl_label  = 'vtkBMPWriter'
    
    m_WriteToMemory: bpy.props.BoolProperty(name='WriteToMemory', default=True) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d") #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="") #type: ignore
    m_FileDimensionality: bpy.props.IntProperty(name='FileDimensionality', default=2) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_WriteToMemory','m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKBMPWriter )        
TYPENAMES.append('VTKBMPWriterType' )

#--------------------------------------------------------------
class VTKBYUWriter(Node, PBVTK_Node):

    bl_idname = 'VTKBYUWriterType'
    bl_label  = 'vtkBYUWriter'
    
    m_WriteDisplacement: bpy.props.BoolProperty(name='WriteDisplacement', default=True) #type: ignore
    m_WriteScalar: bpy.props.BoolProperty(name='WriteScalar', default=True) #type: ignore
    m_WriteTexture: bpy.props.BoolProperty(name='WriteTexture', default=True) #type: ignore
    m_DisplacementFileName: bpy.props.StringProperty(name='DisplacementFileName', default="", subtype='FILE_PATH') #type: ignore
    m_GeometryFileName: bpy.props.StringProperty(name='GeometryFileName', default="", subtype='FILE_PATH') #type: ignore
    m_ScalarFileName: bpy.props.StringProperty(name='ScalarFileName', default="", subtype='FILE_PATH') #type: ignore
    m_TextureFileName: bpy.props.StringProperty(name='TextureFileName', default="", subtype='FILE_PATH') #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_WriteDisplacement','m_WriteScalar','m_WriteTexture','m_DisplacementFileName','m_GeometryFileName','m_ScalarFileName','m_TextureFileName',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKBYUWriter )        
TYPENAMES.append('VTKBYUWriterType' )

#--------------------------------------------------------------
class VTKCellGridWriter(Node, PBVTK_Node):

    bl_idname = 'VTKCellGridWriterType'
    bl_label  = 'vtkCellGridWriter'
    
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_FileName',]
    def m_connections( self ):
        return (['VTK Input'], [], ['FileFormat'], []) 
    
add_class( VTKCellGridWriter )        
TYPENAMES.append('VTKCellGridWriterType' )

#--------------------------------------------------------------
class VTKCesium3DTilesWriter(Node, PBVTK_Node):

    bl_idname = 'VTKCesium3DTilesWriterType'
    bl_label  = 'vtkCesium3DTilesWriter'
    
    m_ContentGLTF: bpy.props.BoolProperty(name='ContentGLTF', default=False) #type: ignore
    m_ContentGLTFSaveGLB: bpy.props.BoolProperty(name='ContentGLTFSaveGLB', default=True) #type: ignore
    m_MergeTilePolyData: bpy.props.BoolProperty(name='MergeTilePolyData', default=False) #type: ignore
    m_SaveTextures: bpy.props.BoolProperty(name='SaveTextures', default=True) #type: ignore
    m_SaveTiles: bpy.props.BoolProperty(name='SaveTiles', default=True) #type: ignore
    m_CRS: bpy.props.StringProperty(name='CRS', default="") #type: ignore
    m_DirectoryName: bpy.props.StringProperty(name='DirectoryName', default="", subtype='DIR_PATH') #type: ignore
    m_PropertyTextureFile: bpy.props.StringProperty(name='PropertyTextureFile', default="") #type: ignore
    m_TextureBaseDirectory: bpy.props.StringProperty(name='TextureBaseDirectory', default="") #type: ignore
    m_InputType: bpy.props.IntProperty(name='InputType', default=0) #type: ignore
    m_MergedTextureWidth: bpy.props.IntProperty(name='MergedTextureWidth', default=1000000000) #type: ignore
    m_NumberOfFeaturesPerTile: bpy.props.IntProperty(name='NumberOfFeaturesPerTile', default=100) #type: ignore
    m_Offset: bpy.props.FloatVectorProperty(name='Offset', default=[0.0, 0.0, 0.0], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_ContentGLTF','m_ContentGLTFSaveGLB','m_MergeTilePolyData','m_SaveTextures','m_SaveTiles','m_CRS','m_DirectoryName','m_PropertyTextureFile','m_TextureBaseDirectory','m_InputType','m_MergedTextureWidth','m_NumberOfFeaturesPerTile','m_Offset',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKCesium3DTilesWriter )        
TYPENAMES.append('VTKCesium3DTilesWriterType' )

#--------------------------------------------------------------
class VTKCesiumPointCloudWriter(Node, PBVTK_Node):

    bl_idname = 'VTKCesiumPointCloudWriterType'
    bl_label  = 'vtkCesiumPointCloudWriter'
    
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_FileName',]
    def m_connections( self ):
        return (['VTK Input'], [], ['PointIds'], []) 
    
add_class( VTKCesiumPointCloudWriter )        
TYPENAMES.append('VTKCesiumPointCloudWriterType' )

#--------------------------------------------------------------
class VTKCompositeDataWriter(Node, PBVTK_Node):

    bl_idname = 'VTKCompositeDataWriterType'
    bl_label  = 'vtkCompositeDataWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData: bpy.props.BoolProperty(name='WriteArrayMetaData', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=True) #type: ignore
    m_EdgeFlagsName: bpy.props.StringProperty(name='EdgeFlagsName', default="") #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="FieldData") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_GlobalIdsName: bpy.props.StringProperty(name='GlobalIdsName', default="") #type: ignore
    m_Header: bpy.props.StringProperty(name='Header', default="vtk output") #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="lookup_table") #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="") #type: ignore
    m_PedigreeIdsName: bpy.props.StringProperty(name='PedigreeIdsName', default="") #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="") #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="") #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="") #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="") #type: ignore
    m_FileVersion: bpy.props.IntProperty(name='FileVersion', default=51) #type: ignore
    e_FileType: bpy.props.EnumProperty(name='FileType', default="ASCII", items=e_FileType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','m_FileVersion','e_FileType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKCompositeDataWriter )        
TYPENAMES.append('VTKCompositeDataWriterType' )

#--------------------------------------------------------------
class VTKDIMACSGraphWriter(Node, PBVTK_Node):

    bl_idname = 'VTKDIMACSGraphWriterType'
    bl_label  = 'vtkDIMACSGraphWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData: bpy.props.BoolProperty(name='WriteArrayMetaData', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=True) #type: ignore
    m_EdgeFlagsName: bpy.props.StringProperty(name='EdgeFlagsName', default="") #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="FieldData") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_GlobalIdsName: bpy.props.StringProperty(name='GlobalIdsName', default="") #type: ignore
    m_Header: bpy.props.StringProperty(name='Header', default="vtk output") #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="lookup_table") #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="") #type: ignore
    m_PedigreeIdsName: bpy.props.StringProperty(name='PedigreeIdsName', default="") #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="") #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="") #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="") #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="") #type: ignore
    m_FileVersion: bpy.props.IntProperty(name='FileVersion', default=51) #type: ignore
    e_FileType: bpy.props.EnumProperty(name='FileType', default="ASCII", items=e_FileType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','m_FileVersion','e_FileType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKDIMACSGraphWriter )        
TYPENAMES.append('VTKDIMACSGraphWriterType' )

#--------------------------------------------------------------
class VTKDataObjectWriter(Node, PBVTK_Node):

    bl_idname = 'VTKDataObjectWriterType'
    bl_label  = 'vtkDataObjectWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=True) #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="FieldData") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_Header: bpy.props.StringProperty(name='Header', default="vtk output") #type: ignore
    e_FileType: bpy.props.EnumProperty(name='FileType', default="ASCII", items=e_FileType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_WriteToOutputString','m_FieldDataName','m_FileName','m_Header','e_FileType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKDataObjectWriter )        
TYPENAMES.append('VTKDataObjectWriterType' )

#--------------------------------------------------------------
class VTKDataSetWriter(Node, PBVTK_Node):

    bl_idname = 'VTKDataSetWriterType'
    bl_label  = 'vtkDataSetWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData: bpy.props.BoolProperty(name='WriteArrayMetaData', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=True) #type: ignore
    m_EdgeFlagsName: bpy.props.StringProperty(name='EdgeFlagsName', default="") #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="FieldData") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_GlobalIdsName: bpy.props.StringProperty(name='GlobalIdsName', default="") #type: ignore
    m_Header: bpy.props.StringProperty(name='Header', default="vtk output") #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="lookup_table") #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="") #type: ignore
    m_PedigreeIdsName: bpy.props.StringProperty(name='PedigreeIdsName', default="") #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="") #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="") #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="") #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="") #type: ignore
    m_FileVersion: bpy.props.IntProperty(name='FileVersion', default=51) #type: ignore
    e_FileType: bpy.props.EnumProperty(name='FileType', default="ASCII", items=e_FileType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','m_FileVersion','e_FileType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKDataSetWriter )        
TYPENAMES.append('VTKDataSetWriterType' )

#--------------------------------------------------------------
class VTKDataWriter(Node, PBVTK_Node):

    bl_idname = 'VTKDataWriterType'
    bl_label  = 'vtkDataWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData: bpy.props.BoolProperty(name='WriteArrayMetaData', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=True) #type: ignore
    m_EdgeFlagsName: bpy.props.StringProperty(name='EdgeFlagsName', default="") #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="FieldData") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_GlobalIdsName: bpy.props.StringProperty(name='GlobalIdsName', default="") #type: ignore
    m_Header: bpy.props.StringProperty(name='Header', default="vtk output") #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="lookup_table") #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="") #type: ignore
    m_PedigreeIdsName: bpy.props.StringProperty(name='PedigreeIdsName', default="") #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="") #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="") #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="") #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="") #type: ignore
    m_FileVersion: bpy.props.IntProperty(name='FileVersion', default=51) #type: ignore
    e_FileType: bpy.props.EnumProperty(name='FileType', default="ASCII", items=e_FileType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','m_FileVersion','e_FileType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKDataWriter )        
TYPENAMES.append('VTKDataWriterType' )

#--------------------------------------------------------------
class VTKDelimitedTextWriter(Node, PBVTK_Node):

    bl_idname = 'VTKDelimitedTextWriterType'
    bl_label  = 'vtkDelimitedTextWriter'
    
    m_UseStringDelimiter: bpy.props.BoolProperty(name='UseStringDelimiter', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FieldDelimiter: bpy.props.StringProperty(name='FieldDelimiter', default=",") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_StringDelimiter: bpy.props.StringProperty(name='StringDelimiter', default="") #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_UseStringDelimiter','m_WriteToOutputString','m_FieldDelimiter','m_FileName','m_StringDelimiter',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKDelimitedTextWriter )        
TYPENAMES.append('VTKDelimitedTextWriterType' )

#--------------------------------------------------------------
class VTKEnSightWriter(Node, PBVTK_Node):

    bl_idname = 'VTKEnSightWriterType'
    bl_label  = 'vtkEnSightWriter'
    
    m_TransientGeometry: bpy.props.BoolProperty(name='TransientGeometry', default=False) #type: ignore
    m_WriteElementIDs: bpy.props.BoolProperty(name='WriteElementIDs', default=True) #type: ignore
    m_WriteNodeIDs: bpy.props.BoolProperty(name='WriteNodeIDs', default=True) #type: ignore
    m_BaseName: bpy.props.StringProperty(name='BaseName', default="") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_Path: bpy.props.StringProperty(name='Path', default="") #type: ignore
    m_GhostLevel: bpy.props.IntProperty(name='GhostLevel', default=0) #type: ignore
    m_NumberOfBlocks: bpy.props.IntProperty(name='NumberOfBlocks', default=0) #type: ignore
    m_ProcessNumber: bpy.props.IntProperty(name='ProcessNumber', default=0) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_TransientGeometry','m_WriteElementIDs','m_WriteNodeIDs','m_BaseName','m_FileName','m_Path','m_GhostLevel','m_NumberOfBlocks','m_ProcessNumber','m_TimeStep',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKEnSightWriter )        
TYPENAMES.append('VTKEnSightWriterType' )

#--------------------------------------------------------------
class VTKExodusIIWriter(Node, PBVTK_Node):

    bl_idname = 'VTKExodusIIWriterType'
    bl_label  = 'vtkExodusIIWriter'
    
    m_IgnoreMetaDataWarning: bpy.props.BoolProperty(name='IgnoreMetaDataWarning', default=False) #type: ignore
    m_WriteAllTimeSteps: bpy.props.BoolProperty(name='WriteAllTimeSteps', default=True) #type: ignore
    m_WriteOutBlockIdArray: bpy.props.BoolProperty(name='WriteOutBlockIdArray', default=True) #type: ignore
    m_WriteOutGlobalElementIdArray: bpy.props.BoolProperty(name='WriteOutGlobalElementIdArray', default=True) #type: ignore
    m_WriteOutGlobalNodeIdArray: bpy.props.BoolProperty(name='WriteOutGlobalNodeIdArray', default=True) #type: ignore
    m_BlockIdArrayName: bpy.props.StringProperty(name='BlockIdArrayName', default="") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_GhostLevel: bpy.props.IntProperty(name='GhostLevel', default=0) #type: ignore
    m_StoreDoubles: bpy.props.IntProperty(name='StoreDoubles', default=-1) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_IgnoreMetaDataWarning','m_WriteAllTimeSteps','m_WriteOutBlockIdArray','m_WriteOutGlobalElementIdArray','m_WriteOutGlobalNodeIdArray','m_BlockIdArrayName','m_FileName','m_GhostLevel','m_StoreDoubles',]
    def m_connections( self ):
        return (['VTK Input'], [], ['ModelMetadata'], []) 
    
add_class( VTKExodusIIWriter )        
TYPENAMES.append('VTKExodusIIWriterType' )

#--------------------------------------------------------------
class VTKFacetWriter(Node, PBVTK_Node):

    bl_idname = 'VTKFacetWriterType'
    bl_label  = 'vtkFacetWriter'
    
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_FileName',]
    def m_connections( self ):
        return (['VTK Input'], ['VTK Output'], [], []) 
    
add_class( VTKFacetWriter )        
TYPENAMES.append('VTKFacetWriterType' )

#--------------------------------------------------------------
class VTKGLTFWriter(Node, PBVTK_Node):

    bl_idname = 'VTKGLTFWriterType'
    bl_label  = 'vtkGLTFWriter'
    
    m_CopyTextures: bpy.props.BoolProperty(name='CopyTextures', default=False) #type: ignore
    m_InlineData: bpy.props.BoolProperty(name='InlineData', default=False) #type: ignore
    m_RelativeCoordinates: bpy.props.BoolProperty(name='RelativeCoordinates', default=False) #type: ignore
    m_SaveActivePointColor: bpy.props.BoolProperty(name='SaveActivePointColor', default=False) #type: ignore
    m_SaveBatchId: bpy.props.BoolProperty(name='SaveBatchId', default=False) #type: ignore
    m_SaveNormal: bpy.props.BoolProperty(name='SaveNormal', default=False) #type: ignore
    m_SaveTextures: bpy.props.BoolProperty(name='SaveTextures', default=True) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_PropertyTextureFile: bpy.props.StringProperty(name='PropertyTextureFile', default="") #type: ignore
    m_TextureBaseDirectory: bpy.props.StringProperty(name='TextureBaseDirectory', default="") #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_CopyTextures','m_InlineData','m_RelativeCoordinates','m_SaveActivePointColor','m_SaveBatchId','m_SaveNormal','m_SaveTextures','m_FileName','m_PropertyTextureFile','m_TextureBaseDirectory',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKGLTFWriter )        
TYPENAMES.append('VTKGLTFWriterType' )

#--------------------------------------------------------------
class VTKGenericDataObjectWriter(Node, PBVTK_Node):

    bl_idname = 'VTKGenericDataObjectWriterType'
    bl_label  = 'vtkGenericDataObjectWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData: bpy.props.BoolProperty(name='WriteArrayMetaData', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=True) #type: ignore
    m_EdgeFlagsName: bpy.props.StringProperty(name='EdgeFlagsName', default="") #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="FieldData") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_GlobalIdsName: bpy.props.StringProperty(name='GlobalIdsName', default="") #type: ignore
    m_Header: bpy.props.StringProperty(name='Header', default="vtk output") #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="lookup_table") #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="") #type: ignore
    m_PedigreeIdsName: bpy.props.StringProperty(name='PedigreeIdsName', default="") #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="") #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="") #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="") #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="") #type: ignore
    m_FileVersion: bpy.props.IntProperty(name='FileVersion', default=51) #type: ignore
    e_FileType: bpy.props.EnumProperty(name='FileType', default="ASCII", items=e_FileType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','m_FileVersion','e_FileType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKGenericDataObjectWriter )        
TYPENAMES.append('VTKGenericDataObjectWriterType' )

#--------------------------------------------------------------
class VTKGeoJSONWriter(Node, PBVTK_Node):

    bl_idname = 'VTKGeoJSONWriterType'
    bl_label  = 'vtkGeoJSONWriter'
    
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_ScalarFormat: bpy.props.IntProperty(name='ScalarFormat', default=2) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_WriteToOutputString','m_FileName','m_ScalarFormat',]
    def m_connections( self ):
        return (['VTK Input'], [], ['LookupTable'], []) 
    
add_class( VTKGeoJSONWriter )        
TYPENAMES.append('VTKGeoJSONWriterType' )

#--------------------------------------------------------------
class VTKGraphWriter(Node, PBVTK_Node):

    bl_idname = 'VTKGraphWriterType'
    bl_label  = 'vtkGraphWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData: bpy.props.BoolProperty(name='WriteArrayMetaData', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=True) #type: ignore
    m_EdgeFlagsName: bpy.props.StringProperty(name='EdgeFlagsName', default="") #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="FieldData") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_GlobalIdsName: bpy.props.StringProperty(name='GlobalIdsName', default="") #type: ignore
    m_Header: bpy.props.StringProperty(name='Header', default="vtk output") #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="lookup_table") #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="") #type: ignore
    m_PedigreeIdsName: bpy.props.StringProperty(name='PedigreeIdsName', default="") #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="") #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="") #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="") #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="") #type: ignore
    m_FileVersion: bpy.props.IntProperty(name='FileVersion', default=51) #type: ignore
    e_FileType: bpy.props.EnumProperty(name='FileType', default="ASCII", items=e_FileType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','m_FileVersion','e_FileType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKGraphWriter )        
TYPENAMES.append('VTKGraphWriterType' )

#--------------------------------------------------------------
class VTKHDFWriter(Node, PBVTK_Node):

    bl_idname = 'VTKHDFWriterType'
    bl_label  = 'vtkHDFWriter'
    
    m_Overwrite: bpy.props.BoolProperty(name='Overwrite', default=True) #type: ignore
    m_UseExternalComposite: bpy.props.BoolProperty(name='UseExternalComposite', default=False) #type: ignore
    m_UseExternalPartitions: bpy.props.BoolProperty(name='UseExternalPartitions', default=False) #type: ignore
    m_UseExternalTimeSteps: bpy.props.BoolProperty(name='UseExternalTimeSteps', default=False) #type: ignore
    m_WriteAllTimeSteps: bpy.props.BoolProperty(name='WriteAllTimeSteps', default=True) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_ChunkSize: bpy.props.IntProperty(name='ChunkSize', default=25000) #type: ignore
    m_CompressionLevel: bpy.props.IntProperty(name='CompressionLevel', default=0) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Overwrite','m_UseExternalComposite','m_UseExternalPartitions','m_UseExternalTimeSteps','m_WriteAllTimeSteps','m_FileName','m_ChunkSize','m_CompressionLevel',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKHDFWriter )        
TYPENAMES.append('VTKHDFWriterType' )

#--------------------------------------------------------------
class VTKHoudiniPolyDataWriter(Node, PBVTK_Node):

    bl_idname = 'VTKHoudiniPolyDataWriterType'
    bl_label  = 'vtkHoudiniPolyDataWriter'
    
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_FileName',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKHoudiniPolyDataWriter )        
TYPENAMES.append('VTKHoudiniPolyDataWriterType' )

#--------------------------------------------------------------
class VTKIOSSWriter(Node, PBVTK_Node):

    bl_idname = 'VTKIOSSWriterType'
    bl_label  = 'vtkIOSSWriter'
    
    m_ChooseFieldsToWrite: bpy.props.BoolProperty(name='ChooseFieldsToWrite', default=False) #type: ignore
    m_OffsetGlobalIds: bpy.props.BoolProperty(name='OffsetGlobalIds', default=False) #type: ignore
    m_PreserveOriginalIds: bpy.props.BoolProperty(name='PreserveOriginalIds', default=False) #type: ignore
    m_RemoveGhosts: bpy.props.BoolProperty(name='RemoveGhosts', default=True) #type: ignore
    m_WriteQAAndInformationRecords: bpy.props.BoolProperty(name='WriteQAAndInformationRecords', default=True) #type: ignore
    m_AssemblyName: bpy.props.StringProperty(name='AssemblyName', default="Hierarchy") #type: ignore
    m_EdgeBlockSelector: bpy.props.StringProperty(name='EdgeBlockSelector', default="0") #type: ignore
    m_EdgeSetSelector: bpy.props.StringProperty(name='EdgeSetSelector', default="0") #type: ignore
    m_ElementBlockSelector: bpy.props.StringProperty(name='ElementBlockSelector', default="0") #type: ignore
    m_ElementSetSelector: bpy.props.StringProperty(name='ElementSetSelector', default="0") #type: ignore
    m_FaceBlockSelector: bpy.props.StringProperty(name='FaceBlockSelector', default="0") #type: ignore
    m_FaceSetSelector: bpy.props.StringProperty(name='FaceSetSelector', default="0") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_NodeSetSelector: bpy.props.StringProperty(name='NodeSetSelector', default="0") #type: ignore
    m_SideSetSelector: bpy.props.StringProperty(name='SideSetSelector', default="0") #type: ignore
    m_TimeStepStride: bpy.props.IntProperty(name='TimeStepStride', default=1) #type: ignore
    m_DisplacementMagnitude: bpy.props.FloatProperty(name='DisplacementMagnitude', default=1.0) #type: ignore
    m_TimeStepRange: bpy.props.IntVectorProperty(name='TimeStepRange', default=[0, 1000000000], size=2) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_ChooseFieldsToWrite','m_OffsetGlobalIds','m_PreserveOriginalIds','m_RemoveGhosts','m_WriteQAAndInformationRecords','m_AssemblyName','m_EdgeBlockSelector','m_EdgeSetSelector','m_ElementBlockSelector','m_ElementSetSelector','m_FaceBlockSelector','m_FaceSetSelector','m_FileName','m_NodeSetSelector','m_SideSetSelector','m_TimeStepStride','m_DisplacementMagnitude','m_TimeStepRange',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKIOSSWriter )        
TYPENAMES.append('VTKIOSSWriterType' )

#--------------------------------------------------------------
class VTKIVWriter(Node, PBVTK_Node):

    bl_idname = 'VTKIVWriterType'
    bl_label  = 'vtkIVWriter'
    
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_FileName',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKIVWriter )        
TYPENAMES.append('VTKIVWriterType' )

#--------------------------------------------------------------
class VTKImageWriter(Node, PBVTK_Node):

    bl_idname = 'VTKImageWriterType'
    bl_label  = 'vtkImageWriter'
    
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d") #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="") #type: ignore
    m_FileDimensionality: bpy.props.IntProperty(name='FileDimensionality', default=2) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKImageWriter )        
TYPENAMES.append('VTKImageWriterType' )

#--------------------------------------------------------------
class VTKJPEGWriter(Node, PBVTK_Node):

    bl_idname = 'VTKJPEGWriterType'
    bl_label  = 'vtkJPEGWriter'
    
    m_Progressive: bpy.props.BoolProperty(name='Progressive', default=True) #type: ignore
    m_WriteToMemory: bpy.props.BoolProperty(name='WriteToMemory', default=True) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d") #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="") #type: ignore
    m_FileDimensionality: bpy.props.IntProperty(name='FileDimensionality', default=2) #type: ignore
    m_Quality: bpy.props.IntProperty(name='Quality', default=95) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Progressive','m_WriteToMemory','m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_Quality',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKJPEGWriter )        
TYPENAMES.append('VTKJPEGWriterType' )

#--------------------------------------------------------------
class VTKJSONDataSetWriter(Node, PBVTK_Node):

    bl_idname = 'VTKJSONDataSetWriterType'
    bl_label  = 'vtkJSONDataSetWriter'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['VTK Input'], [], ['Archiver'], []) 
    
add_class( VTKJSONDataSetWriter )        
TYPENAMES.append('VTKJSONDataSetWriterType' )

#--------------------------------------------------------------
class VTKJSONImageWriter(Node, PBVTK_Node):

    bl_idname = 'VTKJSONImageWriterType'
    bl_label  = 'vtkJSONImageWriter'
    
    m_ArrayName: bpy.props.StringProperty(name='ArrayName', default="") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_Slice: bpy.props.IntProperty(name='Slice', default=-1) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_ArrayName','m_FileName','m_Slice',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKJSONImageWriter )        
TYPENAMES.append('VTKJSONImageWriterType' )

#--------------------------------------------------------------
class VTKJavaScriptDataWriter(Node, PBVTK_Node):

    bl_idname = 'VTKJavaScriptDataWriterType'
    bl_label  = 'vtkJavaScriptDataWriter'
    
    m_IncludeFieldNames: bpy.props.BoolProperty(name='IncludeFieldNames', default=True) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_VariableName: bpy.props.StringProperty(name='VariableName', default="data") #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_IncludeFieldNames','m_FileName','m_VariableName',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKJavaScriptDataWriter )        
TYPENAMES.append('VTKJavaScriptDataWriterType' )

#--------------------------------------------------------------
class VTKLegacyCellGridWriter(Node, PBVTK_Node):

    bl_idname = 'VTKLegacyCellGridWriterType'
    bl_label  = 'vtkLegacyCellGridWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData: bpy.props.BoolProperty(name='WriteArrayMetaData', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=True) #type: ignore
    m_EdgeFlagsName: bpy.props.StringProperty(name='EdgeFlagsName', default="") #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="FieldData") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_GlobalIdsName: bpy.props.StringProperty(name='GlobalIdsName', default="") #type: ignore
    m_Header: bpy.props.StringProperty(name='Header', default="vtk output") #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="lookup_table") #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="") #type: ignore
    m_PedigreeIdsName: bpy.props.StringProperty(name='PedigreeIdsName', default="") #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="") #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="") #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="") #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="") #type: ignore
    m_FileVersion: bpy.props.IntProperty(name='FileVersion', default=51) #type: ignore
    e_FileType: bpy.props.EnumProperty(name='FileType', default="ASCII", items=e_FileType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','m_FileVersion','e_FileType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKLegacyCellGridWriter )        
TYPENAMES.append('VTKLegacyCellGridWriterType' )

#--------------------------------------------------------------
class VTKMCubesWriter(Node, PBVTK_Node):

    bl_idname = 'VTKMCubesWriterType'
    bl_label  = 'vtkMCubesWriter'
    
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_LimitsFileName: bpy.props.StringProperty(name='LimitsFileName', default="", subtype='FILE_PATH') #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_FileName','m_LimitsFileName',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKMCubesWriter )        
TYPENAMES.append('VTKMCubesWriterType' )

#--------------------------------------------------------------
class VTKMINCImageWriter(Node, PBVTK_Node):

    bl_idname = 'VTKMINCImageWriterType'
    bl_label  = 'vtkMINCImageWriter'
    
    m_StrictValidation: bpy.props.BoolProperty(name='StrictValidation', default=True) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d") #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="") #type: ignore
    m_HistoryAddition: bpy.props.StringProperty(name='HistoryAddition', default="") #type: ignore
    m_FileDimensionality: bpy.props.IntProperty(name='FileDimensionality', default=2) #type: ignore
    m_RescaleIntercept: bpy.props.FloatProperty(name='RescaleIntercept', default=0.0) #type: ignore
    m_RescaleSlope: bpy.props.FloatProperty(name='RescaleSlope', default=0.0) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_StrictValidation','m_FileName','m_FilePattern','m_FilePrefix','m_HistoryAddition','m_FileDimensionality','m_RescaleIntercept','m_RescaleSlope',]
    def m_connections( self ):
        return (['VTK Input'], [], ['DirectionCosines', 'ImageAttributes'], []) 
    
add_class( VTKMINCImageWriter )        
TYPENAMES.append('VTKMINCImageWriterType' )

#--------------------------------------------------------------
class VTKMNIObjectWriter(Node, PBVTK_Node):

    bl_idname = 'VTKMNIObjectWriterType'
    bl_label  = 'vtkMNIObjectWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    e_FileType: bpy.props.EnumProperty(name='FileType', default="ASCII", items=e_FileType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_FileName','e_FileType',]
    def m_connections( self ):
        return (['VTK Input'], [], ['LookupTable', 'Mapper', 'Property'], []) 
    
add_class( VTKMNIObjectWriter )        
TYPENAMES.append('VTKMNIObjectWriterType' )

#--------------------------------------------------------------
class VTKMNITagPointWriter(Node, PBVTK_Node):

    bl_idname = 'VTKMNITagPointWriterType'
    bl_label  = 'vtkMNITagPointWriter'
    
    m_Comments: bpy.props.StringProperty(name='Comments', default="") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Comments','m_FileName',]
    def m_connections( self ):
        return (['VTK Input 0', 'VTK Input 1'], [], ['LabelText', 'PatientIds', 'StructureIds', 'Weights'], []) 
    
add_class( VTKMNITagPointWriter )        
TYPENAMES.append('VTKMNITagPointWriterType' )

#--------------------------------------------------------------
class VTKMNITransformWriter(Node, PBVTK_Node):

    bl_idname = 'VTKMNITransformWriterType'
    bl_label  = 'vtkMNITransformWriter'
    
    m_Comments: bpy.props.StringProperty(name='Comments', default="") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Comments','m_FileName',]
    def m_connections( self ):
        return ([], [], ['Transform'], []) 
    
add_class( VTKMNITransformWriter )        
TYPENAMES.append('VTKMNITransformWriterType' )

#--------------------------------------------------------------
class VTKMetaImageWriter(Node, PBVTK_Node):

    bl_idname = 'VTKMetaImageWriterType'
    bl_label  = 'vtkMetaImageWriter'
    
    m_Compression: bpy.props.BoolProperty(name='Compression', default=True) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d") #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="") #type: ignore
    m_RAWFileName: bpy.props.StringProperty(name='RAWFileName', default="", subtype='FILE_PATH') #type: ignore
    m_FileDimensionality: bpy.props.IntProperty(name='FileDimensionality', default=2) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Compression','m_FileName','m_FilePattern','m_FilePrefix','m_RAWFileName','m_FileDimensionality',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKMetaImageWriter )        
TYPENAMES.append('VTKMetaImageWriterType' )

#--------------------------------------------------------------
class VTKNIFTIImageWriter(Node, PBVTK_Node):

    bl_idname = 'VTKNIFTIImageWriterType'
    bl_label  = 'vtkNIFTIImageWriter'
    
    m_PlanarRGB: bpy.props.BoolProperty(name='PlanarRGB', default=False) #type: ignore
    m_Description: bpy.props.StringProperty(name='Description', default="VTK9.5.2") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d") #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="") #type: ignore
    m_FileDimensionality: bpy.props.IntProperty(name='FileDimensionality', default=3) #type: ignore
    m_NIFTIVersion: bpy.props.IntProperty(name='NIFTIVersion', default=0) #type: ignore
    m_TimeDimension: bpy.props.IntProperty(name='TimeDimension', default=0) #type: ignore
    m_QFac: bpy.props.FloatProperty(name='QFac', default=0.0) #type: ignore
    m_RescaleIntercept: bpy.props.FloatProperty(name='RescaleIntercept', default=0.0) #type: ignore
    m_RescaleSlope: bpy.props.FloatProperty(name='RescaleSlope', default=0.0) #type: ignore
    m_TimeSpacing: bpy.props.FloatProperty(name='TimeSpacing', default=1.0) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_PlanarRGB','m_Description','m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_NIFTIVersion','m_TimeDimension','m_QFac','m_RescaleIntercept','m_RescaleSlope','m_TimeSpacing',]
    def m_connections( self ):
        return (['VTK Input'], [], ['NIFTIHeader', 'QFormMatrix', 'SFormMatrix'], []) 
    
add_class( VTKNIFTIImageWriter )        
TYPENAMES.append('VTKNIFTIImageWriterType' )

#--------------------------------------------------------------
class VTKNetCDFCFWriter(Node, PBVTK_Node):

    bl_idname = 'VTKNetCDFCFWriterType'
    bl_label  = 'vtkNetCDFCFWriter'
    
    m_FillBlankedAttributes: bpy.props.BoolProperty(name='FillBlankedAttributes', default=False) #type: ignore
    m_CellArrayNamePostfix: bpy.props.StringProperty(name='CellArrayNamePostfix', default="_c") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_AttributeType: bpy.props.IntProperty(name='AttributeType', default=0) #type: ignore
    m_FillValue: bpy.props.IntProperty(name='FillValue', default=-1000000000) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_FillBlankedAttributes','m_CellArrayNamePostfix','m_FileName','m_AttributeType','m_FillValue',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKNetCDFCFWriter )        
TYPENAMES.append('VTKNetCDFCFWriterType' )

#--------------------------------------------------------------
class VTKNewickTreeWriter(Node, PBVTK_Node):

    bl_idname = 'VTKNewickTreeWriterType'
    bl_label  = 'vtkNewickTreeWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData: bpy.props.BoolProperty(name='WriteArrayMetaData', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=True) #type: ignore
    m_EdgeFlagsName: bpy.props.StringProperty(name='EdgeFlagsName', default="") #type: ignore
    m_EdgeWeightArrayName: bpy.props.StringProperty(name='EdgeWeightArrayName', default="weight") #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="FieldData") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_GlobalIdsName: bpy.props.StringProperty(name='GlobalIdsName', default="") #type: ignore
    m_Header: bpy.props.StringProperty(name='Header', default="vtk output") #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="lookup_table") #type: ignore
    m_NodeNameArrayName: bpy.props.StringProperty(name='NodeNameArrayName', default="node name") #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="") #type: ignore
    m_PedigreeIdsName: bpy.props.StringProperty(name='PedigreeIdsName', default="") #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="") #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="") #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="") #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="") #type: ignore
    m_FileVersion: bpy.props.IntProperty(name='FileVersion', default=51) #type: ignore
    e_FileType: bpy.props.EnumProperty(name='FileType', default="ASCII", items=e_FileType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_EdgeWeightArrayName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NodeNameArrayName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','m_FileVersion','e_FileType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKNewickTreeWriter )        
TYPENAMES.append('VTKNewickTreeWriterType' )

#--------------------------------------------------------------
class VTKOBJWriter(Node, PBVTK_Node):

    bl_idname = 'VTKOBJWriterType'
    bl_label  = 'vtkOBJWriter'
    
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_TextureFileName: bpy.props.StringProperty(name='TextureFileName', default="", subtype='FILE_PATH') #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_FileName','m_TextureFileName',]
    def m_connections( self ):
        return (['VTK Input 0', 'VTK Input 1'], [], [], []) 
    
add_class( VTKOBJWriter )        
TYPENAMES.append('VTKOBJWriterType' )

#--------------------------------------------------------------
class VTKOggTheoraWriter(Node, PBVTK_Node):

    bl_idname = 'VTKOggTheoraWriterType'
    bl_label  = 'vtkOggTheoraWriter'
    
    m_Subsampling: bpy.props.BoolProperty(name='Subsampling', default=True) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_Quality: bpy.props.IntProperty(name='Quality', default=2) #type: ignore
    m_Rate: bpy.props.IntProperty(name='Rate', default=25) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_Subsampling','m_FileName','m_Quality','m_Rate',]
    def m_connections( self ):
        return (['VTK Input'], ['VTK Output'], [], []) 
    
add_class( VTKOggTheoraWriter )        
TYPENAMES.append('VTKOggTheoraWriterType' )

#--------------------------------------------------------------
class VTKPDataSetWriter(Node, PBVTK_Node):

    bl_idname = 'VTKPDataSetWriterType'
    bl_label  = 'vtkPDataSetWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_UseRelativeFileNames: bpy.props.BoolProperty(name='UseRelativeFileNames', default=True) #type: ignore
    m_WriteArrayMetaData: bpy.props.BoolProperty(name='WriteArrayMetaData', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=True) #type: ignore
    m_EdgeFlagsName: bpy.props.StringProperty(name='EdgeFlagsName', default="") #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="FieldData") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d.vtk") #type: ignore
    m_GlobalIdsName: bpy.props.StringProperty(name='GlobalIdsName', default="") #type: ignore
    m_Header: bpy.props.StringProperty(name='Header', default="vtk output") #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="lookup_table") #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="") #type: ignore
    m_PedigreeIdsName: bpy.props.StringProperty(name='PedigreeIdsName', default="") #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="") #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="") #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="") #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="") #type: ignore
    m_EndPiece: bpy.props.IntProperty(name='EndPiece', default=0) #type: ignore
    m_FileVersion: bpy.props.IntProperty(name='FileVersion', default=51) #type: ignore
    m_GhostLevel: bpy.props.IntProperty(name='GhostLevel', default=0) #type: ignore
    m_NumberOfPieces: bpy.props.IntProperty(name='NumberOfPieces', default=1) #type: ignore
    m_StartPiece: bpy.props.IntProperty(name='StartPiece', default=0) #type: ignore
    e_FileType: bpy.props.EnumProperty(name='FileType', default="ASCII", items=e_FileType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=22, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_UseRelativeFileNames','m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_FilePattern','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','m_EndPiece','m_FileVersion','m_GhostLevel','m_NumberOfPieces','m_StartPiece','e_FileType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKPDataSetWriter )        
TYPENAMES.append('VTKPDataSetWriterType' )

#--------------------------------------------------------------
class VTKPExodusIIWriter(Node, PBVTK_Node):

    bl_idname = 'VTKPExodusIIWriterType'
    bl_label  = 'vtkPExodusIIWriter'
    
    m_IgnoreMetaDataWarning: bpy.props.BoolProperty(name='IgnoreMetaDataWarning', default=False) #type: ignore
    m_WriteAllTimeSteps: bpy.props.BoolProperty(name='WriteAllTimeSteps', default=True) #type: ignore
    m_WriteOutBlockIdArray: bpy.props.BoolProperty(name='WriteOutBlockIdArray', default=True) #type: ignore
    m_WriteOutGlobalElementIdArray: bpy.props.BoolProperty(name='WriteOutGlobalElementIdArray', default=True) #type: ignore
    m_WriteOutGlobalNodeIdArray: bpy.props.BoolProperty(name='WriteOutGlobalNodeIdArray', default=True) #type: ignore
    m_BlockIdArrayName: bpy.props.StringProperty(name='BlockIdArrayName', default="") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_GhostLevel: bpy.props.IntProperty(name='GhostLevel', default=0) #type: ignore
    m_StoreDoubles: bpy.props.IntProperty(name='StoreDoubles', default=-1) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_IgnoreMetaDataWarning','m_WriteAllTimeSteps','m_WriteOutBlockIdArray','m_WriteOutGlobalElementIdArray','m_WriteOutGlobalNodeIdArray','m_BlockIdArrayName','m_FileName','m_GhostLevel','m_StoreDoubles',]
    def m_connections( self ):
        return (['VTK Input'], [], ['ModelMetadata'], []) 
    
add_class( VTKPExodusIIWriter )        
TYPENAMES.append('VTKPExodusIIWriterType' )

#--------------------------------------------------------------
class VTKPImageWriter(Node, PBVTK_Node):

    bl_idname = 'VTKPImageWriterType'
    bl_label  = 'vtkPImageWriter'
    
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d") #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="") #type: ignore
    m_FileDimensionality: bpy.props.IntProperty(name='FileDimensionality', default=2) #type: ignore
    m_MemoryLimit: bpy.props.IntProperty(name='MemoryLimit', default=1048576) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','m_MemoryLimit',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKPImageWriter )        
TYPENAMES.append('VTKPImageWriterType' )

#--------------------------------------------------------------
class VTKPLYWriter(Node, PBVTK_Node):

    bl_idname = 'VTKPLYWriterType'
    bl_label  = 'vtkPLYWriter'
    e_ColorMode_items=[ (x,x,x) for x in ['Default', 'UniformCellColor', 'UniformPointColor', 'UniformColor', 'Off']]
    e_DataByteOrder_items=[ (x,x,x) for x in ['LittleEndian', 'BigEndian']]
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    e_TextureCoordinatesName_items=[ (x,x,x) for x in ['UV', 'TextureUV']]
    
    m_EnableAlpha: bpy.props.BoolProperty(name='EnableAlpha', default=False) #type: ignore
    m_WriteObjectInformation: bpy.props.BoolProperty(name='WriteObjectInformation', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_ArrayName: bpy.props.StringProperty(name='ArrayName', default="") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_Alpha: bpy.props.IntProperty(name='Alpha', default=255) #type: ignore
    m_Component: bpy.props.IntProperty(name='Component', default=0) #type: ignore
    e_ColorMode: bpy.props.EnumProperty(name='ColorMode', default="Default", items=e_ColorMode_items) #type: ignore
    e_DataByteOrder: bpy.props.EnumProperty(name='DataByteOrder', default="LittleEndian", items=e_DataByteOrder_items) #type: ignore
    e_FileType: bpy.props.EnumProperty(name='FileType', default="Binary", items=e_FileType_items) #type: ignore
    e_TextureCoordinatesName: bpy.props.EnumProperty(name='TextureCoordinatesName', default="UV", items=e_TextureCoordinatesName_items) #type: ignore
    m_Color: bpy.props.IntVectorProperty(name='Color', default=[255, 255, 255], size=3) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_EnableAlpha','m_WriteObjectInformation','m_WriteToOutputString','m_ArrayName','m_FileName','m_Alpha','m_Component','e_ColorMode','e_DataByteOrder','e_FileType','e_TextureCoordinatesName','m_Color',]
    def m_connections( self ):
        return (['VTK Input'], [], ['LookupTable'], []) 
    
add_class( VTKPLYWriter )        
TYPENAMES.append('VTKPLYWriterType' )

#--------------------------------------------------------------
class VTKPNGWriter(Node, PBVTK_Node):

    bl_idname = 'VTKPNGWriterType'
    bl_label  = 'vtkPNGWriter'
    
    m_WriteToMemory: bpy.props.BoolProperty(name='WriteToMemory', default=True) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d") #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="") #type: ignore
    m_CompressionLevel: bpy.props.IntProperty(name='CompressionLevel', default=5) #type: ignore
    m_FileDimensionality: bpy.props.IntProperty(name='FileDimensionality', default=2) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_WriteToMemory','m_FileName','m_FilePattern','m_FilePrefix','m_CompressionLevel','m_FileDimensionality',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKPNGWriter )        
TYPENAMES.append('VTKPNGWriterType' )

#--------------------------------------------------------------
class VTKPNMWriter(Node, PBVTK_Node):

    bl_idname = 'VTKPNMWriterType'
    bl_label  = 'vtkPNMWriter'
    
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d") #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="") #type: ignore
    m_FileDimensionality: bpy.props.IntProperty(name='FileDimensionality', default=2) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKPNMWriter )        
TYPENAMES.append('VTKPNMWriterType' )

#--------------------------------------------------------------
class VTKPhyloXMLTreeWriter(Node, PBVTK_Node):

    bl_idname = 'VTKPhyloXMLTreeWriterType'
    bl_label  = 'vtkPhyloXMLTreeWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData: bpy.props.BoolProperty(name='EncodeAppendedData', default=True) #type: ignore
    m_WriteTimeValue: bpy.props.BoolProperty(name='WriteTimeValue', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_EdgeWeightArrayName: bpy.props.StringProperty(name='EdgeWeightArrayName', default="weight") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_NodeNameArrayName: bpy.props.StringProperty(name='NodeNameArrayName', default="node name") #type: ignore
    m_BlockSize: bpy.props.IntProperty(name='BlockSize', default=32768) #type: ignore
    m_CompressionLevel: bpy.props.IntProperty(name='CompressionLevel', default=5) #type: ignore
    m_NumberOfTimeSteps: bpy.props.IntProperty(name='NumberOfTimeSteps', default=1) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="LittleEndian", items=e_ByteOrder_items) #type: ignore
    e_DataMode: bpy.props.EnumProperty(name='DataMode', default="Appended", items=e_DataMode_items) #type: ignore
    e_HeaderType: bpy.props.EnumProperty(name='HeaderType', default="UInt32", items=e_HeaderType_items) #type: ignore
    e_IdType: bpy.props.EnumProperty(name='IdType', default="Int64", items=e_IdType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteTimeValue','m_WriteToOutputString','m_EdgeWeightArrayName','m_FileName','m_NodeNameArrayName','m_BlockSize','m_CompressionLevel','m_NumberOfTimeSteps','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKPhyloXMLTreeWriter )        
TYPENAMES.append('VTKPhyloXMLTreeWriterType' )

#--------------------------------------------------------------
class VTKPolyDataWriter(Node, PBVTK_Node):

    bl_idname = 'VTKPolyDataWriterType'
    bl_label  = 'vtkPolyDataWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData: bpy.props.BoolProperty(name='WriteArrayMetaData', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=True) #type: ignore
    m_EdgeFlagsName: bpy.props.StringProperty(name='EdgeFlagsName', default="") #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="FieldData") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_GlobalIdsName: bpy.props.StringProperty(name='GlobalIdsName', default="") #type: ignore
    m_Header: bpy.props.StringProperty(name='Header', default="vtk output") #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="lookup_table") #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="") #type: ignore
    m_PedigreeIdsName: bpy.props.StringProperty(name='PedigreeIdsName', default="") #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="") #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="") #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="") #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="") #type: ignore
    m_FileVersion: bpy.props.IntProperty(name='FileVersion', default=51) #type: ignore
    e_FileType: bpy.props.EnumProperty(name='FileType', default="ASCII", items=e_FileType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','m_FileVersion','e_FileType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKPolyDataWriter )        
TYPENAMES.append('VTKPolyDataWriterType' )

#--------------------------------------------------------------
class VTKPostScriptWriter(Node, PBVTK_Node):

    bl_idname = 'VTKPostScriptWriterType'
    bl_label  = 'vtkPostScriptWriter'
    
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d") #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="") #type: ignore
    m_FileDimensionality: bpy.props.IntProperty(name='FileDimensionality', default=2) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKPostScriptWriter )        
TYPENAMES.append('VTKPostScriptWriterType' )

#--------------------------------------------------------------
class VTKRectilinearGridWriter(Node, PBVTK_Node):

    bl_idname = 'VTKRectilinearGridWriterType'
    bl_label  = 'vtkRectilinearGridWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData: bpy.props.BoolProperty(name='WriteArrayMetaData', default=True) #type: ignore
    m_WriteExtent: bpy.props.BoolProperty(name='WriteExtent', default=False) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=True) #type: ignore
    m_EdgeFlagsName: bpy.props.StringProperty(name='EdgeFlagsName', default="") #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="FieldData") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_GlobalIdsName: bpy.props.StringProperty(name='GlobalIdsName', default="") #type: ignore
    m_Header: bpy.props.StringProperty(name='Header', default="vtk output") #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="lookup_table") #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="") #type: ignore
    m_PedigreeIdsName: bpy.props.StringProperty(name='PedigreeIdsName', default="") #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="") #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="") #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="") #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="") #type: ignore
    m_FileVersion: bpy.props.IntProperty(name='FileVersion', default=51) #type: ignore
    e_FileType: bpy.props.EnumProperty(name='FileType', default="ASCII", items=e_FileType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=17, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteExtent','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','m_FileVersion','e_FileType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKRectilinearGridWriter )        
TYPENAMES.append('VTKRectilinearGridWriterType' )

#--------------------------------------------------------------
class VTKSTLWriter(Node, PBVTK_Node):

    bl_idname = 'VTKSTLWriterType'
    bl_label  = 'vtkSTLWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_Header: bpy.props.StringProperty(name='Header', default="Visualization Toolkit generated SLA File") #type: ignore
    e_FileType: bpy.props.EnumProperty(name='FileType', default="ASCII", items=e_FileType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_FileName','m_Header','e_FileType',]
    def m_connections( self ):
        return (['VTK Input'], [], ['BinaryHeader'], []) 
    
add_class( VTKSTLWriter )        
TYPENAMES.append('VTKSTLWriterType' )

#--------------------------------------------------------------
class VTKSimplePointsWriter(Node, PBVTK_Node):

    bl_idname = 'VTKSimplePointsWriterType'
    bl_label  = 'vtkSimplePointsWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData: bpy.props.BoolProperty(name='WriteArrayMetaData', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=True) #type: ignore
    m_EdgeFlagsName: bpy.props.StringProperty(name='EdgeFlagsName', default="") #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="FieldData") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_GlobalIdsName: bpy.props.StringProperty(name='GlobalIdsName', default="") #type: ignore
    m_Header: bpy.props.StringProperty(name='Header', default="vtk output") #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="lookup_table") #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="") #type: ignore
    m_PedigreeIdsName: bpy.props.StringProperty(name='PedigreeIdsName', default="") #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="") #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="") #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="") #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="") #type: ignore
    m_DecimalPrecision: bpy.props.IntProperty(name='DecimalPrecision', default=6) #type: ignore
    m_FileVersion: bpy.props.IntProperty(name='FileVersion', default=51) #type: ignore
    e_FileType: bpy.props.EnumProperty(name='FileType', default="ASCII", items=e_FileType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=17, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','m_DecimalPrecision','m_FileVersion','e_FileType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKSimplePointsWriter )        
TYPENAMES.append('VTKSimplePointsWriterType' )

#--------------------------------------------------------------
class VTKStructuredGridWriter(Node, PBVTK_Node):

    bl_idname = 'VTKStructuredGridWriterType'
    bl_label  = 'vtkStructuredGridWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData: bpy.props.BoolProperty(name='WriteArrayMetaData', default=True) #type: ignore
    m_WriteExtent: bpy.props.BoolProperty(name='WriteExtent', default=False) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=True) #type: ignore
    m_EdgeFlagsName: bpy.props.StringProperty(name='EdgeFlagsName', default="") #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="FieldData") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_GlobalIdsName: bpy.props.StringProperty(name='GlobalIdsName', default="") #type: ignore
    m_Header: bpy.props.StringProperty(name='Header', default="vtk output") #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="lookup_table") #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="") #type: ignore
    m_PedigreeIdsName: bpy.props.StringProperty(name='PedigreeIdsName', default="") #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="") #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="") #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="") #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="") #type: ignore
    m_FileVersion: bpy.props.IntProperty(name='FileVersion', default=51) #type: ignore
    e_FileType: bpy.props.EnumProperty(name='FileType', default="ASCII", items=e_FileType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=17, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteExtent','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','m_FileVersion','e_FileType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKStructuredGridWriter )        
TYPENAMES.append('VTKStructuredGridWriterType' )

#--------------------------------------------------------------
class VTKStructuredPointsWriter(Node, PBVTK_Node):

    bl_idname = 'VTKStructuredPointsWriterType'
    bl_label  = 'vtkStructuredPointsWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData: bpy.props.BoolProperty(name='WriteArrayMetaData', default=True) #type: ignore
    m_WriteExtent: bpy.props.BoolProperty(name='WriteExtent', default=False) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=True) #type: ignore
    m_EdgeFlagsName: bpy.props.StringProperty(name='EdgeFlagsName', default="") #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="FieldData") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_GlobalIdsName: bpy.props.StringProperty(name='GlobalIdsName', default="") #type: ignore
    m_Header: bpy.props.StringProperty(name='Header', default="vtk output") #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="lookup_table") #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="") #type: ignore
    m_PedigreeIdsName: bpy.props.StringProperty(name='PedigreeIdsName', default="") #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="") #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="") #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="") #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="") #type: ignore
    m_FileVersion: bpy.props.IntProperty(name='FileVersion', default=51) #type: ignore
    e_FileType: bpy.props.EnumProperty(name='FileType', default="ASCII", items=e_FileType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=17, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteExtent','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','m_FileVersion','e_FileType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKStructuredPointsWriter )        
TYPENAMES.append('VTKStructuredPointsWriterType' )

#--------------------------------------------------------------
class VTKTIFFWriter(Node, PBVTK_Node):

    bl_idname = 'VTKTIFFWriterType'
    bl_label  = 'vtkTIFFWriter'
    e_Compression_items=[ (x,x,x) for x in ['NoCompression', 'PackBits', 'JPEG', 'Deflate', 'LZW']]
    
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d") #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="") #type: ignore
    m_FileDimensionality: bpy.props.IntProperty(name='FileDimensionality', default=2) #type: ignore
    e_Compression: bpy.props.EnumProperty(name='Compression', default="PackBits", items=e_Compression_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_FileName','m_FilePattern','m_FilePrefix','m_FileDimensionality','e_Compression',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKTIFFWriter )        
TYPENAMES.append('VTKTIFFWriterType' )

#--------------------------------------------------------------
class VTKTableToSQLiteWriter(Node, PBVTK_Node):

    bl_idname = 'VTKTableToSQLiteWriterType'
    bl_label  = 'vtkTableToSQLiteWriter'
    
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=1, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return []
    def m_connections( self ):
        return (['VTK Input'], [], ['Database'], []) 
    
add_class( VTKTableToSQLiteWriter )        
TYPENAMES.append('VTKTableToSQLiteWriterType' )

#--------------------------------------------------------------
class VTKTableWriter(Node, PBVTK_Node):

    bl_idname = 'VTKTableWriterType'
    bl_label  = 'vtkTableWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData: bpy.props.BoolProperty(name='WriteArrayMetaData', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=True) #type: ignore
    m_EdgeFlagsName: bpy.props.StringProperty(name='EdgeFlagsName', default="") #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="FieldData") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_GlobalIdsName: bpy.props.StringProperty(name='GlobalIdsName', default="") #type: ignore
    m_Header: bpy.props.StringProperty(name='Header', default="vtk output") #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="lookup_table") #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="") #type: ignore
    m_PedigreeIdsName: bpy.props.StringProperty(name='PedigreeIdsName', default="") #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="") #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="") #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="") #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="") #type: ignore
    m_FileVersion: bpy.props.IntProperty(name='FileVersion', default=51) #type: ignore
    e_FileType: bpy.props.EnumProperty(name='FileType', default="ASCII", items=e_FileType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','m_FileVersion','e_FileType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKTableWriter )        
TYPENAMES.append('VTKTableWriterType' )

#--------------------------------------------------------------
class VTKTreeWriter(Node, PBVTK_Node):

    bl_idname = 'VTKTreeWriterType'
    bl_label  = 'vtkTreeWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData: bpy.props.BoolProperty(name='WriteArrayMetaData', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=True) #type: ignore
    m_EdgeFlagsName: bpy.props.StringProperty(name='EdgeFlagsName', default="") #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="FieldData") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_GlobalIdsName: bpy.props.StringProperty(name='GlobalIdsName', default="") #type: ignore
    m_Header: bpy.props.StringProperty(name='Header', default="vtk output") #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="lookup_table") #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="") #type: ignore
    m_PedigreeIdsName: bpy.props.StringProperty(name='PedigreeIdsName', default="") #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="") #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="") #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="") #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="") #type: ignore
    m_FileVersion: bpy.props.IntProperty(name='FileVersion', default=51) #type: ignore
    e_FileType: bpy.props.EnumProperty(name='FileType', default="ASCII", items=e_FileType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','m_FileVersion','e_FileType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKTreeWriter )        
TYPENAMES.append('VTKTreeWriterType' )

#--------------------------------------------------------------
class VTKUnstructuredGridWriter(Node, PBVTK_Node):

    bl_idname = 'VTKUnstructuredGridWriterType'
    bl_label  = 'vtkUnstructuredGridWriter'
    e_FileType_items=[ (x,x,x) for x in ['ASCII', 'Binary']]
    
    m_WriteArrayMetaData: bpy.props.BoolProperty(name='WriteArrayMetaData', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=True) #type: ignore
    m_EdgeFlagsName: bpy.props.StringProperty(name='EdgeFlagsName', default="") #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="FieldData") #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_GlobalIdsName: bpy.props.StringProperty(name='GlobalIdsName', default="") #type: ignore
    m_Header: bpy.props.StringProperty(name='Header', default="vtk output") #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="lookup_table") #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="") #type: ignore
    m_PedigreeIdsName: bpy.props.StringProperty(name='PedigreeIdsName', default="") #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="") #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="") #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="") #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="") #type: ignore
    m_FileVersion: bpy.props.IntProperty(name='FileVersion', default=51) #type: ignore
    e_FileType: bpy.props.EnumProperty(name='FileType', default="ASCII", items=e_FileType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_WriteArrayMetaData','m_WriteToOutputString','m_EdgeFlagsName','m_FieldDataName','m_FileName','m_GlobalIdsName','m_Header','m_LookupTableName','m_NormalsName','m_PedigreeIdsName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName','m_FileVersion','e_FileType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKUnstructuredGridWriter )        
TYPENAMES.append('VTKUnstructuredGridWriterType' )

#--------------------------------------------------------------
class VTKXMLDataObjectWriter(Node, PBVTK_Node):

    bl_idname = 'VTKXMLDataObjectWriterType'
    bl_label  = 'vtkXMLDataObjectWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData: bpy.props.BoolProperty(name='EncodeAppendedData', default=True) #type: ignore
    m_WriteTimeValue: bpy.props.BoolProperty(name='WriteTimeValue', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_BlockSize: bpy.props.IntProperty(name='BlockSize', default=32768) #type: ignore
    m_CompressionLevel: bpy.props.IntProperty(name='CompressionLevel', default=5) #type: ignore
    m_NumberOfTimeSteps: bpy.props.IntProperty(name='NumberOfTimeSteps', default=1) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="LittleEndian", items=e_ByteOrder_items) #type: ignore
    e_DataMode: bpy.props.EnumProperty(name='DataMode', default="Appended", items=e_DataMode_items) #type: ignore
    e_HeaderType: bpy.props.EnumProperty(name='HeaderType', default="UInt32", items=e_HeaderType_items) #type: ignore
    e_IdType: bpy.props.EnumProperty(name='IdType', default="Int64", items=e_IdType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteTimeValue','m_WriteToOutputString','m_FileName','m_BlockSize','m_CompressionLevel','m_NumberOfTimeSteps','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKXMLDataObjectWriter )        
TYPENAMES.append('VTKXMLDataObjectWriterType' )

#--------------------------------------------------------------
class VTKXMLDataSetWriter(Node, PBVTK_Node):

    bl_idname = 'VTKXMLDataSetWriterType'
    bl_label  = 'vtkXMLDataSetWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData: bpy.props.BoolProperty(name='EncodeAppendedData', default=True) #type: ignore
    m_WriteTimeValue: bpy.props.BoolProperty(name='WriteTimeValue', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_BlockSize: bpy.props.IntProperty(name='BlockSize', default=32768) #type: ignore
    m_CompressionLevel: bpy.props.IntProperty(name='CompressionLevel', default=5) #type: ignore
    m_NumberOfTimeSteps: bpy.props.IntProperty(name='NumberOfTimeSteps', default=1) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="LittleEndian", items=e_ByteOrder_items) #type: ignore
    e_DataMode: bpy.props.EnumProperty(name='DataMode', default="Appended", items=e_DataMode_items) #type: ignore
    e_HeaderType: bpy.props.EnumProperty(name='HeaderType', default="UInt32", items=e_HeaderType_items) #type: ignore
    e_IdType: bpy.props.EnumProperty(name='IdType', default="Int64", items=e_IdType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteTimeValue','m_WriteToOutputString','m_FileName','m_BlockSize','m_CompressionLevel','m_NumberOfTimeSteps','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKXMLDataSetWriter )        
TYPENAMES.append('VTKXMLDataSetWriterType' )

#--------------------------------------------------------------
class VTKXMLDataWriterHelper(Node, PBVTK_Node):

    bl_idname = 'VTKXMLDataWriterHelperType'
    bl_label  = 'vtkXMLDataWriterHelper'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData: bpy.props.BoolProperty(name='EncodeAppendedData', default=True) #type: ignore
    m_WriteTimeValue: bpy.props.BoolProperty(name='WriteTimeValue', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_BlockSize: bpy.props.IntProperty(name='BlockSize', default=32768) #type: ignore
    m_CompressionLevel: bpy.props.IntProperty(name='CompressionLevel', default=5) #type: ignore
    m_NumberOfTimeSteps: bpy.props.IntProperty(name='NumberOfTimeSteps', default=1) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="LittleEndian", items=e_ByteOrder_items) #type: ignore
    e_DataMode: bpy.props.EnumProperty(name='DataMode', default="Appended", items=e_DataMode_items) #type: ignore
    e_HeaderType: bpy.props.EnumProperty(name='HeaderType', default="UInt32", items=e_HeaderType_items) #type: ignore
    e_IdType: bpy.props.EnumProperty(name='IdType', default="Int64", items=e_IdType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteTimeValue','m_WriteToOutputString','m_FileName','m_BlockSize','m_CompressionLevel','m_NumberOfTimeSteps','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['VTK Input'], [], ['Writer'], []) 
    
add_class( VTKXMLDataWriterHelper )        
TYPENAMES.append('VTKXMLDataWriterHelperType' )

#--------------------------------------------------------------
class VTKXMLHierarchicalBoxDataWriter(Node, PBVTK_Node):

    bl_idname = 'VTKXMLHierarchicalBoxDataWriterType'
    bl_label  = 'vtkXMLHierarchicalBoxDataWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData: bpy.props.BoolProperty(name='EncodeAppendedData', default=True) #type: ignore
    m_WriteTimeValue: bpy.props.BoolProperty(name='WriteTimeValue', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_BlockSize: bpy.props.IntProperty(name='BlockSize', default=32768) #type: ignore
    m_CompressionLevel: bpy.props.IntProperty(name='CompressionLevel', default=5) #type: ignore
    m_GhostLevel: bpy.props.IntProperty(name='GhostLevel', default=0) #type: ignore
    m_NumberOfTimeSteps: bpy.props.IntProperty(name='NumberOfTimeSteps', default=1) #type: ignore
    m_WriteMetaFile: bpy.props.IntProperty(name='WriteMetaFile', default=1) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="LittleEndian", items=e_ByteOrder_items) #type: ignore
    e_DataMode: bpy.props.EnumProperty(name='DataMode', default="Appended", items=e_DataMode_items) #type: ignore
    e_HeaderType: bpy.props.EnumProperty(name='HeaderType', default="UInt32", items=e_HeaderType_items) #type: ignore
    e_IdType: bpy.props.EnumProperty(name='IdType', default="Int64", items=e_IdType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteTimeValue','m_WriteToOutputString','m_FileName','m_BlockSize','m_CompressionLevel','m_GhostLevel','m_NumberOfTimeSteps','m_WriteMetaFile','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKXMLHierarchicalBoxDataWriter )        
TYPENAMES.append('VTKXMLHierarchicalBoxDataWriterType' )

#--------------------------------------------------------------
class VTKXMLHyperTreeGridWriter(Node, PBVTK_Node):

    bl_idname = 'VTKXMLHyperTreeGridWriterType'
    bl_label  = 'vtkXMLHyperTreeGridWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData: bpy.props.BoolProperty(name='EncodeAppendedData', default=True) #type: ignore
    m_WriteTimeValue: bpy.props.BoolProperty(name='WriteTimeValue', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_BlockSize: bpy.props.IntProperty(name='BlockSize', default=32768) #type: ignore
    m_CompressionLevel: bpy.props.IntProperty(name='CompressionLevel', default=5) #type: ignore
    m_NumberOfTimeSteps: bpy.props.IntProperty(name='NumberOfTimeSteps', default=1) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="LittleEndian", items=e_ByteOrder_items) #type: ignore
    e_DataMode: bpy.props.EnumProperty(name='DataMode', default="Appended", items=e_DataMode_items) #type: ignore
    e_HeaderType: bpy.props.EnumProperty(name='HeaderType', default="UInt32", items=e_HeaderType_items) #type: ignore
    e_IdType: bpy.props.EnumProperty(name='IdType', default="Int64", items=e_IdType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteTimeValue','m_WriteToOutputString','m_FileName','m_BlockSize','m_CompressionLevel','m_NumberOfTimeSteps','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKXMLHyperTreeGridWriter )        
TYPENAMES.append('VTKXMLHyperTreeGridWriterType' )

#--------------------------------------------------------------
class VTKXMLImageDataWriter(Node, PBVTK_Node):

    bl_idname = 'VTKXMLImageDataWriterType'
    bl_label  = 'vtkXMLImageDataWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData: bpy.props.BoolProperty(name='EncodeAppendedData', default=True) #type: ignore
    m_WriteTimeValue: bpy.props.BoolProperty(name='WriteTimeValue', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_BlockSize: bpy.props.IntProperty(name='BlockSize', default=32768) #type: ignore
    m_CompressionLevel: bpy.props.IntProperty(name='CompressionLevel', default=5) #type: ignore
    m_GhostLevel: bpy.props.IntProperty(name='GhostLevel', default=0) #type: ignore
    m_NumberOfPieces: bpy.props.IntProperty(name='NumberOfPieces', default=1) #type: ignore
    m_NumberOfTimeSteps: bpy.props.IntProperty(name='NumberOfTimeSteps', default=1) #type: ignore
    m_WritePiece: bpy.props.IntProperty(name='WritePiece', default=-1) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="LittleEndian", items=e_ByteOrder_items) #type: ignore
    e_DataMode: bpy.props.EnumProperty(name='DataMode', default="Appended", items=e_DataMode_items) #type: ignore
    e_HeaderType: bpy.props.EnumProperty(name='HeaderType', default="UInt32", items=e_HeaderType_items) #type: ignore
    e_IdType: bpy.props.EnumProperty(name='IdType', default="Int64", items=e_IdType_items) #type: ignore
    m_WriteExtent: bpy.props.IntVectorProperty(name='WriteExtent', default=[0, -1, 0, -1, 0, -1], size=6) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteTimeValue','m_WriteToOutputString','m_FileName','m_BlockSize','m_CompressionLevel','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_WritePiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType','m_WriteExtent',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKXMLImageDataWriter )        
TYPENAMES.append('VTKXMLImageDataWriterType' )

#--------------------------------------------------------------
class VTKXMLMultiBlockDataWriter(Node, PBVTK_Node):

    bl_idname = 'VTKXMLMultiBlockDataWriterType'
    bl_label  = 'vtkXMLMultiBlockDataWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData: bpy.props.BoolProperty(name='EncodeAppendedData', default=True) #type: ignore
    m_WriteTimeValue: bpy.props.BoolProperty(name='WriteTimeValue', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_BlockSize: bpy.props.IntProperty(name='BlockSize', default=32768) #type: ignore
    m_CompressionLevel: bpy.props.IntProperty(name='CompressionLevel', default=5) #type: ignore
    m_GhostLevel: bpy.props.IntProperty(name='GhostLevel', default=0) #type: ignore
    m_NumberOfTimeSteps: bpy.props.IntProperty(name='NumberOfTimeSteps', default=1) #type: ignore
    m_WriteMetaFile: bpy.props.IntProperty(name='WriteMetaFile', default=1) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="LittleEndian", items=e_ByteOrder_items) #type: ignore
    e_DataMode: bpy.props.EnumProperty(name='DataMode', default="Appended", items=e_DataMode_items) #type: ignore
    e_HeaderType: bpy.props.EnumProperty(name='HeaderType', default="UInt32", items=e_HeaderType_items) #type: ignore
    e_IdType: bpy.props.EnumProperty(name='IdType', default="Int64", items=e_IdType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteTimeValue','m_WriteToOutputString','m_FileName','m_BlockSize','m_CompressionLevel','m_GhostLevel','m_NumberOfTimeSteps','m_WriteMetaFile','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKXMLMultiBlockDataWriter )        
TYPENAMES.append('VTKXMLMultiBlockDataWriterType' )

#--------------------------------------------------------------
class VTKXMLPDataSetWriter(Node, PBVTK_Node):

    bl_idname = 'VTKXMLPDataSetWriterType'
    bl_label  = 'vtkXMLPDataSetWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData: bpy.props.BoolProperty(name='EncodeAppendedData', default=True) #type: ignore
    m_UseSubdirectory: bpy.props.BoolProperty(name='UseSubdirectory', default=False) #type: ignore
    m_WriteSummaryFile: bpy.props.BoolProperty(name='WriteSummaryFile', default=True) #type: ignore
    m_WriteTimeValue: bpy.props.BoolProperty(name='WriteTimeValue', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_BlockSize: bpy.props.IntProperty(name='BlockSize', default=32768) #type: ignore
    m_CompressionLevel: bpy.props.IntProperty(name='CompressionLevel', default=5) #type: ignore
    m_EndPiece: bpy.props.IntProperty(name='EndPiece', default=0) #type: ignore
    m_GhostLevel: bpy.props.IntProperty(name='GhostLevel', default=0) #type: ignore
    m_NumberOfPieces: bpy.props.IntProperty(name='NumberOfPieces', default=1) #type: ignore
    m_NumberOfTimeSteps: bpy.props.IntProperty(name='NumberOfTimeSteps', default=1) #type: ignore
    m_StartPiece: bpy.props.IntProperty(name='StartPiece', default=0) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="LittleEndian", items=e_ByteOrder_items) #type: ignore
    e_DataMode: bpy.props.EnumProperty(name='DataMode', default="Appended", items=e_DataMode_items) #type: ignore
    e_HeaderType: bpy.props.EnumProperty(name='HeaderType', default="UInt32", items=e_HeaderType_items) #type: ignore
    e_IdType: bpy.props.EnumProperty(name='IdType', default="Int64", items=e_IdType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=17, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_UseSubdirectory','m_WriteSummaryFile','m_WriteTimeValue','m_WriteToOutputString','m_FileName','m_BlockSize','m_CompressionLevel','m_EndPiece','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_StartPiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKXMLPDataSetWriter )        
TYPENAMES.append('VTKXMLPDataSetWriterType' )

#--------------------------------------------------------------
class VTKXMLPHierarchicalBoxDataWriter(Node, PBVTK_Node):

    bl_idname = 'VTKXMLPHierarchicalBoxDataWriterType'
    bl_label  = 'vtkXMLPHierarchicalBoxDataWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData: bpy.props.BoolProperty(name='EncodeAppendedData', default=True) #type: ignore
    m_WriteTimeValue: bpy.props.BoolProperty(name='WriteTimeValue', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_BlockSize: bpy.props.IntProperty(name='BlockSize', default=32768) #type: ignore
    m_CompressionLevel: bpy.props.IntProperty(name='CompressionLevel', default=5) #type: ignore
    m_GhostLevel: bpy.props.IntProperty(name='GhostLevel', default=0) #type: ignore
    m_NumberOfTimeSteps: bpy.props.IntProperty(name='NumberOfTimeSteps', default=1) #type: ignore
    m_WriteMetaFile: bpy.props.IntProperty(name='WriteMetaFile', default=1) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="LittleEndian", items=e_ByteOrder_items) #type: ignore
    e_DataMode: bpy.props.EnumProperty(name='DataMode', default="Appended", items=e_DataMode_items) #type: ignore
    e_HeaderType: bpy.props.EnumProperty(name='HeaderType', default="UInt32", items=e_HeaderType_items) #type: ignore
    e_IdType: bpy.props.EnumProperty(name='IdType', default="Int64", items=e_IdType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteTimeValue','m_WriteToOutputString','m_FileName','m_BlockSize','m_CompressionLevel','m_GhostLevel','m_NumberOfTimeSteps','m_WriteMetaFile','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKXMLPHierarchicalBoxDataWriter )        
TYPENAMES.append('VTKXMLPHierarchicalBoxDataWriterType' )

#--------------------------------------------------------------
class VTKXMLPHyperTreeGridWriter(Node, PBVTK_Node):

    bl_idname = 'VTKXMLPHyperTreeGridWriterType'
    bl_label  = 'vtkXMLPHyperTreeGridWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData: bpy.props.BoolProperty(name='EncodeAppendedData', default=True) #type: ignore
    m_UseSubdirectory: bpy.props.BoolProperty(name='UseSubdirectory', default=False) #type: ignore
    m_WriteSummaryFile: bpy.props.BoolProperty(name='WriteSummaryFile', default=True) #type: ignore
    m_WriteTimeValue: bpy.props.BoolProperty(name='WriteTimeValue', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_BlockSize: bpy.props.IntProperty(name='BlockSize', default=32768) #type: ignore
    m_CompressionLevel: bpy.props.IntProperty(name='CompressionLevel', default=5) #type: ignore
    m_EndPiece: bpy.props.IntProperty(name='EndPiece', default=0) #type: ignore
    m_GhostLevel: bpy.props.IntProperty(name='GhostLevel', default=0) #type: ignore
    m_NumberOfPieces: bpy.props.IntProperty(name='NumberOfPieces', default=1) #type: ignore
    m_NumberOfTimeSteps: bpy.props.IntProperty(name='NumberOfTimeSteps', default=1) #type: ignore
    m_StartPiece: bpy.props.IntProperty(name='StartPiece', default=0) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="LittleEndian", items=e_ByteOrder_items) #type: ignore
    e_DataMode: bpy.props.EnumProperty(name='DataMode', default="Appended", items=e_DataMode_items) #type: ignore
    e_HeaderType: bpy.props.EnumProperty(name='HeaderType', default="UInt32", items=e_HeaderType_items) #type: ignore
    e_IdType: bpy.props.EnumProperty(name='IdType', default="Int64", items=e_IdType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=17, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_UseSubdirectory','m_WriteSummaryFile','m_WriteTimeValue','m_WriteToOutputString','m_FileName','m_BlockSize','m_CompressionLevel','m_EndPiece','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_StartPiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKXMLPHyperTreeGridWriter )        
TYPENAMES.append('VTKXMLPHyperTreeGridWriterType' )

#--------------------------------------------------------------
class VTKXMLPImageDataWriter(Node, PBVTK_Node):

    bl_idname = 'VTKXMLPImageDataWriterType'
    bl_label  = 'vtkXMLPImageDataWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData: bpy.props.BoolProperty(name='EncodeAppendedData', default=True) #type: ignore
    m_UseSubdirectory: bpy.props.BoolProperty(name='UseSubdirectory', default=False) #type: ignore
    m_WriteSummaryFile: bpy.props.BoolProperty(name='WriteSummaryFile', default=True) #type: ignore
    m_WriteTimeValue: bpy.props.BoolProperty(name='WriteTimeValue', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_BlockSize: bpy.props.IntProperty(name='BlockSize', default=32768) #type: ignore
    m_CompressionLevel: bpy.props.IntProperty(name='CompressionLevel', default=5) #type: ignore
    m_EndPiece: bpy.props.IntProperty(name='EndPiece', default=0) #type: ignore
    m_GhostLevel: bpy.props.IntProperty(name='GhostLevel', default=0) #type: ignore
    m_NumberOfPieces: bpy.props.IntProperty(name='NumberOfPieces', default=1) #type: ignore
    m_NumberOfTimeSteps: bpy.props.IntProperty(name='NumberOfTimeSteps', default=1) #type: ignore
    m_StartPiece: bpy.props.IntProperty(name='StartPiece', default=0) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="LittleEndian", items=e_ByteOrder_items) #type: ignore
    e_DataMode: bpy.props.EnumProperty(name='DataMode', default="Appended", items=e_DataMode_items) #type: ignore
    e_HeaderType: bpy.props.EnumProperty(name='HeaderType', default="UInt32", items=e_HeaderType_items) #type: ignore
    e_IdType: bpy.props.EnumProperty(name='IdType', default="Int64", items=e_IdType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=17, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_UseSubdirectory','m_WriteSummaryFile','m_WriteTimeValue','m_WriteToOutputString','m_FileName','m_BlockSize','m_CompressionLevel','m_EndPiece','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_StartPiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKXMLPImageDataWriter )        
TYPENAMES.append('VTKXMLPImageDataWriterType' )

#--------------------------------------------------------------
class VTKXMLPMultiBlockDataWriter(Node, PBVTK_Node):

    bl_idname = 'VTKXMLPMultiBlockDataWriterType'
    bl_label  = 'vtkXMLPMultiBlockDataWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData: bpy.props.BoolProperty(name='EncodeAppendedData', default=True) #type: ignore
    m_WriteTimeValue: bpy.props.BoolProperty(name='WriteTimeValue', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_BlockSize: bpy.props.IntProperty(name='BlockSize', default=32768) #type: ignore
    m_CompressionLevel: bpy.props.IntProperty(name='CompressionLevel', default=5) #type: ignore
    m_GhostLevel: bpy.props.IntProperty(name='GhostLevel', default=0) #type: ignore
    m_NumberOfPieces: bpy.props.IntProperty(name='NumberOfPieces', default=1) #type: ignore
    m_NumberOfTimeSteps: bpy.props.IntProperty(name='NumberOfTimeSteps', default=1) #type: ignore
    m_StartPiece: bpy.props.IntProperty(name='StartPiece', default=0) #type: ignore
    m_WriteMetaFile: bpy.props.IntProperty(name='WriteMetaFile', default=1) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="LittleEndian", items=e_ByteOrder_items) #type: ignore
    e_DataMode: bpy.props.EnumProperty(name='DataMode', default="Appended", items=e_DataMode_items) #type: ignore
    e_HeaderType: bpy.props.EnumProperty(name='HeaderType', default="UInt32", items=e_HeaderType_items) #type: ignore
    e_IdType: bpy.props.EnumProperty(name='IdType', default="Int64", items=e_IdType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteTimeValue','m_WriteToOutputString','m_FileName','m_BlockSize','m_CompressionLevel','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_StartPiece','m_WriteMetaFile','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKXMLPMultiBlockDataWriter )        
TYPENAMES.append('VTKXMLPMultiBlockDataWriterType' )

#--------------------------------------------------------------
class VTKXMLPPolyDataWriter(Node, PBVTK_Node):

    bl_idname = 'VTKXMLPPolyDataWriterType'
    bl_label  = 'vtkXMLPPolyDataWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData: bpy.props.BoolProperty(name='EncodeAppendedData', default=True) #type: ignore
    m_UseSubdirectory: bpy.props.BoolProperty(name='UseSubdirectory', default=False) #type: ignore
    m_WriteSummaryFile: bpy.props.BoolProperty(name='WriteSummaryFile', default=True) #type: ignore
    m_WriteTimeValue: bpy.props.BoolProperty(name='WriteTimeValue', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_BlockSize: bpy.props.IntProperty(name='BlockSize', default=32768) #type: ignore
    m_CompressionLevel: bpy.props.IntProperty(name='CompressionLevel', default=5) #type: ignore
    m_EndPiece: bpy.props.IntProperty(name='EndPiece', default=0) #type: ignore
    m_GhostLevel: bpy.props.IntProperty(name='GhostLevel', default=0) #type: ignore
    m_NumberOfPieces: bpy.props.IntProperty(name='NumberOfPieces', default=1) #type: ignore
    m_NumberOfTimeSteps: bpy.props.IntProperty(name='NumberOfTimeSteps', default=1) #type: ignore
    m_StartPiece: bpy.props.IntProperty(name='StartPiece', default=0) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="LittleEndian", items=e_ByteOrder_items) #type: ignore
    e_DataMode: bpy.props.EnumProperty(name='DataMode', default="Appended", items=e_DataMode_items) #type: ignore
    e_HeaderType: bpy.props.EnumProperty(name='HeaderType', default="UInt32", items=e_HeaderType_items) #type: ignore
    e_IdType: bpy.props.EnumProperty(name='IdType', default="Int64", items=e_IdType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=17, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_UseSubdirectory','m_WriteSummaryFile','m_WriteTimeValue','m_WriteToOutputString','m_FileName','m_BlockSize','m_CompressionLevel','m_EndPiece','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_StartPiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKXMLPPolyDataWriter )        
TYPENAMES.append('VTKXMLPPolyDataWriterType' )

#--------------------------------------------------------------
class VTKXMLPRectilinearGridWriter(Node, PBVTK_Node):

    bl_idname = 'VTKXMLPRectilinearGridWriterType'
    bl_label  = 'vtkXMLPRectilinearGridWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData: bpy.props.BoolProperty(name='EncodeAppendedData', default=True) #type: ignore
    m_UseSubdirectory: bpy.props.BoolProperty(name='UseSubdirectory', default=False) #type: ignore
    m_WriteSummaryFile: bpy.props.BoolProperty(name='WriteSummaryFile', default=True) #type: ignore
    m_WriteTimeValue: bpy.props.BoolProperty(name='WriteTimeValue', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_BlockSize: bpy.props.IntProperty(name='BlockSize', default=32768) #type: ignore
    m_CompressionLevel: bpy.props.IntProperty(name='CompressionLevel', default=5) #type: ignore
    m_EndPiece: bpy.props.IntProperty(name='EndPiece', default=0) #type: ignore
    m_GhostLevel: bpy.props.IntProperty(name='GhostLevel', default=0) #type: ignore
    m_NumberOfPieces: bpy.props.IntProperty(name='NumberOfPieces', default=1) #type: ignore
    m_NumberOfTimeSteps: bpy.props.IntProperty(name='NumberOfTimeSteps', default=1) #type: ignore
    m_StartPiece: bpy.props.IntProperty(name='StartPiece', default=0) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="LittleEndian", items=e_ByteOrder_items) #type: ignore
    e_DataMode: bpy.props.EnumProperty(name='DataMode', default="Appended", items=e_DataMode_items) #type: ignore
    e_HeaderType: bpy.props.EnumProperty(name='HeaderType', default="UInt32", items=e_HeaderType_items) #type: ignore
    e_IdType: bpy.props.EnumProperty(name='IdType', default="Int64", items=e_IdType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=17, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_UseSubdirectory','m_WriteSummaryFile','m_WriteTimeValue','m_WriteToOutputString','m_FileName','m_BlockSize','m_CompressionLevel','m_EndPiece','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_StartPiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKXMLPRectilinearGridWriter )        
TYPENAMES.append('VTKXMLPRectilinearGridWriterType' )

#--------------------------------------------------------------
class VTKXMLPStructuredGridWriter(Node, PBVTK_Node):

    bl_idname = 'VTKXMLPStructuredGridWriterType'
    bl_label  = 'vtkXMLPStructuredGridWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData: bpy.props.BoolProperty(name='EncodeAppendedData', default=True) #type: ignore
    m_UseSubdirectory: bpy.props.BoolProperty(name='UseSubdirectory', default=False) #type: ignore
    m_WriteSummaryFile: bpy.props.BoolProperty(name='WriteSummaryFile', default=True) #type: ignore
    m_WriteTimeValue: bpy.props.BoolProperty(name='WriteTimeValue', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_BlockSize: bpy.props.IntProperty(name='BlockSize', default=32768) #type: ignore
    m_CompressionLevel: bpy.props.IntProperty(name='CompressionLevel', default=5) #type: ignore
    m_EndPiece: bpy.props.IntProperty(name='EndPiece', default=0) #type: ignore
    m_GhostLevel: bpy.props.IntProperty(name='GhostLevel', default=0) #type: ignore
    m_NumberOfPieces: bpy.props.IntProperty(name='NumberOfPieces', default=1) #type: ignore
    m_NumberOfTimeSteps: bpy.props.IntProperty(name='NumberOfTimeSteps', default=1) #type: ignore
    m_StartPiece: bpy.props.IntProperty(name='StartPiece', default=0) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="LittleEndian", items=e_ByteOrder_items) #type: ignore
    e_DataMode: bpy.props.EnumProperty(name='DataMode', default="Appended", items=e_DataMode_items) #type: ignore
    e_HeaderType: bpy.props.EnumProperty(name='HeaderType', default="UInt32", items=e_HeaderType_items) #type: ignore
    e_IdType: bpy.props.EnumProperty(name='IdType', default="Int64", items=e_IdType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=17, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_UseSubdirectory','m_WriteSummaryFile','m_WriteTimeValue','m_WriteToOutputString','m_FileName','m_BlockSize','m_CompressionLevel','m_EndPiece','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_StartPiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKXMLPStructuredGridWriter )        
TYPENAMES.append('VTKXMLPStructuredGridWriterType' )

#--------------------------------------------------------------
class VTKXMLPTableWriter(Node, PBVTK_Node):

    bl_idname = 'VTKXMLPTableWriterType'
    bl_label  = 'vtkXMLPTableWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData: bpy.props.BoolProperty(name='EncodeAppendedData', default=True) #type: ignore
    m_UseSubdirectory: bpy.props.BoolProperty(name='UseSubdirectory', default=False) #type: ignore
    m_WriteSummaryFile: bpy.props.BoolProperty(name='WriteSummaryFile', default=True) #type: ignore
    m_WriteTimeValue: bpy.props.BoolProperty(name='WriteTimeValue', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_BlockSize: bpy.props.IntProperty(name='BlockSize', default=32768) #type: ignore
    m_CompressionLevel: bpy.props.IntProperty(name='CompressionLevel', default=5) #type: ignore
    m_EndPiece: bpy.props.IntProperty(name='EndPiece', default=0) #type: ignore
    m_GhostLevel: bpy.props.IntProperty(name='GhostLevel', default=0) #type: ignore
    m_NumberOfPieces: bpy.props.IntProperty(name='NumberOfPieces', default=1) #type: ignore
    m_NumberOfTimeSteps: bpy.props.IntProperty(name='NumberOfTimeSteps', default=1) #type: ignore
    m_StartPiece: bpy.props.IntProperty(name='StartPiece', default=0) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="LittleEndian", items=e_ByteOrder_items) #type: ignore
    e_DataMode: bpy.props.EnumProperty(name='DataMode', default="Appended", items=e_DataMode_items) #type: ignore
    e_HeaderType: bpy.props.EnumProperty(name='HeaderType', default="UInt32", items=e_HeaderType_items) #type: ignore
    e_IdType: bpy.props.EnumProperty(name='IdType', default="Int64", items=e_IdType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=17, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_UseSubdirectory','m_WriteSummaryFile','m_WriteTimeValue','m_WriteToOutputString','m_FileName','m_BlockSize','m_CompressionLevel','m_EndPiece','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_StartPiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKXMLPTableWriter )        
TYPENAMES.append('VTKXMLPTableWriterType' )

#--------------------------------------------------------------
class VTKXMLPUniformGridAMRWriter(Node, PBVTK_Node):

    bl_idname = 'VTKXMLPUniformGridAMRWriterType'
    bl_label  = 'vtkXMLPUniformGridAMRWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData: bpy.props.BoolProperty(name='EncodeAppendedData', default=True) #type: ignore
    m_WriteTimeValue: bpy.props.BoolProperty(name='WriteTimeValue', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_BlockSize: bpy.props.IntProperty(name='BlockSize', default=32768) #type: ignore
    m_CompressionLevel: bpy.props.IntProperty(name='CompressionLevel', default=5) #type: ignore
    m_GhostLevel: bpy.props.IntProperty(name='GhostLevel', default=0) #type: ignore
    m_NumberOfTimeSteps: bpy.props.IntProperty(name='NumberOfTimeSteps', default=1) #type: ignore
    m_WriteMetaFile: bpy.props.IntProperty(name='WriteMetaFile', default=1) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="LittleEndian", items=e_ByteOrder_items) #type: ignore
    e_DataMode: bpy.props.EnumProperty(name='DataMode', default="Appended", items=e_DataMode_items) #type: ignore
    e_HeaderType: bpy.props.EnumProperty(name='HeaderType', default="UInt32", items=e_HeaderType_items) #type: ignore
    e_IdType: bpy.props.EnumProperty(name='IdType', default="Int64", items=e_IdType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteTimeValue','m_WriteToOutputString','m_FileName','m_BlockSize','m_CompressionLevel','m_GhostLevel','m_NumberOfTimeSteps','m_WriteMetaFile','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKXMLPUniformGridAMRWriter )        
TYPENAMES.append('VTKXMLPUniformGridAMRWriterType' )

#--------------------------------------------------------------
class VTKXMLPUnstructuredGridWriter(Node, PBVTK_Node):

    bl_idname = 'VTKXMLPUnstructuredGridWriterType'
    bl_label  = 'vtkXMLPUnstructuredGridWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData: bpy.props.BoolProperty(name='EncodeAppendedData', default=True) #type: ignore
    m_UseSubdirectory: bpy.props.BoolProperty(name='UseSubdirectory', default=False) #type: ignore
    m_WriteSummaryFile: bpy.props.BoolProperty(name='WriteSummaryFile', default=True) #type: ignore
    m_WriteTimeValue: bpy.props.BoolProperty(name='WriteTimeValue', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_BlockSize: bpy.props.IntProperty(name='BlockSize', default=32768) #type: ignore
    m_CompressionLevel: bpy.props.IntProperty(name='CompressionLevel', default=5) #type: ignore
    m_EndPiece: bpy.props.IntProperty(name='EndPiece', default=0) #type: ignore
    m_GhostLevel: bpy.props.IntProperty(name='GhostLevel', default=0) #type: ignore
    m_NumberOfPieces: bpy.props.IntProperty(name='NumberOfPieces', default=1) #type: ignore
    m_NumberOfTimeSteps: bpy.props.IntProperty(name='NumberOfTimeSteps', default=1) #type: ignore
    m_StartPiece: bpy.props.IntProperty(name='StartPiece', default=0) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="LittleEndian", items=e_ByteOrder_items) #type: ignore
    e_DataMode: bpy.props.EnumProperty(name='DataMode', default="Appended", items=e_DataMode_items) #type: ignore
    e_HeaderType: bpy.props.EnumProperty(name='HeaderType', default="UInt32", items=e_HeaderType_items) #type: ignore
    e_IdType: bpy.props.EnumProperty(name='IdType', default="Int64", items=e_IdType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=17, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_UseSubdirectory','m_WriteSummaryFile','m_WriteTimeValue','m_WriteToOutputString','m_FileName','m_BlockSize','m_CompressionLevel','m_EndPiece','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_StartPiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKXMLPUnstructuredGridWriter )        
TYPENAMES.append('VTKXMLPUnstructuredGridWriterType' )

#--------------------------------------------------------------
class VTKXMLPartitionedDataSetCollectionWriter(Node, PBVTK_Node):

    bl_idname = 'VTKXMLPartitionedDataSetCollectionWriterType'
    bl_label  = 'vtkXMLPartitionedDataSetCollectionWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData: bpy.props.BoolProperty(name='EncodeAppendedData', default=True) #type: ignore
    m_WriteTimeValue: bpy.props.BoolProperty(name='WriteTimeValue', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_BlockSize: bpy.props.IntProperty(name='BlockSize', default=32768) #type: ignore
    m_CompressionLevel: bpy.props.IntProperty(name='CompressionLevel', default=5) #type: ignore
    m_NumberOfGhostLevels: bpy.props.IntProperty(name='NumberOfGhostLevels', default=0) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="LittleEndian", items=e_ByteOrder_items) #type: ignore
    e_DataMode: bpy.props.EnumProperty(name='DataMode', default="Appended", items=e_DataMode_items) #type: ignore
    e_HeaderType: bpy.props.EnumProperty(name='HeaderType', default="UInt32", items=e_HeaderType_items) #type: ignore
    e_IdType: bpy.props.EnumProperty(name='IdType', default="Int64", items=e_IdType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteTimeValue','m_WriteToOutputString','m_FileName','m_BlockSize','m_CompressionLevel','m_NumberOfGhostLevels','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKXMLPartitionedDataSetCollectionWriter )        
TYPENAMES.append('VTKXMLPartitionedDataSetCollectionWriterType' )

#--------------------------------------------------------------
class VTKXMLPartitionedDataSetWriter(Node, PBVTK_Node):

    bl_idname = 'VTKXMLPartitionedDataSetWriterType'
    bl_label  = 'vtkXMLPartitionedDataSetWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData: bpy.props.BoolProperty(name='EncodeAppendedData', default=True) #type: ignore
    m_WriteTimeValue: bpy.props.BoolProperty(name='WriteTimeValue', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_BlockSize: bpy.props.IntProperty(name='BlockSize', default=32768) #type: ignore
    m_CompressionLevel: bpy.props.IntProperty(name='CompressionLevel', default=5) #type: ignore
    m_NumberOfGhostLevels: bpy.props.IntProperty(name='NumberOfGhostLevels', default=0) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="LittleEndian", items=e_ByteOrder_items) #type: ignore
    e_DataMode: bpy.props.EnumProperty(name='DataMode', default="Appended", items=e_DataMode_items) #type: ignore
    e_HeaderType: bpy.props.EnumProperty(name='HeaderType', default="UInt32", items=e_HeaderType_items) #type: ignore
    e_IdType: bpy.props.EnumProperty(name='IdType', default="Int64", items=e_IdType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteTimeValue','m_WriteToOutputString','m_FileName','m_BlockSize','m_CompressionLevel','m_NumberOfGhostLevels','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKXMLPartitionedDataSetWriter )        
TYPENAMES.append('VTKXMLPartitionedDataSetWriterType' )

#--------------------------------------------------------------
class VTKXMLPolyDataWriter(Node, PBVTK_Node):

    bl_idname = 'VTKXMLPolyDataWriterType'
    bl_label  = 'vtkXMLPolyDataWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData: bpy.props.BoolProperty(name='EncodeAppendedData', default=True) #type: ignore
    m_WriteTimeValue: bpy.props.BoolProperty(name='WriteTimeValue', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_BlockSize: bpy.props.IntProperty(name='BlockSize', default=32768) #type: ignore
    m_CompressionLevel: bpy.props.IntProperty(name='CompressionLevel', default=5) #type: ignore
    m_GhostLevel: bpy.props.IntProperty(name='GhostLevel', default=0) #type: ignore
    m_NumberOfPieces: bpy.props.IntProperty(name='NumberOfPieces', default=1) #type: ignore
    m_NumberOfTimeSteps: bpy.props.IntProperty(name='NumberOfTimeSteps', default=1) #type: ignore
    m_WritePiece: bpy.props.IntProperty(name='WritePiece', default=-1) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="LittleEndian", items=e_ByteOrder_items) #type: ignore
    e_DataMode: bpy.props.EnumProperty(name='DataMode', default="Appended", items=e_DataMode_items) #type: ignore
    e_HeaderType: bpy.props.EnumProperty(name='HeaderType', default="UInt32", items=e_HeaderType_items) #type: ignore
    e_IdType: bpy.props.EnumProperty(name='IdType', default="Int64", items=e_IdType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=14, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteTimeValue','m_WriteToOutputString','m_FileName','m_BlockSize','m_CompressionLevel','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_WritePiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKXMLPolyDataWriter )        
TYPENAMES.append('VTKXMLPolyDataWriterType' )

#--------------------------------------------------------------
class VTKXMLRectilinearGridWriter(Node, PBVTK_Node):

    bl_idname = 'VTKXMLRectilinearGridWriterType'
    bl_label  = 'vtkXMLRectilinearGridWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData: bpy.props.BoolProperty(name='EncodeAppendedData', default=True) #type: ignore
    m_WriteTimeValue: bpy.props.BoolProperty(name='WriteTimeValue', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_BlockSize: bpy.props.IntProperty(name='BlockSize', default=32768) #type: ignore
    m_CompressionLevel: bpy.props.IntProperty(name='CompressionLevel', default=5) #type: ignore
    m_GhostLevel: bpy.props.IntProperty(name='GhostLevel', default=0) #type: ignore
    m_NumberOfPieces: bpy.props.IntProperty(name='NumberOfPieces', default=1) #type: ignore
    m_NumberOfTimeSteps: bpy.props.IntProperty(name='NumberOfTimeSteps', default=1) #type: ignore
    m_WritePiece: bpy.props.IntProperty(name='WritePiece', default=-1) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="LittleEndian", items=e_ByteOrder_items) #type: ignore
    e_DataMode: bpy.props.EnumProperty(name='DataMode', default="Appended", items=e_DataMode_items) #type: ignore
    e_HeaderType: bpy.props.EnumProperty(name='HeaderType', default="UInt32", items=e_HeaderType_items) #type: ignore
    e_IdType: bpy.props.EnumProperty(name='IdType', default="Int64", items=e_IdType_items) #type: ignore
    m_WriteExtent: bpy.props.IntVectorProperty(name='WriteExtent', default=[0, -1, 0, -1, 0, -1], size=6) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteTimeValue','m_WriteToOutputString','m_FileName','m_BlockSize','m_CompressionLevel','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_WritePiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType','m_WriteExtent',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKXMLRectilinearGridWriter )        
TYPENAMES.append('VTKXMLRectilinearGridWriterType' )

#--------------------------------------------------------------
class VTKXMLStructuredGridWriter(Node, PBVTK_Node):

    bl_idname = 'VTKXMLStructuredGridWriterType'
    bl_label  = 'vtkXMLStructuredGridWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData: bpy.props.BoolProperty(name='EncodeAppendedData', default=True) #type: ignore
    m_WriteTimeValue: bpy.props.BoolProperty(name='WriteTimeValue', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_BlockSize: bpy.props.IntProperty(name='BlockSize', default=32768) #type: ignore
    m_CompressionLevel: bpy.props.IntProperty(name='CompressionLevel', default=5) #type: ignore
    m_GhostLevel: bpy.props.IntProperty(name='GhostLevel', default=0) #type: ignore
    m_NumberOfPieces: bpy.props.IntProperty(name='NumberOfPieces', default=1) #type: ignore
    m_NumberOfTimeSteps: bpy.props.IntProperty(name='NumberOfTimeSteps', default=1) #type: ignore
    m_WritePiece: bpy.props.IntProperty(name='WritePiece', default=-1) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="LittleEndian", items=e_ByteOrder_items) #type: ignore
    e_DataMode: bpy.props.EnumProperty(name='DataMode', default="Appended", items=e_DataMode_items) #type: ignore
    e_HeaderType: bpy.props.EnumProperty(name='HeaderType', default="UInt32", items=e_HeaderType_items) #type: ignore
    e_IdType: bpy.props.EnumProperty(name='IdType', default="Int64", items=e_IdType_items) #type: ignore
    m_WriteExtent: bpy.props.IntVectorProperty(name='WriteExtent', default=[0, -1, 0, -1, 0, -1], size=6) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteTimeValue','m_WriteToOutputString','m_FileName','m_BlockSize','m_CompressionLevel','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_WritePiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType','m_WriteExtent',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKXMLStructuredGridWriter )        
TYPENAMES.append('VTKXMLStructuredGridWriterType' )

#--------------------------------------------------------------
class VTKXMLTableWriter(Node, PBVTK_Node):

    bl_idname = 'VTKXMLTableWriterType'
    bl_label  = 'vtkXMLTableWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData: bpy.props.BoolProperty(name='EncodeAppendedData', default=True) #type: ignore
    m_WriteTimeValue: bpy.props.BoolProperty(name='WriteTimeValue', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_BlockSize: bpy.props.IntProperty(name='BlockSize', default=32768) #type: ignore
    m_CompressionLevel: bpy.props.IntProperty(name='CompressionLevel', default=5) #type: ignore
    m_NumberOfPieces: bpy.props.IntProperty(name='NumberOfPieces', default=1) #type: ignore
    m_NumberOfTimeSteps: bpy.props.IntProperty(name='NumberOfTimeSteps', default=1) #type: ignore
    m_WritePiece: bpy.props.IntProperty(name='WritePiece', default=-1) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="LittleEndian", items=e_ByteOrder_items) #type: ignore
    e_DataMode: bpy.props.EnumProperty(name='DataMode', default="Appended", items=e_DataMode_items) #type: ignore
    e_HeaderType: bpy.props.EnumProperty(name='HeaderType', default="UInt32", items=e_HeaderType_items) #type: ignore
    e_IdType: bpy.props.EnumProperty(name='IdType', default="Int64", items=e_IdType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteTimeValue','m_WriteToOutputString','m_FileName','m_BlockSize','m_CompressionLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_WritePiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKXMLTableWriter )        
TYPENAMES.append('VTKXMLTableWriterType' )

#--------------------------------------------------------------
class VTKXMLUniformGridAMRWriter(Node, PBVTK_Node):

    bl_idname = 'VTKXMLUniformGridAMRWriterType'
    bl_label  = 'vtkXMLUniformGridAMRWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData: bpy.props.BoolProperty(name='EncodeAppendedData', default=True) #type: ignore
    m_WriteTimeValue: bpy.props.BoolProperty(name='WriteTimeValue', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_BlockSize: bpy.props.IntProperty(name='BlockSize', default=32768) #type: ignore
    m_CompressionLevel: bpy.props.IntProperty(name='CompressionLevel', default=5) #type: ignore
    m_GhostLevel: bpy.props.IntProperty(name='GhostLevel', default=0) #type: ignore
    m_NumberOfTimeSteps: bpy.props.IntProperty(name='NumberOfTimeSteps', default=1) #type: ignore
    m_WriteMetaFile: bpy.props.IntProperty(name='WriteMetaFile', default=1) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="LittleEndian", items=e_ByteOrder_items) #type: ignore
    e_DataMode: bpy.props.EnumProperty(name='DataMode', default="Appended", items=e_DataMode_items) #type: ignore
    e_HeaderType: bpy.props.EnumProperty(name='HeaderType', default="UInt32", items=e_HeaderType_items) #type: ignore
    e_IdType: bpy.props.EnumProperty(name='IdType', default="Int64", items=e_IdType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteTimeValue','m_WriteToOutputString','m_FileName','m_BlockSize','m_CompressionLevel','m_GhostLevel','m_NumberOfTimeSteps','m_WriteMetaFile','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKXMLUniformGridAMRWriter )        
TYPENAMES.append('VTKXMLUniformGridAMRWriterType' )

#--------------------------------------------------------------
class VTKXMLUnstructuredGridWriter(Node, PBVTK_Node):

    bl_idname = 'VTKXMLUnstructuredGridWriterType'
    bl_label  = 'vtkXMLUnstructuredGridWriter'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataMode_items=[ (x,x,x) for x in ['Ascii', 'Binary', 'Appended']]
    e_HeaderType_items=[ (x,x,x) for x in ['UInt32', 'UInt64']]
    e_IdType_items=[ (x,x,x) for x in ['Int32', 'Int64']]
    
    m_EncodeAppendedData: bpy.props.BoolProperty(name='EncodeAppendedData', default=True) #type: ignore
    m_WriteTimeValue: bpy.props.BoolProperty(name='WriteTimeValue', default=True) #type: ignore
    m_WriteToOutputString: bpy.props.BoolProperty(name='WriteToOutputString', default=False) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_BlockSize: bpy.props.IntProperty(name='BlockSize', default=32768) #type: ignore
    m_CompressionLevel: bpy.props.IntProperty(name='CompressionLevel', default=5) #type: ignore
    m_GhostLevel: bpy.props.IntProperty(name='GhostLevel', default=0) #type: ignore
    m_NumberOfPieces: bpy.props.IntProperty(name='NumberOfPieces', default=1) #type: ignore
    m_NumberOfTimeSteps: bpy.props.IntProperty(name='NumberOfTimeSteps', default=1) #type: ignore
    m_WritePiece: bpy.props.IntProperty(name='WritePiece', default=-1) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="LittleEndian", items=e_ByteOrder_items) #type: ignore
    e_DataMode: bpy.props.EnumProperty(name='DataMode', default="Appended", items=e_DataMode_items) #type: ignore
    e_HeaderType: bpy.props.EnumProperty(name='HeaderType', default="UInt32", items=e_HeaderType_items) #type: ignore
    e_IdType: bpy.props.EnumProperty(name='IdType', default="Int64", items=e_IdType_items) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=14, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_EncodeAppendedData','m_WriteTimeValue','m_WriteToOutputString','m_FileName','m_BlockSize','m_CompressionLevel','m_GhostLevel','m_NumberOfPieces','m_NumberOfTimeSteps','m_WritePiece','e_ByteOrder','e_DataMode','e_HeaderType','e_IdType',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKXMLUnstructuredGridWriter )        
TYPENAMES.append('VTKXMLUnstructuredGridWriterType' )

#--------------------------------------------------------------
class VTKXdmfWriter(Node, PBVTK_Node):

    bl_idname = 'VTKXdmfWriterType'
    bl_label  = 'vtkXdmfWriter'
    
    m_MeshStaticOverTime: bpy.props.BoolProperty(name='MeshStaticOverTime', default=False) #type: ignore
    m_WriteAllTimeSteps: bpy.props.BoolProperty(name='WriteAllTimeSteps', default=True) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH') #type: ignore
    m_HeavyDataFileName: bpy.props.StringProperty(name='HeavyDataFileName', default="", subtype='FILE_PATH') #type: ignore
    m_HeavyDataGroupName: bpy.props.StringProperty(name='HeavyDataGroupName', default="") #type: ignore
    m_LightDataLimit: bpy.props.IntProperty(name='LightDataLimit', default=100) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_MeshStaticOverTime','m_WriteAllTimeSteps','m_FileName','m_HeavyDataFileName','m_HeavyDataGroupName','m_LightDataLimit',]
    def m_connections( self ):
        return (['VTK Input'], [], [], []) 
    
add_class( VTKXdmfWriter )        
TYPENAMES.append('VTKXdmfWriterType' )

#--------------------------------------------------------------
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( PBVTK_NodeCategory( 'Writer', 'Writer', items=menu_items) )