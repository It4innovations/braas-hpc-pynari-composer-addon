# Generated definitions for VTK class group: Reader
# VTK version: 9.5.2

from .core import *    
TYPENAMES = []

#--------------------------------------------------------------
class VTKAMREnzoParticlesReader(Node, PBVTK_Node):

    bl_idname = 'VTKAMREnzoParticlesReaderType'
    bl_label  = 'vtkAMREnzoParticlesReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilterLocation: bpy.props.BoolProperty(name='FilterLocation', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Frequency: bpy.props.IntProperty(name='Frequency', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ParticleType: bpy.props.IntProperty(name='ParticleType', default=-1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FilterLocation','m_FileName','m_ObjectName','m_Frequency','m_ParticleType',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAMREnzoParticlesReader )        
TYPENAMES.append('VTKAMREnzoParticlesReaderType' )

#--------------------------------------------------------------
class VTKAMREnzoReader(Node, PBVTK_Node):

    bl_idname = 'VTKAMREnzoReaderType'
    bl_label  = 'vtkAMREnzoReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ConvertToCGS: bpy.props.BoolProperty(name='ConvertToCGS', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableCaching: bpy.props.BoolProperty(name='EnableCaching', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ConvertToCGS','m_EnableCaching','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAMREnzoReader )        
TYPENAMES.append('VTKAMREnzoReaderType' )

#--------------------------------------------------------------
class VTKAMRFlashParticlesReader(Node, PBVTK_Node):

    bl_idname = 'VTKAMRFlashParticlesReaderType'
    bl_label  = 'vtkAMRFlashParticlesReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilterLocation: bpy.props.BoolProperty(name='FilterLocation', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Frequency: bpy.props.IntProperty(name='Frequency', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FilterLocation','m_FileName','m_ObjectName','m_Frequency',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAMRFlashParticlesReader )        
TYPENAMES.append('VTKAMRFlashParticlesReaderType' )

#--------------------------------------------------------------
class VTKAMRFlashReader(Node, PBVTK_Node):

    bl_idname = 'VTKAMRFlashReaderType'
    bl_label  = 'vtkAMRFlashReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableCaching: bpy.props.BoolProperty(name='EnableCaching', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableCaching','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAMRFlashReader )        
TYPENAMES.append('VTKAMRFlashReaderType' )

#--------------------------------------------------------------
class VTKAMRVelodyneReader(Node, PBVTK_Node):

    bl_idname = 'VTKAMRVelodyneReaderType'
    bl_label  = 'vtkAMRVelodyneReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableCaching: bpy.props.BoolProperty(name='EnableCaching', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableCaching','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAMRVelodyneReader )        
TYPENAMES.append('VTKAMRVelodyneReaderType' )

#--------------------------------------------------------------
class VTKAMReXGridReader(Node, PBVTK_Node):

    bl_idname = 'VTKAMReXGridReaderType'
    bl_label  = 'vtkAMReXGridReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableCaching: bpy.props.BoolProperty(name='EnableCaching', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableCaching','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAMReXGridReader )        
TYPENAMES.append('VTKAMReXGridReaderType' )

#--------------------------------------------------------------
class VTKAMReXParticlesReader(Node, PBVTK_Node):

    bl_idname = 'VTKAMReXParticlesReaderType'
    bl_label  = 'vtkAMReXParticlesReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ParticleType: bpy.props.StringProperty(name='ParticleType', default="particles", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PlotFileName: bpy.props.StringProperty(name='PlotFileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_ParticleType','m_PlotFileName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAMReXParticlesReader )        
TYPENAMES.append('VTKAMReXParticlesReaderType' )

#--------------------------------------------------------------
class VTKAVSucdReader(Node, PBVTK_Node):

    bl_idname = 'VTKAVSucdReaderType'
    bl_label  = 'vtkAVSucdReader'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BinaryFile: bpy.props.BoolProperty(name='BinaryFile', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="BigEndian", items=e_ByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_BinaryFile','m_FileName','m_ObjectName','e_ByteOrder',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAVSucdReader )        
TYPENAMES.append('VTKAVSucdReaderType' )

#--------------------------------------------------------------
class VTKArrayDataReader(Node, PBVTK_Node):

    bl_idname = 'VTKArrayDataReaderType'
    bl_label  = 'vtkArrayDataReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InputString: bpy.props.StringProperty(name='InputString', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadFromInputString','m_FileName','m_InputString','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKArrayDataReader )        
TYPENAMES.append('VTKArrayDataReaderType' )

#--------------------------------------------------------------
class VTKArrayReader(Node, PBVTK_Node):

    bl_idname = 'VTKArrayReaderType'
    bl_label  = 'vtkArrayReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InputString: bpy.props.StringProperty(name='InputString', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadFromInputString','m_FileName','m_InputString','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKArrayReader )        
TYPENAMES.append('VTKArrayReaderType' )

#--------------------------------------------------------------
class VTKAvmeshReader(Node, PBVTK_Node):

    bl_idname = 'VTKAvmeshReaderType'
    bl_label  = 'vtkAvmeshReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BuildConnectivityIteratively: bpy.props.BoolProperty(name='BuildConnectivityIteratively', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SurfaceOnly: bpy.props.BoolProperty(name='SurfaceOnly', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_BuildConnectivityIteratively','m_SurfaceOnly','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAvmeshReader )        
TYPENAMES.append('VTKAvmeshReaderType' )

#--------------------------------------------------------------
class VTKBMPReader(Node, PBVTK_Node):

    bl_idname = 'VTKBMPReaderType'
    bl_label  = 'vtkBMPReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Allow8BitBMP: bpy.props.BoolProperty(name='Allow8BitBMP', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileLowerLeft: bpy.props.BoolProperty(name='FileLowerLeft', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SwapBytes: bpy.props.BoolProperty(name='SwapBytes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarArrayName: bpy.props.StringProperty(name='ScalarArrayName', default="ImageFile", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataMask: bpy.props.IntProperty(name='DataMask', default=1000000000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileDimensionality: bpy.props.IntProperty(name='FileDimensionality', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceOffset: bpy.props.IntProperty(name='FileNameSliceOffset', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceSpacing: bpy.props.IntProperty(name='FileNameSliceSpacing', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HeaderSize: bpy.props.IntProperty(name='HeaderSize', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MemoryBufferLength: bpy.props.IntProperty(name='MemoryBufferLength', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfScalarComponents: bpy.props.IntProperty(name='NumberOfScalarComponents', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataByteOrder: bpy.props.EnumProperty(name='DataByteOrder', default="LittleEndian", items=e_DataByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataScalarType: bpy.props.EnumProperty(name='DataScalarType', default="Short", items=e_DataScalarType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataVOI: bpy.props.IntVectorProperty(name='DataVOI', default=[0, 0, 0, 0, 0, 0], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataOrigin: bpy.props.FloatVectorProperty(name='DataOrigin', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataSpacing: bpy.props.FloatVectorProperty(name='DataSpacing', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=21, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Allow8BitBMP','m_FileLowerLeft','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_ObjectName','m_ScalarArrayName','m_DataMask','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataVOI','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'Transform'], []) 
    
add_class( VTKBMPReader )        
TYPENAMES.append('VTKBMPReaderType' )

#--------------------------------------------------------------
class VTKBTSReader(Node, PBVTK_Node):

    bl_idname = 'VTKBTSReaderType'
    bl_label  = 'vtkBTSReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'Stream'], []) 
    
add_class( VTKBTSReader )        
TYPENAMES.append('VTKBTSReaderType' )

#--------------------------------------------------------------
class VTKBYUReader(Node, PBVTK_Node):

    bl_idname = 'VTKBYUReaderType'
    bl_label  = 'vtkBYUReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadDisplacement: bpy.props.BoolProperty(name='ReadDisplacement', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadScalar: bpy.props.BoolProperty(name='ReadScalar', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadTexture: bpy.props.BoolProperty(name='ReadTexture', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DisplacementFileName: bpy.props.StringProperty(name='DisplacementFileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GeometryFileName: bpy.props.StringProperty(name='GeometryFileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarFileName: bpy.props.StringProperty(name='ScalarFileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TextureFileName: bpy.props.StringProperty(name='TextureFileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PartNumber: bpy.props.IntProperty(name='PartNumber', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadDisplacement','m_ReadScalar','m_ReadTexture','m_DisplacementFileName','m_FileName','m_GeometryFileName','m_ObjectName','m_ScalarFileName','m_TextureFileName','m_PartNumber',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKBYUReader )        
TYPENAMES.append('VTKBYUReaderType' )

#--------------------------------------------------------------
class VTKBiomTableReader(Node, PBVTK_Node):

    bl_idname = 'VTKBiomTableReaderType'
    bl_label  = 'vtkBiomTableReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllColorScalars: bpy.props.BoolProperty(name='ReadAllColorScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllFields: bpy.props.BoolProperty(name='ReadAllFields', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllNormals: bpy.props.BoolProperty(name='ReadAllNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllScalars: bpy.props.BoolProperty(name='ReadAllScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTCoords: bpy.props.BoolProperty(name='ReadAllTCoords', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTensors: bpy.props.BoolProperty(name='ReadAllTensors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllVectors: bpy.props.BoolProperty(name='ReadAllVectors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ObjectName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'InputArray'], []) 
    
add_class( VTKBiomTableReader )        
TYPENAMES.append('VTKBiomTableReaderType' )

#--------------------------------------------------------------
class VTKCGNSFileSeriesReader(Node, PBVTK_Node):

    bl_idname = 'VTKCGNSFileSeriesReaderType'
    bl_label  = 'vtkCGNSFileSeriesReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IgnoreReaderTime: bpy.props.BoolProperty(name='IgnoreReaderTime', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_IgnoreReaderTime','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'Reader'], []) 
    
add_class( VTKCGNSFileSeriesReader )        
TYPENAMES.append('VTKCGNSFileSeriesReaderType' )

#--------------------------------------------------------------
class VTKCGNSReader(Node, PBVTK_Node):

    bl_idname = 'VTKCGNSReaderType'
    bl_label  = 'vtkCGNSReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CacheConnectivity: bpy.props.BoolProperty(name='CacheConnectivity', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CacheMesh: bpy.props.BoolProperty(name='CacheMesh', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CreateEachSolutionAsBlock: bpy.props.BoolProperty(name='CreateEachSolutionAsBlock', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DistributeBlocks: bpy.props.BoolProperty(name='DistributeBlocks', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DoublePrecisionMesh: bpy.props.BoolProperty(name='DoublePrecisionMesh', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IgnoreFlowSolutionPointers: bpy.props.BoolProperty(name='IgnoreFlowSolutionPointers', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LoadBndPatch: bpy.props.BoolProperty(name='LoadBndPatch', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LoadMesh: bpy.props.BoolProperty(name='LoadMesh', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LoadSurfacePatch: bpy.props.BoolProperty(name='LoadSurfacePatch', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Use3DVector: bpy.props.BoolProperty(name='Use3DVector', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseUnsteadyPattern: bpy.props.BoolProperty(name='UseUnsteadyPattern', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataLocation: bpy.props.IntProperty(name='DataLocation', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UnsteadySolutionStartTimestep: bpy.props.IntProperty(name='UnsteadySolutionStartTimestep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CacheConnectivity','m_CacheMesh','m_CreateEachSolutionAsBlock','m_DistributeBlocks','m_DoublePrecisionMesh','m_IgnoreFlowSolutionPointers','m_LoadBndPatch','m_LoadMesh','m_LoadSurfacePatch','m_Use3DVector','m_UseUnsteadyPattern','m_FileName','m_ObjectName','m_DataLocation','m_UnsteadySolutionStartTimestep',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCGNSReader )        
TYPENAMES.append('VTKCGNSReaderType' )

#--------------------------------------------------------------
class VTKCMLMoleculeReader(Node, PBVTK_Node):

    bl_idname = 'VTKCMLMoleculeReaderType'
    bl_label  = 'vtkCMLMoleculeReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCMLMoleculeReader )        
TYPENAMES.append('VTKCMLMoleculeReaderType' )

#--------------------------------------------------------------
class VTKCONVERGECFDCGNSReader(Node, PBVTK_Node):

    bl_idname = 'VTKCONVERGECFDCGNSReaderType'
    bl_label  = 'vtkCONVERGECFDCGNSReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCONVERGECFDCGNSReader )        
TYPENAMES.append('VTKCONVERGECFDCGNSReaderType' )

#--------------------------------------------------------------
class VTKCONVERGECFDReader(Node, PBVTK_Node):

    bl_idname = 'VTKCONVERGECFDReaderType'
    bl_label  = 'vtkCONVERGECFDReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCONVERGECFDReader )        
TYPENAMES.append('VTKCONVERGECFDReaderType' )

#--------------------------------------------------------------
class VTKCPExodusIIInSituReader(Node, PBVTK_Node):

    bl_idname = 'VTKCPExodusIIInSituReaderType'
    bl_label  = 'vtkCPExodusIIInSituReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CurrentTimeStep: bpy.props.IntProperty(name='CurrentTimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName','m_CurrentTimeStep',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCPExodusIIInSituReader )        
TYPENAMES.append('VTKCPExodusIIInSituReaderType' )

#--------------------------------------------------------------
class VTKCellGridReader(Node, PBVTK_Node):

    bl_idname = 'VTKCellGridReaderType'
    bl_label  = 'vtkCellGridReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCellGridReader )        
TYPENAMES.append('VTKCellGridReaderType' )

#--------------------------------------------------------------
class VTKCesium3DTilesReader(Node, PBVTK_Node):

    bl_idname = 'VTKCesium3DTilesReaderType'
    bl_label  = 'vtkCesium3DTilesReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Level: bpy.props.IntProperty(name='Level', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName','m_Level',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCesium3DTilesReader )        
TYPENAMES.append('VTKCesium3DTilesReaderType' )

#--------------------------------------------------------------
class VTKCesiumB3DMReader(Node, PBVTK_Node):

    bl_idname = 'VTKCesiumB3DMReaderType'
    bl_label  = 'vtkCesiumB3DMReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCesiumB3DMReader )        
TYPENAMES.append('VTKCesiumB3DMReaderType' )

#--------------------------------------------------------------
class VTKChacoGraphReader(Node, PBVTK_Node):

    bl_idname = 'VTKChacoGraphReaderType'
    bl_label  = 'vtkChacoGraphReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKChacoGraphReader )        
TYPENAMES.append('VTKChacoGraphReaderType' )

#--------------------------------------------------------------
class VTKChacoReader(Node, PBVTK_Node):

    bl_idname = 'VTKChacoReaderType'
    bl_label  = 'vtkChacoReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateEdgeWeightArrays: bpy.props.BoolProperty(name='GenerateEdgeWeightArrays', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateGlobalElementIdArray: bpy.props.BoolProperty(name='GenerateGlobalElementIdArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateGlobalNodeIdArray: bpy.props.BoolProperty(name='GenerateGlobalNodeIdArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateVertexWeightArrays: bpy.props.BoolProperty(name='GenerateVertexWeightArrays', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BaseName: bpy.props.StringProperty(name='BaseName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_GenerateEdgeWeightArrays','m_GenerateGlobalElementIdArray','m_GenerateGlobalNodeIdArray','m_GenerateVertexWeightArrays','m_BaseName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKChacoReader )        
TYPENAMES.append('VTKChacoReaderType' )

#--------------------------------------------------------------
class VTKCityGMLReader(Node, PBVTK_Node):

    bl_idname = 'VTKCityGMLReaderType'
    bl_label  = 'vtkCityGMLReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseTransparencyAsOpacity: bpy.props.BoolProperty(name='UseTransparencyAsOpacity', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BeginBuildingIndex: bpy.props.IntProperty(name='BeginBuildingIndex', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EndBuildingIndex: bpy.props.IntProperty(name='EndBuildingIndex', default=1000000000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LOD: bpy.props.IntProperty(name='LOD', default=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfBuildings: bpy.props.IntProperty(name='NumberOfBuildings', default=1000000000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_UseTransparencyAsOpacity','m_FileName','m_ObjectName','m_BeginBuildingIndex','m_EndBuildingIndex','m_LOD','m_NumberOfBuildings',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCityGMLReader )        
TYPENAMES.append('VTKCityGMLReaderType' )

#--------------------------------------------------------------
class VTKCompositeCellGridReader(Node, PBVTK_Node):

    bl_idname = 'VTKCompositeCellGridReaderType'
    bl_label  = 'vtkCompositeCellGridReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCompositeCellGridReader )        
TYPENAMES.append('VTKCompositeCellGridReaderType' )

#--------------------------------------------------------------
class VTKCompositeDataReader(Node, PBVTK_Node):

    bl_idname = 'VTKCompositeDataReaderType'
    bl_label  = 'vtkCompositeDataReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllColorScalars: bpy.props.BoolProperty(name='ReadAllColorScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllFields: bpy.props.BoolProperty(name='ReadAllFields', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllNormals: bpy.props.BoolProperty(name='ReadAllNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllScalars: bpy.props.BoolProperty(name='ReadAllScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTCoords: bpy.props.BoolProperty(name='ReadAllTCoords', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTensors: bpy.props.BoolProperty(name='ReadAllTensors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllVectors: bpy.props.BoolProperty(name='ReadAllVectors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ObjectName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'InputArray'], []) 
    
add_class( VTKCompositeDataReader )        
TYPENAMES.append('VTKCompositeDataReaderType' )

#--------------------------------------------------------------
class VTKDEMReader(Node, PBVTK_Node):

    bl_idname = 'VTKDEMReaderType'
    bl_label  = 'vtkDEMReader'
    e_ElevationReference_items=[ (x,x,x) for x in ['SeaLevel', 'ElevationBounds']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ElevationReference: bpy.props.EnumProperty(name='ElevationReference', default="ElevationBounds", items=e_ElevationReference_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName','e_ElevationReference',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKDEMReader )        
TYPENAMES.append('VTKDEMReaderType' )

#--------------------------------------------------------------
class VTKDICOMImageReader(Node, PBVTK_Node):

    bl_idname = 'VTKDICOMImageReaderType'
    bl_label  = 'vtkDICOMImageReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileLowerLeft: bpy.props.BoolProperty(name='FileLowerLeft', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SwapBytes: bpy.props.BoolProperty(name='SwapBytes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DirectoryName: bpy.props.StringProperty(name='DirectoryName', default="", subtype='DIR_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileDimensionality: bpy.props.IntProperty(name='FileDimensionality', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceOffset: bpy.props.IntProperty(name='FileNameSliceOffset', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceSpacing: bpy.props.IntProperty(name='FileNameSliceSpacing', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HeaderSize: bpy.props.IntProperty(name='HeaderSize', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MemoryBufferLength: bpy.props.IntProperty(name='MemoryBufferLength', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfScalarComponents: bpy.props.IntProperty(name='NumberOfScalarComponents', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataByteOrder: bpy.props.EnumProperty(name='DataByteOrder', default="LittleEndian", items=e_DataByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataScalarType: bpy.props.EnumProperty(name='DataScalarType', default="Short", items=e_DataScalarType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataOrigin: bpy.props.FloatVectorProperty(name='DataOrigin', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataSpacing: bpy.props.FloatVectorProperty(name='DataSpacing', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileLowerLeft','m_SwapBytes','m_DirectoryName','m_FileName','m_FilePattern','m_FilePrefix','m_ObjectName','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKDICOMImageReader )        
TYPENAMES.append('VTKDICOMImageReaderType' )

#--------------------------------------------------------------
class VTKDIMACSGraphReader(Node, PBVTK_Node):

    bl_idname = 'VTKDIMACSGraphReaderType'
    bl_label  = 'vtkDIMACSGraphReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EdgeAttributeArrayName: bpy.props.StringProperty(name='EdgeAttributeArrayName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VertexAttributeArrayName: bpy.props.StringProperty(name='VertexAttributeArrayName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EdgeAttributeArrayName','m_FileName','m_ObjectName','m_VertexAttributeArrayName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKDIMACSGraphReader )        
TYPENAMES.append('VTKDIMACSGraphReaderType' )

#--------------------------------------------------------------
class VTKDataObjectReader(Node, PBVTK_Node):

    bl_idname = 'VTKDataObjectReaderType'
    bl_label  = 'vtkDataObjectReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllColorScalars: bpy.props.BoolProperty(name='ReadAllColorScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllFields: bpy.props.BoolProperty(name='ReadAllFields', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllNormals: bpy.props.BoolProperty(name='ReadAllNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllScalars: bpy.props.BoolProperty(name='ReadAllScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTCoords: bpy.props.BoolProperty(name='ReadAllTCoords', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTensors: bpy.props.BoolProperty(name='ReadAllTensors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllVectors: bpy.props.BoolProperty(name='ReadAllVectors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ObjectName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'InputArray'], []) 
    
add_class( VTKDataObjectReader )        
TYPENAMES.append('VTKDataObjectReaderType' )

#--------------------------------------------------------------
class VTKDataReader(Node, PBVTK_Node):

    bl_idname = 'VTKDataReaderType'
    bl_label  = 'vtkDataReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllColorScalars: bpy.props.BoolProperty(name='ReadAllColorScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllFields: bpy.props.BoolProperty(name='ReadAllFields', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllNormals: bpy.props.BoolProperty(name='ReadAllNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllScalars: bpy.props.BoolProperty(name='ReadAllScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTCoords: bpy.props.BoolProperty(name='ReadAllTCoords', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTensors: bpy.props.BoolProperty(name='ReadAllTensors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllVectors: bpy.props.BoolProperty(name='ReadAllVectors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ObjectName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'InputArray'], []) 
    
add_class( VTKDataReader )        
TYPENAMES.append('VTKDataReaderType' )

#--------------------------------------------------------------
class VTKDataSetReader(Node, PBVTK_Node):

    bl_idname = 'VTKDataSetReaderType'
    bl_label  = 'vtkDataSetReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllColorScalars: bpy.props.BoolProperty(name='ReadAllColorScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllFields: bpy.props.BoolProperty(name='ReadAllFields', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllNormals: bpy.props.BoolProperty(name='ReadAllNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllScalars: bpy.props.BoolProperty(name='ReadAllScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTCoords: bpy.props.BoolProperty(name='ReadAllTCoords', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTensors: bpy.props.BoolProperty(name='ReadAllTensors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllVectors: bpy.props.BoolProperty(name='ReadAllVectors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ObjectName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'InputArray'], []) 
    
add_class( VTKDataSetReader )        
TYPENAMES.append('VTKDataSetReaderType' )

#--------------------------------------------------------------
class VTKDelimitedTextReader(Node, PBVTK_Node):

    bl_idname = 'VTKDelimitedTextReaderType'
    bl_label  = 'vtkDelimitedTextReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AddTabFieldDelimiter: bpy.props.BoolProperty(name='AddTabFieldDelimiter', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DetectNumericColumns: bpy.props.BoolProperty(name='DetectNumericColumns', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ForceDouble: bpy.props.BoolProperty(name='ForceDouble', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GeneratePedigreeIds: bpy.props.BoolProperty(name='GeneratePedigreeIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HaveHeaders: bpy.props.BoolProperty(name='HaveHeaders', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MergeConsecutiveDelimiters: bpy.props.BoolProperty(name='MergeConsecutiveDelimiters', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputPedigreeIds: bpy.props.BoolProperty(name='OutputPedigreeIds', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TrimWhitespacePriorToNumericConversion: bpy.props.BoolProperty(name='TrimWhitespacePriorToNumericConversion', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseStringDelimiter: bpy.props.BoolProperty(name='UseStringDelimiter', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CommentCharacters: bpy.props.StringProperty(name='CommentCharacters', default="#", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldDelimiterCharacters: bpy.props.StringProperty(name='FieldDelimiterCharacters', default=",", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PedigreeIdArrayName: bpy.props.StringProperty(name='PedigreeIdArrayName', default="id", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_StringDelimiter: bpy.props.StringProperty(name='StringDelimiter', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UTF8FieldDelimiters: bpy.props.StringProperty(name='UTF8FieldDelimiters', default=",", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UTF8RecordDelimiters: bpy.props.StringProperty(name='UTF8RecordDelimiters', default="\n", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UTF8StringDelimiters: bpy.props.StringProperty(name='UTF8StringDelimiters', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UnicodeCharacterSet: bpy.props.StringProperty(name='UnicodeCharacterSet', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DefaultIntegerValue: bpy.props.IntProperty(name='DefaultIntegerValue', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaxRecords: bpy.props.IntProperty(name='MaxRecords', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PreviewNumberOfLines: bpy.props.IntProperty(name='PreviewNumberOfLines', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReplacementCharacter: bpy.props.IntProperty(name='ReplacementCharacter', default=120, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SkippedRecords: bpy.props.IntProperty(name='SkippedRecords', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DefaultDoubleValue: bpy.props.FloatProperty(name='DefaultDoubleValue', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=27, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AddTabFieldDelimiter','m_DetectNumericColumns','m_ForceDouble','m_GeneratePedigreeIds','m_HaveHeaders','m_MergeConsecutiveDelimiters','m_OutputPedigreeIds','m_ReadFromInputString','m_TrimWhitespacePriorToNumericConversion','m_UseStringDelimiter','m_CommentCharacters','m_FieldDelimiterCharacters','m_FileName','m_ObjectName','m_PedigreeIdArrayName','m_StringDelimiter','m_UTF8FieldDelimiters','m_UTF8RecordDelimiters','m_UTF8StringDelimiters','m_UnicodeCharacterSet','m_DefaultIntegerValue','m_MaxRecords','m_PreviewNumberOfLines','m_ReplacementCharacter','m_SkippedRecords','m_DefaultDoubleValue',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKDelimitedTextReader )        
TYPENAMES.append('VTKDelimitedTextReaderType' )

#--------------------------------------------------------------
class VTKERFReader(Node, PBVTK_Node):

    bl_idname = 'VTKERFReaderType'
    bl_label  = 'vtkERFReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKERFReader )        
TYPENAMES.append('VTKERFReaderType' )

#--------------------------------------------------------------
class VTKEnSight6BinaryReader(Node, PBVTK_Node):

    bl_idname = 'VTKEnSight6BinaryReaderType'
    bl_label  = 'vtkEnSight6BinaryReader'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ApplyTetrahedralize: bpy.props.BoolProperty(name='ApplyTetrahedralize', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ParticleCoordinatesByIndex: bpy.props.BoolProperty(name='ParticleCoordinatesByIndex', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllVariables: bpy.props.BoolProperty(name='ReadAllVariables', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CaseFileName: bpy.props.StringProperty(name='CaseFileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePath: bpy.props.StringProperty(name='FilePath', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeValue: bpy.props.FloatProperty(name='TimeValue', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="BigEndian", items=e_ByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ApplyTetrahedralize','m_ParticleCoordinatesByIndex','m_ReadAllVariables','m_CaseFileName','m_FilePath','m_ObjectName','m_TimeValue','e_ByteOrder',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKEnSight6BinaryReader )        
TYPENAMES.append('VTKEnSight6BinaryReaderType' )

#--------------------------------------------------------------
class VTKEnSight6Reader(Node, PBVTK_Node):

    bl_idname = 'VTKEnSight6ReaderType'
    bl_label  = 'vtkEnSight6Reader'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ApplyTetrahedralize: bpy.props.BoolProperty(name='ApplyTetrahedralize', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ParticleCoordinatesByIndex: bpy.props.BoolProperty(name='ParticleCoordinatesByIndex', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllVariables: bpy.props.BoolProperty(name='ReadAllVariables', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CaseFileName: bpy.props.StringProperty(name='CaseFileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePath: bpy.props.StringProperty(name='FilePath', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeValue: bpy.props.FloatProperty(name='TimeValue', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="BigEndian", items=e_ByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ApplyTetrahedralize','m_ParticleCoordinatesByIndex','m_ReadAllVariables','m_CaseFileName','m_FilePath','m_ObjectName','m_TimeValue','e_ByteOrder',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKEnSight6Reader )        
TYPENAMES.append('VTKEnSight6ReaderType' )

#--------------------------------------------------------------
class VTKEnSightGoldBinaryReader(Node, PBVTK_Node):

    bl_idname = 'VTKEnSightGoldBinaryReaderType'
    bl_label  = 'vtkEnSightGoldBinaryReader'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ApplyTetrahedralize: bpy.props.BoolProperty(name='ApplyTetrahedralize', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ParticleCoordinatesByIndex: bpy.props.BoolProperty(name='ParticleCoordinatesByIndex', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllVariables: bpy.props.BoolProperty(name='ReadAllVariables', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CaseFileName: bpy.props.StringProperty(name='CaseFileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePath: bpy.props.StringProperty(name='FilePath', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeValue: bpy.props.FloatProperty(name='TimeValue', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="BigEndian", items=e_ByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ApplyTetrahedralize','m_ParticleCoordinatesByIndex','m_ReadAllVariables','m_CaseFileName','m_FilePath','m_ObjectName','m_TimeValue','e_ByteOrder',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKEnSightGoldBinaryReader )        
TYPENAMES.append('VTKEnSightGoldBinaryReaderType' )

#--------------------------------------------------------------
class VTKEnSightGoldCombinedReader(Node, PBVTK_Node):

    bl_idname = 'VTKEnSightGoldCombinedReaderType'
    bl_label  = 'vtkEnSightGoldCombinedReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PartOfSOSFile: bpy.props.BoolProperty(name='PartOfSOSFile', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CaseFileName: bpy.props.StringProperty(name='CaseFileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePath: bpy.props.StringProperty(name='FilePath', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeValue: bpy.props.FloatProperty(name='TimeValue', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_PartOfSOSFile','m_CaseFileName','m_FilePath','m_ObjectName','m_TimeValue',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKEnSightGoldCombinedReader )        
TYPENAMES.append('VTKEnSightGoldCombinedReaderType' )

#--------------------------------------------------------------
class VTKEnSightGoldReader(Node, PBVTK_Node):

    bl_idname = 'VTKEnSightGoldReaderType'
    bl_label  = 'vtkEnSightGoldReader'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ApplyTetrahedralize: bpy.props.BoolProperty(name='ApplyTetrahedralize', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ParticleCoordinatesByIndex: bpy.props.BoolProperty(name='ParticleCoordinatesByIndex', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllVariables: bpy.props.BoolProperty(name='ReadAllVariables', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CaseFileName: bpy.props.StringProperty(name='CaseFileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePath: bpy.props.StringProperty(name='FilePath', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeValue: bpy.props.FloatProperty(name='TimeValue', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="BigEndian", items=e_ByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ApplyTetrahedralize','m_ParticleCoordinatesByIndex','m_ReadAllVariables','m_CaseFileName','m_FilePath','m_ObjectName','m_TimeValue','e_ByteOrder',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKEnSightGoldReader )        
TYPENAMES.append('VTKEnSightGoldReaderType' )

#--------------------------------------------------------------
class VTKEnSightMasterServerReader(Node, PBVTK_Node):

    bl_idname = 'VTKEnSightMasterServerReaderType'
    bl_label  = 'vtkEnSightMasterServerReader'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ApplyTetrahedralize: bpy.props.BoolProperty(name='ApplyTetrahedralize', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ParticleCoordinatesByIndex: bpy.props.BoolProperty(name='ParticleCoordinatesByIndex', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllVariables: bpy.props.BoolProperty(name='ReadAllVariables', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CaseFileName: bpy.props.StringProperty(name='CaseFileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePath: bpy.props.StringProperty(name='FilePath', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CurrentPiece: bpy.props.IntProperty(name='CurrentPiece', default=-1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeValue: bpy.props.FloatProperty(name='TimeValue', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="BigEndian", items=e_ByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ApplyTetrahedralize','m_ParticleCoordinatesByIndex','m_ReadAllVariables','m_CaseFileName','m_FilePath','m_ObjectName','m_CurrentPiece','m_TimeValue','e_ByteOrder',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKEnSightMasterServerReader )        
TYPENAMES.append('VTKEnSightMasterServerReaderType' )

#--------------------------------------------------------------
class VTKEnSightSOSGoldReader(Node, PBVTK_Node):

    bl_idname = 'VTKEnSightSOSGoldReaderType'
    bl_label  = 'vtkEnSightSOSGoldReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CaseFileName: bpy.props.StringProperty(name='CaseFileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CaseFileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKEnSightSOSGoldReader )        
TYPENAMES.append('VTKEnSightSOSGoldReaderType' )

#--------------------------------------------------------------
class VTKExodusIIReader(Node, PBVTK_Node):

    bl_idname = 'VTKExodusIIReaderType'
    bl_label  = 'vtkExodusIIReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AnimateModeShapes: bpy.props.BoolProperty(name='AnimateModeShapes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ApplyDisplacements: bpy.props.BoolProperty(name='ApplyDisplacements', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateFileIdArray: bpy.props.BoolProperty(name='GenerateFileIdArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateGlobalElementIdArray: bpy.props.BoolProperty(name='GenerateGlobalElementIdArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateGlobalNodeIdArray: bpy.props.BoolProperty(name='GenerateGlobalNodeIdArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateImplicitElementIdArray: bpy.props.BoolProperty(name='GenerateImplicitElementIdArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateImplicitNodeIdArray: bpy.props.BoolProperty(name='GenerateImplicitNodeIdArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateObjectIdCellArray: bpy.props.BoolProperty(name='GenerateObjectIdCellArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HasModeShapes: bpy.props.BoolProperty(name='HasModeShapes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IgnoreFileTime: bpy.props.BoolProperty(name='IgnoreFileTime', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SqueezePoints: bpy.props.BoolProperty(name='SqueezePoints', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseLegacyBlockNames: bpy.props.BoolProperty(name='UseLegacyBlockNames', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_XMLFileName: bpy.props.StringProperty(name='XMLFileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DisplayType: bpy.props.IntProperty(name='DisplayType', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileId: bpy.props.IntProperty(name='FileId', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CacheSize: bpy.props.FloatProperty(name='CacheSize', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DisplacementMagnitude: bpy.props.FloatProperty(name='DisplacementMagnitude', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ModeShapeTime: bpy.props.FloatProperty(name='ModeShapeTime', default=-1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=22, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AnimateModeShapes','m_ApplyDisplacements','m_GenerateFileIdArray','m_GenerateGlobalElementIdArray','m_GenerateGlobalNodeIdArray','m_GenerateImplicitElementIdArray','m_GenerateImplicitNodeIdArray','m_GenerateObjectIdCellArray','m_HasModeShapes','m_IgnoreFileTime','m_SqueezePoints','m_UseLegacyBlockNames','m_FileName','m_ObjectName','m_XMLFileName','m_DisplayType','m_FileId','m_TimeStep','m_CacheSize','m_DisplacementMagnitude','m_ModeShapeTime',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExodusIIReader )        
TYPENAMES.append('VTKExodusIIReaderType' )

#--------------------------------------------------------------
class VTKFDSReader(Node, PBVTK_Node):

    bl_idname = 'VTKFDSReaderType'
    bl_label  = 'vtkFDSReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeTolerance: bpy.props.FloatProperty(name='TimeTolerance', default=1e-05, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName','m_TimeTolerance',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'Stream'], []) 
    
add_class( VTKFDSReader )        
TYPENAMES.append('VTKFDSReaderType' )

#--------------------------------------------------------------
class VTKFLUENTCFFReader(Node, PBVTK_Node):

    bl_idname = 'VTKFLUENTCFFReaderType'
    bl_label  = 'vtkFLUENTCFFReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKFLUENTCFFReader )        
TYPENAMES.append('VTKFLUENTCFFReaderType' )

#--------------------------------------------------------------
class VTKFLUENTReader(Node, PBVTK_Node):

    bl_idname = 'VTKFLUENTReaderType'
    bl_label  = 'vtkFLUENTReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CacheData: bpy.props.BoolProperty(name='CacheData', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataByteOrder: bpy.props.EnumProperty(name='DataByteOrder', default="LittleEndian", items=e_DataByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CacheData','m_FileName','m_ObjectName','e_DataByteOrder',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKFLUENTReader )        
TYPENAMES.append('VTKFLUENTReaderType' )

#--------------------------------------------------------------
class VTKFacetReader(Node, PBVTK_Node):

    bl_idname = 'VTKFacetReaderType'
    bl_label  = 'vtkFacetReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKFacetReader )        
TYPENAMES.append('VTKFacetReaderType' )

#--------------------------------------------------------------
class VTKFixedWidthTextReader(Node, PBVTK_Node):

    bl_idname = 'VTKFixedWidthTextReaderType'
    bl_label  = 'vtkFixedWidthTextReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HaveHeaders: bpy.props.BoolProperty(name='HaveHeaders', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_StripWhiteSpace: bpy.props.BoolProperty(name='StripWhiteSpace', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldWidth: bpy.props.IntProperty(name='FieldWidth', default=10, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_HaveHeaders','m_StripWhiteSpace','m_FileName','m_ObjectName','m_FieldWidth',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'TableErrorObserver'], []) 
    
add_class( VTKFixedWidthTextReader )        
TYPENAMES.append('VTKFixedWidthTextReaderType' )

#--------------------------------------------------------------
class VTKGAMBITReader(Node, PBVTK_Node):

    bl_idname = 'VTKGAMBITReaderType'
    bl_label  = 'vtkGAMBITReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKGAMBITReader )        
TYPENAMES.append('VTKGAMBITReaderType' )

#--------------------------------------------------------------
class VTKGESignaReader(Node, PBVTK_Node):

    bl_idname = 'VTKGESignaReaderType'
    bl_label  = 'vtkGESignaReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileLowerLeft: bpy.props.BoolProperty(name='FileLowerLeft', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SwapBytes: bpy.props.BoolProperty(name='SwapBytes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Date: bpy.props.StringProperty(name='Date', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ImageNumber: bpy.props.StringProperty(name='ImageNumber', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Modality: bpy.props.StringProperty(name='Modality', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PatientID: bpy.props.StringProperty(name='PatientID', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PatientName: bpy.props.StringProperty(name='PatientName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Series: bpy.props.StringProperty(name='Series', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Study: bpy.props.StringProperty(name='Study', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileDimensionality: bpy.props.IntProperty(name='FileDimensionality', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceOffset: bpy.props.IntProperty(name='FileNameSliceOffset', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceSpacing: bpy.props.IntProperty(name='FileNameSliceSpacing', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HeaderSize: bpy.props.IntProperty(name='HeaderSize', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MemoryBufferLength: bpy.props.IntProperty(name='MemoryBufferLength', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfScalarComponents: bpy.props.IntProperty(name='NumberOfScalarComponents', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataByteOrder: bpy.props.EnumProperty(name='DataByteOrder', default="LittleEndian", items=e_DataByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataScalarType: bpy.props.EnumProperty(name='DataScalarType', default="Short", items=e_DataScalarType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataOrigin: bpy.props.FloatVectorProperty(name='DataOrigin', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataSpacing: bpy.props.FloatVectorProperty(name='DataSpacing', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=24, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileLowerLeft','m_SwapBytes','m_Date','m_FileName','m_FilePattern','m_FilePrefix','m_ImageNumber','m_Modality','m_ObjectName','m_PatientID','m_PatientName','m_Series','m_Study','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKGESignaReader )        
TYPENAMES.append('VTKGESignaReaderType' )

#--------------------------------------------------------------
class VTKGLTFReader(Node, PBVTK_Node):

    bl_idname = 'VTKGLTFReaderType'
    bl_label  = 'vtkGLTFReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ApplyDeformationsToGeometry: bpy.props.BoolProperty(name='ApplyDeformationsToGeometry', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CurrentScene: bpy.props.IntProperty(name='CurrentScene', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FrameRate: bpy.props.IntProperty(name='FrameRate', default=60, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GLBStart: bpy.props.IntProperty(name='GLBStart', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ApplyDeformationsToGeometry','m_FileName','m_ObjectName','m_CurrentScene','m_FrameRate','m_GLBStart',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'Stream', 'URILoader'], []) 
    
add_class( VTKGLTFReader )        
TYPENAMES.append('VTKGLTFReaderType' )

#--------------------------------------------------------------
class VTKGaussianCubeReader(Node, PBVTK_Node):

    bl_idname = 'VTKGaussianCubeReaderType'
    bl_label  = 'vtkGaussianCubeReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BScale: bpy.props.FloatProperty(name='BScale', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HBScale: bpy.props.FloatProperty(name='HBScale', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName','m_BScale','m_HBScale',]
    def m_connections( self ):
        return ([], ['output 0', 'output 1'], ['ContainerAlgorithm'], []) 
    
add_class( VTKGaussianCubeReader )        
TYPENAMES.append('VTKGaussianCubeReaderType' )

#--------------------------------------------------------------
class VTKGaussianCubeReader2(Node, PBVTK_Node):

    bl_idname = 'VTKGaussianCubeReader2Type'
    bl_label  = 'vtkGaussianCubeReader2'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output 0', 'output 1'], ['ContainerAlgorithm'], []) 
    
add_class( VTKGaussianCubeReader2 )        
TYPENAMES.append('VTKGaussianCubeReader2Type' )

#--------------------------------------------------------------
class VTKGenericDataObjectReader(Node, PBVTK_Node):

    bl_idname = 'VTKGenericDataObjectReaderType'
    bl_label  = 'vtkGenericDataObjectReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllColorScalars: bpy.props.BoolProperty(name='ReadAllColorScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllFields: bpy.props.BoolProperty(name='ReadAllFields', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllNormals: bpy.props.BoolProperty(name='ReadAllNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllScalars: bpy.props.BoolProperty(name='ReadAllScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTCoords: bpy.props.BoolProperty(name='ReadAllTCoords', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTensors: bpy.props.BoolProperty(name='ReadAllTensors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllVectors: bpy.props.BoolProperty(name='ReadAllVectors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ObjectName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'InputArray'], []) 
    
add_class( VTKGenericDataObjectReader )        
TYPENAMES.append('VTKGenericDataObjectReaderType' )

#--------------------------------------------------------------
class VTKGenericEnSightReader(Node, PBVTK_Node):

    bl_idname = 'VTKGenericEnSightReaderType'
    bl_label  = 'vtkGenericEnSightReader'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ApplyTetrahedralize: bpy.props.BoolProperty(name='ApplyTetrahedralize', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ParticleCoordinatesByIndex: bpy.props.BoolProperty(name='ParticleCoordinatesByIndex', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllVariables: bpy.props.BoolProperty(name='ReadAllVariables', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CaseFileName: bpy.props.StringProperty(name='CaseFileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePath: bpy.props.StringProperty(name='FilePath', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeValue: bpy.props.FloatProperty(name='TimeValue', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="BigEndian", items=e_ByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ApplyTetrahedralize','m_ParticleCoordinatesByIndex','m_ReadAllVariables','m_CaseFileName','m_FilePath','m_ObjectName','m_TimeValue','e_ByteOrder',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKGenericEnSightReader )        
TYPENAMES.append('VTKGenericEnSightReaderType' )

#--------------------------------------------------------------
class VTKGeoJSONReader(Node, PBVTK_Node):

    bl_idname = 'VTKGeoJSONReaderType'
    bl_label  = 'vtkGeoJSONReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutlinePolygons: bpy.props.BoolProperty(name='OutlinePolygons', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_StringInputMode: bpy.props.BoolProperty(name='StringInputMode', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TriangulatePolygons: bpy.props.BoolProperty(name='TriangulatePolygons', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SerializedPropertiesArrayName: bpy.props.StringProperty(name='SerializedPropertiesArrayName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_StringInput: bpy.props.StringProperty(name='StringInput', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_OutlinePolygons','m_StringInputMode','m_TriangulatePolygons','m_FileName','m_ObjectName','m_SerializedPropertiesArrayName','m_StringInput',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKGeoJSONReader )        
TYPENAMES.append('VTKGeoJSONReaderType' )

#--------------------------------------------------------------
class VTKGraphReader(Node, PBVTK_Node):

    bl_idname = 'VTKGraphReaderType'
    bl_label  = 'vtkGraphReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllColorScalars: bpy.props.BoolProperty(name='ReadAllColorScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllFields: bpy.props.BoolProperty(name='ReadAllFields', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllNormals: bpy.props.BoolProperty(name='ReadAllNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllScalars: bpy.props.BoolProperty(name='ReadAllScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTCoords: bpy.props.BoolProperty(name='ReadAllTCoords', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTensors: bpy.props.BoolProperty(name='ReadAllTensors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllVectors: bpy.props.BoolProperty(name='ReadAllVectors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ObjectName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'InputArray'], []) 
    
add_class( VTKGraphReader )        
TYPENAMES.append('VTKGraphReaderType' )

#--------------------------------------------------------------
class VTKH5PartReader(Node, PBVTK_Node):

    bl_idname = 'VTKH5PartReaderType'
    bl_label  = 'vtkH5PartReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CombineVectorComponents: bpy.props.BoolProperty(name='CombineVectorComponents', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateVertexCells: bpy.props.BoolProperty(name='GenerateVertexCells', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaskOutOfTimeRangeOutput: bpy.props.BoolProperty(name='MaskOutOfTimeRangeOutput', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Xarray: bpy.props.StringProperty(name='Xarray', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Yarray: bpy.props.StringProperty(name='Yarray', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Zarray: bpy.props.StringProperty(name='Zarray', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CombineVectorComponents','m_GenerateVertexCells','m_MaskOutOfTimeRangeOutput','m_FileName','m_ObjectName','m_Xarray','m_Yarray','m_Zarray',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKH5PartReader )        
TYPENAMES.append('VTKH5PartReaderType' )

#--------------------------------------------------------------
class VTKH5RageReader(Node, PBVTK_Node):

    bl_idname = 'VTKH5RageReaderType'
    bl_label  = 'vtkH5RageReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CurrentTimeStep: bpy.props.IntProperty(name='CurrentTimeStep', default=-1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName','m_CurrentTimeStep',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKH5RageReader )        
TYPENAMES.append('VTKH5RageReaderType' )

#--------------------------------------------------------------
class VTKHDFReader(Node, PBVTK_Node):

    bl_idname = 'VTKHDFReaderType'
    bl_label  = 'vtkHDFReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MergeParts: bpy.props.BoolProperty(name='MergeParts', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseCache: bpy.props.BoolProperty(name='UseCache', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumLevelsToReadByDefaultForAMR: bpy.props.IntProperty(name='MaximumLevelsToReadByDefaultForAMR', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Step: bpy.props.IntProperty(name='Step', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_MergeParts','m_UseCache','m_FileName','m_ObjectName','m_MaximumLevelsToReadByDefaultForAMR','m_Step',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHDFReader )        
TYPENAMES.append('VTKHDFReaderType' )

#--------------------------------------------------------------
class VTKHDRReader(Node, PBVTK_Node):

    bl_idname = 'VTKHDRReaderType'
    bl_label  = 'vtkHDRReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileLowerLeft: bpy.props.BoolProperty(name='FileLowerLeft', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SwapBytes: bpy.props.BoolProperty(name='SwapBytes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarArrayName: bpy.props.StringProperty(name='ScalarArrayName', default="ImageFile", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataMask: bpy.props.IntProperty(name='DataMask', default=1000000000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileDimensionality: bpy.props.IntProperty(name='FileDimensionality', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceOffset: bpy.props.IntProperty(name='FileNameSliceOffset', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceSpacing: bpy.props.IntProperty(name='FileNameSliceSpacing', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HeaderSize: bpy.props.IntProperty(name='HeaderSize', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MemoryBufferLength: bpy.props.IntProperty(name='MemoryBufferLength', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfScalarComponents: bpy.props.IntProperty(name='NumberOfScalarComponents', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataByteOrder: bpy.props.EnumProperty(name='DataByteOrder', default="LittleEndian", items=e_DataByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataScalarType: bpy.props.EnumProperty(name='DataScalarType', default="Short", items=e_DataScalarType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataVOI: bpy.props.IntVectorProperty(name='DataVOI', default=[0, 0, 0, 0, 0, 0], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataOrigin: bpy.props.FloatVectorProperty(name='DataOrigin', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataSpacing: bpy.props.FloatVectorProperty(name='DataSpacing', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=20, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileLowerLeft','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_ObjectName','m_ScalarArrayName','m_DataMask','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataVOI','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'Transform'], []) 
    
add_class( VTKHDRReader )        
TYPENAMES.append('VTKHDRReaderType' )

#--------------------------------------------------------------
class VTKIOSSReader(Node, PBVTK_Node):

    bl_idname = 'VTKIOSSReaderType'
    bl_label  = 'vtkIOSSReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ApplyDisplacements: bpy.props.BoolProperty(name='ApplyDisplacements', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Caching: bpy.props.BoolProperty(name='Caching', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ElementAndSideIds: bpy.props.BoolProperty(name='ElementAndSideIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateFileId: bpy.props.BoolProperty(name='GenerateFileId', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GroupNumericVectorFieldComponents: bpy.props.BoolProperty(name='GroupNumericVectorFieldComponents', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MergeExodusEntityBlocks: bpy.props.BoolProperty(name='MergeExodusEntityBlocks', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllFilesToDetermineStructure: bpy.props.BoolProperty(name='ReadAllFilesToDetermineStructure', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadGlobalFields: bpy.props.BoolProperty(name='ReadGlobalFields', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadIds: bpy.props.BoolProperty(name='ReadIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadQAAndInformationRecords: bpy.props.BoolProperty(name='ReadQAAndInformationRecords', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RemoveUnusedPoints: bpy.props.BoolProperty(name='RemoveUnusedPoints', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScanForRelatedFiles: bpy.props.BoolProperty(name='ScanForRelatedFiles', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DatabaseTypeOverride: bpy.props.StringProperty(name='DatabaseTypeOverride', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldSuffixSeparator: bpy.props.StringProperty(name='FieldSuffixSeparator', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="0", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Selector: bpy.props.StringProperty(name='Selector', default="0", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileStride: bpy.props.IntProperty(name='FileStride', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DisplacementMagnitude: bpy.props.FloatProperty(name='DisplacementMagnitude', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileRange: bpy.props.IntVectorProperty(name='FileRange', default=[0, -1], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=21, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ApplyDisplacements','m_Caching','m_ElementAndSideIds','m_GenerateFileId','m_GroupNumericVectorFieldComponents','m_MergeExodusEntityBlocks','m_ReadAllFilesToDetermineStructure','m_ReadGlobalFields','m_ReadIds','m_ReadQAAndInformationRecords','m_RemoveUnusedPoints','m_ScanForRelatedFiles','m_DatabaseTypeOverride','m_FieldSuffixSeparator','m_FileName','m_ObjectName','m_Selector','m_FileStride','m_DisplacementMagnitude','m_FileRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKIOSSReader )        
TYPENAMES.append('VTKIOSSReaderType' )

#--------------------------------------------------------------
class VTKISIReader(Node, PBVTK_Node):

    bl_idname = 'VTKISIReaderType'
    bl_label  = 'vtkISIReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Delimiter: bpy.props.StringProperty(name='Delimiter', default=";", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaxRecords: bpy.props.IntProperty(name='MaxRecords', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Delimiter','m_FileName','m_ObjectName','m_MaxRecords',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKISIReader )        
TYPENAMES.append('VTKISIReaderType' )

#--------------------------------------------------------------
class VTKImageReader(Node, PBVTK_Node):

    bl_idname = 'VTKImageReaderType'
    bl_label  = 'vtkImageReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileLowerLeft: bpy.props.BoolProperty(name='FileLowerLeft', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SwapBytes: bpy.props.BoolProperty(name='SwapBytes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarArrayName: bpy.props.StringProperty(name='ScalarArrayName', default="ImageFile", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataMask: bpy.props.IntProperty(name='DataMask', default=1000000000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileDimensionality: bpy.props.IntProperty(name='FileDimensionality', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceOffset: bpy.props.IntProperty(name='FileNameSliceOffset', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceSpacing: bpy.props.IntProperty(name='FileNameSliceSpacing', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HeaderSize: bpy.props.IntProperty(name='HeaderSize', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MemoryBufferLength: bpy.props.IntProperty(name='MemoryBufferLength', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfScalarComponents: bpy.props.IntProperty(name='NumberOfScalarComponents', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataByteOrder: bpy.props.EnumProperty(name='DataByteOrder', default="LittleEndian", items=e_DataByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataScalarType: bpy.props.EnumProperty(name='DataScalarType', default="Short", items=e_DataScalarType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataVOI: bpy.props.IntVectorProperty(name='DataVOI', default=[0, 0, 0, 0, 0, 0], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataOrigin: bpy.props.FloatVectorProperty(name='DataOrigin', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataSpacing: bpy.props.FloatVectorProperty(name='DataSpacing', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=20, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileLowerLeft','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_ObjectName','m_ScalarArrayName','m_DataMask','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataVOI','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'Transform'], []) 
    
add_class( VTKImageReader )        
TYPENAMES.append('VTKImageReaderType' )

#--------------------------------------------------------------
class VTKImageReader2(Node, PBVTK_Node):

    bl_idname = 'VTKImageReader2Type'
    bl_label  = 'vtkImageReader2'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileLowerLeft: bpy.props.BoolProperty(name='FileLowerLeft', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SwapBytes: bpy.props.BoolProperty(name='SwapBytes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileDimensionality: bpy.props.IntProperty(name='FileDimensionality', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceOffset: bpy.props.IntProperty(name='FileNameSliceOffset', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceSpacing: bpy.props.IntProperty(name='FileNameSliceSpacing', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HeaderSize: bpy.props.IntProperty(name='HeaderSize', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MemoryBufferLength: bpy.props.IntProperty(name='MemoryBufferLength', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfScalarComponents: bpy.props.IntProperty(name='NumberOfScalarComponents', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataByteOrder: bpy.props.EnumProperty(name='DataByteOrder', default="LittleEndian", items=e_DataByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataScalarType: bpy.props.EnumProperty(name='DataScalarType', default="Short", items=e_DataScalarType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataOrigin: bpy.props.FloatVectorProperty(name='DataOrigin', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataSpacing: bpy.props.FloatVectorProperty(name='DataSpacing', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=17, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileLowerLeft','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_ObjectName','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageReader2 )        
TYPENAMES.append('VTKImageReader2Type' )

#--------------------------------------------------------------
class VTKJPEGReader(Node, PBVTK_Node):

    bl_idname = 'VTKJPEGReaderType'
    bl_label  = 'vtkJPEGReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileLowerLeft: bpy.props.BoolProperty(name='FileLowerLeft', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SwapBytes: bpy.props.BoolProperty(name='SwapBytes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileDimensionality: bpy.props.IntProperty(name='FileDimensionality', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceOffset: bpy.props.IntProperty(name='FileNameSliceOffset', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceSpacing: bpy.props.IntProperty(name='FileNameSliceSpacing', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HeaderSize: bpy.props.IntProperty(name='HeaderSize', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MemoryBufferLength: bpy.props.IntProperty(name='MemoryBufferLength', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfScalarComponents: bpy.props.IntProperty(name='NumberOfScalarComponents', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataByteOrder: bpy.props.EnumProperty(name='DataByteOrder', default="LittleEndian", items=e_DataByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataScalarType: bpy.props.EnumProperty(name='DataScalarType', default="Short", items=e_DataScalarType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataOrigin: bpy.props.FloatVectorProperty(name='DataOrigin', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataSpacing: bpy.props.FloatVectorProperty(name='DataSpacing', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=17, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileLowerLeft','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_ObjectName','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKJPEGReader )        
TYPENAMES.append('VTKJPEGReaderType' )

#--------------------------------------------------------------
class VTKLANLX3DReader(Node, PBVTK_Node):

    bl_idname = 'VTKLANLX3DReaderType'
    bl_label  = 'vtkLANLX3DReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllPieces: bpy.props.BoolProperty(name='ReadAllPieces', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadAllPieces','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKLANLX3DReader )        
TYPENAMES.append('VTKLANLX3DReaderType' )

#--------------------------------------------------------------
class VTKLSDynaReader(Node, PBVTK_Node):

    bl_idname = 'VTKLSDynaReaderType'
    bl_label  = 'vtkLSDynaReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DeformedMesh: bpy.props.BoolProperty(name='DeformedMesh', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DeletedCellsAsGhostArray: bpy.props.BoolProperty(name='DeletedCellsAsGhostArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RemoveDeletedCells: bpy.props.BoolProperty(name='RemoveDeletedCells', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DatabaseDirectory: bpy.props.StringProperty(name='DatabaseDirectory', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="/d3plot", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InputDeck: bpy.props.StringProperty(name='InputDeck', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepRange: bpy.props.IntVectorProperty(name='TimeStepRange', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_DeformedMesh','m_DeletedCellsAsGhostArray','m_RemoveDeletedCells','m_DatabaseDirectory','m_FileName','m_InputDeck','m_ObjectName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKLSDynaReader )        
TYPENAMES.append('VTKLSDynaReaderType' )

#--------------------------------------------------------------
class VTKLegacyCellGridReader(Node, PBVTK_Node):

    bl_idname = 'VTKLegacyCellGridReaderType'
    bl_label  = 'vtkLegacyCellGridReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllColorScalars: bpy.props.BoolProperty(name='ReadAllColorScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllFields: bpy.props.BoolProperty(name='ReadAllFields', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllNormals: bpy.props.BoolProperty(name='ReadAllNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllScalars: bpy.props.BoolProperty(name='ReadAllScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTCoords: bpy.props.BoolProperty(name='ReadAllTCoords', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTensors: bpy.props.BoolProperty(name='ReadAllTensors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllVectors: bpy.props.BoolProperty(name='ReadAllVectors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ObjectName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'InputArray'], []) 
    
add_class( VTKLegacyCellGridReader )        
TYPENAMES.append('VTKLegacyCellGridReaderType' )

#--------------------------------------------------------------
class VTKMCubesReader(Node, PBVTK_Node):

    bl_idname = 'VTKMCubesReaderType'
    bl_label  = 'vtkMCubesReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FlipNormals: bpy.props.BoolProperty(name='FlipNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Normals: bpy.props.BoolProperty(name='Normals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SwapBytes: bpy.props.BoolProperty(name='SwapBytes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LimitsFileName: bpy.props.StringProperty(name='LimitsFileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HeaderSize: bpy.props.IntProperty(name='HeaderSize', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataByteOrder: bpy.props.EnumProperty(name='DataByteOrder', default="BigEndian", items=e_DataByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FlipNormals','m_Normals','m_SwapBytes','m_FileName','m_LimitsFileName','m_ObjectName','m_HeaderSize','e_DataByteOrder',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMCubesReader )        
TYPENAMES.append('VTKMCubesReaderType' )

#--------------------------------------------------------------
class VTKMFIXReader(Node, PBVTK_Node):

    bl_idname = 'VTKMFIXReaderType'
    bl_label  = 'vtkMFIXReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepRange: bpy.props.IntVectorProperty(name='TimeStepRange', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMFIXReader )        
TYPENAMES.append('VTKMFIXReaderType' )

#--------------------------------------------------------------
class VTKMINCImageReader(Node, PBVTK_Node):

    bl_idname = 'VTKMINCImageReaderType'
    bl_label  = 'vtkMINCImageReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileLowerLeft: bpy.props.BoolProperty(name='FileLowerLeft', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RescaleRealValues: bpy.props.BoolProperty(name='RescaleRealValues', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SwapBytes: bpy.props.BoolProperty(name='SwapBytes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileDimensionality: bpy.props.IntProperty(name='FileDimensionality', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceOffset: bpy.props.IntProperty(name='FileNameSliceOffset', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceSpacing: bpy.props.IntProperty(name='FileNameSliceSpacing', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HeaderSize: bpy.props.IntProperty(name='HeaderSize', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MemoryBufferLength: bpy.props.IntProperty(name='MemoryBufferLength', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfScalarComponents: bpy.props.IntProperty(name='NumberOfScalarComponents', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataByteOrder: bpy.props.EnumProperty(name='DataByteOrder', default="LittleEndian", items=e_DataByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataScalarType: bpy.props.EnumProperty(name='DataScalarType', default="Short", items=e_DataScalarType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataOrigin: bpy.props.FloatVectorProperty(name='DataOrigin', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataSpacing: bpy.props.FloatVectorProperty(name='DataSpacing', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=19, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileLowerLeft','m_RescaleRealValues','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_ObjectName','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','m_TimeStep','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMINCImageReader )        
TYPENAMES.append('VTKMINCImageReaderType' )

#--------------------------------------------------------------
class VTKMNIObjectReader(Node, PBVTK_Node):

    bl_idname = 'VTKMNIObjectReaderType'
    bl_label  = 'vtkMNIObjectReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMNIObjectReader )        
TYPENAMES.append('VTKMNIObjectReaderType' )

#--------------------------------------------------------------
class VTKMNITagPointReader(Node, PBVTK_Node):

    bl_idname = 'VTKMNITagPointReaderType'
    bl_label  = 'vtkMNITagPointReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output 0', 'output 1'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMNITagPointReader )        
TYPENAMES.append('VTKMNITagPointReaderType' )

#--------------------------------------------------------------
class VTKMNITransformReader(Node, PBVTK_Node):

    bl_idname = 'VTKMNITransformReaderType'
    bl_label  = 'vtkMNITransformReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], [], ['ContainerAlgorithm'], []) 
    
add_class( VTKMNITransformReader )        
TYPENAMES.append('VTKMNITransformReaderType' )

#--------------------------------------------------------------
class VTKMPASReader(Node, PBVTK_Node):

    bl_idname = 'VTKMPASReaderType'
    bl_label  = 'vtkMPASReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IsAtmosphere: bpy.props.BoolProperty(name='IsAtmosphere', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IsZeroCentered: bpy.props.BoolProperty(name='IsZeroCentered', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ProjectLatLon: bpy.props.BoolProperty(name='ProjectLatLon', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ShowMultilayerView: bpy.props.BoolProperty(name='ShowMultilayerView', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseDimensionedArrayNames: bpy.props.BoolProperty(name='UseDimensionedArrayNames', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VerticalDimension: bpy.props.StringProperty(name='VerticalDimension', default="nVertLevels", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LayerThickness: bpy.props.IntProperty(name='LayerThickness', default=10000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VerticalLevel: bpy.props.IntProperty(name='VerticalLevel', default=-1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_IsAtmosphere','m_IsZeroCentered','m_ProjectLatLon','m_ShowMultilayerView','m_UseDimensionedArrayNames','m_FileName','m_ObjectName','m_VerticalDimension','m_LayerThickness','m_VerticalLevel',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMPASReader )        
TYPENAMES.append('VTKMPASReaderType' )

#--------------------------------------------------------------
class VTKMRCReader(Node, PBVTK_Node):

    bl_idname = 'VTKMRCReaderType'
    bl_label  = 'vtkMRCReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMRCReader )        
TYPENAMES.append('VTKMRCReaderType' )

#--------------------------------------------------------------
class VTKMedicalImageReader2(Node, PBVTK_Node):

    bl_idname = 'VTKMedicalImageReader2Type'
    bl_label  = 'vtkMedicalImageReader2'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileLowerLeft: bpy.props.BoolProperty(name='FileLowerLeft', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SwapBytes: bpy.props.BoolProperty(name='SwapBytes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Date: bpy.props.StringProperty(name='Date', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ImageNumber: bpy.props.StringProperty(name='ImageNumber', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Modality: bpy.props.StringProperty(name='Modality', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PatientID: bpy.props.StringProperty(name='PatientID', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PatientName: bpy.props.StringProperty(name='PatientName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Series: bpy.props.StringProperty(name='Series', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Study: bpy.props.StringProperty(name='Study', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileDimensionality: bpy.props.IntProperty(name='FileDimensionality', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceOffset: bpy.props.IntProperty(name='FileNameSliceOffset', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceSpacing: bpy.props.IntProperty(name='FileNameSliceSpacing', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HeaderSize: bpy.props.IntProperty(name='HeaderSize', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MemoryBufferLength: bpy.props.IntProperty(name='MemoryBufferLength', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfScalarComponents: bpy.props.IntProperty(name='NumberOfScalarComponents', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataByteOrder: bpy.props.EnumProperty(name='DataByteOrder', default="LittleEndian", items=e_DataByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataScalarType: bpy.props.EnumProperty(name='DataScalarType', default="Short", items=e_DataScalarType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataOrigin: bpy.props.FloatVectorProperty(name='DataOrigin', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataSpacing: bpy.props.FloatVectorProperty(name='DataSpacing', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=24, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileLowerLeft','m_SwapBytes','m_Date','m_FileName','m_FilePattern','m_FilePrefix','m_ImageNumber','m_Modality','m_ObjectName','m_PatientID','m_PatientName','m_Series','m_Study','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMedicalImageReader2 )        
TYPENAMES.append('VTKMedicalImageReader2Type' )

#--------------------------------------------------------------
class VTKMetaImageReader(Node, PBVTK_Node):

    bl_idname = 'VTKMetaImageReaderType'
    bl_label  = 'vtkMetaImageReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileLowerLeft: bpy.props.BoolProperty(name='FileLowerLeft', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SwapBytes: bpy.props.BoolProperty(name='SwapBytes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileDimensionality: bpy.props.IntProperty(name='FileDimensionality', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceOffset: bpy.props.IntProperty(name='FileNameSliceOffset', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceSpacing: bpy.props.IntProperty(name='FileNameSliceSpacing', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HeaderSize: bpy.props.IntProperty(name='HeaderSize', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MemoryBufferLength: bpy.props.IntProperty(name='MemoryBufferLength', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfScalarComponents: bpy.props.IntProperty(name='NumberOfScalarComponents', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataByteOrder: bpy.props.EnumProperty(name='DataByteOrder', default="LittleEndian", items=e_DataByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataScalarType: bpy.props.EnumProperty(name='DataScalarType', default="Short", items=e_DataScalarType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataOrigin: bpy.props.FloatVectorProperty(name='DataOrigin', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataSpacing: bpy.props.FloatVectorProperty(name='DataSpacing', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=17, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileLowerLeft','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_ObjectName','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMetaImageReader )        
TYPENAMES.append('VTKMetaImageReaderType' )

#--------------------------------------------------------------
class VTKMotionFXCFGReader(Node, PBVTK_Node):

    bl_idname = 'VTKMotionFXCFGReaderType'
    bl_label  = 'vtkMotionFXCFGReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeResolution: bpy.props.IntProperty(name='TimeResolution', default=100, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName','m_TimeResolution',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMotionFXCFGReader )        
TYPENAMES.append('VTKMotionFXCFGReaderType' )

#--------------------------------------------------------------
class VTKMultiBlockPLOT3DReader(Node, PBVTK_Node):

    bl_idname = 'VTKMultiBlockPLOT3DReaderType'
    bl_label  = 'vtkMultiBlockPLOT3DReader'
    e_ByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AutoDetectFormat: bpy.props.BoolProperty(name='AutoDetectFormat', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BinaryFile: bpy.props.BoolProperty(name='BinaryFile', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DoublePrecision: bpy.props.BoolProperty(name='DoublePrecision', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ForceRead: bpy.props.BoolProperty(name='ForceRead', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HasByteCount: bpy.props.BoolProperty(name='HasByteCount', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IBlanking: bpy.props.BoolProperty(name='IBlanking', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MultiGrid: bpy.props.BoolProperty(name='MultiGrid', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PreserveIntermediateFunctions: bpy.props.BoolProperty(name='PreserveIntermediateFunctions', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TwoDimensionalGeometry: bpy.props.BoolProperty(name='TwoDimensionalGeometry', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FunctionFileName: bpy.props.StringProperty(name='FunctionFileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_QFileName: bpy.props.StringProperty(name='QFileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_XYZFileName: bpy.props.StringProperty(name='XYZFileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarFunctionNumber: bpy.props.IntProperty(name='ScalarFunctionNumber', default=100, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VectorFunctionNumber: bpy.props.IntProperty(name='VectorFunctionNumber', default=202, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Gamma: bpy.props.FloatProperty(name='Gamma', default=1.4, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_R: bpy.props.FloatProperty(name='R', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ByteOrder: bpy.props.EnumProperty(name='ByteOrder', default="BigEndian", items=e_ByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=20, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AutoDetectFormat','m_BinaryFile','m_DoublePrecision','m_ForceRead','m_HasByteCount','m_IBlanking','m_MultiGrid','m_PreserveIntermediateFunctions','m_TwoDimensionalGeometry','m_FileName','m_FunctionFileName','m_ObjectName','m_QFileName','m_XYZFileName','m_ScalarFunctionNumber','m_VectorFunctionNumber','m_Gamma','m_R','e_ByteOrder',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMultiBlockPLOT3DReader )        
TYPENAMES.append('VTKMultiBlockPLOT3DReaderType' )

#--------------------------------------------------------------
class VTKMultiNewickTreeReader(Node, PBVTK_Node):

    bl_idname = 'VTKMultiNewickTreeReaderType'
    bl_label  = 'vtkMultiNewickTreeReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllColorScalars: bpy.props.BoolProperty(name='ReadAllColorScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllFields: bpy.props.BoolProperty(name='ReadAllFields', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllNormals: bpy.props.BoolProperty(name='ReadAllNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllScalars: bpy.props.BoolProperty(name='ReadAllScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTCoords: bpy.props.BoolProperty(name='ReadAllTCoords', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTensors: bpy.props.BoolProperty(name='ReadAllTensors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllVectors: bpy.props.BoolProperty(name='ReadAllVectors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ObjectName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'InputArray'], []) 
    
add_class( VTKMultiNewickTreeReader )        
TYPENAMES.append('VTKMultiNewickTreeReaderType' )

#--------------------------------------------------------------
class VTKNIFTIImageReader(Node, PBVTK_Node):

    bl_idname = 'VTKNIFTIImageReaderType'
    bl_label  = 'vtkNIFTIImageReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileLowerLeft: bpy.props.BoolProperty(name='FileLowerLeft', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PlanarRGB: bpy.props.BoolProperty(name='PlanarRGB', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SwapBytes: bpy.props.BoolProperty(name='SwapBytes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeAsVector: bpy.props.BoolProperty(name='TimeAsVector', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileDimensionality: bpy.props.IntProperty(name='FileDimensionality', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceOffset: bpy.props.IntProperty(name='FileNameSliceOffset', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceSpacing: bpy.props.IntProperty(name='FileNameSliceSpacing', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HeaderSize: bpy.props.IntProperty(name='HeaderSize', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MemoryBufferLength: bpy.props.IntProperty(name='MemoryBufferLength', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfScalarComponents: bpy.props.IntProperty(name='NumberOfScalarComponents', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataByteOrder: bpy.props.EnumProperty(name='DataByteOrder', default="LittleEndian", items=e_DataByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataScalarType: bpy.props.EnumProperty(name='DataScalarType', default="Short", items=e_DataScalarType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataOrigin: bpy.props.FloatVectorProperty(name='DataOrigin', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataSpacing: bpy.props.FloatVectorProperty(name='DataSpacing', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=19, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileLowerLeft','m_PlanarRGB','m_SwapBytes','m_TimeAsVector','m_FileName','m_FilePattern','m_FilePrefix','m_ObjectName','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKNIFTIImageReader )        
TYPENAMES.append('VTKNIFTIImageReaderType' )

#--------------------------------------------------------------
class VTKNek5000Reader(Node, PBVTK_Node):

    bl_idname = 'VTKNek5000ReaderType'
    bl_label  = 'vtkNek5000Reader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CleanGrid: bpy.props.BoolProperty(name='CleanGrid', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SpectralElementIds: bpy.props.BoolProperty(name='SpectralElementIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataFileName: bpy.props.StringProperty(name='DataFileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepRange: bpy.props.IntVectorProperty(name='TimeStepRange', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CleanGrid','m_SpectralElementIds','m_DataFileName','m_FileName','m_ObjectName','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKNek5000Reader )        
TYPENAMES.append('VTKNek5000ReaderType' )

#--------------------------------------------------------------
class VTKNetCDFCFReader(Node, PBVTK_Node):

    bl_idname = 'VTKNetCDFCFReaderType'
    bl_label  = 'vtkNetCDFCFReader'
    e_OutputType_items=[ (x,x,x) for x in ['Automatic', 'Structured', 'Rectilinear', 'Unstructured', 'Image']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReplaceFillValueWithNan: bpy.props.BoolProperty(name='ReplaceFillValueWithNan', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SphericalCoordinates: bpy.props.BoolProperty(name='SphericalCoordinates', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LatitudeDimensionName: bpy.props.StringProperty(name='LatitudeDimensionName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LongitudeDimensionName: bpy.props.StringProperty(name='LongitudeDimensionName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeDimensionName: bpy.props.StringProperty(name='TimeDimensionName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VerticalDimensionName: bpy.props.StringProperty(name='VerticalDimensionName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VerticalBias: bpy.props.FloatProperty(name='VerticalBias', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VerticalScale: bpy.props.FloatProperty(name='VerticalScale', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_OutputType: bpy.props.EnumProperty(name='OutputType', default="Automatic", items=e_OutputType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReplaceFillValueWithNan','m_SphericalCoordinates','m_FileName','m_LatitudeDimensionName','m_LongitudeDimensionName','m_ObjectName','m_TimeDimensionName','m_VerticalDimensionName','m_VerticalBias','m_VerticalScale','e_OutputType',]
    def m_connections( self ):
        return ([], ['output'], ['Accessor', 'ContainerAlgorithm'], []) 
    
add_class( VTKNetCDFCFReader )        
TYPENAMES.append('VTKNetCDFCFReaderType' )

#--------------------------------------------------------------
class VTKNetCDFPOPReader(Node, PBVTK_Node):

    bl_idname = 'VTKNetCDFPOPReaderType'
    bl_label  = 'vtkNetCDFPOPReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Stride: bpy.props.IntVectorProperty(name='Stride', default=[1, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName','m_Stride',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKNetCDFPOPReader )        
TYPENAMES.append('VTKNetCDFPOPReaderType' )

#--------------------------------------------------------------
class VTKNetCDFReader(Node, PBVTK_Node):

    bl_idname = 'VTKNetCDFReaderType'
    bl_label  = 'vtkNetCDFReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReplaceFillValueWithNan: bpy.props.BoolProperty(name='ReplaceFillValueWithNan', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReplaceFillValueWithNan','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['Accessor', 'ContainerAlgorithm'], []) 
    
add_class( VTKNetCDFReader )        
TYPENAMES.append('VTKNetCDFReaderType' )

#--------------------------------------------------------------
class VTKNetCDFUGRIDReader(Node, PBVTK_Node):

    bl_idname = 'VTKNetCDFUGRIDReaderType'
    bl_label  = 'vtkNetCDFUGRIDReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReplaceFillValueWithNan: bpy.props.BoolProperty(name='ReplaceFillValueWithNan', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReplaceFillValueWithNan','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKNetCDFUGRIDReader )        
TYPENAMES.append('VTKNetCDFUGRIDReaderType' )

#--------------------------------------------------------------
class VTKNewickTreeReader(Node, PBVTK_Node):

    bl_idname = 'VTKNewickTreeReaderType'
    bl_label  = 'vtkNewickTreeReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllColorScalars: bpy.props.BoolProperty(name='ReadAllColorScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllFields: bpy.props.BoolProperty(name='ReadAllFields', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllNormals: bpy.props.BoolProperty(name='ReadAllNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllScalars: bpy.props.BoolProperty(name='ReadAllScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTCoords: bpy.props.BoolProperty(name='ReadAllTCoords', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTensors: bpy.props.BoolProperty(name='ReadAllTensors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllVectors: bpy.props.BoolProperty(name='ReadAllVectors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ObjectName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'InputArray'], []) 
    
add_class( VTKNewickTreeReader )        
TYPENAMES.append('VTKNewickTreeReaderType' )

#--------------------------------------------------------------
class VTKNrrdReader(Node, PBVTK_Node):

    bl_idname = 'VTKNrrdReaderType'
    bl_label  = 'vtkNrrdReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileLowerLeft: bpy.props.BoolProperty(name='FileLowerLeft', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SwapBytes: bpy.props.BoolProperty(name='SwapBytes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarArrayName: bpy.props.StringProperty(name='ScalarArrayName', default="ImageFile", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataMask: bpy.props.IntProperty(name='DataMask', default=1000000000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileDimensionality: bpy.props.IntProperty(name='FileDimensionality', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceOffset: bpy.props.IntProperty(name='FileNameSliceOffset', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceSpacing: bpy.props.IntProperty(name='FileNameSliceSpacing', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HeaderSize: bpy.props.IntProperty(name='HeaderSize', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MemoryBufferLength: bpy.props.IntProperty(name='MemoryBufferLength', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfScalarComponents: bpy.props.IntProperty(name='NumberOfScalarComponents', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataByteOrder: bpy.props.EnumProperty(name='DataByteOrder', default="LittleEndian", items=e_DataByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataScalarType: bpy.props.EnumProperty(name='DataScalarType', default="Short", items=e_DataScalarType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataVOI: bpy.props.IntVectorProperty(name='DataVOI', default=[0, 0, 0, 0, 0, 0], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataOrigin: bpy.props.FloatVectorProperty(name='DataOrigin', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataSpacing: bpy.props.FloatVectorProperty(name='DataSpacing', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=20, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileLowerLeft','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_ObjectName','m_ScalarArrayName','m_DataMask','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataVOI','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'Transform'], []) 
    
add_class( VTKNrrdReader )        
TYPENAMES.append('VTKNrrdReaderType' )

#--------------------------------------------------------------
class VTKOBJReader(Node, PBVTK_Node):

    bl_idname = 'VTKOBJReaderType'
    bl_label  = 'vtkOBJReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'Stream'], []) 
    
add_class( VTKOBJReader )        
TYPENAMES.append('VTKOBJReaderType' )

#--------------------------------------------------------------
class VTKOFFReader(Node, PBVTK_Node):

    bl_idname = 'VTKOFFReaderType'
    bl_label  = 'vtkOFFReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'Stream'], []) 
    
add_class( VTKOFFReader )        
TYPENAMES.append('VTKOFFReaderType' )

#--------------------------------------------------------------
class VTKOMETIFFReader(Node, PBVTK_Node):

    bl_idname = 'VTKOMETIFFReaderType'
    bl_label  = 'vtkOMETIFFReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileLowerLeft: bpy.props.BoolProperty(name='FileLowerLeft', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IgnoreColorMap: bpy.props.BoolProperty(name='IgnoreColorMap', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OriginSpecifiedFlag: bpy.props.BoolProperty(name='OriginSpecifiedFlag', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SpacingSpecifiedFlag: bpy.props.BoolProperty(name='SpacingSpecifiedFlag', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SwapBytes: bpy.props.BoolProperty(name='SwapBytes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileDimensionality: bpy.props.IntProperty(name='FileDimensionality', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceOffset: bpy.props.IntProperty(name='FileNameSliceOffset', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceSpacing: bpy.props.IntProperty(name='FileNameSliceSpacing', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HeaderSize: bpy.props.IntProperty(name='HeaderSize', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MemoryBufferLength: bpy.props.IntProperty(name='MemoryBufferLength', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfScalarComponents: bpy.props.IntProperty(name='NumberOfScalarComponents', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OrientationType: bpy.props.IntProperty(name='OrientationType', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataByteOrder: bpy.props.EnumProperty(name='DataByteOrder', default="LittleEndian", items=e_DataByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataScalarType: bpy.props.EnumProperty(name='DataScalarType', default="Short", items=e_DataScalarType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataOrigin: bpy.props.FloatVectorProperty(name='DataOrigin', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataSpacing: bpy.props.FloatVectorProperty(name='DataSpacing', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=21, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileLowerLeft','m_IgnoreColorMap','m_OriginSpecifiedFlag','m_SpacingSpecifiedFlag','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_ObjectName','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','m_OrientationType','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKOMETIFFReader )        
TYPENAMES.append('VTKOMETIFFReaderType' )

#--------------------------------------------------------------
class VTKOMFReader(Node, PBVTK_Node):

    bl_idname = 'VTKOMFReaderType'
    bl_label  = 'vtkOMFReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ColumnMajorOrdering: bpy.props.BoolProperty(name='ColumnMajorOrdering', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_WriteOutTextures: bpy.props.BoolProperty(name='WriteOutTextures', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ColumnMajorOrdering','m_WriteOutTextures','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKOMFReader )        
TYPENAMES.append('VTKOMFReaderType' )

#--------------------------------------------------------------
class VTKOpenFOAMReader(Node, PBVTK_Node):

    bl_idname = 'VTKOpenFOAMReaderType'
    bl_label  = 'vtkOpenFOAMReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AddDimensionsToArrayNames: bpy.props.BoolProperty(name='AddDimensionsToArrayNames', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CacheMesh: bpy.props.BoolProperty(name='CacheMesh', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CopyDataToCellZones: bpy.props.BoolProperty(name='CopyDataToCellZones', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CreateCellToPoint: bpy.props.BoolProperty(name='CreateCellToPoint', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IgnoreRestartFiles: bpy.props.BoolProperty(name='IgnoreRestartFiles', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ListTimeStepsByControlDict: bpy.props.BoolProperty(name='ListTimeStepsByControlDict', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PositionsIsIn13Format: bpy.props.BoolProperty(name='PositionsIsIn13Format', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadZones: bpy.props.BoolProperty(name='ReadZones', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SequentialProcessing: bpy.props.BoolProperty(name='SequentialProcessing', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SizeAverageCellToPoint: bpy.props.BoolProperty(name='SizeAverageCellToPoint', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SkipZeroTime: bpy.props.BoolProperty(name='SkipZeroTime', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Use64BitFloats: bpy.props.BoolProperty(name='Use64BitFloats', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Use64BitLabels: bpy.props.BoolProperty(name='Use64BitLabels', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeValue: bpy.props.FloatProperty(name='TimeValue', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=17, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AddDimensionsToArrayNames','m_CacheMesh','m_CopyDataToCellZones','m_CreateCellToPoint','m_IgnoreRestartFiles','m_ListTimeStepsByControlDict','m_PositionsIsIn13Format','m_ReadZones','m_SequentialProcessing','m_SizeAverageCellToPoint','m_SkipZeroTime','m_Use64BitFloats','m_Use64BitLabels','m_FileName','m_ObjectName','m_TimeValue',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKOpenFOAMReader )        
TYPENAMES.append('VTKOpenFOAMReaderType' )

#--------------------------------------------------------------
class VTKPChacoReader(Node, PBVTK_Node):

    bl_idname = 'VTKPChacoReaderType'
    bl_label  = 'vtkPChacoReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateEdgeWeightArrays: bpy.props.BoolProperty(name='GenerateEdgeWeightArrays', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateGlobalElementIdArray: bpy.props.BoolProperty(name='GenerateGlobalElementIdArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateGlobalNodeIdArray: bpy.props.BoolProperty(name='GenerateGlobalNodeIdArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateVertexWeightArrays: bpy.props.BoolProperty(name='GenerateVertexWeightArrays', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BaseName: bpy.props.StringProperty(name='BaseName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_GenerateEdgeWeightArrays','m_GenerateGlobalElementIdArray','m_GenerateGlobalNodeIdArray','m_GenerateVertexWeightArrays','m_BaseName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPChacoReader )        
TYPENAMES.append('VTKPChacoReaderType' )

#--------------------------------------------------------------
class VTKPDBReader(Node, PBVTK_Node):

    bl_idname = 'VTKPDBReaderType'
    bl_label  = 'vtkPDBReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BScale: bpy.props.FloatProperty(name='BScale', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HBScale: bpy.props.FloatProperty(name='HBScale', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName','m_BScale','m_HBScale',]
    def m_connections( self ):
        return ([], ['output 0', 'output 1'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPDBReader )        
TYPENAMES.append('VTKPDBReaderType' )

#--------------------------------------------------------------
class VTKPDataSetReader(Node, PBVTK_Node):

    bl_idname = 'VTKPDataSetReaderType'
    bl_label  = 'vtkPDataSetReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPDataSetReader )        
TYPENAMES.append('VTKPDataSetReaderType' )

#--------------------------------------------------------------
class VTKPExodusIIReader(Node, PBVTK_Node):

    bl_idname = 'VTKPExodusIIReaderType'
    bl_label  = 'vtkPExodusIIReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AnimateModeShapes: bpy.props.BoolProperty(name='AnimateModeShapes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ApplyDisplacements: bpy.props.BoolProperty(name='ApplyDisplacements', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateFileIdArray: bpy.props.BoolProperty(name='GenerateFileIdArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateGlobalElementIdArray: bpy.props.BoolProperty(name='GenerateGlobalElementIdArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateGlobalNodeIdArray: bpy.props.BoolProperty(name='GenerateGlobalNodeIdArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateImplicitElementIdArray: bpy.props.BoolProperty(name='GenerateImplicitElementIdArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateImplicitNodeIdArray: bpy.props.BoolProperty(name='GenerateImplicitNodeIdArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateObjectIdCellArray: bpy.props.BoolProperty(name='GenerateObjectIdCellArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HasModeShapes: bpy.props.BoolProperty(name='HasModeShapes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IgnoreFileTime: bpy.props.BoolProperty(name='IgnoreFileTime', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SqueezePoints: bpy.props.BoolProperty(name='SqueezePoints', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseLegacyBlockNames: bpy.props.BoolProperty(name='UseLegacyBlockNames', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_XMLFileName: bpy.props.StringProperty(name='XMLFileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DisplayType: bpy.props.IntProperty(name='DisplayType', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileId: bpy.props.IntProperty(name='FileId', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CacheSize: bpy.props.FloatProperty(name='CacheSize', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DisplacementMagnitude: bpy.props.FloatProperty(name='DisplacementMagnitude', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ModeShapeTime: bpy.props.FloatProperty(name='ModeShapeTime', default=-1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VariableCacheSize: bpy.props.FloatProperty(name='VariableCacheSize', default=100.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileRange: bpy.props.IntVectorProperty(name='FileRange', default=[-1, -1], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=26, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AnimateModeShapes','m_ApplyDisplacements','m_GenerateFileIdArray','m_GenerateGlobalElementIdArray','m_GenerateGlobalNodeIdArray','m_GenerateImplicitElementIdArray','m_GenerateImplicitNodeIdArray','m_GenerateObjectIdCellArray','m_HasModeShapes','m_IgnoreFileTime','m_SqueezePoints','m_UseLegacyBlockNames','m_FileName','m_FilePattern','m_FilePrefix','m_ObjectName','m_XMLFileName','m_DisplayType','m_FileId','m_TimeStep','m_CacheSize','m_DisplacementMagnitude','m_ModeShapeTime','m_VariableCacheSize','m_FileRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPExodusIIReader )        
TYPENAMES.append('VTKPExodusIIReaderType' )

#--------------------------------------------------------------
class VTKPIOReader(Node, PBVTK_Node):

    bl_idname = 'VTKPIOReaderType'
    bl_label  = 'vtkPIOReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Float64: bpy.props.BoolProperty(name='Float64', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HyperTreeGrid: bpy.props.BoolProperty(name='HyperTreeGrid', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Tracers: bpy.props.BoolProperty(name='Tracers', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ActiveTimeDataArrayName: bpy.props.StringProperty(name='ActiveTimeDataArrayName', default="CycleIndex", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CurrentTimeStep: bpy.props.IntProperty(name='CurrentTimeStep', default=-1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Float64','m_HyperTreeGrid','m_Tracers','m_ActiveTimeDataArrayName','m_FileName','m_ObjectName','m_CurrentTimeStep',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPIOReader )        
TYPENAMES.append('VTKPIOReaderType' )

#--------------------------------------------------------------
class VTKPLSDynaReader(Node, PBVTK_Node):

    bl_idname = 'VTKPLSDynaReaderType'
    bl_label  = 'vtkPLSDynaReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DeformedMesh: bpy.props.BoolProperty(name='DeformedMesh', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DeletedCellsAsGhostArray: bpy.props.BoolProperty(name='DeletedCellsAsGhostArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RemoveDeletedCells: bpy.props.BoolProperty(name='RemoveDeletedCells', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DatabaseDirectory: bpy.props.StringProperty(name='DatabaseDirectory', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="/d3plot", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InputDeck: bpy.props.StringProperty(name='InputDeck', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepRange: bpy.props.IntVectorProperty(name='TimeStepRange', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_DeformedMesh','m_DeletedCellsAsGhostArray','m_RemoveDeletedCells','m_DatabaseDirectory','m_FileName','m_InputDeck','m_ObjectName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPLSDynaReader )        
TYPENAMES.append('VTKPLSDynaReaderType' )

#--------------------------------------------------------------
class VTKPLYReader(Node, PBVTK_Node):

    bl_idname = 'VTKPLYReaderType'
    bl_label  = 'vtkPLYReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DuplicatePointsForFaceTexture: bpy.props.BoolProperty(name='DuplicatePointsForFaceTexture', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputStream: bpy.props.BoolProperty(name='ReadFromInputStream', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FaceTextureTolerance: bpy.props.FloatProperty(name='FaceTextureTolerance', default=9.999999974752427e-07, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_DuplicatePointsForFaceTexture','m_ReadFromInputStream','m_ReadFromInputString','m_FileName','m_ObjectName','m_FaceTextureTolerance',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'Stream'], []) 
    
add_class( VTKPLYReader )        
TYPENAMES.append('VTKPLYReaderType' )

#--------------------------------------------------------------
class VTKPNGReader(Node, PBVTK_Node):

    bl_idname = 'VTKPNGReaderType'
    bl_label  = 'vtkPNGReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileLowerLeft: bpy.props.BoolProperty(name='FileLowerLeft', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadSpacingFromFile: bpy.props.BoolProperty(name='ReadSpacingFromFile', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SwapBytes: bpy.props.BoolProperty(name='SwapBytes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileDimensionality: bpy.props.IntProperty(name='FileDimensionality', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceOffset: bpy.props.IntProperty(name='FileNameSliceOffset', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceSpacing: bpy.props.IntProperty(name='FileNameSliceSpacing', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HeaderSize: bpy.props.IntProperty(name='HeaderSize', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MemoryBufferLength: bpy.props.IntProperty(name='MemoryBufferLength', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfScalarComponents: bpy.props.IntProperty(name='NumberOfScalarComponents', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataByteOrder: bpy.props.EnumProperty(name='DataByteOrder', default="LittleEndian", items=e_DataByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataScalarType: bpy.props.EnumProperty(name='DataScalarType', default="Short", items=e_DataScalarType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataOrigin: bpy.props.FloatVectorProperty(name='DataOrigin', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataSpacing: bpy.props.FloatVectorProperty(name='DataSpacing', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileLowerLeft','m_ReadSpacingFromFile','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_ObjectName','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPNGReader )        
TYPENAMES.append('VTKPNGReaderType' )

#--------------------------------------------------------------
class VTKPNMReader(Node, PBVTK_Node):

    bl_idname = 'VTKPNMReaderType'
    bl_label  = 'vtkPNMReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileLowerLeft: bpy.props.BoolProperty(name='FileLowerLeft', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SwapBytes: bpy.props.BoolProperty(name='SwapBytes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarArrayName: bpy.props.StringProperty(name='ScalarArrayName', default="ImageFile", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataMask: bpy.props.IntProperty(name='DataMask', default=1000000000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileDimensionality: bpy.props.IntProperty(name='FileDimensionality', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceOffset: bpy.props.IntProperty(name='FileNameSliceOffset', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceSpacing: bpy.props.IntProperty(name='FileNameSliceSpacing', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HeaderSize: bpy.props.IntProperty(name='HeaderSize', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MemoryBufferLength: bpy.props.IntProperty(name='MemoryBufferLength', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfScalarComponents: bpy.props.IntProperty(name='NumberOfScalarComponents', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataByteOrder: bpy.props.EnumProperty(name='DataByteOrder', default="LittleEndian", items=e_DataByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataScalarType: bpy.props.EnumProperty(name='DataScalarType', default="Short", items=e_DataScalarType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataVOI: bpy.props.IntVectorProperty(name='DataVOI', default=[0, 0, 0, 0, 0, 0], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataOrigin: bpy.props.FloatVectorProperty(name='DataOrigin', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataSpacing: bpy.props.FloatVectorProperty(name='DataSpacing', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=20, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileLowerLeft','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_ObjectName','m_ScalarArrayName','m_DataMask','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataVOI','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'Transform'], []) 
    
add_class( VTKPNMReader )        
TYPENAMES.append('VTKPNMReaderType' )

#--------------------------------------------------------------
class VTKPOpenFOAMReader(Node, PBVTK_Node):

    bl_idname = 'VTKPOpenFOAMReaderType'
    bl_label  = 'vtkPOpenFOAMReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AddDimensionsToArrayNames: bpy.props.BoolProperty(name='AddDimensionsToArrayNames', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CacheMesh: bpy.props.BoolProperty(name='CacheMesh', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CopyDataToCellZones: bpy.props.BoolProperty(name='CopyDataToCellZones', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CreateCellToPoint: bpy.props.BoolProperty(name='CreateCellToPoint', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IgnoreRestartFiles: bpy.props.BoolProperty(name='IgnoreRestartFiles', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ListTimeStepsByControlDict: bpy.props.BoolProperty(name='ListTimeStepsByControlDict', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PositionsIsIn13Format: bpy.props.BoolProperty(name='PositionsIsIn13Format', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllFilesToDetermineStructure: bpy.props.BoolProperty(name='ReadAllFilesToDetermineStructure', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadZones: bpy.props.BoolProperty(name='ReadZones', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SequentialProcessing: bpy.props.BoolProperty(name='SequentialProcessing', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SizeAverageCellToPoint: bpy.props.BoolProperty(name='SizeAverageCellToPoint', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SkipZeroTime: bpy.props.BoolProperty(name='SkipZeroTime', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Use64BitFloats: bpy.props.BoolProperty(name='Use64BitFloats', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Use64BitLabels: bpy.props.BoolProperty(name='Use64BitLabels', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeValue: bpy.props.FloatProperty(name='TimeValue', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AddDimensionsToArrayNames','m_CacheMesh','m_CopyDataToCellZones','m_CreateCellToPoint','m_IgnoreRestartFiles','m_ListTimeStepsByControlDict','m_PositionsIsIn13Format','m_ReadAllFilesToDetermineStructure','m_ReadZones','m_SequentialProcessing','m_SizeAverageCellToPoint','m_SkipZeroTime','m_Use64BitFloats','m_Use64BitLabels','m_FileName','m_ObjectName','m_TimeValue',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPOpenFOAMReader )        
TYPENAMES.append('VTKPOpenFOAMReaderType' )

#--------------------------------------------------------------
class VTKPTSReader(Node, PBVTK_Node):

    bl_idname = 'VTKPTSReaderType'
    bl_label  = 'vtkPTSReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CreateCells: bpy.props.BoolProperty(name='CreateCells', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IncludeColorAndLuminance: bpy.props.BoolProperty(name='IncludeColorAndLuminance', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LimitReadToBounds: bpy.props.BoolProperty(name='LimitReadToBounds', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LimitToMaxNumberOfPoints: bpy.props.BoolProperty(name='LimitToMaxNumberOfPoints', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputDataTypeIsDouble: bpy.props.BoolProperty(name='OutputDataTypeIsDouble', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaxNumberOfPoints: bpy.props.IntProperty(name='MaxNumberOfPoints', default=1000000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadBounds: bpy.props.FloatVectorProperty(name='ReadBounds', default=[1e+30, -1e+30, 1e+30, -1e+30, 1e+30, -1e+30], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CreateCells','m_IncludeColorAndLuminance','m_LimitReadToBounds','m_LimitToMaxNumberOfPoints','m_OutputDataTypeIsDouble','m_FileName','m_ObjectName','m_MaxNumberOfPoints','m_ReadBounds',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPTSReader )        
TYPENAMES.append('VTKPTSReaderType' )

#--------------------------------------------------------------
class VTKParticleReader(Node, PBVTK_Node):

    bl_idname = 'VTKParticleReaderType'
    bl_label  = 'vtkParticleReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_FileType_items=[ (x,x,x) for x in ['Unknown', 'Text', 'Binary']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HasScalar: bpy.props.BoolProperty(name='HasScalar', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SwapBytes: bpy.props.BoolProperty(name='SwapBytes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataByteOrder: bpy.props.EnumProperty(name='DataByteOrder', default="LittleEndian", items=e_DataByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_FileType: bpy.props.EnumProperty(name='FileType', default="Unknown", items=e_FileType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_HasScalar','m_SwapBytes','m_FileName','m_ObjectName','e_DataByteOrder','e_FileType',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKParticleReader )        
TYPENAMES.append('VTKParticleReaderType' )

#--------------------------------------------------------------
class VTKPhyloXMLTreeReader(Node, PBVTK_Node):

    bl_idname = 'VTKPhyloXMLTreeReaderType'
    bl_label  = 'vtkPhyloXMLTreeReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ActiveTimeDataArrayName: bpy.props.StringProperty(name='ActiveTimeDataArrayName', default="TimeValue", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepRange: bpy.props.IntVectorProperty(name='TimeStepRange', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadFromInputString','m_ActiveTimeDataArrayName','m_FileName','m_ObjectName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'ReaderErrorObserver'], []) 
    
add_class( VTKPhyloXMLTreeReader )        
TYPENAMES.append('VTKPhyloXMLTreeReaderType' )

#--------------------------------------------------------------
class VTKPlot3DMetaReader(Node, PBVTK_Node):

    bl_idname = 'VTKPlot3DMetaReaderType'
    bl_label  = 'vtkPlot3DMetaReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPlot3DMetaReader )        
TYPENAMES.append('VTKPlot3DMetaReaderType' )

#--------------------------------------------------------------
class VTKPolyDataReader(Node, PBVTK_Node):

    bl_idname = 'VTKPolyDataReaderType'
    bl_label  = 'vtkPolyDataReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllColorScalars: bpy.props.BoolProperty(name='ReadAllColorScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllFields: bpy.props.BoolProperty(name='ReadAllFields', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllNormals: bpy.props.BoolProperty(name='ReadAllNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllScalars: bpy.props.BoolProperty(name='ReadAllScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTCoords: bpy.props.BoolProperty(name='ReadAllTCoords', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTensors: bpy.props.BoolProperty(name='ReadAllTensors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllVectors: bpy.props.BoolProperty(name='ReadAllVectors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ObjectName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'InputArray'], []) 
    
add_class( VTKPolyDataReader )        
TYPENAMES.append('VTKPolyDataReaderType' )

#--------------------------------------------------------------
class VTKProStarReader(Node, PBVTK_Node):

    bl_idname = 'VTKProStarReaderType'
    bl_label  = 'vtkProStarReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScaleFactor: bpy.props.FloatProperty(name='ScaleFactor', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName','m_ScaleFactor',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKProStarReader )        
TYPENAMES.append('VTKProStarReaderType' )

#--------------------------------------------------------------
class VTKRISReader(Node, PBVTK_Node):

    bl_idname = 'VTKRISReaderType'
    bl_label  = 'vtkRISReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Delimiter: bpy.props.StringProperty(name='Delimiter', default=";", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaxRecords: bpy.props.IntProperty(name='MaxRecords', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Delimiter','m_FileName','m_ObjectName','m_MaxRecords',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKRISReader )        
TYPENAMES.append('VTKRISReaderType' )

#--------------------------------------------------------------
class VTKRTXMLPolyDataReader(Node, PBVTK_Node):

    bl_idname = 'VTKRTXMLPolyDataReaderType'
    bl_label  = 'vtkRTXMLPolyDataReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ActiveTimeDataArrayName: bpy.props.StringProperty(name='ActiveTimeDataArrayName', default="TimeValue", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepRange: bpy.props.IntVectorProperty(name='TimeStepRange', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadFromInputString','m_ActiveTimeDataArrayName','m_FileName','m_ObjectName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'ReaderErrorObserver'], []) 
    
add_class( VTKRTXMLPolyDataReader )        
TYPENAMES.append('VTKRTXMLPolyDataReaderType' )

#--------------------------------------------------------------
class VTKRectilinearGridReader(Node, PBVTK_Node):

    bl_idname = 'VTKRectilinearGridReaderType'
    bl_label  = 'vtkRectilinearGridReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllColorScalars: bpy.props.BoolProperty(name='ReadAllColorScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllFields: bpy.props.BoolProperty(name='ReadAllFields', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllNormals: bpy.props.BoolProperty(name='ReadAllNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllScalars: bpy.props.BoolProperty(name='ReadAllScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTCoords: bpy.props.BoolProperty(name='ReadAllTCoords', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTensors: bpy.props.BoolProperty(name='ReadAllTensors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllVectors: bpy.props.BoolProperty(name='ReadAllVectors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ObjectName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'InputArray'], []) 
    
add_class( VTKRectilinearGridReader )        
TYPENAMES.append('VTKRectilinearGridReaderType' )

#--------------------------------------------------------------
class VTKSEPReader(Node, PBVTK_Node):

    bl_idname = 'VTKSEPReaderType'
    bl_label  = 'vtkSEPReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ExtentSplitMode: bpy.props.IntProperty(name='ExtentSplitMode', default=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputGridDimension: bpy.props.IntProperty(name='OutputGridDimension', default=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName','m_ExtentSplitMode','m_OutputGridDimension',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKSEPReader )        
TYPENAMES.append('VTKSEPReaderType' )

#--------------------------------------------------------------
class VTKSLACParticleReader(Node, PBVTK_Node):

    bl_idname = 'VTKSLACParticleReaderType'
    bl_label  = 'vtkSLACParticleReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKSLACParticleReader )        
TYPENAMES.append('VTKSLACParticleReaderType' )

#--------------------------------------------------------------
class VTKSLACReader(Node, PBVTK_Node):

    bl_idname = 'VTKSLACReaderType'
    bl_label  = 'vtkSLACReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadExternalSurface: bpy.props.BoolProperty(name='ReadExternalSurface', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadInternalVolume: bpy.props.BoolProperty(name='ReadInternalVolume', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadMidpoints: bpy.props.BoolProperty(name='ReadMidpoints', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MeshFileName: bpy.props.StringProperty(name='MeshFileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadExternalSurface','m_ReadInternalVolume','m_ReadMidpoints','m_MeshFileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output 0', 'output 1'], ['ContainerAlgorithm'], []) 
    
add_class( VTKSLACReader )        
TYPENAMES.append('VTKSLACReaderType' )

#--------------------------------------------------------------
class VTKSLCReader(Node, PBVTK_Node):

    bl_idname = 'VTKSLCReaderType'
    bl_label  = 'vtkSLCReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileLowerLeft: bpy.props.BoolProperty(name='FileLowerLeft', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SwapBytes: bpy.props.BoolProperty(name='SwapBytes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileDimensionality: bpy.props.IntProperty(name='FileDimensionality', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceOffset: bpy.props.IntProperty(name='FileNameSliceOffset', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceSpacing: bpy.props.IntProperty(name='FileNameSliceSpacing', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HeaderSize: bpy.props.IntProperty(name='HeaderSize', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MemoryBufferLength: bpy.props.IntProperty(name='MemoryBufferLength', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfScalarComponents: bpy.props.IntProperty(name='NumberOfScalarComponents', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataByteOrder: bpy.props.EnumProperty(name='DataByteOrder', default="LittleEndian", items=e_DataByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataScalarType: bpy.props.EnumProperty(name='DataScalarType', default="Short", items=e_DataScalarType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataOrigin: bpy.props.FloatVectorProperty(name='DataOrigin', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataSpacing: bpy.props.FloatVectorProperty(name='DataSpacing', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=17, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileLowerLeft','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_ObjectName','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKSLCReader )        
TYPENAMES.append('VTKSLCReaderType' )

#--------------------------------------------------------------
class VTKSQLiteToTableReader(Node, PBVTK_Node):

    bl_idname = 'VTKSQLiteToTableReaderType'
    bl_label  = 'vtkSQLiteToTableReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'Database'], []) 
    
add_class( VTKSQLiteToTableReader )        
TYPENAMES.append('VTKSQLiteToTableReaderType' )

#--------------------------------------------------------------
class VTKSTLReader(Node, PBVTK_Node):

    bl_idname = 'VTKSTLReaderType'
    bl_label  = 'vtkSTLReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Merging: bpy.props.BoolProperty(name='Merging', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarTags: bpy.props.BoolProperty(name='ScalarTags', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Merging','m_ScalarTags','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'Stream'], []) 
    
add_class( VTKSTLReader )        
TYPENAMES.append('VTKSTLReaderType' )

#--------------------------------------------------------------
class VTKSegYReader(Node, PBVTK_Node):

    bl_idname = 'VTKSegYReaderType'
    bl_label  = 'vtkSegYReader'
    e_XYCoordMode_items=[ (x,x,x) for x in ['Source', 'CDP', 'Custom']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Force2D: bpy.props.BoolProperty(name='Force2D', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_StructuredGrid: bpy.props.BoolProperty(name='StructuredGrid', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VerticalCRS: bpy.props.IntProperty(name='VerticalCRS', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_XCoordByte: bpy.props.IntProperty(name='XCoordByte', default=73, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_YCoordByte: bpy.props.IntProperty(name='YCoordByte', default=77, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_XYCoordMode: bpy.props.EnumProperty(name='XYCoordMode', default="Source", items=e_XYCoordMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Force2D','m_StructuredGrid','m_FileName','m_ObjectName','m_VerticalCRS','m_XCoordByte','m_YCoordByte','e_XYCoordMode',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKSegYReader )        
TYPENAMES.append('VTKSegYReaderType' )

#--------------------------------------------------------------
class VTKSimplePointsReader(Node, PBVTK_Node):

    bl_idname = 'VTKSimplePointsReaderType'
    bl_label  = 'vtkSimplePointsReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKSimplePointsReader )        
TYPENAMES.append('VTKSimplePointsReaderType' )

#--------------------------------------------------------------
class VTKStructuredGridReader(Node, PBVTK_Node):

    bl_idname = 'VTKStructuredGridReaderType'
    bl_label  = 'vtkStructuredGridReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllColorScalars: bpy.props.BoolProperty(name='ReadAllColorScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllFields: bpy.props.BoolProperty(name='ReadAllFields', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllNormals: bpy.props.BoolProperty(name='ReadAllNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllScalars: bpy.props.BoolProperty(name='ReadAllScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTCoords: bpy.props.BoolProperty(name='ReadAllTCoords', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTensors: bpy.props.BoolProperty(name='ReadAllTensors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllVectors: bpy.props.BoolProperty(name='ReadAllVectors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ObjectName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'InputArray'], []) 
    
add_class( VTKStructuredGridReader )        
TYPENAMES.append('VTKStructuredGridReaderType' )

#--------------------------------------------------------------
class VTKStructuredPointsReader(Node, PBVTK_Node):

    bl_idname = 'VTKStructuredPointsReaderType'
    bl_label  = 'vtkStructuredPointsReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllColorScalars: bpy.props.BoolProperty(name='ReadAllColorScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllFields: bpy.props.BoolProperty(name='ReadAllFields', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllNormals: bpy.props.BoolProperty(name='ReadAllNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllScalars: bpy.props.BoolProperty(name='ReadAllScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTCoords: bpy.props.BoolProperty(name='ReadAllTCoords', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTensors: bpy.props.BoolProperty(name='ReadAllTensors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllVectors: bpy.props.BoolProperty(name='ReadAllVectors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ObjectName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'InputArray'], []) 
    
add_class( VTKStructuredPointsReader )        
TYPENAMES.append('VTKStructuredPointsReaderType' )

#--------------------------------------------------------------
class VTKTGAReader(Node, PBVTK_Node):

    bl_idname = 'VTKTGAReaderType'
    bl_label  = 'vtkTGAReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileLowerLeft: bpy.props.BoolProperty(name='FileLowerLeft', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SwapBytes: bpy.props.BoolProperty(name='SwapBytes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileDimensionality: bpy.props.IntProperty(name='FileDimensionality', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceOffset: bpy.props.IntProperty(name='FileNameSliceOffset', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceSpacing: bpy.props.IntProperty(name='FileNameSliceSpacing', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HeaderSize: bpy.props.IntProperty(name='HeaderSize', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MemoryBufferLength: bpy.props.IntProperty(name='MemoryBufferLength', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfScalarComponents: bpy.props.IntProperty(name='NumberOfScalarComponents', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataByteOrder: bpy.props.EnumProperty(name='DataByteOrder', default="LittleEndian", items=e_DataByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataScalarType: bpy.props.EnumProperty(name='DataScalarType', default="Short", items=e_DataScalarType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataOrigin: bpy.props.FloatVectorProperty(name='DataOrigin', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataSpacing: bpy.props.FloatVectorProperty(name='DataSpacing', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=17, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileLowerLeft','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_ObjectName','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTGAReader )        
TYPENAMES.append('VTKTGAReaderType' )

#--------------------------------------------------------------
class VTKTIFFReader(Node, PBVTK_Node):

    bl_idname = 'VTKTIFFReaderType'
    bl_label  = 'vtkTIFFReader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    e_DataScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Float', 'Double', 'SignedChar']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileLowerLeft: bpy.props.BoolProperty(name='FileLowerLeft', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IgnoreColorMap: bpy.props.BoolProperty(name='IgnoreColorMap', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OriginSpecifiedFlag: bpy.props.BoolProperty(name='OriginSpecifiedFlag', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SpacingSpecifiedFlag: bpy.props.BoolProperty(name='SpacingSpecifiedFlag', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SwapBytes: bpy.props.BoolProperty(name='SwapBytes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileDimensionality: bpy.props.IntProperty(name='FileDimensionality', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceOffset: bpy.props.IntProperty(name='FileNameSliceOffset', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileNameSliceSpacing: bpy.props.IntProperty(name='FileNameSliceSpacing', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HeaderSize: bpy.props.IntProperty(name='HeaderSize', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MemoryBufferLength: bpy.props.IntProperty(name='MemoryBufferLength', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfScalarComponents: bpy.props.IntProperty(name='NumberOfScalarComponents', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OrientationType: bpy.props.IntProperty(name='OrientationType', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataByteOrder: bpy.props.EnumProperty(name='DataByteOrder', default="LittleEndian", items=e_DataByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataScalarType: bpy.props.EnumProperty(name='DataScalarType', default="Short", items=e_DataScalarType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataOrigin: bpy.props.FloatVectorProperty(name='DataOrigin', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataSpacing: bpy.props.FloatVectorProperty(name='DataSpacing', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=21, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileLowerLeft','m_IgnoreColorMap','m_OriginSpecifiedFlag','m_SpacingSpecifiedFlag','m_SwapBytes','m_FileName','m_FilePattern','m_FilePrefix','m_ObjectName','m_FileDimensionality','m_FileNameSliceOffset','m_FileNameSliceSpacing','m_HeaderSize','m_MemoryBufferLength','m_NumberOfScalarComponents','m_OrientationType','e_DataByteOrder','e_DataScalarType','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTIFFReader )        
TYPENAMES.append('VTKTIFFReaderType' )

#--------------------------------------------------------------
class VTKTRUCHASReader(Node, PBVTK_Node):

    bl_idname = 'VTKTRUCHASReaderType'
    bl_label  = 'vtkTRUCHASReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTRUCHASReader )        
TYPENAMES.append('VTKTRUCHASReaderType' )

#--------------------------------------------------------------
class VTKTableReader(Node, PBVTK_Node):

    bl_idname = 'VTKTableReaderType'
    bl_label  = 'vtkTableReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllColorScalars: bpy.props.BoolProperty(name='ReadAllColorScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllFields: bpy.props.BoolProperty(name='ReadAllFields', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllNormals: bpy.props.BoolProperty(name='ReadAllNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllScalars: bpy.props.BoolProperty(name='ReadAllScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTCoords: bpy.props.BoolProperty(name='ReadAllTCoords', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTensors: bpy.props.BoolProperty(name='ReadAllTensors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllVectors: bpy.props.BoolProperty(name='ReadAllVectors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ObjectName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'InputArray'], []) 
    
add_class( VTKTableReader )        
TYPENAMES.append('VTKTableReaderType' )

#--------------------------------------------------------------
class VTKTecplotReader(Node, PBVTK_Node):

    bl_idname = 'VTKTecplotReaderType'
    bl_label  = 'vtkTecplotReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTecplotReader )        
TYPENAMES.append('VTKTecplotReaderType' )

#--------------------------------------------------------------
class VTKTecplotTableReader(Node, PBVTK_Node):

    bl_idname = 'VTKTecplotTableReaderType'
    bl_label  = 'vtkTecplotTableReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GeneratePedigreeIds: bpy.props.BoolProperty(name='GeneratePedigreeIds', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputPedigreeIds: bpy.props.BoolProperty(name='OutputPedigreeIds', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PedigreeIdArrayName: bpy.props.StringProperty(name='PedigreeIdArrayName', default="id", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ColumnNamesOnLine: bpy.props.IntProperty(name='ColumnNamesOnLine', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HeaderLines: bpy.props.IntProperty(name='HeaderLines', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaxRecords: bpy.props.IntProperty(name='MaxRecords', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SkipColumnNames: bpy.props.IntProperty(name='SkipColumnNames', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_GeneratePedigreeIds','m_OutputPedigreeIds','m_FileName','m_ObjectName','m_PedigreeIdArrayName','m_ColumnNamesOnLine','m_HeaderLines','m_MaxRecords','m_SkipColumnNames',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTecplotTableReader )        
TYPENAMES.append('VTKTecplotTableReaderType' )

#--------------------------------------------------------------
class VTKTemporalDelimitedTextReader(Node, PBVTK_Node):

    bl_idname = 'VTKTemporalDelimitedTextReaderType'
    bl_label  = 'vtkTemporalDelimitedTextReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AddTabFieldDelimiter: bpy.props.BoolProperty(name='AddTabFieldDelimiter', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DetectNumericColumns: bpy.props.BoolProperty(name='DetectNumericColumns', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ForceDouble: bpy.props.BoolProperty(name='ForceDouble', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GeneratePedigreeIds: bpy.props.BoolProperty(name='GeneratePedigreeIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HaveHeaders: bpy.props.BoolProperty(name='HaveHeaders', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MergeConsecutiveDelimiters: bpy.props.BoolProperty(name='MergeConsecutiveDelimiters', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputPedigreeIds: bpy.props.BoolProperty(name='OutputPedigreeIds', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RemoveTimeStepColumn: bpy.props.BoolProperty(name='RemoveTimeStepColumn', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TrimWhitespacePriorToNumericConversion: bpy.props.BoolProperty(name='TrimWhitespacePriorToNumericConversion', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseStringDelimiter: bpy.props.BoolProperty(name='UseStringDelimiter', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CommentCharacters: bpy.props.StringProperty(name='CommentCharacters', default="#", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldDelimiterCharacters: bpy.props.StringProperty(name='FieldDelimiterCharacters', default=",", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PedigreeIdArrayName: bpy.props.StringProperty(name='PedigreeIdArrayName', default="id", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_StringDelimiter: bpy.props.StringProperty(name='StringDelimiter', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeColumnName: bpy.props.StringProperty(name='TimeColumnName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UTF8FieldDelimiters: bpy.props.StringProperty(name='UTF8FieldDelimiters', default=",", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UTF8RecordDelimiters: bpy.props.StringProperty(name='UTF8RecordDelimiters', default="\n", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UTF8StringDelimiters: bpy.props.StringProperty(name='UTF8StringDelimiters', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UnicodeCharacterSet: bpy.props.StringProperty(name='UnicodeCharacterSet', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DefaultIntegerValue: bpy.props.IntProperty(name='DefaultIntegerValue', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaxRecords: bpy.props.IntProperty(name='MaxRecords', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PreviewNumberOfLines: bpy.props.IntProperty(name='PreviewNumberOfLines', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReplacementCharacter: bpy.props.IntProperty(name='ReplacementCharacter', default=120, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SkippedRecords: bpy.props.IntProperty(name='SkippedRecords', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeColumnId: bpy.props.IntProperty(name='TimeColumnId', default=-1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DefaultDoubleValue: bpy.props.FloatProperty(name='DefaultDoubleValue', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=30, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AddTabFieldDelimiter','m_DetectNumericColumns','m_ForceDouble','m_GeneratePedigreeIds','m_HaveHeaders','m_MergeConsecutiveDelimiters','m_OutputPedigreeIds','m_ReadFromInputString','m_RemoveTimeStepColumn','m_TrimWhitespacePriorToNumericConversion','m_UseStringDelimiter','m_CommentCharacters','m_FieldDelimiterCharacters','m_FileName','m_ObjectName','m_PedigreeIdArrayName','m_StringDelimiter','m_TimeColumnName','m_UTF8FieldDelimiters','m_UTF8RecordDelimiters','m_UTF8StringDelimiters','m_UnicodeCharacterSet','m_DefaultIntegerValue','m_MaxRecords','m_PreviewNumberOfLines','m_ReplacementCharacter','m_SkippedRecords','m_TimeColumnId','m_DefaultDoubleValue',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTemporalDelimitedTextReader )        
TYPENAMES.append('VTKTemporalDelimitedTextReaderType' )

#--------------------------------------------------------------
class VTKTreeReader(Node, PBVTK_Node):

    bl_idname = 'VTKTreeReaderType'
    bl_label  = 'vtkTreeReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllColorScalars: bpy.props.BoolProperty(name='ReadAllColorScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllFields: bpy.props.BoolProperty(name='ReadAllFields', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllNormals: bpy.props.BoolProperty(name='ReadAllNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllScalars: bpy.props.BoolProperty(name='ReadAllScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTCoords: bpy.props.BoolProperty(name='ReadAllTCoords', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTensors: bpy.props.BoolProperty(name='ReadAllTensors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllVectors: bpy.props.BoolProperty(name='ReadAllVectors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ObjectName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'InputArray'], []) 
    
add_class( VTKTreeReader )        
TYPENAMES.append('VTKTreeReaderType' )

#--------------------------------------------------------------
class VTKTulipReader(Node, PBVTK_Node):

    bl_idname = 'VTKTulipReaderType'
    bl_label  = 'vtkTulipReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output 0', 'output 1'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTulipReader )        
TYPENAMES.append('VTKTulipReaderType' )

#--------------------------------------------------------------
class VTKUnstructuredGridReader(Node, PBVTK_Node):

    bl_idname = 'VTKUnstructuredGridReaderType'
    bl_label  = 'vtkUnstructuredGridReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllColorScalars: bpy.props.BoolProperty(name='ReadAllColorScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllFields: bpy.props.BoolProperty(name='ReadAllFields', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllNormals: bpy.props.BoolProperty(name='ReadAllNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllScalars: bpy.props.BoolProperty(name='ReadAllScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTCoords: bpy.props.BoolProperty(name='ReadAllTCoords', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllTensors: bpy.props.BoolProperty(name='ReadAllTensors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadAllVectors: bpy.props.BoolProperty(name='ReadAllVectors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldDataName: bpy.props.StringProperty(name='FieldDataName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LookupTableName: bpy.props.StringProperty(name='LookupTableName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NormalsName: bpy.props.StringProperty(name='NormalsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TCoordsName: bpy.props.StringProperty(name='TCoordsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TensorsName: bpy.props.StringProperty(name='TensorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VectorsName: bpy.props.StringProperty(name='VectorsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadAllColorScalars','m_ReadAllFields','m_ReadAllNormals','m_ReadAllScalars','m_ReadAllTCoords','m_ReadAllTensors','m_ReadAllVectors','m_ReadFromInputString','m_FieldDataName','m_FileName','m_LookupTableName','m_NormalsName','m_ObjectName','m_ScalarsName','m_TCoordsName','m_TensorsName','m_VectorsName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'InputArray'], []) 
    
add_class( VTKUnstructuredGridReader )        
TYPENAMES.append('VTKUnstructuredGridReaderType' )

#--------------------------------------------------------------
class VTKVASPAnimationReader(Node, PBVTK_Node):

    bl_idname = 'VTKVASPAnimationReaderType'
    bl_label  = 'vtkVASPAnimationReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKVASPAnimationReader )        
TYPENAMES.append('VTKVASPAnimationReaderType' )

#--------------------------------------------------------------
class VTKVASPTessellationReader(Node, PBVTK_Node):

    bl_idname = 'VTKVASPTessellationReaderType'
    bl_label  = 'vtkVASPTessellationReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output 0', 'output 1'], ['ContainerAlgorithm'], []) 
    
add_class( VTKVASPTessellationReader )        
TYPENAMES.append('VTKVASPTessellationReaderType' )

#--------------------------------------------------------------
class VTKVPICReader(Node, PBVTK_Node):

    bl_idname = 'VTKVPICReaderType'
    bl_label  = 'vtkVPICReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Stride: bpy.props.IntVectorProperty(name='Stride', default=[1, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName','m_Stride',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKVPICReader )        
TYPENAMES.append('VTKVPICReaderType' )

#--------------------------------------------------------------
class VTKVeraOutReader(Node, PBVTK_Node):

    bl_idname = 'VTKVeraOutReaderType'
    bl_label  = 'vtkVeraOutReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKVeraOutReader )        
TYPENAMES.append('VTKVeraOutReaderType' )

#--------------------------------------------------------------
class VTKVolume16Reader(Node, PBVTK_Node):

    bl_idname = 'VTKVolume16ReaderType'
    bl_label  = 'vtkVolume16Reader'
    e_DataByteOrder_items=[ (x,x,x) for x in ['BigEndian', 'LittleEndian']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SwapBytes: bpy.props.BoolProperty(name='SwapBytes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePattern: bpy.props.StringProperty(name='FilePattern', default="%s.%d", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FilePrefix: bpy.props.StringProperty(name='FilePrefix', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataMask: bpy.props.IntProperty(name='DataMask', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HeaderSize: bpy.props.IntProperty(name='HeaderSize', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataByteOrder: bpy.props.EnumProperty(name='DataByteOrder', default="LittleEndian", items=e_DataByteOrder_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataDimensions: bpy.props.IntVectorProperty(name='DataDimensions', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ImageRange: bpy.props.IntVectorProperty(name='ImageRange', default=[1, 1], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataOrigin: bpy.props.FloatVectorProperty(name='DataOrigin', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataSpacing: bpy.props.FloatVectorProperty(name='DataSpacing', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_SwapBytes','m_FilePattern','m_FilePrefix','m_ObjectName','m_DataMask','m_HeaderSize','e_DataByteOrder','m_DataDimensions','m_ImageRange','m_DataOrigin','m_DataSpacing',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'Transform'], []) 
    
add_class( VTKVolume16Reader )        
TYPENAMES.append('VTKVolume16ReaderType' )

#--------------------------------------------------------------
class VTKWindBladeReader(Node, PBVTK_Node):

    bl_idname = 'VTKWindBladeReaderType'
    bl_label  = 'vtkWindBladeReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Filename: bpy.props.StringProperty(name='Filename', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SubExtent: bpy.props.IntVectorProperty(name='SubExtent', default=[1000000000, 360, 1000000000, 360, 1000000000, 360], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Filename','m_ObjectName','m_SubExtent',]
    def m_connections( self ):
        return ([], ['output 0', 'output 1', 'output 2'], ['ContainerAlgorithm'], []) 
    
add_class( VTKWindBladeReader )        
TYPENAMES.append('VTKWindBladeReaderType' )

#--------------------------------------------------------------
class VTKXGMLReader(Node, PBVTK_Node):

    bl_idname = 'VTKXGMLReaderType'
    bl_label  = 'vtkXGMLReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKXGMLReader )        
TYPENAMES.append('VTKXGMLReaderType' )

#--------------------------------------------------------------
class VTKXMLGenericDataObjectReader(Node, PBVTK_Node):

    bl_idname = 'VTKXMLGenericDataObjectReaderType'
    bl_label  = 'vtkXMLGenericDataObjectReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ActiveTimeDataArrayName: bpy.props.StringProperty(name='ActiveTimeDataArrayName', default="TimeValue", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepRange: bpy.props.IntVectorProperty(name='TimeStepRange', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadFromInputString','m_ActiveTimeDataArrayName','m_FileName','m_ObjectName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'ReaderErrorObserver'], []) 
    
add_class( VTKXMLGenericDataObjectReader )        
TYPENAMES.append('VTKXMLGenericDataObjectReaderType' )

#--------------------------------------------------------------
class VTKXMLHierarchicalBoxDataReader(Node, PBVTK_Node):

    bl_idname = 'VTKXMLHierarchicalBoxDataReaderType'
    bl_label  = 'vtkXMLHierarchicalBoxDataReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ActiveTimeDataArrayName: bpy.props.StringProperty(name='ActiveTimeDataArrayName', default="TimeValue", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumLevelsToReadByDefault: bpy.props.IntProperty(name='MaximumLevelsToReadByDefault', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PieceDistribution: bpy.props.IntProperty(name='PieceDistribution', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepRange: bpy.props.IntVectorProperty(name='TimeStepRange', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadFromInputString','m_ActiveTimeDataArrayName','m_FileName','m_ObjectName','m_MaximumLevelsToReadByDefault','m_PieceDistribution','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'ReaderErrorObserver'], []) 
    
add_class( VTKXMLHierarchicalBoxDataReader )        
TYPENAMES.append('VTKXMLHierarchicalBoxDataReaderType' )

#--------------------------------------------------------------
class VTKXMLHierarchicalDataReader(Node, PBVTK_Node):

    bl_idname = 'VTKXMLHierarchicalDataReaderType'
    bl_label  = 'vtkXMLHierarchicalDataReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ActiveTimeDataArrayName: bpy.props.StringProperty(name='ActiveTimeDataArrayName', default="TimeValue", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PieceDistribution: bpy.props.IntProperty(name='PieceDistribution', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepRange: bpy.props.IntVectorProperty(name='TimeStepRange', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadFromInputString','m_ActiveTimeDataArrayName','m_FileName','m_ObjectName','m_PieceDistribution','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'ReaderErrorObserver'], []) 
    
add_class( VTKXMLHierarchicalDataReader )        
TYPENAMES.append('VTKXMLHierarchicalDataReaderType' )

#--------------------------------------------------------------
class VTKXMLHyperTreeGridReader(Node, PBVTK_Node):

    bl_idname = 'VTKXMLHyperTreeGridReaderType'
    bl_label  = 'vtkXMLHyperTreeGridReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ActiveTimeDataArrayName: bpy.props.StringProperty(name='ActiveTimeDataArrayName', default="TimeValue", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FixedLevel: bpy.props.IntProperty(name='FixedLevel', default=1000000000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepRange: bpy.props.IntVectorProperty(name='TimeStepRange', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadFromInputString','m_ActiveTimeDataArrayName','m_FileName','m_ObjectName','m_FixedLevel','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'ReaderErrorObserver'], []) 
    
add_class( VTKXMLHyperTreeGridReader )        
TYPENAMES.append('VTKXMLHyperTreeGridReaderType' )

#--------------------------------------------------------------
class VTKXMLImageDataReader(Node, PBVTK_Node):

    bl_idname = 'VTKXMLImageDataReaderType'
    bl_label  = 'vtkXMLImageDataReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_WholeSlices: bpy.props.BoolProperty(name='WholeSlices', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ActiveTimeDataArrayName: bpy.props.StringProperty(name='ActiveTimeDataArrayName', default="TimeValue", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepRange: bpy.props.IntVectorProperty(name='TimeStepRange', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadFromInputString','m_WholeSlices','m_ActiveTimeDataArrayName','m_FileName','m_ObjectName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'ReaderErrorObserver'], []) 
    
add_class( VTKXMLImageDataReader )        
TYPENAMES.append('VTKXMLImageDataReaderType' )

#--------------------------------------------------------------
class VTKXMLMultiBlockDataReader(Node, PBVTK_Node):

    bl_idname = 'VTKXMLMultiBlockDataReaderType'
    bl_label  = 'vtkXMLMultiBlockDataReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ActiveTimeDataArrayName: bpy.props.StringProperty(name='ActiveTimeDataArrayName', default="TimeValue", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PieceDistribution: bpy.props.IntProperty(name='PieceDistribution', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepRange: bpy.props.IntVectorProperty(name='TimeStepRange', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadFromInputString','m_ActiveTimeDataArrayName','m_FileName','m_ObjectName','m_PieceDistribution','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'ReaderErrorObserver'], []) 
    
add_class( VTKXMLMultiBlockDataReader )        
TYPENAMES.append('VTKXMLMultiBlockDataReaderType' )

#--------------------------------------------------------------
class VTKXMLMultiGroupDataReader(Node, PBVTK_Node):

    bl_idname = 'VTKXMLMultiGroupDataReaderType'
    bl_label  = 'vtkXMLMultiGroupDataReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ActiveTimeDataArrayName: bpy.props.StringProperty(name='ActiveTimeDataArrayName', default="TimeValue", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PieceDistribution: bpy.props.IntProperty(name='PieceDistribution', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepRange: bpy.props.IntVectorProperty(name='TimeStepRange', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadFromInputString','m_ActiveTimeDataArrayName','m_FileName','m_ObjectName','m_PieceDistribution','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'ReaderErrorObserver'], []) 
    
add_class( VTKXMLMultiGroupDataReader )        
TYPENAMES.append('VTKXMLMultiGroupDataReaderType' )

#--------------------------------------------------------------
class VTKXMLPHyperTreeGridReader(Node, PBVTK_Node):

    bl_idname = 'VTKXMLPHyperTreeGridReaderType'
    bl_label  = 'vtkXMLPHyperTreeGridReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ActiveTimeDataArrayName: bpy.props.StringProperty(name='ActiveTimeDataArrayName', default="TimeValue", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepRange: bpy.props.IntVectorProperty(name='TimeStepRange', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadFromInputString','m_ActiveTimeDataArrayName','m_FileName','m_ObjectName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'ReaderErrorObserver'], []) 
    
add_class( VTKXMLPHyperTreeGridReader )        
TYPENAMES.append('VTKXMLPHyperTreeGridReaderType' )

#--------------------------------------------------------------
class VTKXMLPImageDataReader(Node, PBVTK_Node):

    bl_idname = 'VTKXMLPImageDataReaderType'
    bl_label  = 'vtkXMLPImageDataReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ActiveTimeDataArrayName: bpy.props.StringProperty(name='ActiveTimeDataArrayName', default="TimeValue", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepRange: bpy.props.IntVectorProperty(name='TimeStepRange', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadFromInputString','m_ActiveTimeDataArrayName','m_FileName','m_ObjectName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'ReaderErrorObserver'], []) 
    
add_class( VTKXMLPImageDataReader )        
TYPENAMES.append('VTKXMLPImageDataReaderType' )

#--------------------------------------------------------------
class VTKXMLPPolyDataReader(Node, PBVTK_Node):

    bl_idname = 'VTKXMLPPolyDataReaderType'
    bl_label  = 'vtkXMLPPolyDataReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ActiveTimeDataArrayName: bpy.props.StringProperty(name='ActiveTimeDataArrayName', default="TimeValue", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepRange: bpy.props.IntVectorProperty(name='TimeStepRange', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadFromInputString','m_ActiveTimeDataArrayName','m_FileName','m_ObjectName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'ReaderErrorObserver'], []) 
    
add_class( VTKXMLPPolyDataReader )        
TYPENAMES.append('VTKXMLPPolyDataReaderType' )

#--------------------------------------------------------------
class VTKXMLPRectilinearGridReader(Node, PBVTK_Node):

    bl_idname = 'VTKXMLPRectilinearGridReaderType'
    bl_label  = 'vtkXMLPRectilinearGridReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ActiveTimeDataArrayName: bpy.props.StringProperty(name='ActiveTimeDataArrayName', default="TimeValue", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepRange: bpy.props.IntVectorProperty(name='TimeStepRange', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadFromInputString','m_ActiveTimeDataArrayName','m_FileName','m_ObjectName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'ReaderErrorObserver'], []) 
    
add_class( VTKXMLPRectilinearGridReader )        
TYPENAMES.append('VTKXMLPRectilinearGridReaderType' )

#--------------------------------------------------------------
class VTKXMLPStructuredGridReader(Node, PBVTK_Node):

    bl_idname = 'VTKXMLPStructuredGridReaderType'
    bl_label  = 'vtkXMLPStructuredGridReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ActiveTimeDataArrayName: bpy.props.StringProperty(name='ActiveTimeDataArrayName', default="TimeValue", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepRange: bpy.props.IntVectorProperty(name='TimeStepRange', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadFromInputString','m_ActiveTimeDataArrayName','m_FileName','m_ObjectName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'ReaderErrorObserver'], []) 
    
add_class( VTKXMLPStructuredGridReader )        
TYPENAMES.append('VTKXMLPStructuredGridReaderType' )

#--------------------------------------------------------------
class VTKXMLPTableReader(Node, PBVTK_Node):

    bl_idname = 'VTKXMLPTableReaderType'
    bl_label  = 'vtkXMLPTableReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ActiveTimeDataArrayName: bpy.props.StringProperty(name='ActiveTimeDataArrayName', default="TimeValue", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepRange: bpy.props.IntVectorProperty(name='TimeStepRange', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadFromInputString','m_ActiveTimeDataArrayName','m_FileName','m_ObjectName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'ReaderErrorObserver'], []) 
    
add_class( VTKXMLPTableReader )        
TYPENAMES.append('VTKXMLPTableReaderType' )

#--------------------------------------------------------------
class VTKXMLPUnstructuredGridReader(Node, PBVTK_Node):

    bl_idname = 'VTKXMLPUnstructuredGridReaderType'
    bl_label  = 'vtkXMLPUnstructuredGridReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ActiveTimeDataArrayName: bpy.props.StringProperty(name='ActiveTimeDataArrayName', default="TimeValue", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepRange: bpy.props.IntVectorProperty(name='TimeStepRange', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadFromInputString','m_ActiveTimeDataArrayName','m_FileName','m_ObjectName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'ReaderErrorObserver'], []) 
    
add_class( VTKXMLPUnstructuredGridReader )        
TYPENAMES.append('VTKXMLPUnstructuredGridReaderType' )

#--------------------------------------------------------------
class VTKXMLPartitionedDataSetCollectionReader(Node, PBVTK_Node):

    bl_idname = 'VTKXMLPartitionedDataSetCollectionReaderType'
    bl_label  = 'vtkXMLPartitionedDataSetCollectionReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ActiveTimeDataArrayName: bpy.props.StringProperty(name='ActiveTimeDataArrayName', default="TimeValue", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PieceDistribution: bpy.props.IntProperty(name='PieceDistribution', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepRange: bpy.props.IntVectorProperty(name='TimeStepRange', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadFromInputString','m_ActiveTimeDataArrayName','m_FileName','m_ObjectName','m_PieceDistribution','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'ReaderErrorObserver'], []) 
    
add_class( VTKXMLPartitionedDataSetCollectionReader )        
TYPENAMES.append('VTKXMLPartitionedDataSetCollectionReaderType' )

#--------------------------------------------------------------
class VTKXMLPartitionedDataSetReader(Node, PBVTK_Node):

    bl_idname = 'VTKXMLPartitionedDataSetReaderType'
    bl_label  = 'vtkXMLPartitionedDataSetReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ActiveTimeDataArrayName: bpy.props.StringProperty(name='ActiveTimeDataArrayName', default="TimeValue", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PieceDistribution: bpy.props.IntProperty(name='PieceDistribution', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepRange: bpy.props.IntVectorProperty(name='TimeStepRange', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadFromInputString','m_ActiveTimeDataArrayName','m_FileName','m_ObjectName','m_PieceDistribution','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'ReaderErrorObserver'], []) 
    
add_class( VTKXMLPartitionedDataSetReader )        
TYPENAMES.append('VTKXMLPartitionedDataSetReaderType' )

#--------------------------------------------------------------
class VTKXMLPolyDataReader(Node, PBVTK_Node):

    bl_idname = 'VTKXMLPolyDataReaderType'
    bl_label  = 'vtkXMLPolyDataReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ActiveTimeDataArrayName: bpy.props.StringProperty(name='ActiveTimeDataArrayName', default="TimeValue", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepRange: bpy.props.IntVectorProperty(name='TimeStepRange', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadFromInputString','m_ActiveTimeDataArrayName','m_FileName','m_ObjectName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'ReaderErrorObserver'], []) 
    
add_class( VTKXMLPolyDataReader )        
TYPENAMES.append('VTKXMLPolyDataReaderType' )

#--------------------------------------------------------------
class VTKXMLRectilinearGridReader(Node, PBVTK_Node):

    bl_idname = 'VTKXMLRectilinearGridReaderType'
    bl_label  = 'vtkXMLRectilinearGridReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_WholeSlices: bpy.props.BoolProperty(name='WholeSlices', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ActiveTimeDataArrayName: bpy.props.StringProperty(name='ActiveTimeDataArrayName', default="TimeValue", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepRange: bpy.props.IntVectorProperty(name='TimeStepRange', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadFromInputString','m_WholeSlices','m_ActiveTimeDataArrayName','m_FileName','m_ObjectName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'ReaderErrorObserver'], []) 
    
add_class( VTKXMLRectilinearGridReader )        
TYPENAMES.append('VTKXMLRectilinearGridReaderType' )

#--------------------------------------------------------------
class VTKXMLStructuredGridReader(Node, PBVTK_Node):

    bl_idname = 'VTKXMLStructuredGridReaderType'
    bl_label  = 'vtkXMLStructuredGridReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_WholeSlices: bpy.props.BoolProperty(name='WholeSlices', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ActiveTimeDataArrayName: bpy.props.StringProperty(name='ActiveTimeDataArrayName', default="TimeValue", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepRange: bpy.props.IntVectorProperty(name='TimeStepRange', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadFromInputString','m_WholeSlices','m_ActiveTimeDataArrayName','m_FileName','m_ObjectName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'ReaderErrorObserver'], []) 
    
add_class( VTKXMLStructuredGridReader )        
TYPENAMES.append('VTKXMLStructuredGridReaderType' )

#--------------------------------------------------------------
class VTKXMLTableReader(Node, PBVTK_Node):

    bl_idname = 'VTKXMLTableReaderType'
    bl_label  = 'vtkXMLTableReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ActiveTimeDataArrayName: bpy.props.StringProperty(name='ActiveTimeDataArrayName', default="TimeValue", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepRange: bpy.props.IntVectorProperty(name='TimeStepRange', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadFromInputString','m_ActiveTimeDataArrayName','m_FileName','m_ObjectName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'ReaderErrorObserver'], []) 
    
add_class( VTKXMLTableReader )        
TYPENAMES.append('VTKXMLTableReaderType' )

#--------------------------------------------------------------
class VTKXMLTreeReader(Node, PBVTK_Node):

    bl_idname = 'VTKXMLTreeReaderType'
    bl_label  = 'vtkXMLTreeReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateEdgePedigreeIds: bpy.props.BoolProperty(name='GenerateEdgePedigreeIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateVertexPedigreeIds: bpy.props.BoolProperty(name='GenerateVertexPedigreeIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaskArrays: bpy.props.BoolProperty(name='MaskArrays', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadCharData: bpy.props.BoolProperty(name='ReadCharData', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadTagName: bpy.props.BoolProperty(name='ReadTagName', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EdgePedigreeIdArrayName: bpy.props.StringProperty(name='EdgePedigreeIdArrayName', default="edge id", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VertexPedigreeIdArrayName: bpy.props.StringProperty(name='VertexPedigreeIdArrayName', default="vertex id", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_XMLString: bpy.props.StringProperty(name='XMLString', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_GenerateEdgePedigreeIds','m_GenerateVertexPedigreeIds','m_MaskArrays','m_ReadCharData','m_ReadTagName','m_EdgePedigreeIdArrayName','m_FileName','m_ObjectName','m_VertexPedigreeIdArrayName','m_XMLString',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKXMLTreeReader )        
TYPENAMES.append('VTKXMLTreeReaderType' )

#--------------------------------------------------------------
class VTKXMLUniformGridAMRReader(Node, PBVTK_Node):

    bl_idname = 'VTKXMLUniformGridAMRReaderType'
    bl_label  = 'vtkXMLUniformGridAMRReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ActiveTimeDataArrayName: bpy.props.StringProperty(name='ActiveTimeDataArrayName', default="TimeValue", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumLevelsToReadByDefault: bpy.props.IntProperty(name='MaximumLevelsToReadByDefault', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PieceDistribution: bpy.props.IntProperty(name='PieceDistribution', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepRange: bpy.props.IntVectorProperty(name='TimeStepRange', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadFromInputString','m_ActiveTimeDataArrayName','m_FileName','m_ObjectName','m_MaximumLevelsToReadByDefault','m_PieceDistribution','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'ReaderErrorObserver'], []) 
    
add_class( VTKXMLUniformGridAMRReader )        
TYPENAMES.append('VTKXMLUniformGridAMRReaderType' )

#--------------------------------------------------------------
class VTKXMLUnstructuredGridReader(Node, PBVTK_Node):

    bl_idname = 'VTKXMLUnstructuredGridReaderType'
    bl_label  = 'vtkXMLUnstructuredGridReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ActiveTimeDataArrayName: bpy.props.StringProperty(name='ActiveTimeDataArrayName', default="TimeValue", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepRange: bpy.props.IntVectorProperty(name='TimeStepRange', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadFromInputString','m_ActiveTimeDataArrayName','m_FileName','m_ObjectName','m_TimeStep','m_TimeStepRange',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'ReaderErrorObserver'], []) 
    
add_class( VTKXMLUnstructuredGridReader )        
TYPENAMES.append('VTKXMLUnstructuredGridReaderType' )

#--------------------------------------------------------------
class VTKXYZMolReader(Node, PBVTK_Node):

    bl_idname = 'VTKXYZMolReaderType'
    bl_label  = 'vtkXYZMolReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStep: bpy.props.IntProperty(name='TimeStep', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BScale: bpy.props.FloatProperty(name='BScale', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HBScale: bpy.props.FloatProperty(name='HBScale', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName','m_TimeStep','m_BScale','m_HBScale',]
    def m_connections( self ):
        return ([], ['output 0', 'output 1'], ['ContainerAlgorithm'], []) 
    
add_class( VTKXYZMolReader )        
TYPENAMES.append('VTKXYZMolReaderType' )

#--------------------------------------------------------------
class VTKXYZMolReader2(Node, PBVTK_Node):

    bl_idname = 'VTKXYZMolReader2Type'
    bl_label  = 'vtkXYZMolReader2'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FileName','m_ObjectName',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKXYZMolReader2 )        
TYPENAMES.append('VTKXYZMolReader2Type' )

#--------------------------------------------------------------
class VTKXdmfReader(Node, PBVTK_Node):

    bl_idname = 'VTKXdmfReaderType'
    bl_label  = 'vtkXdmfReader'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReadFromInputString: bpy.props.BoolProperty(name='ReadFromInputString', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DomainName: bpy.props.StringProperty(name='DomainName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FileName: bpy.props.StringProperty(name='FileName', default="", subtype='FILE_PATH', update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Stride: bpy.props.IntVectorProperty(name='Stride', default=[1, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReadFromInputString','m_DomainName','m_FileName','m_ObjectName','m_Stride',]
    def m_connections( self ):
        return ([], ['output'], ['ContainerAlgorithm', 'InputArray'], []) 
    
add_class( VTKXdmfReader )        
TYPENAMES.append('VTKXdmfReaderType' )

#--------------------------------------------------------------
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( PBVTK_NodeCategory( 'Reader', 'Reader', items=menu_items) )