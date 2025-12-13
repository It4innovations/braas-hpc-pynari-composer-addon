# Generated definitions for VTK class group: Filter1
# VTK version: 9.5.2

from .core import *    
TYPENAMES = []

#--------------------------------------------------------------
class VTK3DLinearGridCrinkleExtractor(Node, PBVTK_Node):

    bl_idname = 'VTK3DLinearGridCrinkleExtractorType'
    bl_label  = 'vtk3DLinearGridCrinkleExtractor'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CopyCellData: bpy.props.BoolProperty(name='CopyCellData', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CopyPointData: bpy.props.BoolProperty(name='CopyPointData', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RemoveUnusedPoints: bpy.props.BoolProperty(name='RemoveUnusedPoints', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SequentialProcessing: bpy.props.BoolProperty(name='SequentialProcessing', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CopyCellData','m_CopyPointData','m_RemoveUnusedPoints','m_SequentialProcessing','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'ImplicitFunction'], []) 
    
add_class( VTK3DLinearGridCrinkleExtractor )        
TYPENAMES.append('VTK3DLinearGridCrinkleExtractorType' )

#--------------------------------------------------------------
class VTK3DLinearGridPlaneCutter(Node, PBVTK_Node):

    bl_idname = 'VTK3DLinearGridPlaneCutterType'
    bl_label  = 'vtk3DLinearGridPlaneCutter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeNormals: bpy.props.BoolProperty(name='ComputeNormals', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InterpolateAttributes: bpy.props.BoolProperty(name='InterpolateAttributes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MergePoints: bpy.props.BoolProperty(name='MergePoints', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SequentialProcessing: bpy.props.BoolProperty(name='SequentialProcessing', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeNormals','m_InterpolateAttributes','m_MergePoints','m_SequentialProcessing','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['Plane', 'ContainerAlgorithm'], []) 
    
add_class( VTK3DLinearGridPlaneCutter )        
TYPENAMES.append('VTK3DLinearGridPlaneCutterType' )

#--------------------------------------------------------------
class VTKAMRCutPlane(Node, PBVTK_Node):

    bl_idname = 'VTKAMRCutPlaneType'
    bl_label  = 'vtkAMRCutPlane'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseNativeCutter: bpy.props.BoolProperty(name='UseNativeCutter', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LevelOfResolution: bpy.props.IntProperty(name='LevelOfResolution', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_UseNativeCutter','m_ObjectName','m_LevelOfResolution',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAMRCutPlane )        
TYPENAMES.append('VTKAMRCutPlaneType' )

#--------------------------------------------------------------
class VTKAMRResampleFilter(Node, PBVTK_Node):

    bl_idname = 'VTKAMRResampleFilterType'
    bl_label  = 'vtkAMRResampleFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseBiasVector: bpy.props.BoolProperty(name='UseBiasVector', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DemandDrivenMode: bpy.props.IntProperty(name='DemandDrivenMode', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfPartitions: bpy.props.IntProperty(name='NumberOfPartitions', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TransferToNodes: bpy.props.IntProperty(name='TransferToNodes', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfSamples: bpy.props.IntVectorProperty(name='NumberOfSamples', default=[10, 10, 10], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BiasVector: bpy.props.FloatVectorProperty(name='BiasVector', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Max: bpy.props.FloatVectorProperty(name='Max', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Min: bpy.props.FloatVectorProperty(name='Min', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_UseBiasVector','m_ObjectName','m_DemandDrivenMode','m_NumberOfPartitions','m_TransferToNodes','m_NumberOfSamples','m_BiasVector','m_Max','m_Min',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAMRResampleFilter )        
TYPENAMES.append('VTKAMRResampleFilterType' )

#--------------------------------------------------------------
class VTKAMRSliceFilter(Node, PBVTK_Node):

    bl_idname = 'VTKAMRSliceFilterType'
    bl_label  = 'vtkAMRSliceFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaxResolution: bpy.props.IntProperty(name='MaxResolution', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Normal: bpy.props.IntProperty(name='Normal', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OffsetFromOrigin: bpy.props.FloatProperty(name='OffsetFromOrigin', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_MaxResolution','m_Normal','m_OffsetFromOrigin',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAMRSliceFilter )        
TYPENAMES.append('VTKAMRSliceFilterType' )

#--------------------------------------------------------------
class VTKAMRToMultiBlockFilter(Node, PBVTK_Node):

    bl_idname = 'VTKAMRToMultiBlockFilterType'
    bl_label  = 'vtkAMRToMultiBlockFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAMRToMultiBlockFilter )        
TYPENAMES.append('VTKAMRToMultiBlockFilterType' )

#--------------------------------------------------------------
class VTKAdaptiveDataSetSurfaceFilter(Node, PBVTK_Node):

    bl_idname = 'VTKAdaptiveDataSetSurfaceFilterType'
    bl_label  = 'vtkAdaptiveDataSetSurfaceFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BBSelection: bpy.props.BoolProperty(name='BBSelection', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CellClipping: bpy.props.BoolProperty(name='CellClipping', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CircleSelection: bpy.props.BoolProperty(name='CircleSelection', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Delegation: bpy.props.BoolProperty(name='Delegation', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ExtentClipping: bpy.props.BoolProperty(name='ExtentClipping', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FastMode: bpy.props.BoolProperty(name='FastMode', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Merging: bpy.props.BoolProperty(name='Merging', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassThroughCellIds: bpy.props.BoolProperty(name='PassThroughCellIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassThroughPointIds: bpy.props.BoolProperty(name='PassThroughPointIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PointClipping: bpy.props.BoolProperty(name='PointClipping', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RemoveGhostInterfaces: bpy.props.BoolProperty(name='RemoveGhostInterfaces', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ViewPointDepend: bpy.props.BoolProperty(name='ViewPointDepend', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OriginalCellIdsName: bpy.props.StringProperty(name='OriginalCellIdsName', default="vtkOriginalCellIds", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OriginalPointIdsName: bpy.props.StringProperty(name='OriginalPointIdsName', default="vtkOriginalPointIds", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CellMaximum: bpy.props.IntProperty(name='CellMaximum', default=1000000000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CellMinimum: bpy.props.IntProperty(name='CellMinimum', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DynamicDecimateLevelMax: bpy.props.IntProperty(name='DynamicDecimateLevelMax', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FixedLevelMax: bpy.props.IntProperty(name='FixedLevelMax', default=-1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MatchBoundariesIgnoringCellOrder: bpy.props.IntProperty(name='MatchBoundariesIgnoringCellOrder', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NonlinearSubdivisionLevel: bpy.props.IntProperty(name='NonlinearSubdivisionLevel', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PieceInvariant: bpy.props.IntProperty(name='PieceInvariant', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PointMaximum: bpy.props.IntProperty(name='PointMaximum', default=1000000000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PointMinimum: bpy.props.IntProperty(name='PointMinimum', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Extent: bpy.props.FloatVectorProperty(name='Extent', default=[-1e+30, 1e+30, -1e+30, 1e+30, -1e+30, 1e+30], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=26, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_BBSelection','m_CellClipping','m_CircleSelection','m_Delegation','m_ExtentClipping','m_FastMode','m_Merging','m_PassThroughCellIds','m_PassThroughPointIds','m_PointClipping','m_RemoveGhostInterfaces','m_ViewPointDepend','m_ObjectName','m_OriginalCellIdsName','m_OriginalPointIdsName','m_CellMaximum','m_CellMinimum','m_DynamicDecimateLevelMax','m_FixedLevelMax','m_MatchBoundariesIgnoringCellOrder','m_NonlinearSubdivisionLevel','m_PieceInvariant','m_PointMaximum','m_PointMinimum','m_Extent',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'Renderer'], []) 
    
add_class( VTKAdaptiveDataSetSurfaceFilter )        
TYPENAMES.append('VTKAdaptiveDataSetSurfaceFilterType' )

#--------------------------------------------------------------
class VTKAdaptiveResampleToImage(Node, PBVTK_Node):

    bl_idname = 'VTKAdaptiveResampleToImageType'
    bl_label  = 'vtkAdaptiveResampleToImage'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfImages: bpy.props.IntProperty(name='NumberOfImages', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SamplingDimensions: bpy.props.IntVectorProperty(name='SamplingDimensions', default=[64, 64, 64], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_NumberOfImages','m_SamplingDimensions',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAdaptiveResampleToImage )        
TYPENAMES.append('VTKAdaptiveResampleToImageType' )

#--------------------------------------------------------------
class VTKAdaptiveSubdivisionFilter(Node, PBVTK_Node):

    bl_idname = 'VTKAdaptiveSubdivisionFilterType'
    bl_label  = 'vtkAdaptiveSubdivisionFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumNumberOfPasses: bpy.props.IntProperty(name='MaximumNumberOfPasses', default=1000000000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumNumberOfTriangles: bpy.props.IntProperty(name='MaximumNumberOfTriangles', default=1000000000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumEdgeLength: bpy.props.FloatProperty(name='MaximumEdgeLength', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumTriangleArea: bpy.props.FloatProperty(name='MaximumTriangleArea', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_MaximumNumberOfPasses','m_MaximumNumberOfTriangles','m_MaximumEdgeLength','m_MaximumTriangleArea',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAdaptiveSubdivisionFilter )        
TYPENAMES.append('VTKAdaptiveSubdivisionFilterType' )

#--------------------------------------------------------------
class VTKAdaptiveTemporalInterpolator(Node, PBVTK_Node):

    bl_idname = 'VTKAdaptiveTemporalInterpolatorType'
    bl_label  = 'vtkAdaptiveTemporalInterpolator'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CacheData: bpy.props.BoolProperty(name='CacheData', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ResampleFactor: bpy.props.IntProperty(name='ResampleFactor', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DiscreteTimeStepInterval: bpy.props.FloatProperty(name='DiscreteTimeStepInterval', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CacheData','m_ObjectName','m_ResampleFactor','m_DiscreteTimeStepInterval',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAdaptiveTemporalInterpolator )        
TYPENAMES.append('VTKAdaptiveTemporalInterpolatorType' )

#--------------------------------------------------------------
class VTKAggregateDataSetFilter(Node, PBVTK_Node):

    bl_idname = 'VTKAggregateDataSetFilterType'
    bl_label  = 'vtkAggregateDataSetFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MergePoints: bpy.props.BoolProperty(name='MergePoints', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfTargetProcesses: bpy.props.IntProperty(name='NumberOfTargetProcesses', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_MergePoints','m_ObjectName','m_NumberOfTargetProcesses',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAggregateDataSetFilter )        
TYPENAMES.append('VTKAggregateDataSetFilterType' )

#--------------------------------------------------------------
class VTKAlignImageDataSetFilter(Node, PBVTK_Node):

    bl_idname = 'VTKAlignImageDataSetFilterType'
    bl_label  = 'vtkAlignImageDataSetFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumExtent: bpy.props.IntVectorProperty(name='MinimumExtent', default=[0, 0, 0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_MinimumExtent',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAlignImageDataSetFilter )        
TYPENAMES.append('VTKAlignImageDataSetFilterType' )

#--------------------------------------------------------------
class VTKAngularPeriodicFilter(Node, PBVTK_Node):

    bl_idname = 'VTKAngularPeriodicFilterType'
    bl_label  = 'vtkAngularPeriodicFilter'
    e_IterationMode_items=[ (x,x,x) for x in ['DirectNb', 'Max']]
    e_RotationAxis_items=[ (x,x,x) for x in ['X', 'Y', 'Z']]
    e_RotationMode_items=[ (x,x,x) for x in ['DirectAngle', 'ArrayValue']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeRotationsOnTheFly: bpy.props.BoolProperty(name='ComputeRotationsOnTheFly', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RotationArrayName: bpy.props.StringProperty(name='RotationArrayName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfPeriods: bpy.props.IntProperty(name='NumberOfPeriods', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RotationAngle: bpy.props.FloatProperty(name='RotationAngle', default=180.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_IterationMode: bpy.props.EnumProperty(name='IterationMode', default="Max", items=e_IterationMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_RotationAxis: bpy.props.EnumProperty(name='RotationAxis', default="X", items=e_RotationAxis_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_RotationMode: bpy.props.EnumProperty(name='RotationMode', default="DirectAngle", items=e_RotationMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeRotationsOnTheFly','m_ObjectName','m_RotationArrayName','m_NumberOfPeriods','m_RotationAngle','e_IterationMode','e_RotationAxis','e_RotationMode','m_Center',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAngularPeriodicFilter )        
TYPENAMES.append('VTKAngularPeriodicFilterType' )

#--------------------------------------------------------------
class VTKAnimateModes(Node, PBVTK_Node):

    bl_idname = 'VTKAnimateModesType'
    bl_label  = 'vtkAnimateModes'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AnimateVibrations: bpy.props.BoolProperty(name='AnimateVibrations', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DisplacementPreapplied: bpy.props.BoolProperty(name='DisplacementPreapplied', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ModeShape: bpy.props.IntProperty(name='ModeShape', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DisplacementMagnitude: bpy.props.FloatProperty(name='DisplacementMagnitude', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AnimateVibrations','m_DisplacementPreapplied','m_ObjectName','m_ModeShape','m_DisplacementMagnitude',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAnimateModes )        
TYPENAMES.append('VTKAnimateModesType' )

#--------------------------------------------------------------
class VTKAnnotationLayersAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKAnnotationLayersAlgorithmType'
    bl_label  = 'vtkAnnotationLayersAlgorithm'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAnnotationLayersAlgorithm )        
TYPENAMES.append('VTKAnnotationLayersAlgorithmType' )

#--------------------------------------------------------------
class VTKAppendArcLength(Node, PBVTK_Node):

    bl_idname = 'VTKAppendArcLengthType'
    bl_label  = 'vtkAppendArcLength'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAppendArcLength )        
TYPENAMES.append('VTKAppendArcLengthType' )

#--------------------------------------------------------------
class VTKAppendCompositeDataLeaves(Node, PBVTK_Node):

    bl_idname = 'VTKAppendCompositeDataLeavesType'
    bl_label  = 'vtkAppendCompositeDataLeaves'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AppendFieldData: bpy.props.BoolProperty(name='AppendFieldData', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AppendFieldData','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAppendCompositeDataLeaves )        
TYPENAMES.append('VTKAppendCompositeDataLeavesType' )

#--------------------------------------------------------------
class VTKAppendDataSets(Node, PBVTK_Node):

    bl_idname = 'VTKAppendDataSetsType'
    bl_label  = 'vtkAppendDataSets'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MergePoints: bpy.props.BoolProperty(name='MergePoints', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ToleranceIsAbsolute: bpy.props.BoolProperty(name='ToleranceIsAbsolute', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputDataSetType: bpy.props.IntProperty(name='OutputDataSetType', default=4, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_MergePoints','m_ToleranceIsAbsolute','m_ObjectName','m_OutputDataSetType','m_Tolerance',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAppendDataSets )        
TYPENAMES.append('VTKAppendDataSetsType' )

#--------------------------------------------------------------
class VTKAppendFilter(Node, PBVTK_Node):

    bl_idname = 'VTKAppendFilterType'
    bl_label  = 'vtkAppendFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MergePoints: bpy.props.BoolProperty(name='MergePoints', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ToleranceIsAbsolute: bpy.props.BoolProperty(name='ToleranceIsAbsolute', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_MergePoints','m_ToleranceIsAbsolute','m_ObjectName','m_Tolerance',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAppendFilter )        
TYPENAMES.append('VTKAppendFilterType' )

#--------------------------------------------------------------
class VTKAppendLocationAttributes(Node, PBVTK_Node):

    bl_idname = 'VTKAppendLocationAttributesType'
    bl_label  = 'vtkAppendLocationAttributes'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AppendCellCenters: bpy.props.BoolProperty(name='AppendCellCenters', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AppendPointLocations: bpy.props.BoolProperty(name='AppendPointLocations', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AppendCellCenters','m_AppendPointLocations','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAppendLocationAttributes )        
TYPENAMES.append('VTKAppendLocationAttributesType' )

#--------------------------------------------------------------
class VTKAppendPartitionedDataSetCollection(Node, PBVTK_Node):

    bl_idname = 'VTKAppendPartitionedDataSetCollectionType'
    bl_label  = 'vtkAppendPartitionedDataSetCollection'
    e_AppendMode_items=[ (x,x,x) for x in ['AppendPartitions', 'MergePartitions']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AppendFieldData: bpy.props.BoolProperty(name='AppendFieldData', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_AppendMode: bpy.props.EnumProperty(name='AppendMode', default="AppendPartitions", items=e_AppendMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AppendFieldData','m_ObjectName','e_AppendMode',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAppendPartitionedDataSetCollection )        
TYPENAMES.append('VTKAppendPartitionedDataSetCollectionType' )

#--------------------------------------------------------------
class VTKAppendPoints(Node, PBVTK_Node):

    bl_idname = 'VTKAppendPointsType'
    bl_label  = 'vtkAppendPoints'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InputIdArrayName: bpy.props.StringProperty(name='InputIdArrayName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_InputIdArrayName','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAppendPoints )        
TYPENAMES.append('VTKAppendPointsType' )

#--------------------------------------------------------------
class VTKAppendPolyData(Node, PBVTK_Node):

    bl_idname = 'VTKAppendPolyDataType'
    bl_label  = 'vtkAppendPolyData'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ParallelStreaming: bpy.props.BoolProperty(name='ParallelStreaming', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UserManagedInputs: bpy.props.BoolProperty(name='UserManagedInputs', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ParallelStreaming','m_UserManagedInputs','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAppendPolyData )        
TYPENAMES.append('VTKAppendPolyDataType' )

#--------------------------------------------------------------
class VTKAppendSelection(Node, PBVTK_Node):

    bl_idname = 'VTKAppendSelectionType'
    bl_label  = 'vtkAppendSelection'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AppendByUnion: bpy.props.BoolProperty(name='AppendByUnion', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Inverse: bpy.props.BoolProperty(name='Inverse', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UserManagedInputs: bpy.props.BoolProperty(name='UserManagedInputs', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Expression: bpy.props.StringProperty(name='Expression', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AppendByUnion','m_Inverse','m_UserManagedInputs','m_Expression','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAppendSelection )        
TYPENAMES.append('VTKAppendSelectionType' )

#--------------------------------------------------------------
class VTKArcPlotter(Node, PBVTK_Node):

    bl_idname = 'VTKArcPlotterType'
    bl_label  = 'vtkArcPlotter'
    e_PlotMode_items=[ (x,x,x) for x in ['PlotScalars', 'PlotVectors', 'PlotNormals', 'PlotTCoords', 'PlotTensors', 'PlotFieldData']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseDefaultNormal: bpy.props.BoolProperty(name='UseDefaultNormal', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldDataArray: bpy.props.IntProperty(name='FieldDataArray', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PlotComponent: bpy.props.IntProperty(name='PlotComponent', default=-1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Height: bpy.props.FloatProperty(name='Height', default=0.5, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Offset: bpy.props.FloatProperty(name='Offset', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Radius: bpy.props.FloatProperty(name='Radius', default=0.5, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_PlotMode: bpy.props.EnumProperty(name='PlotMode', default="PlotScalars", items=e_PlotMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DefaultNormal: bpy.props.FloatVectorProperty(name='DefaultNormal', default=[0.0, 0.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_UseDefaultNormal','m_ObjectName','m_FieldDataArray','m_PlotComponent','m_Height','m_Offset','m_Radius','e_PlotMode','m_DefaultNormal',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKArcPlotter )        
TYPENAMES.append('VTKArcPlotterType' )

#--------------------------------------------------------------
class VTKArrayCalculator(Node, PBVTK_Node):

    bl_idname = 'VTKArrayCalculatorType'
    bl_label  = 'vtkArrayCalculator'
    e_AttributeType_items=[ (x,x,x) for x in ['Default', 'PointData', 'CellData', 'VertexData', 'EdgeData', 'RowData']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CoordinateResults: bpy.props.BoolProperty(name='CoordinateResults', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IgnoreMissingArrays: bpy.props.BoolProperty(name='IgnoreMissingArrays', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReplaceInvalidValues: bpy.props.BoolProperty(name='ReplaceInvalidValues', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ResultNormals: bpy.props.BoolProperty(name='ResultNormals', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ResultTCoords: bpy.props.BoolProperty(name='ResultTCoords', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Function: bpy.props.StringProperty(name='Function', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ResultArrayName: bpy.props.StringProperty(name='ResultArrayName', default="resultArray", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ResultArrayType: bpy.props.IntProperty(name='ResultArrayType', default=11, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReplacementValue: bpy.props.FloatProperty(name='ReplacementValue', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_AttributeType: bpy.props.EnumProperty(name='AttributeType', default="Default", items=e_AttributeType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CoordinateResults','m_IgnoreMissingArrays','m_ReplaceInvalidValues','m_ResultNormals','m_ResultTCoords','m_Function','m_ObjectName','m_ResultArrayName','m_ResultArrayType','m_ReplacementValue','e_AttributeType',]
    def m_connections( self ):
        return (['input'], ['output'], ['FunctionParserType', 'ContainerAlgorithm'], []) 
    
add_class( VTKArrayCalculator )        
TYPENAMES.append('VTKArrayCalculatorType' )

#--------------------------------------------------------------
class VTKArrayDataAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKArrayDataAlgorithmType'
    bl_label  = 'vtkArrayDataAlgorithm'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKArrayDataAlgorithm )        
TYPENAMES.append('VTKArrayDataAlgorithmType' )

#--------------------------------------------------------------
class VTKArrayRename(Node, PBVTK_Node):

    bl_idname = 'VTKArrayRenameType'
    bl_label  = 'vtkArrayRename'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKArrayRename )        
TYPENAMES.append('VTKArrayRenameType' )

#--------------------------------------------------------------
class VTKAssignAttribute(Node, PBVTK_Node):

    bl_idname = 'VTKAssignAttributeType'
    bl_label  = 'vtkAssignAttribute'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAssignAttribute )        
TYPENAMES.append('VTKAssignAttributeType' )

#--------------------------------------------------------------
class VTKAttributeDataToFieldDataFilter(Node, PBVTK_Node):

    bl_idname = 'VTKAttributeDataToFieldDataFilterType'
    bl_label  = 'vtkAttributeDataToFieldDataFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassAttributeData: bpy.props.BoolProperty(name='PassAttributeData', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_PassAttributeData','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAttributeDataToFieldDataFilter )        
TYPENAMES.append('VTKAttributeDataToFieldDataFilterType' )

#--------------------------------------------------------------
class VTKAttributeDataToTableFilter(Node, PBVTK_Node):

    bl_idname = 'VTKAttributeDataToTableFilterType'
    bl_label  = 'vtkAttributeDataToTableFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AddMetaData: bpy.props.BoolProperty(name='AddMetaData', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateCellConnectivity: bpy.props.BoolProperty(name='GenerateCellConnectivity', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateOriginalIds: bpy.props.BoolProperty(name='GenerateOriginalIds', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldAssociation: bpy.props.IntProperty(name='FieldAssociation', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AddMetaData','m_GenerateCellConnectivity','m_GenerateOriginalIds','m_ObjectName','m_FieldAssociation',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAttributeDataToTableFilter )        
TYPENAMES.append('VTKAttributeDataToTableFilterType' )

#--------------------------------------------------------------
class VTKAttributeSmoothingFilter(Node, PBVTK_Node):

    bl_idname = 'VTKAttributeSmoothingFilterType'
    bl_label  = 'vtkAttributeSmoothingFilter'
    e_SmoothingStrategy_items=[ (x,x,x) for x in ['AllPoints', 'AllButBoundary', 'AdjacentToBoundary', 'SmoothingMask']]
    e_WeightsType_items=[ (x,x,x) for x in ['Average', 'Distance', 'Distance2']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfIterations: bpy.props.IntProperty(name='NumberOfIterations', default=5, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RelaxationFactor: bpy.props.FloatProperty(name='RelaxationFactor', default=0.1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SmoothingStrategy: bpy.props.EnumProperty(name='SmoothingStrategy', default="AllPoints", items=e_SmoothingStrategy_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_WeightsType: bpy.props.EnumProperty(name='WeightsType', default="Distance2", items=e_WeightsType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_NumberOfIterations','m_RelaxationFactor','e_SmoothingStrategy','e_WeightsType',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'SmoothingMask'], []) 
    
add_class( VTKAttributeSmoothingFilter )        
TYPENAMES.append('VTKAttributeSmoothingFilterType' )

#--------------------------------------------------------------
class VTKAxisAlignedReflectionFilter(Node, PBVTK_Node):

    bl_idname = 'VTKAxisAlignedReflectionFilterType'
    bl_label  = 'vtkAxisAlignedReflectionFilter'
    e_PlaneMode_items=[ (x,x,x) for x in ['Plane', 'XMin', 'YMin', 'ZMin', 'XMax', 'YMax', 'ZMax']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CopyInput: bpy.props.BoolProperty(name='CopyInput', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReflectAllInputArrays: bpy.props.BoolProperty(name='ReflectAllInputArrays', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_PlaneMode: bpy.props.EnumProperty(name='PlaneMode', default="Plane", items=e_PlaneMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CopyInput','m_ReflectAllInputArrays','m_ObjectName','e_PlaneMode',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'ReflectionPlane'], []) 
    
add_class( VTKAxisAlignedReflectionFilter )        
TYPENAMES.append('VTKAxisAlignedReflectionFilterType' )

#--------------------------------------------------------------
class VTKAxisAlignedTransformFilter(Node, PBVTK_Node):

    bl_idname = 'VTKAxisAlignedTransformFilterType'
    bl_label  = 'vtkAxisAlignedTransformFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RotationAngle: bpy.props.IntProperty(name='RotationAngle', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RotationAxis: bpy.props.IntProperty(name='RotationAxis', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Scale: bpy.props.FloatVectorProperty(name='Scale', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Translation: bpy.props.FloatVectorProperty(name='Translation', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_RotationAngle','m_RotationAxis','m_Scale','m_Translation',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKAxisAlignedTransformFilter )        
TYPENAMES.append('VTKAxisAlignedTransformFilterType' )

#--------------------------------------------------------------
class VTKBinnedDecimation(Node, PBVTK_Node):

    bl_idname = 'VTKBinnedDecimationType'
    bl_label  = 'vtkBinnedDecimation'
    e_PointGenerationMode_items=[ (x,x,x) for x in ['UseInputPoints', 'BinPoints', 'BinCenters', 'BinAverages']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AutoAdjustNumberOfDivisions: bpy.props.BoolProperty(name='AutoAdjustNumberOfDivisions', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ProduceCellData: bpy.props.BoolProperty(name='ProduceCellData', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ProducePointData: bpy.props.BoolProperty(name='ProducePointData', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfXDivisions: bpy.props.IntProperty(name='NumberOfXDivisions', default=256, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfYDivisions: bpy.props.IntProperty(name='NumberOfYDivisions', default=256, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfZDivisions: bpy.props.IntProperty(name='NumberOfZDivisions', default=256, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_PointGenerationMode: bpy.props.EnumProperty(name='PointGenerationMode', default="BinPoints", items=e_PointGenerationMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DivisionOrigin: bpy.props.FloatVectorProperty(name='DivisionOrigin', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DivisionSpacing: bpy.props.FloatVectorProperty(name='DivisionSpacing', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AutoAdjustNumberOfDivisions','m_ProduceCellData','m_ProducePointData','m_ObjectName','m_NumberOfXDivisions','m_NumberOfYDivisions','m_NumberOfZDivisions','e_PointGenerationMode','m_DivisionOrigin','m_DivisionSpacing',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKBinnedDecimation )        
TYPENAMES.append('VTKBinnedDecimationType' )

#--------------------------------------------------------------
class VTKBlankStructuredGrid(Node, PBVTK_Node):

    bl_idname = 'VTKBlankStructuredGridType'
    bl_label  = 'vtkBlankStructuredGrid'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ArrayName: bpy.props.StringProperty(name='ArrayName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ArrayId: bpy.props.IntProperty(name='ArrayId', default=-1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Component: bpy.props.IntProperty(name='Component', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaxBlankingValue: bpy.props.FloatProperty(name='MaxBlankingValue', default=1e+30, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinBlankingValue: bpy.props.FloatProperty(name='MinBlankingValue', default=1e+30, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ArrayName','m_ObjectName','m_ArrayId','m_Component','m_MaxBlankingValue','m_MinBlankingValue',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKBlankStructuredGrid )        
TYPENAMES.append('VTKBlankStructuredGridType' )

#--------------------------------------------------------------
class VTKBlockIdScalars(Node, PBVTK_Node):

    bl_idname = 'VTKBlockIdScalarsType'
    bl_label  = 'vtkBlockIdScalars'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKBlockIdScalars )        
TYPENAMES.append('VTKBlockIdScalarsType' )

#--------------------------------------------------------------
class VTKBoundaryMeshQuality(Node, PBVTK_Node):

    bl_idname = 'VTKBoundaryMeshQualityType'
    bl_label  = 'vtkBoundaryMeshQuality'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AngleFaceNormalAndCellCenterToFaceCenterVector: bpy.props.BoolProperty(name='AngleFaceNormalAndCellCenterToFaceCenterVector', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DistanceFromCellCenterToFaceCenter: bpy.props.BoolProperty(name='DistanceFromCellCenterToFaceCenter', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DistanceFromCellCenterToFacePlane: bpy.props.BoolProperty(name='DistanceFromCellCenterToFacePlane', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AngleFaceNormalAndCellCenterToFaceCenterVector','m_DistanceFromCellCenterToFaceCenter','m_DistanceFromCellCenterToFacePlane','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKBoundaryMeshQuality )        
TYPENAMES.append('VTKBoundaryMeshQualityType' )

#--------------------------------------------------------------
class VTKBrownianPoints(Node, PBVTK_Node):

    bl_idname = 'VTKBrownianPointsType'
    bl_label  = 'vtkBrownianPoints'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumSpeed: bpy.props.FloatProperty(name='MaximumSpeed', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumSpeed: bpy.props.FloatProperty(name='MinimumSpeed', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_MaximumSpeed','m_MinimumSpeed',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKBrownianPoints )        
TYPENAMES.append('VTKBrownianPointsType' )

#--------------------------------------------------------------
class VTKButterflySubdivisionFilter(Node, PBVTK_Node):

    bl_idname = 'VTKButterflySubdivisionFilterType'
    bl_label  = 'vtkButterflySubdivisionFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CheckForTriangles: bpy.props.BoolProperty(name='CheckForTriangles', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfSubdivisions: bpy.props.IntProperty(name='NumberOfSubdivisions', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CheckForTriangles','m_ObjectName','m_NumberOfSubdivisions',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKButterflySubdivisionFilter )        
TYPENAMES.append('VTKButterflySubdivisionFilterType' )

#--------------------------------------------------------------
class VTKCastToConcrete(Node, PBVTK_Node):

    bl_idname = 'VTKCastToConcreteType'
    bl_label  = 'vtkCastToConcrete'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCastToConcrete )        
TYPENAMES.append('VTKCastToConcreteType' )

#--------------------------------------------------------------
class VTKCellCenters(Node, PBVTK_Node):

    bl_idname = 'VTKCellCentersType'
    bl_label  = 'vtkCellCenters'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ConvertGhostCellsToGhostPoints: bpy.props.BoolProperty(name='ConvertGhostCellsToGhostPoints', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CopyArrays: bpy.props.BoolProperty(name='CopyArrays', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VertexCells: bpy.props.BoolProperty(name='VertexCells', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ConvertGhostCellsToGhostPoints','m_CopyArrays','m_VertexCells','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCellCenters )        
TYPENAMES.append('VTKCellCentersType' )

#--------------------------------------------------------------
class VTKCellDataToPointData(Node, PBVTK_Node):

    bl_idname = 'VTKCellDataToPointDataType'
    bl_label  = 'vtkCellDataToPointData'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassCellData: bpy.props.BoolProperty(name='PassCellData', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PieceInvariant: bpy.props.BoolProperty(name='PieceInvariant', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ProcessAllArrays: bpy.props.BoolProperty(name='ProcessAllArrays', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ContributingCellOption: bpy.props.IntProperty(name='ContributingCellOption', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_PassCellData','m_PieceInvariant','m_ProcessAllArrays','m_ObjectName','m_ContributingCellOption',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCellDataToPointData )        
TYPENAMES.append('VTKCellDataToPointDataType' )

#--------------------------------------------------------------
class VTKCellDerivatives(Node, PBVTK_Node):

    bl_idname = 'VTKCellDerivativesType'
    bl_label  = 'vtkCellDerivatives'
    e_TensorMode_items=[ (x,x,x) for x in ['PassTensors', 'ComputeGradient', 'ComputeStrain', 'ComputeGreenLagrangeStrain']]
    e_VectorMode_items=[ (x,x,x) for x in ['PassVectors', 'ComputeGradient', 'ComputeVorticity']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_TensorMode: bpy.props.EnumProperty(name='TensorMode', default="ComputeGradient", items=e_TensorMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_VectorMode: bpy.props.EnumProperty(name='VectorMode', default="ComputeGradient", items=e_VectorMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','e_TensorMode','e_VectorMode',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCellDerivatives )        
TYPENAMES.append('VTKCellDerivativesType' )

#--------------------------------------------------------------
class VTKCellGridAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKCellGridAlgorithmType'
    bl_label  = 'vtkCellGridAlgorithm'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCellGridAlgorithm )        
TYPENAMES.append('VTKCellGridAlgorithmType' )

#--------------------------------------------------------------
class VTKCellGridCellCenters(Node, PBVTK_Node):

    bl_idname = 'VTKCellGridCellCentersType'
    bl_label  = 'vtkCellGridCellCenters'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCellGridCellCenters )        
TYPENAMES.append('VTKCellGridCellCentersType' )

#--------------------------------------------------------------
class VTKCellGridComputeSides(Node, PBVTK_Node):

    bl_idname = 'VTKCellGridComputeSidesType'
    bl_label  = 'vtkCellGridComputeSides'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OmitSidesForRenderableInputs: bpy.props.BoolProperty(name='OmitSidesForRenderableInputs', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PreserveRenderableInputs: bpy.props.BoolProperty(name='PreserveRenderableInputs', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputDimensionControl: bpy.props.IntProperty(name='OutputDimensionControl', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_OmitSidesForRenderableInputs','m_PreserveRenderableInputs','m_ObjectName','m_OutputDimensionControl',]
    def m_connections( self ):
        return (['input'], ['output'], ['Strategy', 'ContainerAlgorithm', 'SelectionType'], []) 
    
add_class( VTKCellGridComputeSides )        
TYPENAMES.append('VTKCellGridComputeSidesType' )

#--------------------------------------------------------------
class VTKCellGridElevation(Node, PBVTK_Node):

    bl_idname = 'VTKCellGridElevationType'
    bl_label  = 'vtkCellGridElevation'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AttributeName: bpy.props.StringProperty(name='AttributeName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfAxes: bpy.props.IntProperty(name='NumberOfAxes', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Shock: bpy.props.FloatProperty(name='Shock', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Axis: bpy.props.FloatVectorProperty(name='Axis', default=[0.0, 0.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Origin: bpy.props.FloatVectorProperty(name='Origin', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AttributeName','m_ObjectName','m_NumberOfAxes','m_Shock','m_Axis','m_Origin',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCellGridElevation )        
TYPENAMES.append('VTKCellGridElevationType' )

#--------------------------------------------------------------
class VTKCellGridToUnstructuredGrid(Node, PBVTK_Node):

    bl_idname = 'VTKCellGridToUnstructuredGridType'
    bl_label  = 'vtkCellGridToUnstructuredGrid'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCellGridToUnstructuredGrid )        
TYPENAMES.append('VTKCellGridToUnstructuredGridType' )

#--------------------------------------------------------------
class VTKCellGridTransform(Node, PBVTK_Node):

    bl_idname = 'VTKCellGridTransformType'
    bl_label  = 'vtkCellGridTransform'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCellGridTransform )        
TYPENAMES.append('VTKCellGridTransformType' )

#--------------------------------------------------------------
class VTKCellGridWarp(Node, PBVTK_Node):

    bl_idname = 'VTKCellGridWarpType'
    bl_label  = 'vtkCellGridWarp'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScaleFactor: bpy.props.FloatProperty(name='ScaleFactor', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_ScaleFactor',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCellGridWarp )        
TYPENAMES.append('VTKCellGridWarpType' )

#--------------------------------------------------------------
class VTKCellQuality(Node, PBVTK_Node):

    bl_idname = 'VTKCellQualityType'
    bl_label  = 'vtkCellQuality'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UndefinedQuality: bpy.props.FloatProperty(name='UndefinedQuality', default=-1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UnsupportedGeometry: bpy.props.FloatProperty(name='UnsupportedGeometry', default=-1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_UndefinedQuality','m_UnsupportedGeometry',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCellQuality )        
TYPENAMES.append('VTKCellQualityType' )

#--------------------------------------------------------------
class VTKCellSizeFilter(Node, PBVTK_Node):

    bl_idname = 'VTKCellSizeFilterType'
    bl_label  = 'vtkCellSizeFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeArea: bpy.props.BoolProperty(name='ComputeArea', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeLength: bpy.props.BoolProperty(name='ComputeLength', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeSum: bpy.props.BoolProperty(name='ComputeSum', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeVertexCount: bpy.props.BoolProperty(name='ComputeVertexCount', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeVolume: bpy.props.BoolProperty(name='ComputeVolume', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AreaArrayName: bpy.props.StringProperty(name='AreaArrayName', default="Area", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LengthArrayName: bpy.props.StringProperty(name='LengthArrayName', default="Length", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VertexCountArrayName: bpy.props.StringProperty(name='VertexCountArrayName', default="VertexCount", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VolumeArrayName: bpy.props.StringProperty(name='VolumeArrayName', default="Volume", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeArea','m_ComputeLength','m_ComputeSum','m_ComputeVertexCount','m_ComputeVolume','m_AreaArrayName','m_LengthArrayName','m_ObjectName','m_VertexCountArrayName','m_VolumeArrayName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCellSizeFilter )        
TYPENAMES.append('VTKCellSizeFilterType' )

#--------------------------------------------------------------
class VTKCellValidator(Node, PBVTK_Node):

    bl_idname = 'VTKCellValidatorType'
    bl_label  = 'vtkCellValidator'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=1.1920928955078125e-07, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_Tolerance',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCellValidator )        
TYPENAMES.append('VTKCellValidatorType' )

#--------------------------------------------------------------
class VTKCheckerboardSplatter(Node, PBVTK_Node):

    bl_idname = 'VTKCheckerboardSplatterType'
    bl_label  = 'vtkCheckerboardSplatter'
    e_AccumulationMode_items=[ (x,x,x) for x in ['Min', 'Max', 'Sum']]
    e_OutputScalarType_items=[ (x,x,x) for x in ['Float', 'Double']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Capping: bpy.props.BoolProperty(name='Capping', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NormalWarping: bpy.props.BoolProperty(name='NormalWarping', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarWarping: bpy.props.BoolProperty(name='ScalarWarping', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Footprint: bpy.props.IntProperty(name='Footprint', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumDimension: bpy.props.IntProperty(name='MaximumDimension', default=50, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ParallelSplatCrossover: bpy.props.IntProperty(name='ParallelSplatCrossover', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CapValue: bpy.props.FloatProperty(name='CapValue', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Eccentricity: bpy.props.FloatProperty(name='Eccentricity', default=2.5, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ExponentFactor: bpy.props.FloatProperty(name='ExponentFactor', default=-5.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NullValue: bpy.props.FloatProperty(name='NullValue', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Radius: bpy.props.FloatProperty(name='Radius', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScaleFactor: bpy.props.FloatProperty(name='ScaleFactor', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_AccumulationMode: bpy.props.EnumProperty(name='AccumulationMode', default="Max", items=e_AccumulationMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_OutputScalarType: bpy.props.EnumProperty(name='OutputScalarType', default="Float", items=e_OutputScalarType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SampleDimensions: bpy.props.IntVectorProperty(name='SampleDimensions', default=[50, 50, 50], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ModelBounds: bpy.props.FloatVectorProperty(name='ModelBounds', default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Capping','m_NormalWarping','m_ScalarWarping','m_ObjectName','m_Footprint','m_MaximumDimension','m_ParallelSplatCrossover','m_CapValue','m_Eccentricity','m_ExponentFactor','m_NullValue','m_Radius','m_ScaleFactor','e_AccumulationMode','e_OutputScalarType','m_SampleDimensions','m_ModelBounds',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCheckerboardSplatter )        
TYPENAMES.append('VTKCheckerboardSplatterType' )

#--------------------------------------------------------------
class VTKCleanArrays(Node, PBVTK_Node):

    bl_idname = 'VTKCleanArraysType'
    bl_label  = 'vtkCleanArrays'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FillPartialArrays: bpy.props.BoolProperty(name='FillPartialArrays', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MarkFilledPartialArrays: bpy.props.BoolProperty(name='MarkFilledPartialArrays', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FillPartialArrays','m_MarkFilledPartialArrays','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCleanArrays )        
TYPENAMES.append('VTKCleanArraysType' )

#--------------------------------------------------------------
class VTKCleanPolyData(Node, PBVTK_Node):

    bl_idname = 'VTKCleanPolyDataType'
    bl_label  = 'vtkCleanPolyData'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ConvertLinesToPoints: bpy.props.BoolProperty(name='ConvertLinesToPoints', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ConvertPolysToLines: bpy.props.BoolProperty(name='ConvertPolysToLines', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ConvertStripsToPolys: bpy.props.BoolProperty(name='ConvertStripsToPolys', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PieceInvariant: bpy.props.BoolProperty(name='PieceInvariant', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PointMerging: bpy.props.BoolProperty(name='PointMerging', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ToleranceIsAbsolute: bpy.props.BoolProperty(name='ToleranceIsAbsolute', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AbsoluteTolerance: bpy.props.FloatProperty(name='AbsoluteTolerance', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ConvertLinesToPoints','m_ConvertPolysToLines','m_ConvertStripsToPolys','m_PieceInvariant','m_PointMerging','m_ToleranceIsAbsolute','m_ObjectName','m_AbsoluteTolerance','m_Tolerance',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCleanPolyData )        
TYPENAMES.append('VTKCleanPolyDataType' )

#--------------------------------------------------------------
class VTKCleanUnstructuredGrid(Node, PBVTK_Node):

    bl_idname = 'VTKCleanUnstructuredGridType'
    bl_label  = 'vtkCleanUnstructuredGrid'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RemovePointsWithoutCells: bpy.props.BoolProperty(name='RemovePointsWithoutCells', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ToleranceIsAbsolute: bpy.props.BoolProperty(name='ToleranceIsAbsolute', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PointDataWeighingStrategy: bpy.props.IntProperty(name='PointDataWeighingStrategy', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AbsoluteTolerance: bpy.props.FloatProperty(name='AbsoluteTolerance', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_RemovePointsWithoutCells','m_ToleranceIsAbsolute','m_ObjectName','m_PointDataWeighingStrategy','m_AbsoluteTolerance','m_Tolerance',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCleanUnstructuredGrid )        
TYPENAMES.append('VTKCleanUnstructuredGridType' )

#--------------------------------------------------------------
class VTKCleanUnstructuredGridCells(Node, PBVTK_Node):

    bl_idname = 'VTKCleanUnstructuredGridCellsType'
    bl_label  = 'vtkCleanUnstructuredGridCells'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCleanUnstructuredGridCells )        
TYPENAMES.append('VTKCleanUnstructuredGridCellsType' )

#--------------------------------------------------------------
class VTKClipConvexPolyData(Node, PBVTK_Node):

    bl_idname = 'VTKClipConvexPolyDataType'
    bl_label  = 'vtkClipConvexPolyData'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'Planes'], []) 
    
add_class( VTKClipConvexPolyData )        
TYPENAMES.append('VTKClipConvexPolyDataType' )

#--------------------------------------------------------------
class VTKCollectGraph(Node, PBVTK_Node):

    bl_idname = 'VTKCollectGraphType'
    bl_label  = 'vtkCollectGraph'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassThrough: bpy.props.BoolProperty(name='PassThrough', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputType: bpy.props.IntProperty(name='OutputType', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_PassThrough','m_ObjectName','m_OutputType',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCollectGraph )        
TYPENAMES.append('VTKCollectGraphType' )

#--------------------------------------------------------------
class VTKCollectPolyData(Node, PBVTK_Node):

    bl_idname = 'VTKCollectPolyDataType'
    bl_label  = 'vtkCollectPolyData'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassThrough: bpy.props.BoolProperty(name='PassThrough', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_PassThrough','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCollectPolyData )        
TYPENAMES.append('VTKCollectPolyDataType' )

#--------------------------------------------------------------
class VTKCollectTable(Node, PBVTK_Node):

    bl_idname = 'VTKCollectTableType'
    bl_label  = 'vtkCollectTable'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassThrough: bpy.props.BoolProperty(name='PassThrough', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_PassThrough','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCollectTable )        
TYPENAMES.append('VTKCollectTableType' )

#--------------------------------------------------------------
class VTKCompositeCutter(Node, PBVTK_Node):

    bl_idname = 'VTKCompositeCutterType'
    bl_label  = 'vtkCompositeCutter'
    e_SortBy_items=[ (x,x,x) for x in ['SortByValue', 'SortByCell']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateCutScalars: bpy.props.BoolProperty(name='GenerateCutScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateTriangles: bpy.props.BoolProperty(name='GenerateTriangles', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfContours: bpy.props.IntProperty(name='NumberOfContours', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SortBy: bpy.props.EnumProperty(name='SortBy', default="SortByValue", items=e_SortBy_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_GenerateCutScalars','m_GenerateTriangles','m_ObjectName','m_NumberOfContours','e_SortBy',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'CutFunction'], []) 
    
add_class( VTKCompositeCutter )        
TYPENAMES.append('VTKCompositeCutterType' )

#--------------------------------------------------------------
class VTKCompositeDataGeometryFilter(Node, PBVTK_Node):

    bl_idname = 'VTKCompositeDataGeometryFilterType'
    bl_label  = 'vtkCompositeDataGeometryFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCompositeDataGeometryFilter )        
TYPENAMES.append('VTKCompositeDataGeometryFilterType' )

#--------------------------------------------------------------
class VTKCompositeDataSetAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKCompositeDataSetAlgorithmType'
    bl_label  = 'vtkCompositeDataSetAlgorithm'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCompositeDataSetAlgorithm )        
TYPENAMES.append('VTKCompositeDataSetAlgorithmType' )

#--------------------------------------------------------------
class VTKComputeQuantiles(Node, PBVTK_Node):

    bl_idname = 'VTKComputeQuantilesType'
    bl_label  = 'vtkComputeQuantiles'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfIntervals: bpy.props.IntProperty(name='NumberOfIntervals', default=4, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_NumberOfIntervals',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKComputeQuantiles )        
TYPENAMES.append('VTKComputeQuantilesType' )

#--------------------------------------------------------------
class VTKComputeQuartiles(Node, PBVTK_Node):

    bl_idname = 'VTKComputeQuartilesType'
    bl_label  = 'vtkComputeQuartiles'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfIntervals: bpy.props.IntProperty(name='NumberOfIntervals', default=4, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_NumberOfIntervals',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKComputeQuartiles )        
TYPENAMES.append('VTKComputeQuartilesType' )

#--------------------------------------------------------------
class VTKConnectedPointsFilter(Node, PBVTK_Node):

    bl_idname = 'VTKConnectedPointsFilterType'
    bl_label  = 'vtkConnectedPointsFilter'
    e_ExtractionMode_items=[ (x,x,x) for x in ['PointSeededRegions', 'SpecifiedRegions', 'LargestRegion', 'AllRegions', 'ClosestPointRegion']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AlignedNormals: bpy.props.BoolProperty(name='AlignedNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarConnectivity: bpy.props.BoolProperty(name='ScalarConnectivity', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NormalAngle: bpy.props.FloatProperty(name='NormalAngle', default=10.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Radius: bpy.props.FloatProperty(name='Radius', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ExtractionMode: bpy.props.EnumProperty(name='ExtractionMode', default="AllRegions", items=e_ExtractionMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ClosestPoint: bpy.props.FloatVectorProperty(name='ClosestPoint', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarRange: bpy.props.FloatVectorProperty(name='ScalarRange', default=[0.0, 1.0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AlignedNormals','m_ScalarConnectivity','m_ObjectName','m_NormalAngle','m_Radius','e_ExtractionMode','m_ClosestPoint','m_ScalarRange',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKConnectedPointsFilter )        
TYPENAMES.append('VTKConnectedPointsFilterType' )

#--------------------------------------------------------------
class VTKConnectivityFilter(Node, PBVTK_Node):

    bl_idname = 'VTKConnectivityFilterType'
    bl_label  = 'vtkConnectivityFilter'
    e_ExtractionMode_items=[ (x,x,x) for x in ['PointSeededRegions', 'CellSeededRegions', 'SpecifiedRegions', 'LargestRegion', 'AllRegions', 'ClosestPointRegion']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ColorRegions: bpy.props.BoolProperty(name='ColorRegions', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CompressArrays: bpy.props.BoolProperty(name='CompressArrays', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarConnectivity: bpy.props.BoolProperty(name='ScalarConnectivity', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RegionIdAssignmentMode: bpy.props.IntProperty(name='RegionIdAssignmentMode', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ExtractionMode: bpy.props.EnumProperty(name='ExtractionMode', default="LargestRegion", items=e_ExtractionMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ClosestPoint: bpy.props.FloatVectorProperty(name='ClosestPoint', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarRange: bpy.props.FloatVectorProperty(name='ScalarRange', default=[0.0, 1.0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ColorRegions','m_CompressArrays','m_ScalarConnectivity','m_ObjectName','m_RegionIdAssignmentMode','e_ExtractionMode','m_ClosestPoint','m_ScalarRange',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKConnectivityFilter )        
TYPENAMES.append('VTKConnectivityFilterType' )

#--------------------------------------------------------------
class VTKConstrainedSmoothingFilter(Node, PBVTK_Node):

    bl_idname = 'VTKConstrainedSmoothingFilterType'
    bl_label  = 'vtkConstrainedSmoothingFilter'
    e_ConstraintStrategy_items=[ (x,x,x) for x in ['Default', 'ConstraintDistance', 'ConstraintBox', 'ConstraintArray']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateErrorScalars: bpy.props.BoolProperty(name='GenerateErrorScalars', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateErrorVectors: bpy.props.BoolProperty(name='GenerateErrorVectors', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfIterations: bpy.props.IntProperty(name='NumberOfIterations', default=10, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ConstraintDistance: bpy.props.FloatProperty(name='ConstraintDistance', default=0.001, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Convergence: bpy.props.FloatProperty(name='Convergence', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RelaxationFactor: bpy.props.FloatProperty(name='RelaxationFactor', default=0.01, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ConstraintStrategy: bpy.props.EnumProperty(name='ConstraintStrategy', default="Default", items=e_ConstraintStrategy_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ConstraintBox: bpy.props.FloatVectorProperty(name='ConstraintBox', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_GenerateErrorScalars','m_GenerateErrorVectors','m_ObjectName','m_NumberOfIterations','m_ConstraintDistance','m_Convergence','m_RelaxationFactor','e_ConstraintStrategy','m_ConstraintBox',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'SmoothingStencils'], []) 
    
add_class( VTKConstrainedSmoothingFilter )        
TYPENAMES.append('VTKConstrainedSmoothingFilterType' )

#--------------------------------------------------------------
class VTKContour3DLinearGrid(Node, PBVTK_Node):

    bl_idname = 'VTKContour3DLinearGridType'
    bl_label  = 'vtkContour3DLinearGrid'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeNormals: bpy.props.BoolProperty(name='ComputeNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeScalars: bpy.props.BoolProperty(name='ComputeScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InterpolateAttributes: bpy.props.BoolProperty(name='InterpolateAttributes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MergePoints: bpy.props.BoolProperty(name='MergePoints', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SequentialProcessing: bpy.props.BoolProperty(name='SequentialProcessing', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfContours: bpy.props.IntProperty(name='NumberOfContours', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeNormals','m_ComputeScalars','m_InterpolateAttributes','m_MergePoints','m_SequentialProcessing','m_ObjectName','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKContour3DLinearGrid )        
TYPENAMES.append('VTKContour3DLinearGridType' )

#--------------------------------------------------------------
class VTKContourFilter(Node, PBVTK_Node):

    bl_idname = 'VTKContourFilterType'
    bl_label  = 'vtkContourFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeGradients: bpy.props.BoolProperty(name='ComputeGradients', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeNormals: bpy.props.BoolProperty(name='ComputeNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeScalars: bpy.props.BoolProperty(name='ComputeScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FastMode: bpy.props.BoolProperty(name='FastMode', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateTriangles: bpy.props.BoolProperty(name='GenerateTriangles', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ArrayComponent: bpy.props.IntProperty(name='ArrayComponent', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfContours: bpy.props.IntProperty(name='NumberOfContours', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeGradients','m_ComputeNormals','m_ComputeScalars','m_FastMode','m_GenerateTriangles','m_ObjectName','m_ArrayComponent','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKContourFilter )        
TYPENAMES.append('VTKContourFilterType' )

#--------------------------------------------------------------
class VTKContourGrid(Node, PBVTK_Node):

    bl_idname = 'VTKContourGridType'
    bl_label  = 'vtkContourGrid'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeNormals: bpy.props.BoolProperty(name='ComputeNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeScalars: bpy.props.BoolProperty(name='ComputeScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateTriangles: bpy.props.BoolProperty(name='GenerateTriangles', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfContours: bpy.props.IntProperty(name='NumberOfContours', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeNormals','m_ComputeScalars','m_GenerateTriangles','m_ObjectName','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKContourGrid )        
TYPENAMES.append('VTKContourGridType' )

#--------------------------------------------------------------
class VTKContourLoopExtraction(Node, PBVTK_Node):

    bl_idname = 'VTKContourLoopExtractionType'
    bl_label  = 'vtkContourLoopExtraction'
    e_LoopClosure_items=[ (x,x,x) for x in ['Off', 'Boundary', 'All']]
    e_OutputMode_items=[ (x,x,x) for x in ['Polygons', 'Polylines', 'Both']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CleanPoints: bpy.props.BoolProperty(name='CleanPoints', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarThresholding: bpy.props.BoolProperty(name='ScalarThresholding', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_LoopClosure: bpy.props.EnumProperty(name='LoopClosure', default="Boundary", items=e_LoopClosure_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_OutputMode: bpy.props.EnumProperty(name='OutputMode', default="Polygons", items=e_OutputMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Normal: bpy.props.FloatVectorProperty(name='Normal', default=[0.0, 0.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarRange: bpy.props.FloatVectorProperty(name='ScalarRange', default=[0.0, 1.0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CleanPoints','m_ScalarThresholding','m_ObjectName','e_LoopClosure','e_OutputMode','m_Normal','m_ScalarRange',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKContourLoopExtraction )        
TYPENAMES.append('VTKContourLoopExtractionType' )

#--------------------------------------------------------------
class VTKContourTriangulator(Node, PBVTK_Node):

    bl_idname = 'VTKContourTriangulatorType'
    bl_label  = 'vtkContourTriangulator'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TriangulationErrorDisplay: bpy.props.BoolProperty(name='TriangulationErrorDisplay', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_TriangulationErrorDisplay','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKContourTriangulator )        
TYPENAMES.append('VTKContourTriangulatorType' )

#--------------------------------------------------------------
class VTKConvertToMultiBlockDataSet(Node, PBVTK_Node):

    bl_idname = 'VTKConvertToMultiBlockDataSetType'
    bl_label  = 'vtkConvertToMultiBlockDataSet'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKConvertToMultiBlockDataSet )        
TYPENAMES.append('VTKConvertToMultiBlockDataSetType' )

#--------------------------------------------------------------
class VTKConvertToPartitionedDataSetCollection(Node, PBVTK_Node):

    bl_idname = 'VTKConvertToPartitionedDataSetCollectionType'
    bl_label  = 'vtkConvertToPartitionedDataSetCollection'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKConvertToPartitionedDataSetCollection )        
TYPENAMES.append('VTKConvertToPartitionedDataSetCollectionType' )

#--------------------------------------------------------------
class VTKConvertToPointCloud(Node, PBVTK_Node):

    bl_idname = 'VTKConvertToPointCloudType'
    bl_label  = 'vtkConvertToPointCloud'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CellGenerationMode: bpy.props.IntProperty(name='CellGenerationMode', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_CellGenerationMode',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKConvertToPointCloud )        
TYPENAMES.append('VTKConvertToPointCloudType' )

#--------------------------------------------------------------
class VTKConvertToPolyhedra(Node, PBVTK_Node):

    bl_idname = 'VTKConvertToPolyhedraType'
    bl_label  = 'vtkConvertToPolyhedra'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputAllCells: bpy.props.BoolProperty(name='OutputAllCells', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_OutputAllCells','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKConvertToPolyhedra )        
TYPENAMES.append('VTKConvertToPolyhedraType' )

#--------------------------------------------------------------
class VTKCountFaces(Node, PBVTK_Node):

    bl_idname = 'VTKCountFacesType'
    bl_label  = 'vtkCountFaces'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseImplicitArray: bpy.props.BoolProperty(name='UseImplicitArray', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputArrayName: bpy.props.StringProperty(name='OutputArrayName', default="Face Count", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_UseImplicitArray','m_ObjectName','m_OutputArrayName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCountFaces )        
TYPENAMES.append('VTKCountFacesType' )

#--------------------------------------------------------------
class VTKCountVertices(Node, PBVTK_Node):

    bl_idname = 'VTKCountVerticesType'
    bl_label  = 'vtkCountVertices'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseImplicitArray: bpy.props.BoolProperty(name='UseImplicitArray', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputArrayName: bpy.props.StringProperty(name='OutputArrayName', default="Vertex Count", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_UseImplicitArray','m_ObjectName','m_OutputArrayName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCountVertices )        
TYPENAMES.append('VTKCountVerticesType' )

#--------------------------------------------------------------
class VTKCriticalTime(Node, PBVTK_Node):

    bl_idname = 'VTKCriticalTimeType'
    bl_label  = 'vtkCriticalTime'
    e_ComponentMode_items=[ (x,x,x) for x in ['UseSelected', 'UseAll', 'UseAny']]
    e_ThresholdCriterion_items=[ (x,x,x) for x in ['Upper']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SelectedComponent: bpy.props.IntProperty(name='SelectedComponent', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LowerThreshold: bpy.props.FloatProperty(name='LowerThreshold', default=-1e+30, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UpperThreshold: bpy.props.FloatProperty(name='UpperThreshold', default=1e+30, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ComponentMode: bpy.props.EnumProperty(name='ComponentMode', default="UseSelected", items=e_ComponentMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ThresholdCriterion: bpy.props.EnumProperty(name='ThresholdCriterion', default="Upper", items=e_ThresholdCriterion_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_SelectedComponent','m_LowerThreshold','m_UpperThreshold','e_ComponentMode','e_ThresholdCriterion',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCriticalTime )        
TYPENAMES.append('VTKCriticalTimeType' )

#--------------------------------------------------------------
class VTKCurvatures(Node, PBVTK_Node):

    bl_idname = 'VTKCurvaturesType'
    bl_label  = 'vtkCurvatures'
    e_CurvatureType_items=[ (x,x,x) for x in ['Gaussian', 'Mean', 'Maximum', 'Minimum']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InvertMeanCurvature: bpy.props.BoolProperty(name='InvertMeanCurvature', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_CurvatureType: bpy.props.EnumProperty(name='CurvatureType', default="Gaussian", items=e_CurvatureType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_InvertMeanCurvature','m_ObjectName','e_CurvatureType',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCurvatures )        
TYPENAMES.append('VTKCurvaturesType' )

#--------------------------------------------------------------
class VTKCutMaterial(Node, PBVTK_Node):

    bl_idname = 'VTKCutMaterialType'
    bl_label  = 'vtkCutMaterial'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ArrayName: bpy.props.StringProperty(name='ArrayName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaterialArrayName: bpy.props.StringProperty(name='MaterialArrayName', default="material", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Material: bpy.props.IntProperty(name='Material', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UpVector: bpy.props.FloatVectorProperty(name='UpVector', default=[0.0, 0.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ArrayName','m_MaterialArrayName','m_ObjectName','m_Material','m_UpVector',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKCutMaterial )        
TYPENAMES.append('VTKCutMaterialType' )

#--------------------------------------------------------------
class VTKCutter(Node, PBVTK_Node):

    bl_idname = 'VTKCutterType'
    bl_label  = 'vtkCutter'
    e_SortBy_items=[ (x,x,x) for x in ['SortByValue', 'SortByCell']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateCutScalars: bpy.props.BoolProperty(name='GenerateCutScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateTriangles: bpy.props.BoolProperty(name='GenerateTriangles', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfContours: bpy.props.IntProperty(name='NumberOfContours', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SortBy: bpy.props.EnumProperty(name='SortBy', default="SortByValue", items=e_SortBy_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_GenerateCutScalars','m_GenerateTriangles','m_ObjectName','m_NumberOfContours','e_SortBy',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'CutFunction'], []) 
    
add_class( VTKCutter )        
TYPENAMES.append('VTKCutterType' )

#--------------------------------------------------------------
class VTKDataObjectAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKDataObjectAlgorithmType'
    bl_label  = 'vtkDataObjectAlgorithm'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKDataObjectAlgorithm )        
TYPENAMES.append('VTKDataObjectAlgorithmType' )

#--------------------------------------------------------------
class VTKDataObjectToDataSetFilter(Node, PBVTK_Node):

    bl_idname = 'VTKDataObjectToDataSetFilterType'
    bl_label  = 'vtkDataObjectToDataSetFilter'
    e_DataSetType_items=[ (x,x,x) for x in ['PolyData', 'StructuredPoints', 'StructuredGrid', 'RectilinearGrid', 'UnstructuredGrid']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DefaultNormalize: bpy.props.BoolProperty(name='DefaultNormalize', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DataSetType: bpy.props.EnumProperty(name='DataSetType', default="PolyData", items=e_DataSetType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Dimensions: bpy.props.IntVectorProperty(name='Dimensions', default=[0, 0, 0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Origin: bpy.props.FloatVectorProperty(name='Origin', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Spacing: bpy.props.FloatVectorProperty(name='Spacing', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_DefaultNormalize','m_ObjectName','e_DataSetType','m_Dimensions','m_Origin','m_Spacing',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKDataObjectToDataSetFilter )        
TYPENAMES.append('VTKDataObjectToDataSetFilterType' )

#--------------------------------------------------------------
class VTKDataSetAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKDataSetAlgorithmType'
    bl_label  = 'vtkDataSetAlgorithm'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKDataSetAlgorithm )        
TYPENAMES.append('VTKDataSetAlgorithmType' )

#--------------------------------------------------------------
class VTKDataSetGradient(Node, PBVTK_Node):

    bl_idname = 'VTKDataSetGradientType'
    bl_label  = 'vtkDataSetGradient'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ResultArrayName: bpy.props.StringProperty(name='ResultArrayName', default="gradient", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_ResultArrayName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKDataSetGradient )        
TYPENAMES.append('VTKDataSetGradientType' )

#--------------------------------------------------------------
class VTKDataSetGradientPrecompute(Node, PBVTK_Node):

    bl_idname = 'VTKDataSetGradientPrecomputeType'
    bl_label  = 'vtkDataSetGradientPrecompute'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKDataSetGradientPrecompute )        
TYPENAMES.append('VTKDataSetGradientPrecomputeType' )

#--------------------------------------------------------------
class VTKDataSetRegionSurfaceFilter(Node, PBVTK_Node):

    bl_idname = 'VTKDataSetRegionSurfaceFilterType'
    bl_label  = 'vtkDataSetRegionSurfaceFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AllowInterpolation: bpy.props.BoolProperty(name='AllowInterpolation', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Delegation: bpy.props.BoolProperty(name='Delegation', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FastMode: bpy.props.BoolProperty(name='FastMode', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassThroughCellIds: bpy.props.BoolProperty(name='PassThroughCellIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassThroughPointIds: bpy.props.BoolProperty(name='PassThroughPointIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SingleSided: bpy.props.BoolProperty(name='SingleSided', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InterfaceIDsName: bpy.props.StringProperty(name='InterfaceIDsName', default="interface_ids", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaterialIDsName: bpy.props.StringProperty(name='MaterialIDsName', default="material_ids", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaterialPIDsName: bpy.props.StringProperty(name='MaterialPIDsName', default="material_ancestors", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaterialPropertiesName: bpy.props.StringProperty(name='MaterialPropertiesName', default="material_properties", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OriginalCellIdsName: bpy.props.StringProperty(name='OriginalCellIdsName', default="vtkOriginalCellIds", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OriginalPointIdsName: bpy.props.StringProperty(name='OriginalPointIdsName', default="vtkOriginalPointIds", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RegionArrayName: bpy.props.StringProperty(name='RegionArrayName', default="material", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MatchBoundariesIgnoringCellOrder: bpy.props.IntProperty(name='MatchBoundariesIgnoringCellOrder', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NonlinearSubdivisionLevel: bpy.props.IntProperty(name='NonlinearSubdivisionLevel', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PieceInvariant: bpy.props.IntProperty(name='PieceInvariant', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AllowInterpolation','m_Delegation','m_FastMode','m_PassThroughCellIds','m_PassThroughPointIds','m_SingleSided','m_InterfaceIDsName','m_MaterialIDsName','m_MaterialPIDsName','m_MaterialPropertiesName','m_ObjectName','m_OriginalCellIdsName','m_OriginalPointIdsName','m_RegionArrayName','m_MatchBoundariesIgnoringCellOrder','m_NonlinearSubdivisionLevel','m_PieceInvariant',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKDataSetRegionSurfaceFilter )        
TYPENAMES.append('VTKDataSetRegionSurfaceFilterType' )

#--------------------------------------------------------------
class VTKDataSetSurfaceFilter(Node, PBVTK_Node):

    bl_idname = 'VTKDataSetSurfaceFilterType'
    bl_label  = 'vtkDataSetSurfaceFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AllowInterpolation: bpy.props.BoolProperty(name='AllowInterpolation', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Delegation: bpy.props.BoolProperty(name='Delegation', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FastMode: bpy.props.BoolProperty(name='FastMode', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassThroughCellIds: bpy.props.BoolProperty(name='PassThroughCellIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassThroughPointIds: bpy.props.BoolProperty(name='PassThroughPointIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OriginalCellIdsName: bpy.props.StringProperty(name='OriginalCellIdsName', default="vtkOriginalCellIds", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OriginalPointIdsName: bpy.props.StringProperty(name='OriginalPointIdsName', default="vtkOriginalPointIds", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MatchBoundariesIgnoringCellOrder: bpy.props.IntProperty(name='MatchBoundariesIgnoringCellOrder', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NonlinearSubdivisionLevel: bpy.props.IntProperty(name='NonlinearSubdivisionLevel', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PieceInvariant: bpy.props.IntProperty(name='PieceInvariant', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AllowInterpolation','m_Delegation','m_FastMode','m_PassThroughCellIds','m_PassThroughPointIds','m_ObjectName','m_OriginalCellIdsName','m_OriginalPointIdsName','m_MatchBoundariesIgnoringCellOrder','m_NonlinearSubdivisionLevel','m_PieceInvariant',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKDataSetSurfaceFilter )        
TYPENAMES.append('VTKDataSetSurfaceFilterType' )

#--------------------------------------------------------------
class VTKDataSetToDataObjectFilter(Node, PBVTK_Node):

    bl_idname = 'VTKDataSetToDataObjectFilterType'
    bl_label  = 'vtkDataSetToDataObjectFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CellData: bpy.props.BoolProperty(name='CellData', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldData: bpy.props.BoolProperty(name='FieldData', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Geometry: bpy.props.BoolProperty(name='Geometry', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LegacyTopology: bpy.props.BoolProperty(name='LegacyTopology', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ModernTopology: bpy.props.BoolProperty(name='ModernTopology', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PointData: bpy.props.BoolProperty(name='PointData', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Topology: bpy.props.BoolProperty(name='Topology', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CellData','m_FieldData','m_Geometry','m_LegacyTopology','m_ModernTopology','m_PointData','m_Topology','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKDataSetToDataObjectFilter )        
TYPENAMES.append('VTKDataSetToDataObjectFilterType' )

#--------------------------------------------------------------
class VTKDataSetTriangleFilter(Node, PBVTK_Node):

    bl_idname = 'VTKDataSetTriangleFilterType'
    bl_label  = 'vtkDataSetTriangleFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TetrahedraOnly: bpy.props.BoolProperty(name='TetrahedraOnly', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_TetrahedraOnly','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKDataSetTriangleFilter )        
TYPENAMES.append('VTKDataSetTriangleFilterType' )

#--------------------------------------------------------------
class VTKDateToNumeric(Node, PBVTK_Node):

    bl_idname = 'VTKDateToNumericType'
    bl_label  = 'vtkDateToNumeric'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DateFormat: bpy.props.StringProperty(name='DateFormat', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_DateFormat','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKDateToNumeric )        
TYPENAMES.append('VTKDateToNumericType' )

#--------------------------------------------------------------
class VTKDecimatePolylineFilter(Node, PBVTK_Node):

    bl_idname = 'VTKDecimatePolylineFilterType'
    bl_label  = 'vtkDecimatePolylineFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumError: bpy.props.FloatProperty(name='MaximumError', default=1e+30, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TargetReduction: bpy.props.FloatProperty(name='TargetReduction', default=0.9, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_MaximumError','m_TargetReduction',]
    def m_connections( self ):
        return (['input'], ['output'], ['DecimationStrategy', 'ContainerAlgorithm'], []) 
    
add_class( VTKDecimatePolylineFilter )        
TYPENAMES.append('VTKDecimatePolylineFilterType' )

#--------------------------------------------------------------
class VTKDecimatePro(Node, PBVTK_Node):

    bl_idname = 'VTKDecimateProType'
    bl_label  = 'vtkDecimatePro'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AccumulateError: bpy.props.BoolProperty(name='AccumulateError', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BoundaryVertexDeletion: bpy.props.BoolProperty(name='BoundaryVertexDeletion', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PreSplitMesh: bpy.props.BoolProperty(name='PreSplitMesh', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PreserveTopology: bpy.props.BoolProperty(name='PreserveTopology', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Splitting: bpy.props.BoolProperty(name='Splitting', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Degree: bpy.props.IntProperty(name='Degree', default=25, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ErrorIsAbsolute: bpy.props.IntProperty(name='ErrorIsAbsolute', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AbsoluteError: bpy.props.FloatProperty(name='AbsoluteError', default=1e+30, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FeatureAngle: bpy.props.FloatProperty(name='FeatureAngle', default=15.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InflectionPointRatio: bpy.props.FloatProperty(name='InflectionPointRatio', default=10.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumError: bpy.props.FloatProperty(name='MaximumError', default=1e+30, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SplitAngle: bpy.props.FloatProperty(name='SplitAngle', default=75.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TargetReduction: bpy.props.FloatProperty(name='TargetReduction', default=0.9, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AccumulateError','m_BoundaryVertexDeletion','m_PreSplitMesh','m_PreserveTopology','m_Splitting','m_ObjectName','m_Degree','m_ErrorIsAbsolute','m_AbsoluteError','m_FeatureAngle','m_InflectionPointRatio','m_MaximumError','m_SplitAngle','m_TargetReduction',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKDecimatePro )        
TYPENAMES.append('VTKDecimateProType' )

#--------------------------------------------------------------
class VTKDeflectNormals(Node, PBVTK_Node):

    bl_idname = 'VTKDeflectNormalsType'
    bl_label  = 'vtkDeflectNormals'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseUserNormal: bpy.props.BoolProperty(name='UseUserNormal', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScaleFactor: bpy.props.FloatProperty(name='ScaleFactor', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UserNormal: bpy.props.FloatVectorProperty(name='UserNormal', default=[0.0, 0.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_UseUserNormal','m_ObjectName','m_ScaleFactor','m_UserNormal',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKDeflectNormals )        
TYPENAMES.append('VTKDeflectNormalsType' )

#--------------------------------------------------------------
class VTKDelaunay3D(Node, PBVTK_Node):

    bl_idname = 'VTKDelaunay3DType'
    bl_label  = 'vtkDelaunay3D'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AlphaLines: bpy.props.BoolProperty(name='AlphaLines', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AlphaTets: bpy.props.BoolProperty(name='AlphaTets', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AlphaTris: bpy.props.BoolProperty(name='AlphaTris', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AlphaVerts: bpy.props.BoolProperty(name='AlphaVerts', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BoundingTriangulation: bpy.props.BoolProperty(name='BoundingTriangulation', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Alpha: bpy.props.FloatProperty(name='Alpha', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Offset: bpy.props.FloatProperty(name='Offset', default=2.5, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=0.001, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AlphaLines','m_AlphaTets','m_AlphaTris','m_AlphaVerts','m_BoundingTriangulation','m_ObjectName','m_Alpha','m_Offset','m_Tolerance',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKDelaunay3D )        
TYPENAMES.append('VTKDelaunay3DType' )

#--------------------------------------------------------------
class VTKDensifyPointCloudFilter(Node, PBVTK_Node):

    bl_idname = 'VTKDensifyPointCloudFilterType'
    bl_label  = 'vtkDensifyPointCloudFilter'
    e_NeighborhoodType_items=[ (x,x,x) for x in ['Radius', 'NClosest']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InterpolateAttributeData: bpy.props.BoolProperty(name='InterpolateAttributeData', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumNumberOfIterations: bpy.props.IntProperty(name='MaximumNumberOfIterations', default=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumNumberOfPoints: bpy.props.IntProperty(name='MaximumNumberOfPoints', default=1000000000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfClosestPoints: bpy.props.IntProperty(name='NumberOfClosestPoints', default=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Radius: bpy.props.FloatProperty(name='Radius', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TargetDistance: bpy.props.FloatProperty(name='TargetDistance', default=0.5, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_NeighborhoodType: bpy.props.EnumProperty(name='NeighborhoodType', default="NClosest", items=e_NeighborhoodType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_InterpolateAttributeData','m_ObjectName','m_MaximumNumberOfIterations','m_MaximumNumberOfPoints','m_NumberOfClosestPoints','m_Radius','m_TargetDistance','e_NeighborhoodType',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKDensifyPointCloudFilter )        
TYPENAMES.append('VTKDensifyPointCloudFilterType' )

#--------------------------------------------------------------
class VTKDensifyPolyData(Node, PBVTK_Node):

    bl_idname = 'VTKDensifyPolyDataType'
    bl_label  = 'vtkDensifyPolyData'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfSubdivisions: bpy.props.IntProperty(name='NumberOfSubdivisions', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_NumberOfSubdivisions',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKDensifyPolyData )        
TYPENAMES.append('VTKDensifyPolyDataType' )

#--------------------------------------------------------------
class VTKDepthSortPolyData(Node, PBVTK_Node):

    bl_idname = 'VTKDepthSortPolyDataType'
    bl_label  = 'vtkDepthSortPolyData'
    e_DepthSortMode_items=[ (x,x,x) for x in ['FirstPoint', 'BoundsCenter', 'ParametricCenter']]
    e_Direction_items=[ (x,x,x) for x in ['BackToFront', 'FrontToBack', 'SpecifiedVector']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SortScalars: bpy.props.BoolProperty(name='SortScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DepthSortMode: bpy.props.EnumProperty(name='DepthSortMode', default="FirstPoint", items=e_DepthSortMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_Direction: bpy.props.EnumProperty(name='Direction', default="BackToFront", items=e_Direction_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Origin: bpy.props.FloatVectorProperty(name='Origin', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Vector: bpy.props.FloatVectorProperty(name='Vector', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_SortScalars','m_ObjectName','e_DepthSortMode','e_Direction','m_Origin','m_Vector',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'Prop3D'], []) 
    
add_class( VTKDepthSortPolyData )        
TYPENAMES.append('VTKDepthSortPolyDataType' )

#--------------------------------------------------------------
class VTKDijkstraGraphGeodesicPath(Node, PBVTK_Node):

    bl_idname = 'VTKDijkstraGraphGeodesicPathType'
    bl_label  = 'vtkDijkstraGraphGeodesicPath'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RepelPathFromVertices: bpy.props.BoolProperty(name='RepelPathFromVertices', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_StopWhenEndReached: bpy.props.BoolProperty(name='StopWhenEndReached', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseScalarWeights: bpy.props.BoolProperty(name='UseScalarWeights', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EndVertex: bpy.props.IntProperty(name='EndVertex', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_StartVertex: bpy.props.IntProperty(name='StartVertex', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_RepelPathFromVertices','m_StopWhenEndReached','m_UseScalarWeights','m_ObjectName','m_EndVertex','m_StartVertex',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'RepelVertices'], []) 
    
add_class( VTKDijkstraGraphGeodesicPath )        
TYPENAMES.append('VTKDijkstraGraphGeodesicPathType' )

#--------------------------------------------------------------
class VTKDijkstraImageGeodesicPath(Node, PBVTK_Node):

    bl_idname = 'VTKDijkstraImageGeodesicPathType'
    bl_label  = 'vtkDijkstraImageGeodesicPath'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RepelPathFromVertices: bpy.props.BoolProperty(name='RepelPathFromVertices', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_StopWhenEndReached: bpy.props.BoolProperty(name='StopWhenEndReached', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseScalarWeights: bpy.props.BoolProperty(name='UseScalarWeights', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EndVertex: bpy.props.IntProperty(name='EndVertex', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_StartVertex: bpy.props.IntProperty(name='StartVertex', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CurvatureWeight: bpy.props.FloatProperty(name='CurvatureWeight', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EdgeLengthWeight: bpy.props.FloatProperty(name='EdgeLengthWeight', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ImageWeight: bpy.props.FloatProperty(name='ImageWeight', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_RepelPathFromVertices','m_StopWhenEndReached','m_UseScalarWeights','m_ObjectName','m_EndVertex','m_StartVertex','m_CurvatureWeight','m_EdgeLengthWeight','m_ImageWeight',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'RepelVertices'], []) 
    
add_class( VTKDijkstraImageGeodesicPath )        
TYPENAMES.append('VTKDijkstraImageGeodesicPathType' )

#--------------------------------------------------------------
class VTKDirectedGraphAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKDirectedGraphAlgorithmType'
    bl_label  = 'vtkDirectedGraphAlgorithm'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKDirectedGraphAlgorithm )        
TYPENAMES.append('VTKDirectedGraphAlgorithmType' )

#--------------------------------------------------------------
class VTKDiscreteFlyingEdges2D(Node, PBVTK_Node):

    bl_idname = 'VTKDiscreteFlyingEdges2DType'
    bl_label  = 'vtkDiscreteFlyingEdges2D'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeScalars: bpy.props.BoolProperty(name='ComputeScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ArrayComponent: bpy.props.IntProperty(name='ArrayComponent', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfContours: bpy.props.IntProperty(name='NumberOfContours', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeScalars','m_ObjectName','m_ArrayComponent','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKDiscreteFlyingEdges2D )        
TYPENAMES.append('VTKDiscreteFlyingEdges2DType' )

#--------------------------------------------------------------
class VTKDiscreteFlyingEdges3D(Node, PBVTK_Node):

    bl_idname = 'VTKDiscreteFlyingEdges3DType'
    bl_label  = 'vtkDiscreteFlyingEdges3D'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeGradients: bpy.props.BoolProperty(name='ComputeGradients', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeNormals: bpy.props.BoolProperty(name='ComputeNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeScalars: bpy.props.BoolProperty(name='ComputeScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InterpolateAttributes: bpy.props.BoolProperty(name='InterpolateAttributes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ArrayComponent: bpy.props.IntProperty(name='ArrayComponent', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfContours: bpy.props.IntProperty(name='NumberOfContours', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeGradients','m_ComputeNormals','m_ComputeScalars','m_InterpolateAttributes','m_ObjectName','m_ArrayComponent','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKDiscreteFlyingEdges3D )        
TYPENAMES.append('VTKDiscreteFlyingEdges3DType' )

#--------------------------------------------------------------
class VTKDiscreteFlyingEdgesClipper2D(Node, PBVTK_Node):

    bl_idname = 'VTKDiscreteFlyingEdgesClipper2DType'
    bl_label  = 'vtkDiscreteFlyingEdgesClipper2D'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeScalars: bpy.props.BoolProperty(name='ComputeScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ArrayComponent: bpy.props.IntProperty(name='ArrayComponent', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfContours: bpy.props.IntProperty(name='NumberOfContours', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeScalars','m_ObjectName','m_ArrayComponent','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKDiscreteFlyingEdgesClipper2D )        
TYPENAMES.append('VTKDiscreteFlyingEdgesClipper2DType' )

#--------------------------------------------------------------
class VTKDiscreteMarchingCubes(Node, PBVTK_Node):

    bl_idname = 'VTKDiscreteMarchingCubesType'
    bl_label  = 'vtkDiscreteMarchingCubes'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeAdjacentScalars: bpy.props.BoolProperty(name='ComputeAdjacentScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeGradients: bpy.props.BoolProperty(name='ComputeGradients', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeNormals: bpy.props.BoolProperty(name='ComputeNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeScalars: bpy.props.BoolProperty(name='ComputeScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfContours: bpy.props.IntProperty(name='NumberOfContours', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeAdjacentScalars','m_ComputeGradients','m_ComputeNormals','m_ComputeScalars','m_ObjectName','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKDiscreteMarchingCubes )        
TYPENAMES.append('VTKDiscreteMarchingCubesType' )

#--------------------------------------------------------------
class VTKDistributedDataFilter(Node, PBVTK_Node):

    bl_idname = 'VTKDistributedDataFilterType'
    bl_label  = 'vtkDistributedDataFilter'
    e_BoundaryMode_items=[ (x,x,x) for x in ['AssignToOneRegion', 'AssignToAllIntersectingRegions', 'SplitBoundaryCells']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ClipCells: bpy.props.BoolProperty(name='ClipCells', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IncludeAllIntersectingCells: bpy.props.BoolProperty(name='IncludeAllIntersectingCells', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RetainKdtree: bpy.props.BoolProperty(name='RetainKdtree', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Timing: bpy.props.BoolProperty(name='Timing', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseMinimalMemory: bpy.props.BoolProperty(name='UseMinimalMemory', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumGhostLevel: bpy.props.IntProperty(name='MinimumGhostLevel', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_BoundaryMode: bpy.props.EnumProperty(name='BoundaryMode', default="AssignToOneRegion", items=e_BoundaryMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ClipCells','m_IncludeAllIntersectingCells','m_RetainKdtree','m_Timing','m_UseMinimalMemory','m_ObjectName','m_MinimumGhostLevel','e_BoundaryMode',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'Cuts'], []) 
    
add_class( VTKDistributedDataFilter )        
TYPENAMES.append('VTKDistributedDataFilterType' )

#--------------------------------------------------------------
class VTKDuplicatePolyData(Node, PBVTK_Node):

    bl_idname = 'VTKDuplicatePolyDataType'
    bl_label  = 'vtkDuplicatePolyData'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Synchronous: bpy.props.BoolProperty(name='Synchronous', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ClientFlag: bpy.props.IntProperty(name='ClientFlag', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Synchronous','m_ObjectName','m_ClientFlag',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKDuplicatePolyData )        
TYPENAMES.append('VTKDuplicatePolyDataType' )

#--------------------------------------------------------------
class VTKEdgePoints(Node, PBVTK_Node):

    bl_idname = 'VTKEdgePointsType'
    bl_label  = 'vtkEdgePoints'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Value: bpy.props.FloatProperty(name='Value', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_Value',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKEdgePoints )        
TYPENAMES.append('VTKEdgePointsType' )

#--------------------------------------------------------------
class VTKElevationFilter(Node, PBVTK_Node):

    bl_idname = 'VTKElevationFilterType'
    bl_label  = 'vtkElevationFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HighPoint: bpy.props.FloatVectorProperty(name='HighPoint', default=[0.0, 0.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LowPoint: bpy.props.FloatVectorProperty(name='LowPoint', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarRange: bpy.props.FloatVectorProperty(name='ScalarRange', default=[0.0, 1.0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_HighPoint','m_LowPoint','m_ScalarRange',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKElevationFilter )        
TYPENAMES.append('VTKElevationFilterType' )

#--------------------------------------------------------------
class VTKEndFor(Node, PBVTK_Node):

    bl_idname = 'VTKEndForType'
    bl_label  = 'vtkEndFor'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKEndFor )        
TYPENAMES.append('VTKEndForType' )

#--------------------------------------------------------------
class VTKEuclideanClusterExtraction(Node, PBVTK_Node):

    bl_idname = 'VTKEuclideanClusterExtractionType'
    bl_label  = 'vtkEuclideanClusterExtraction'
    e_ExtractionMode_items=[ (x,x,x) for x in ['PointSeededClusters', 'SpecifiedClusters', 'LargestCluster', 'AllClusters', 'ClosestPointCluster']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ColorClusters: bpy.props.BoolProperty(name='ColorClusters', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarConnectivity: bpy.props.BoolProperty(name='ScalarConnectivity', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Radius: bpy.props.FloatProperty(name='Radius', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ExtractionMode: bpy.props.EnumProperty(name='ExtractionMode', default="LargestCluster", items=e_ExtractionMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ClosestPoint: bpy.props.FloatVectorProperty(name='ClosestPoint', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarRange: bpy.props.FloatVectorProperty(name='ScalarRange', default=[0.0, 1.0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ColorClusters','m_ScalarConnectivity','m_ObjectName','m_Radius','e_ExtractionMode','m_ClosestPoint','m_ScalarRange',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKEuclideanClusterExtraction )        
TYPENAMES.append('VTKEuclideanClusterExtractionType' )

#--------------------------------------------------------------
class VTKEvenlySpacedStreamlines2D(Node, PBVTK_Node):

    bl_idname = 'VTKEvenlySpacedStreamlines2DType'
    bl_label  = 'vtkEvenlySpacedStreamlines2D'
    e_IntegratorType_items=[ (x,x,x) for x in ['RungeKutta2', 'RungeKutta4']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeVorticity: bpy.props.BoolProperty(name='ComputeVorticity', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IntegrationStepUnit: bpy.props.IntProperty(name='IntegrationStepUnit', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumNumberOfSteps: bpy.props.IntProperty(name='MaximumNumberOfSteps', default=2000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumNumberOfLoopPoints: bpy.props.IntProperty(name='MinimumNumberOfLoopPoints', default=4, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ClosedLoopMaximumDistance: bpy.props.FloatProperty(name='ClosedLoopMaximumDistance', default=1e-06, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InitialIntegrationStep: bpy.props.FloatProperty(name='InitialIntegrationStep', default=0.5, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LoopAngle: bpy.props.FloatProperty(name='LoopAngle', default=0.349066, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SeparatingDistance: bpy.props.FloatProperty(name='SeparatingDistance', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SeparatingDistanceRatio: bpy.props.FloatProperty(name='SeparatingDistanceRatio', default=0.5, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TerminalSpeed: bpy.props.FloatProperty(name='TerminalSpeed', default=1e-12, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_IntegratorType: bpy.props.EnumProperty(name='IntegratorType', default="RungeKutta2", items=e_IntegratorType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_StartPosition: bpy.props.FloatVectorProperty(name='StartPosition', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=14, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeVorticity','m_ObjectName','m_IntegrationStepUnit','m_MaximumNumberOfSteps','m_MinimumNumberOfLoopPoints','m_ClosedLoopMaximumDistance','m_InitialIntegrationStep','m_LoopAngle','m_SeparatingDistance','m_SeparatingDistanceRatio','m_TerminalSpeed','e_IntegratorType','m_StartPosition',]
    def m_connections( self ):
        return (['input'], ['output'], ['Integrator', 'ContainerAlgorithm'], []) 
    
add_class( VTKEvenlySpacedStreamlines2D )        
TYPENAMES.append('VTKEvenlySpacedStreamlines2DType' )

#--------------------------------------------------------------
class VTKExpandMarkedElements(Node, PBVTK_Node):

    bl_idname = 'VTKExpandMarkedElementsType'
    bl_label  = 'vtkExpandMarkedElements'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RemoveIntermediateLayers: bpy.props.BoolProperty(name='RemoveIntermediateLayers', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RemoveSeed: bpy.props.BoolProperty(name='RemoveSeed', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfLayers: bpy.props.IntProperty(name='NumberOfLayers', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_RemoveIntermediateLayers','m_RemoveSeed','m_ObjectName','m_NumberOfLayers',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExpandMarkedElements )        
TYPENAMES.append('VTKExpandMarkedElementsType' )

#--------------------------------------------------------------
class VTKExplicitStructuredGridAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKExplicitStructuredGridAlgorithmType'
    bl_label  = 'vtkExplicitStructuredGridAlgorithm'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExplicitStructuredGridAlgorithm )        
TYPENAMES.append('VTKExplicitStructuredGridAlgorithmType' )

#--------------------------------------------------------------
class VTKExplicitStructuredGridCrop(Node, PBVTK_Node):

    bl_idname = 'VTKExplicitStructuredGridCropType'
    bl_label  = 'vtkExplicitStructuredGridCrop'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExplicitStructuredGridCrop )        
TYPENAMES.append('VTKExplicitStructuredGridCropType' )

#--------------------------------------------------------------
class VTKExplicitStructuredGridSurfaceFilter(Node, PBVTK_Node):

    bl_idname = 'VTKExplicitStructuredGridSurfaceFilterType'
    bl_label  = 'vtkExplicitStructuredGridSurfaceFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassThroughCellIds: bpy.props.BoolProperty(name='PassThroughCellIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassThroughPointIds: bpy.props.BoolProperty(name='PassThroughPointIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OriginalCellIdsName: bpy.props.StringProperty(name='OriginalCellIdsName', default="vtkOriginalCellIds", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OriginalPointIdsName: bpy.props.StringProperty(name='OriginalPointIdsName', default="vtkOriginalPointIds", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_PassThroughCellIds','m_PassThroughPointIds','m_ObjectName','m_OriginalCellIdsName','m_OriginalPointIdsName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExplicitStructuredGridSurfaceFilter )        
TYPENAMES.append('VTKExplicitStructuredGridSurfaceFilterType' )

#--------------------------------------------------------------
class VTKExplicitStructuredGridToUnstructuredGrid(Node, PBVTK_Node):

    bl_idname = 'VTKExplicitStructuredGridToUnstructuredGridType'
    bl_label  = 'vtkExplicitStructuredGridToUnstructuredGrid'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExplicitStructuredGridToUnstructuredGrid )        
TYPENAMES.append('VTKExplicitStructuredGridToUnstructuredGridType' )

#--------------------------------------------------------------
class VTKExplodeDataSet(Node, PBVTK_Node):

    bl_idname = 'VTKExplodeDataSetType'
    bl_label  = 'vtkExplodeDataSet'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExplodeDataSet )        
TYPENAMES.append('VTKExplodeDataSetType' )

#--------------------------------------------------------------
class VTKExtractArray(Node, PBVTK_Node):

    bl_idname = 'VTKExtractArrayType'
    bl_label  = 'vtkExtractArray'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Index: bpy.props.IntProperty(name='Index', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_Index',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExtractArray )        
TYPENAMES.append('VTKExtractArrayType' )

#--------------------------------------------------------------
class VTKExtractBlock(Node, PBVTK_Node):

    bl_idname = 'VTKExtractBlockType'
    bl_label  = 'vtkExtractBlock'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaintainStructure: bpy.props.BoolProperty(name='MaintainStructure', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PruneOutput: bpy.props.BoolProperty(name='PruneOutput', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_MaintainStructure','m_PruneOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExtractBlock )        
TYPENAMES.append('VTKExtractBlockType' )

#--------------------------------------------------------------
class VTKExtractBlockUsingDataAssembly(Node, PBVTK_Node):

    bl_idname = 'VTKExtractBlockUsingDataAssemblyType'
    bl_label  = 'vtkExtractBlockUsingDataAssembly'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PruneDataAssembly: bpy.props.BoolProperty(name='PruneDataAssembly', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SelectSubtrees: bpy.props.BoolProperty(name='SelectSubtrees', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AssemblyName: bpy.props.StringProperty(name='AssemblyName', default="Hierarchy", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Selector: bpy.props.StringProperty(name='Selector', default="0", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_PruneDataAssembly','m_SelectSubtrees','m_AssemblyName','m_ObjectName','m_Selector',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExtractBlockUsingDataAssembly )        
TYPENAMES.append('VTKExtractBlockUsingDataAssemblyType' )

#--------------------------------------------------------------
class VTKExtractCTHPart(Node, PBVTK_Node):

    bl_idname = 'VTKExtractCTHPartType'
    bl_label  = 'vtkExtractCTHPart'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Capping: bpy.props.BoolProperty(name='Capping', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateSolidGeometry: bpy.props.BoolProperty(name='GenerateSolidGeometry', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateTriangles: bpy.props.BoolProperty(name='GenerateTriangles', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RemoveGhostCells: bpy.props.BoolProperty(name='RemoveGhostCells', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VolumeFractionSurfaceValue: bpy.props.FloatProperty(name='VolumeFractionSurfaceValue', default=0.499, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Capping','m_GenerateSolidGeometry','m_GenerateTriangles','m_RemoveGhostCells','m_ObjectName','m_VolumeFractionSurfaceValue',]
    def m_connections( self ):
        return (['input'], ['output'], ['ClipPlane', 'ContainerAlgorithm'], []) 
    
add_class( VTKExtractCTHPart )        
TYPENAMES.append('VTKExtractCTHPartType' )

#--------------------------------------------------------------
class VTKExtractCells(Node, PBVTK_Node):

    bl_idname = 'VTKExtractCellsType'
    bl_label  = 'vtkExtractCells'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AssumeSortedAndUniqueIds: bpy.props.BoolProperty(name='AssumeSortedAndUniqueIds', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ExtractAllCells: bpy.props.BoolProperty(name='ExtractAllCells', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassThroughCellIds: bpy.props.BoolProperty(name='PassThroughCellIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BatchSize: bpy.props.IntProperty(name='BatchSize', default=1000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AssumeSortedAndUniqueIds','m_ExtractAllCells','m_PassThroughCellIds','m_ObjectName','m_BatchSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExtractCells )        
TYPENAMES.append('VTKExtractCellsType' )

#--------------------------------------------------------------
class VTKExtractCellsByType(Node, PBVTK_Node):

    bl_idname = 'VTKExtractCellsByTypeType'
    bl_label  = 'vtkExtractCellsByType'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExtractCellsByType )        
TYPENAMES.append('VTKExtractCellsByTypeType' )

#--------------------------------------------------------------
class VTKExtractDataArraysOverTime(Node, PBVTK_Node):

    bl_idname = 'VTKExtractDataArraysOverTimeType'
    bl_label  = 'vtkExtractDataArraysOverTime'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReportStatisticsOnly: bpy.props.BoolProperty(name='ReportStatisticsOnly', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseGlobalIDs: bpy.props.BoolProperty(name='UseGlobalIDs', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldAssociation: bpy.props.IntProperty(name='FieldAssociation', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReportStatisticsOnly','m_UseGlobalIDs','m_ObjectName','m_FieldAssociation',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExtractDataArraysOverTime )        
TYPENAMES.append('VTKExtractDataArraysOverTimeType' )

#--------------------------------------------------------------
class VTKExtractDataOverTime(Node, PBVTK_Node):

    bl_idname = 'VTKExtractDataOverTimeType'
    bl_label  = 'vtkExtractDataOverTime'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PointIndex: bpy.props.IntProperty(name='PointIndex', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_PointIndex',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExtractDataOverTime )        
TYPENAMES.append('VTKExtractDataOverTimeType' )

#--------------------------------------------------------------
class VTKExtractDataSets(Node, PBVTK_Node):

    bl_idname = 'VTKExtractDataSetsType'
    bl_label  = 'vtkExtractDataSets'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExtractDataSets )        
TYPENAMES.append('VTKExtractDataSetsType' )

#--------------------------------------------------------------
class VTKExtractEdges(Node, PBVTK_Node):

    bl_idname = 'VTKExtractEdgesType'
    bl_label  = 'vtkExtractEdges'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseAllPoints: bpy.props.BoolProperty(name='UseAllPoints', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_UseAllPoints','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExtractEdges )        
TYPENAMES.append('VTKExtractEdgesType' )

#--------------------------------------------------------------
class VTKExtractExodusGlobalTemporalVariables(Node, PBVTK_Node):

    bl_idname = 'VTKExtractExodusGlobalTemporalVariablesType'
    bl_label  = 'vtkExtractExodusGlobalTemporalVariables'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AutoDetectGlobalTemporalDataArrays: bpy.props.BoolProperty(name='AutoDetectGlobalTemporalDataArrays', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AutoDetectGlobalTemporalDataArrays','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExtractExodusGlobalTemporalVariables )        
TYPENAMES.append('VTKExtractExodusGlobalTemporalVariablesType' )

#--------------------------------------------------------------
class VTKExtractGeometry(Node, PBVTK_Node):

    bl_idname = 'VTKExtractGeometryType'
    bl_label  = 'vtkExtractGeometry'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ExtractBoundaryCells: bpy.props.BoolProperty(name='ExtractBoundaryCells', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ExtractInside: bpy.props.BoolProperty(name='ExtractInside', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ExtractOnlyBoundaryCells: bpy.props.BoolProperty(name='ExtractOnlyBoundaryCells', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ExtractBoundaryCells','m_ExtractInside','m_ExtractOnlyBoundaryCells','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'ImplicitFunction'], []) 
    
add_class( VTKExtractGeometry )        
TYPENAMES.append('VTKExtractGeometryType' )

#--------------------------------------------------------------
class VTKExtractGhostCells(Node, PBVTK_Node):

    bl_idname = 'VTKExtractGhostCellsType'
    bl_label  = 'vtkExtractGhostCells'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputGhostArrayName: bpy.props.StringProperty(name='OutputGhostArrayName', default="GhostType", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_OutputGhostArrayName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExtractGhostCells )        
TYPENAMES.append('VTKExtractGhostCellsType' )

#--------------------------------------------------------------
class VTKExtractGrid(Node, PBVTK_Node):

    bl_idname = 'VTKExtractGridType'
    bl_label  = 'vtkExtractGrid'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IncludeBoundary: bpy.props.BoolProperty(name='IncludeBoundary', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SampleRate: bpy.props.IntVectorProperty(name='SampleRate', default=[1, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VOI: bpy.props.IntVectorProperty(name='VOI', default=[0, 1000000000, 0, 1000000000, 0, 1000000000], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_IncludeBoundary','m_ObjectName','m_SampleRate','m_VOI',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExtractGrid )        
TYPENAMES.append('VTKExtractGridType' )

#--------------------------------------------------------------
class VTKExtractHistogram(Node, PBVTK_Node):

    bl_idname = 'VTKExtractHistogramType'
    bl_label  = 'vtkExtractHistogram'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Accumulation: bpy.props.BoolProperty(name='Accumulation', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CalculateAverages: bpy.props.BoolProperty(name='CalculateAverages', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CenterBinsAroundMinAndMax: bpy.props.BoolProperty(name='CenterBinsAroundMinAndMax', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Normalize: bpy.props.BoolProperty(name='Normalize', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseCustomBinRanges: bpy.props.BoolProperty(name='UseCustomBinRanges', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BinAccumulationArrayName: bpy.props.StringProperty(name='BinAccumulationArrayName', default="bin_accumulation", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BinExtentsArrayName: bpy.props.StringProperty(name='BinExtentsArrayName', default="bin_extents", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BinValuesArrayName: bpy.props.StringProperty(name='BinValuesArrayName', default="bin_values", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BinCount: bpy.props.IntProperty(name='BinCount', default=10, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Component: bpy.props.IntProperty(name='Component', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CustomBinRanges: bpy.props.FloatVectorProperty(name='CustomBinRanges', default=[0.0, 100.0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Accumulation','m_CalculateAverages','m_CenterBinsAroundMinAndMax','m_Normalize','m_UseCustomBinRanges','m_BinAccumulationArrayName','m_BinExtentsArrayName','m_BinValuesArrayName','m_ObjectName','m_BinCount','m_Component','m_CustomBinRanges',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExtractHistogram )        
TYPENAMES.append('VTKExtractHistogramType' )

#--------------------------------------------------------------
class VTKExtractLevel(Node, PBVTK_Node):

    bl_idname = 'VTKExtractLevelType'
    bl_label  = 'vtkExtractLevel'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExtractLevel )        
TYPENAMES.append('VTKExtractLevelType' )

#--------------------------------------------------------------
class VTKExtractPiece(Node, PBVTK_Node):

    bl_idname = 'VTKExtractPieceType'
    bl_label  = 'vtkExtractPiece'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExtractPiece )        
TYPENAMES.append('VTKExtractPieceType' )

#--------------------------------------------------------------
class VTKExtractPointCloudPiece(Node, PBVTK_Node):

    bl_idname = 'VTKExtractPointCloudPieceType'
    bl_label  = 'vtkExtractPointCloudPiece'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ModuloOrdering: bpy.props.BoolProperty(name='ModuloOrdering', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ModuloOrdering','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExtractPointCloudPiece )        
TYPENAMES.append('VTKExtractPointCloudPieceType' )

#--------------------------------------------------------------
class VTKExtractPolyDataGeometry(Node, PBVTK_Node):

    bl_idname = 'VTKExtractPolyDataGeometryType'
    bl_label  = 'vtkExtractPolyDataGeometry'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ExtractBoundaryCells: bpy.props.BoolProperty(name='ExtractBoundaryCells', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ExtractInside: bpy.props.BoolProperty(name='ExtractInside', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassPoints: bpy.props.BoolProperty(name='PassPoints', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ExtractBoundaryCells','m_ExtractInside','m_PassPoints','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'ImplicitFunction'], []) 
    
add_class( VTKExtractPolyDataGeometry )        
TYPENAMES.append('VTKExtractPolyDataGeometryType' )

#--------------------------------------------------------------
class VTKExtractPolyDataPiece(Node, PBVTK_Node):

    bl_idname = 'VTKExtractPolyDataPieceType'
    bl_label  = 'vtkExtractPolyDataPiece'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CreateGhostCells: bpy.props.BoolProperty(name='CreateGhostCells', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CreateGhostCells','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExtractPolyDataPiece )        
TYPENAMES.append('VTKExtractPolyDataPieceType' )

#--------------------------------------------------------------
class VTKExtractRectilinearGrid(Node, PBVTK_Node):

    bl_idname = 'VTKExtractRectilinearGridType'
    bl_label  = 'vtkExtractRectilinearGrid'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IncludeBoundary: bpy.props.BoolProperty(name='IncludeBoundary', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SampleRate: bpy.props.IntVectorProperty(name='SampleRate', default=[1, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VOI: bpy.props.IntVectorProperty(name='VOI', default=[0, 1000000000, 0, 1000000000, 0, 1000000000], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_IncludeBoundary','m_ObjectName','m_SampleRate','m_VOI',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExtractRectilinearGrid )        
TYPENAMES.append('VTKExtractRectilinearGridType' )

#--------------------------------------------------------------
class VTKExtractSubsetWithSeed(Node, PBVTK_Node):

    bl_idname = 'VTKExtractSubsetWithSeedType'
    bl_label  = 'vtkExtractSubsetWithSeed'
    e_Direction_items=[ (x,x,x) for x in ['LineI', 'LineJ', 'LineK', 'PlaneIJ', 'PlaneJK', 'PlaneKI']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_Direction: bpy.props.EnumProperty(name='Direction', default="LineI", items=e_Direction_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Seed: bpy.props.FloatVectorProperty(name='Seed', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','e_Direction','m_Seed',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExtractSubsetWithSeed )        
TYPENAMES.append('VTKExtractSubsetWithSeedType' )

#--------------------------------------------------------------
class VTKExtractSurface(Node, PBVTK_Node):

    bl_idname = 'VTKExtractSurfaceType'
    bl_label  = 'vtkExtractSurface'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeGradients: bpy.props.BoolProperty(name='ComputeGradients', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeNormals: bpy.props.BoolProperty(name='ComputeNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HoleFilling: bpy.props.BoolProperty(name='HoleFilling', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Radius: bpy.props.FloatProperty(name='Radius', default=0.1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeGradients','m_ComputeNormals','m_HoleFilling','m_ObjectName','m_Radius',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExtractSurface )        
TYPENAMES.append('VTKExtractSurfaceType' )

#--------------------------------------------------------------
class VTKExtractTensorComponents(Node, PBVTK_Node):

    bl_idname = 'VTKExtractTensorComponentsType'
    bl_label  = 'vtkExtractTensorComponents'
    e_ScalarMode_items=[ (x,x,x) for x in ['Component', 'EffectiveStress', 'Determinant', 'NonNegativeDeterminant', 'Trace']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ExtractNormals: bpy.props.BoolProperty(name='ExtractNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ExtractScalars: bpy.props.BoolProperty(name='ExtractScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ExtractTCoords: bpy.props.BoolProperty(name='ExtractTCoords', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ExtractVectors: bpy.props.BoolProperty(name='ExtractVectors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NormalizeNormals: bpy.props.BoolProperty(name='NormalizeNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassTensorsToOutput: bpy.props.BoolProperty(name='PassTensorsToOutput', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfTCoords: bpy.props.IntProperty(name='NumberOfTCoords', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputPrecision: bpy.props.IntProperty(name='OutputPrecision', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ScalarMode: bpy.props.EnumProperty(name='ScalarMode', default="Component", items=e_ScalarMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NormalComponents: bpy.props.IntVectorProperty(name='NormalComponents', default=[0, 1, 1, 1, 2, 1], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarComponents: bpy.props.IntVectorProperty(name='ScalarComponents', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TCoordComponents: bpy.props.IntVectorProperty(name='TCoordComponents', default=[0, 2, 1, 2, 2, 2], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VectorComponents: bpy.props.IntVectorProperty(name='VectorComponents', default=[0, 0, 1, 0, 2, 0], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ExtractNormals','m_ExtractScalars','m_ExtractTCoords','m_ExtractVectors','m_NormalizeNormals','m_PassTensorsToOutput','m_ObjectName','m_NumberOfTCoords','m_OutputPrecision','e_ScalarMode','m_NormalComponents','m_ScalarComponents','m_TCoordComponents','m_VectorComponents',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExtractTensorComponents )        
TYPENAMES.append('VTKExtractTensorComponentsType' )

#--------------------------------------------------------------
class VTKExtractTimeSteps(Node, PBVTK_Node):

    bl_idname = 'VTKExtractTimeStepsType'
    bl_label  = 'vtkExtractTimeSteps'
    e_TimeEstimationMode_items=[ (x,x,x) for x in ['Previous', 'Next', 'Nearest']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseRange: bpy.props.BoolProperty(name='UseRange', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepInterval: bpy.props.IntProperty(name='TimeStepInterval', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_TimeEstimationMode: bpy.props.EnumProperty(name='TimeEstimationMode', default="Previous", items=e_TimeEstimationMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Range: bpy.props.IntVectorProperty(name='Range', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_UseRange','m_ObjectName','m_TimeStepInterval','e_TimeEstimationMode','m_Range',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExtractTimeSteps )        
TYPENAMES.append('VTKExtractTimeStepsType' )

#--------------------------------------------------------------
class VTKExtractUnstructuredGrid(Node, PBVTK_Node):

    bl_idname = 'VTKExtractUnstructuredGridType'
    bl_label  = 'vtkExtractUnstructuredGrid'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CellClipping: bpy.props.BoolProperty(name='CellClipping', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ExtentClipping: bpy.props.BoolProperty(name='ExtentClipping', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Merging: bpy.props.BoolProperty(name='Merging', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PointClipping: bpy.props.BoolProperty(name='PointClipping', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CellMaximum: bpy.props.IntProperty(name='CellMaximum', default=1000000000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CellMinimum: bpy.props.IntProperty(name='CellMinimum', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PointMaximum: bpy.props.IntProperty(name='PointMaximum', default=1000000000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PointMinimum: bpy.props.IntProperty(name='PointMinimum', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Extent: bpy.props.FloatVectorProperty(name='Extent', default=[-1e+30, 1e+30, -1e+30, 1e+30, -1e+30, 1e+30], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CellClipping','m_ExtentClipping','m_Merging','m_PointClipping','m_ObjectName','m_CellMaximum','m_CellMinimum','m_PointMaximum','m_PointMinimum','m_Extent',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExtractUnstructuredGrid )        
TYPENAMES.append('VTKExtractUnstructuredGridType' )

#--------------------------------------------------------------
class VTKExtractUnstructuredGridPiece(Node, PBVTK_Node):

    bl_idname = 'VTKExtractUnstructuredGridPieceType'
    bl_label  = 'vtkExtractUnstructuredGridPiece'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CreateGhostCells: bpy.props.BoolProperty(name='CreateGhostCells', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CreateGhostCells','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExtractUnstructuredGridPiece )        
TYPENAMES.append('VTKExtractUnstructuredGridPieceType' )

#--------------------------------------------------------------
class VTKExtractUserDefinedPiece(Node, PBVTK_Node):

    bl_idname = 'VTKExtractUserDefinedPieceType'
    bl_label  = 'vtkExtractUserDefinedPiece'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CreateGhostCells: bpy.props.BoolProperty(name='CreateGhostCells', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CreateGhostCells','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExtractUserDefinedPiece )        
TYPENAMES.append('VTKExtractUserDefinedPieceType' )

#--------------------------------------------------------------
class VTKExtractVOI(Node, PBVTK_Node):

    bl_idname = 'VTKExtractVOIType'
    bl_label  = 'vtkExtractVOI'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IncludeBoundary: bpy.props.BoolProperty(name='IncludeBoundary', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SampleRate: bpy.props.IntVectorProperty(name='SampleRate', default=[1, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VOI: bpy.props.IntVectorProperty(name='VOI', default=[0, 1000000000, 0, 1000000000, 0, 1000000000], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_IncludeBoundary','m_ObjectName','m_SampleRate','m_VOI',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKExtractVOI )        
TYPENAMES.append('VTKExtractVOIType' )

#--------------------------------------------------------------
class VTKFeatureEdges(Node, PBVTK_Node):

    bl_idname = 'VTKFeatureEdgesType'
    bl_label  = 'vtkFeatureEdges'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BoundaryEdges: bpy.props.BoolProperty(name='BoundaryEdges', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Coloring: bpy.props.BoolProperty(name='Coloring', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FeatureEdges: bpy.props.BoolProperty(name='FeatureEdges', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ManifoldEdges: bpy.props.BoolProperty(name='ManifoldEdges', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NonManifoldEdges: bpy.props.BoolProperty(name='NonManifoldEdges', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassLines: bpy.props.BoolProperty(name='PassLines', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RemoveGhostInterfaces: bpy.props.BoolProperty(name='RemoveGhostInterfaces', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FeatureAngle: bpy.props.FloatProperty(name='FeatureAngle', default=30.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_BoundaryEdges','m_Coloring','m_FeatureEdges','m_ManifoldEdges','m_NonManifoldEdges','m_PassLines','m_RemoveGhostInterfaces','m_ObjectName','m_FeatureAngle',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKFeatureEdges )        
TYPENAMES.append('VTKFeatureEdgesType' )

#--------------------------------------------------------------
class VTKFieldDataToAttributeDataFilter(Node, PBVTK_Node):

    bl_idname = 'VTKFieldDataToAttributeDataFilterType'
    bl_label  = 'vtkFieldDataToAttributeDataFilter'
    e_InputField_items=[ (x,x,x) for x in ['DataObjectField', 'PointDataField', 'CellDataField']]
    e_OutputAttributeData_items=[ (x,x,x) for x in ['CellData', 'PointData']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DefaultNormalize: bpy.props.BoolProperty(name='DefaultNormalize', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_InputField: bpy.props.EnumProperty(name='InputField', default="DataObjectField", items=e_InputField_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_OutputAttributeData: bpy.props.EnumProperty(name='OutputAttributeData', default="PointData", items=e_OutputAttributeData_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_DefaultNormalize','m_ObjectName','e_InputField','e_OutputAttributeData',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKFieldDataToAttributeDataFilter )        
TYPENAMES.append('VTKFieldDataToAttributeDataFilterType' )

#--------------------------------------------------------------
class VTKFieldDataToDataSetAttribute(Node, PBVTK_Node):

    bl_idname = 'VTKFieldDataToDataSetAttributeType'
    bl_label  = 'vtkFieldDataToDataSetAttribute'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ProcessAllArrays: bpy.props.BoolProperty(name='ProcessAllArrays', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputFieldType: bpy.props.IntProperty(name='OutputFieldType', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ProcessAllArrays','m_ObjectName','m_OutputFieldType',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKFieldDataToDataSetAttribute )        
TYPENAMES.append('VTKFieldDataToDataSetAttributeType' )

#--------------------------------------------------------------
class VTKFillHolesFilter(Node, PBVTK_Node):

    bl_idname = 'VTKFillHolesFilterType'
    bl_label  = 'vtkFillHolesFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HoleSize: bpy.props.FloatProperty(name='HoleSize', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_HoleSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKFillHolesFilter )        
TYPENAMES.append('VTKFillHolesFilterType' )

#--------------------------------------------------------------
class VTKFiniteElementFieldDistributor(Node, PBVTK_Node):

    bl_idname = 'VTKFiniteElementFieldDistributorType'
    bl_label  = 'vtkFiniteElementFieldDistributor'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKFiniteElementFieldDistributor )        
TYPENAMES.append('VTKFiniteElementFieldDistributorType' )

#--------------------------------------------------------------
class VTKFlyingEdges2D(Node, PBVTK_Node):

    bl_idname = 'VTKFlyingEdges2DType'
    bl_label  = 'vtkFlyingEdges2D'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeScalars: bpy.props.BoolProperty(name='ComputeScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ArrayComponent: bpy.props.IntProperty(name='ArrayComponent', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfContours: bpy.props.IntProperty(name='NumberOfContours', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeScalars','m_ObjectName','m_ArrayComponent','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKFlyingEdges2D )        
TYPENAMES.append('VTKFlyingEdges2DType' )

#--------------------------------------------------------------
class VTKFlyingEdges3D(Node, PBVTK_Node):

    bl_idname = 'VTKFlyingEdges3DType'
    bl_label  = 'vtkFlyingEdges3D'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeGradients: bpy.props.BoolProperty(name='ComputeGradients', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeNormals: bpy.props.BoolProperty(name='ComputeNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeScalars: bpy.props.BoolProperty(name='ComputeScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InterpolateAttributes: bpy.props.BoolProperty(name='InterpolateAttributes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ArrayComponent: bpy.props.IntProperty(name='ArrayComponent', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfContours: bpy.props.IntProperty(name='NumberOfContours', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeGradients','m_ComputeNormals','m_ComputeScalars','m_InterpolateAttributes','m_ObjectName','m_ArrayComponent','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKFlyingEdges3D )        
TYPENAMES.append('VTKFlyingEdges3DType' )

#--------------------------------------------------------------
class VTKFlyingEdgesPlaneCutter(Node, PBVTK_Node):

    bl_idname = 'VTKFlyingEdgesPlaneCutterType'
    bl_label  = 'vtkFlyingEdgesPlaneCutter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeNormals: bpy.props.BoolProperty(name='ComputeNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InterpolateAttributes: bpy.props.BoolProperty(name='InterpolateAttributes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ArrayComponent: bpy.props.IntProperty(name='ArrayComponent', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeNormals','m_InterpolateAttributes','m_ObjectName','m_ArrayComponent',]
    def m_connections( self ):
        return (['input'], ['output'], ['Plane', 'ContainerAlgorithm'], []) 
    
add_class( VTKFlyingEdgesPlaneCutter )        
TYPENAMES.append('VTKFlyingEdgesPlaneCutterType' )

#--------------------------------------------------------------
class VTKForEach(Node, PBVTK_Node):

    bl_idname = 'VTKForEachType'
    bl_label  = 'vtkForEach'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKForEach )        
TYPENAMES.append('VTKForEachType' )

#--------------------------------------------------------------
class VTKForceStaticMesh(Node, PBVTK_Node):

    bl_idname = 'VTKForceStaticMeshType'
    bl_label  = 'vtkForceStaticMesh'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AllowNullInput: bpy.props.BoolProperty(name='AllowNullInput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DeepCopyInput: bpy.props.BoolProperty(name='DeepCopyInput', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ForceCacheComputation: bpy.props.BoolProperty(name='ForceCacheComputation', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AllowNullInput','m_DeepCopyInput','m_ForceCacheComputation','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKForceStaticMesh )        
TYPENAMES.append('VTKForceStaticMeshType' )

#--------------------------------------------------------------
class VTKForceTime(Node, PBVTK_Node):

    bl_idname = 'VTKForceTimeType'
    bl_label  = 'vtkForceTime'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IgnorePipelineTime: bpy.props.BoolProperty(name='IgnorePipelineTime', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ForcedTime: bpy.props.FloatProperty(name='ForcedTime', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_IgnorePipelineTime','m_ObjectName','m_ForcedTime',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKForceTime )        
TYPENAMES.append('VTKForceTimeType' )

#--------------------------------------------------------------
class VTKGaussianSplatter(Node, PBVTK_Node):

    bl_idname = 'VTKGaussianSplatterType'
    bl_label  = 'vtkGaussianSplatter'
    e_AccumulationMode_items=[ (x,x,x) for x in ['Min', 'Max', 'Sum']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Capping: bpy.props.BoolProperty(name='Capping', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NormalWarping: bpy.props.BoolProperty(name='NormalWarping', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarWarping: bpy.props.BoolProperty(name='ScalarWarping', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CapValue: bpy.props.FloatProperty(name='CapValue', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Eccentricity: bpy.props.FloatProperty(name='Eccentricity', default=2.5, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ExponentFactor: bpy.props.FloatProperty(name='ExponentFactor', default=-5.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NullValue: bpy.props.FloatProperty(name='NullValue', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Radius: bpy.props.FloatProperty(name='Radius', default=0.1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScaleFactor: bpy.props.FloatProperty(name='ScaleFactor', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_AccumulationMode: bpy.props.EnumProperty(name='AccumulationMode', default="Max", items=e_AccumulationMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SampleDimensions: bpy.props.IntVectorProperty(name='SampleDimensions', default=[50, 50, 50], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ModelBounds: bpy.props.FloatVectorProperty(name='ModelBounds', default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=14, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Capping','m_NormalWarping','m_ScalarWarping','m_ObjectName','m_CapValue','m_Eccentricity','m_ExponentFactor','m_NullValue','m_Radius','m_ScaleFactor','e_AccumulationMode','m_SampleDimensions','m_ModelBounds',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKGaussianSplatter )        
TYPENAMES.append('VTKGaussianSplatterType' )

#--------------------------------------------------------------
class VTKGenerateGlobalIds(Node, PBVTK_Node):

    bl_idname = 'VTKGenerateGlobalIdsType'
    bl_label  = 'vtkGenerateGlobalIds'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_Tolerance',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKGenerateGlobalIds )        
TYPENAMES.append('VTKGenerateGlobalIdsType' )

#--------------------------------------------------------------
class VTKGenerateIds(Node, PBVTK_Node):

    bl_idname = 'VTKGenerateIdsType'
    bl_label  = 'vtkGenerateIds'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CellIds: bpy.props.BoolProperty(name='CellIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldData: bpy.props.BoolProperty(name='FieldData', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PointIds: bpy.props.BoolProperty(name='PointIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CellIdsArrayName: bpy.props.StringProperty(name='CellIdsArrayName', default="vtkCellIds", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PointIdsArrayName: bpy.props.StringProperty(name='PointIdsArrayName', default="vtkPointIds", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CellIds','m_FieldData','m_PointIds','m_CellIdsArrayName','m_ObjectName','m_PointIdsArrayName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKGenerateIds )        
TYPENAMES.append('VTKGenerateIdsType' )

#--------------------------------------------------------------
class VTKGenerateProcessIds(Node, PBVTK_Node):

    bl_idname = 'VTKGenerateProcessIdsType'
    bl_label  = 'vtkGenerateProcessIds'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateCellData: bpy.props.BoolProperty(name='GenerateCellData', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GeneratePointData: bpy.props.BoolProperty(name='GeneratePointData', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_GenerateCellData','m_GeneratePointData','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKGenerateProcessIds )        
TYPENAMES.append('VTKGenerateProcessIdsType' )

#--------------------------------------------------------------
class VTKGenerateRegionIds(Node, PBVTK_Node):

    bl_idname = 'VTKGenerateRegionIdsType'
    bl_label  = 'vtkGenerateRegionIds'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RegionIdsArrayName: bpy.props.StringProperty(name='RegionIdsArrayName', default="vtkRegionIds", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaxAngle: bpy.props.FloatProperty(name='MaxAngle', default=30.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_RegionIdsArrayName','m_MaxAngle',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKGenerateRegionIds )        
TYPENAMES.append('VTKGenerateRegionIdsType' )

#--------------------------------------------------------------
class VTKGenerateTimeSteps(Node, PBVTK_Node):

    bl_idname = 'VTKGenerateTimeStepsType'
    bl_label  = 'vtkGenerateTimeSteps'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKGenerateTimeSteps )        
TYPENAMES.append('VTKGenerateTimeStepsType' )

#--------------------------------------------------------------
class VTKGenericContourFilter(Node, PBVTK_Node):

    bl_idname = 'VTKGenericContourFilterType'
    bl_label  = 'vtkGenericContourFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeGradients: bpy.props.BoolProperty(name='ComputeGradients', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeNormals: bpy.props.BoolProperty(name='ComputeNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeScalars: bpy.props.BoolProperty(name='ComputeScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfContours: bpy.props.IntProperty(name='NumberOfContours', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeGradients','m_ComputeNormals','m_ComputeScalars','m_ObjectName','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKGenericContourFilter )        
TYPENAMES.append('VTKGenericContourFilterType' )

#--------------------------------------------------------------
class VTKGenericCutter(Node, PBVTK_Node):

    bl_idname = 'VTKGenericCutterType'
    bl_label  = 'vtkGenericCutter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateCutScalars: bpy.props.BoolProperty(name='GenerateCutScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfContours: bpy.props.IntProperty(name='NumberOfContours', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_GenerateCutScalars','m_ObjectName','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'CutFunction'], []) 
    
add_class( VTKGenericCutter )        
TYPENAMES.append('VTKGenericCutterType' )

#--------------------------------------------------------------
class VTKGenericDataSetTessellator(Node, PBVTK_Node):

    bl_idname = 'VTKGenericDataSetTessellatorType'
    bl_label  = 'vtkGenericDataSetTessellator'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_KeepCellIds: bpy.props.BoolProperty(name='KeepCellIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Merging: bpy.props.BoolProperty(name='Merging', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_KeepCellIds','m_Merging','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKGenericDataSetTessellator )        
TYPENAMES.append('VTKGenericDataSetTessellatorType' )

#--------------------------------------------------------------
class VTKGenericGeometryFilter(Node, PBVTK_Node):

    bl_idname = 'VTKGenericGeometryFilterType'
    bl_label  = 'vtkGenericGeometryFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CellClipping: bpy.props.BoolProperty(name='CellClipping', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ExtentClipping: bpy.props.BoolProperty(name='ExtentClipping', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Merging: bpy.props.BoolProperty(name='Merging', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassThroughCellIds: bpy.props.BoolProperty(name='PassThroughCellIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PointClipping: bpy.props.BoolProperty(name='PointClipping', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CellMaximum: bpy.props.IntProperty(name='CellMaximum', default=1000000000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CellMinimum: bpy.props.IntProperty(name='CellMinimum', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PointMaximum: bpy.props.IntProperty(name='PointMaximum', default=1000000000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PointMinimum: bpy.props.IntProperty(name='PointMinimum', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CellClipping','m_ExtentClipping','m_Merging','m_PassThroughCellIds','m_PointClipping','m_ObjectName','m_CellMaximum','m_CellMinimum','m_PointMaximum','m_PointMinimum',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKGenericGeometryFilter )        
TYPENAMES.append('VTKGenericGeometryFilterType' )

#--------------------------------------------------------------
class VTKGenericOutlineFilter(Node, PBVTK_Node):

    bl_idname = 'VTKGenericOutlineFilterType'
    bl_label  = 'vtkGenericOutlineFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKGenericOutlineFilter )        
TYPENAMES.append('VTKGenericOutlineFilterType' )

#--------------------------------------------------------------
class VTKGhostCellsGenerator(Node, PBVTK_Node):

    bl_idname = 'VTKGhostCellsGeneratorType'
    bl_label  = 'vtkGhostCellsGenerator'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BuildIfRequired: bpy.props.BoolProperty(name='BuildIfRequired', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateGlobalIds: bpy.props.BoolProperty(name='GenerateGlobalIds', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateProcessIds: bpy.props.BoolProperty(name='GenerateProcessIds', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SynchronizeOnly: bpy.props.BoolProperty(name='SynchronizeOnly', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseStaticMeshCache: bpy.props.BoolProperty(name='UseStaticMeshCache', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfGhostLayers: bpy.props.IntProperty(name='NumberOfGhostLayers', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_BuildIfRequired','m_GenerateGlobalIds','m_GenerateProcessIds','m_SynchronizeOnly','m_UseStaticMeshCache','m_ObjectName','m_NumberOfGhostLayers',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKGhostCellsGenerator )        
TYPENAMES.append('VTKGhostCellsGeneratorType' )

#--------------------------------------------------------------
class VTKGradientFilter(Node, PBVTK_Node):

    bl_idname = 'VTKGradientFilterType'
    bl_label  = 'vtkGradientFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeDivergence: bpy.props.BoolProperty(name='ComputeDivergence', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeGradient: bpy.props.BoolProperty(name='ComputeGradient', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeQCriterion: bpy.props.BoolProperty(name='ComputeQCriterion', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeVorticity: bpy.props.BoolProperty(name='ComputeVorticity', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FasterApproximation: bpy.props.BoolProperty(name='FasterApproximation', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DivergenceArrayName: bpy.props.StringProperty(name='DivergenceArrayName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_QCriterionArrayName: bpy.props.StringProperty(name='QCriterionArrayName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ResultArrayName: bpy.props.StringProperty(name='ResultArrayName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VorticityArrayName: bpy.props.StringProperty(name='VorticityArrayName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ContributingCellOption: bpy.props.IntProperty(name='ContributingCellOption', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReplacementValueOption: bpy.props.IntProperty(name='ReplacementValueOption', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeDivergence','m_ComputeGradient','m_ComputeQCriterion','m_ComputeVorticity','m_FasterApproximation','m_DivergenceArrayName','m_ObjectName','m_QCriterionArrayName','m_ResultArrayName','m_VorticityArrayName','m_ContributingCellOption','m_ReplacementValueOption',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKGradientFilter )        
TYPENAMES.append('VTKGradientFilterType' )

#--------------------------------------------------------------
class VTKGraphAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKGraphAlgorithmType'
    bl_label  = 'vtkGraphAlgorithm'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKGraphAlgorithm )        
TYPENAMES.append('VTKGraphAlgorithmType' )

#--------------------------------------------------------------
class VTKGraphLayoutFilter(Node, PBVTK_Node):

    bl_idname = 'VTKGraphLayoutFilterType'
    bl_label  = 'vtkGraphLayoutFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AutomaticBoundsComputation: bpy.props.BoolProperty(name='AutomaticBoundsComputation', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ThreeDimensionalLayout: bpy.props.BoolProperty(name='ThreeDimensionalLayout', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaxNumberOfIterations: bpy.props.IntProperty(name='MaxNumberOfIterations', default=50, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CoolDownRate: bpy.props.FloatProperty(name='CoolDownRate', default=10.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GraphBounds: bpy.props.FloatVectorProperty(name='GraphBounds', default=[-0.5, 0.5, -0.5, 0.5, -0.5, 0.5], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AutomaticBoundsComputation','m_ThreeDimensionalLayout','m_ObjectName','m_MaxNumberOfIterations','m_CoolDownRate','m_GraphBounds',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKGraphLayoutFilter )        
TYPENAMES.append('VTKGraphLayoutFilterType' )

#--------------------------------------------------------------
class VTKGraphToGlyphs(Node, PBVTK_Node):

    bl_idname = 'VTKGraphToGlyphsType'
    bl_label  = 'vtkGraphToGlyphs'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Filled: bpy.props.BoolProperty(name='Filled', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Scaling: bpy.props.BoolProperty(name='Scaling', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlyphType: bpy.props.IntProperty(name='GlyphType', default=7, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScreenSize: bpy.props.FloatProperty(name='ScreenSize', default=10.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Filled','m_Scaling','m_ObjectName','m_GlyphType','m_ScreenSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'Renderer'], []) 
    
add_class( VTKGraphToGlyphs )        
TYPENAMES.append('VTKGraphToGlyphsType' )

#--------------------------------------------------------------
class VTKGraphToPoints(Node, PBVTK_Node):

    bl_idname = 'VTKGraphToPointsType'
    bl_label  = 'vtkGraphToPoints'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKGraphToPoints )        
TYPENAMES.append('VTKGraphToPointsType' )

#--------------------------------------------------------------
class VTKGraphWeightEuclideanDistanceFilter(Node, PBVTK_Node):

    bl_idname = 'VTKGraphWeightEuclideanDistanceFilterType'
    bl_label  = 'vtkGraphWeightEuclideanDistanceFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKGraphWeightEuclideanDistanceFilter )        
TYPENAMES.append('VTKGraphWeightEuclideanDistanceFilterType' )

#--------------------------------------------------------------
class VTKGreedyTerrainDecimation(Node, PBVTK_Node):

    bl_idname = 'VTKGreedyTerrainDecimationType'
    bl_label  = 'vtkGreedyTerrainDecimation'
    e_ErrorMeasure_items=[ (x,x,x) for x in ['NumberOfTriangles', 'SpecifiedReduction', 'AbsoluteError', 'RelativeError']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BoundaryVertexDeletion: bpy.props.BoolProperty(name='BoundaryVertexDeletion', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeNormals: bpy.props.BoolProperty(name='ComputeNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfTriangles: bpy.props.IntProperty(name='NumberOfTriangles', default=1000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AbsoluteError: bpy.props.FloatProperty(name='AbsoluteError', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Reduction: bpy.props.FloatProperty(name='Reduction', default=0.9, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RelativeError: bpy.props.FloatProperty(name='RelativeError', default=0.01, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ErrorMeasure: bpy.props.EnumProperty(name='ErrorMeasure', default="SpecifiedReduction", items=e_ErrorMeasure_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_BoundaryVertexDeletion','m_ComputeNormals','m_ObjectName','m_NumberOfTriangles','m_AbsoluteError','m_Reduction','m_RelativeError','e_ErrorMeasure',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKGreedyTerrainDecimation )        
TYPENAMES.append('VTKGreedyTerrainDecimationType' )

#--------------------------------------------------------------
class VTKGridSynchronizedTemplates3D(Node, PBVTK_Node):

    bl_idname = 'VTKGridSynchronizedTemplates3DType'
    bl_label  = 'vtkGridSynchronizedTemplates3D'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeGradients: bpy.props.BoolProperty(name='ComputeGradients', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeNormals: bpy.props.BoolProperty(name='ComputeNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeScalars: bpy.props.BoolProperty(name='ComputeScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateTriangles: bpy.props.BoolProperty(name='GenerateTriangles', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfContours: bpy.props.IntProperty(name='NumberOfContours', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeGradients','m_ComputeNormals','m_ComputeScalars','m_GenerateTriangles','m_ObjectName','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKGridSynchronizedTemplates3D )        
TYPENAMES.append('VTKGridSynchronizedTemplates3DType' )

#--------------------------------------------------------------
class VTKGroupDataSetsFilter(Node, PBVTK_Node):

    bl_idname = 'VTKGroupDataSetsFilterType'
    bl_label  = 'vtkGroupDataSetsFilter'
    e_OutputType_items=[ (x,x,x) for x in ['MultiBlockDataSet', 'PartitionedDataSet', 'PartitionedDataSetCollection']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CombineFirstLayerMultiblock: bpy.props.BoolProperty(name='CombineFirstLayerMultiblock', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_OutputType: bpy.props.EnumProperty(name='OutputType', default="PartitionedDataSetCollection", items=e_OutputType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CombineFirstLayerMultiblock','m_ObjectName','e_OutputType',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKGroupDataSetsFilter )        
TYPENAMES.append('VTKGroupDataSetsFilterType' )

#--------------------------------------------------------------
class VTKGroupTimeStepsFilter(Node, PBVTK_Node):

    bl_idname = 'VTKGroupTimeStepsFilterType'
    bl_label  = 'vtkGroupTimeStepsFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKGroupTimeStepsFilter )        
TYPENAMES.append('VTKGroupTimeStepsFilterType' )

#--------------------------------------------------------------
class VTKHedgeHog(Node, PBVTK_Node):

    bl_idname = 'VTKHedgeHogType'
    bl_label  = 'vtkHedgeHog'
    e_VectorMode_items=[ (x,x,x) for x in ['UseVector', 'UseNormal']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScaleFactor: bpy.props.FloatProperty(name='ScaleFactor', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_VectorMode: bpy.props.EnumProperty(name='VectorMode', default="UseVector", items=e_VectorMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_ScaleFactor','e_VectorMode',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHedgeHog )        
TYPENAMES.append('VTKHedgeHogType' )

#--------------------------------------------------------------
class VTKHierarchicalBinningFilter(Node, PBVTK_Node):

    bl_idname = 'VTKHierarchicalBinningFilterType'
    bl_label  = 'vtkHierarchicalBinningFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Automatic: bpy.props.BoolProperty(name='Automatic', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfLevels: bpy.props.IntProperty(name='NumberOfLevels', default=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Divisions: bpy.props.IntVectorProperty(name='Divisions', default=[2, 2, 2], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Bounds: bpy.props.FloatVectorProperty(name='Bounds', default=[0.0, 1.0, 0.0, 1.0, 0.0, 1.0], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Automatic','m_ObjectName','m_NumberOfLevels','m_Divisions','m_Bounds',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHierarchicalBinningFilter )        
TYPENAMES.append('VTKHierarchicalBinningFilterType' )

#--------------------------------------------------------------
class VTKHierarchicalBoxDataSetAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKHierarchicalBoxDataSetAlgorithmType'
    bl_label  = 'vtkHierarchicalBoxDataSetAlgorithm'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHierarchicalBoxDataSetAlgorithm )        
TYPENAMES.append('VTKHierarchicalBoxDataSetAlgorithmType' )

#--------------------------------------------------------------
class VTKHierarchicalDataExtractDataSets(Node, PBVTK_Node):

    bl_idname = 'VTKHierarchicalDataExtractDataSetsType'
    bl_label  = 'vtkHierarchicalDataExtractDataSets'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHierarchicalDataExtractDataSets )        
TYPENAMES.append('VTKHierarchicalDataExtractDataSetsType' )

#--------------------------------------------------------------
class VTKHierarchicalDataExtractLevel(Node, PBVTK_Node):

    bl_idname = 'VTKHierarchicalDataExtractLevelType'
    bl_label  = 'vtkHierarchicalDataExtractLevel'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHierarchicalDataExtractLevel )        
TYPENAMES.append('VTKHierarchicalDataExtractLevelType' )

#--------------------------------------------------------------
class VTKHierarchicalDataLevelFilter(Node, PBVTK_Node):

    bl_idname = 'VTKHierarchicalDataLevelFilterType'
    bl_label  = 'vtkHierarchicalDataLevelFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHierarchicalDataLevelFilter )        
TYPENAMES.append('VTKHierarchicalDataLevelFilterType' )

#--------------------------------------------------------------
class VTKHierarchicalDataSetGeometryFilter(Node, PBVTK_Node):

    bl_idname = 'VTKHierarchicalDataSetGeometryFilterType'
    bl_label  = 'vtkHierarchicalDataSetGeometryFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHierarchicalDataSetGeometryFilter )        
TYPENAMES.append('VTKHierarchicalDataSetGeometryFilterType' )

#--------------------------------------------------------------
class VTKHull(Node, PBVTK_Node):

    bl_idname = 'VTKHullType'
    bl_label  = 'vtkHull'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHull )        
TYPENAMES.append('VTKHullType' )

#--------------------------------------------------------------
class VTKHyperStreamline(Node, PBVTK_Node):

    bl_idname = 'VTKHyperStreamlineType'
    bl_label  = 'vtkHyperStreamline'
    e_IntegrationDirection_items=[ (x,x,x) for x in ['Forward', 'Backward', 'IntegrateBothDirections']]
    e_IntegrationEigenvector_items=[ (x,x,x) for x in ['Major', 'Medium', 'Minor']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LogScaling: bpy.props.BoolProperty(name='LogScaling', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfSides: bpy.props.IntProperty(name='NumberOfSides', default=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IntegrationStepLength: bpy.props.FloatProperty(name='IntegrationStepLength', default=0.2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumPropagationDistance: bpy.props.FloatProperty(name='MaximumPropagationDistance', default=100.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Radius: bpy.props.FloatProperty(name='Radius', default=0.5, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_StepLength: bpy.props.FloatProperty(name='StepLength', default=0.01, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TerminalEigenvalue: bpy.props.FloatProperty(name='TerminalEigenvalue', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_IntegrationDirection: bpy.props.EnumProperty(name='IntegrationDirection', default="Forward", items=e_IntegrationDirection_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_IntegrationEigenvector: bpy.props.EnumProperty(name='IntegrationEigenvector', default="Major", items=e_IntegrationEigenvector_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_LogScaling','m_ObjectName','m_NumberOfSides','m_IntegrationStepLength','m_MaximumPropagationDistance','m_Radius','m_StepLength','m_TerminalEigenvalue','e_IntegrationDirection','e_IntegrationEigenvector',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHyperStreamline )        
TYPENAMES.append('VTKHyperStreamlineType' )

#--------------------------------------------------------------
class VTKHyperTreeGridAxisClip(Node, PBVTK_Node):

    bl_idname = 'VTKHyperTreeGridAxisClipType'
    bl_label  = 'vtkHyperTreeGridAxisClip'
    e_ClipType_items=[ (x,x,x) for x in ['Plane', 'Box', 'Quadric']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InsideOut: bpy.props.BoolProperty(name='InsideOut', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PlaneNormalAxis: bpy.props.IntProperty(name='PlaneNormalAxis', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PlanePosition: bpy.props.FloatProperty(name='PlanePosition', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ClipType: bpy.props.EnumProperty(name='ClipType', default="Plane", items=e_ClipType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Bounds: bpy.props.FloatVectorProperty(name='Bounds', default=[-0.5, 0.5, -0.5, 0.5, -0.5, 0.5], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_InsideOut','m_ObjectName','m_PlaneNormalAxis','m_PlanePosition','e_ClipType','m_Bounds',]
    def m_connections( self ):
        return (['input'], ['output'], ['Quadric', 'ContainerAlgorithm'], []) 
    
add_class( VTKHyperTreeGridAxisClip )        
TYPENAMES.append('VTKHyperTreeGridAxisClipType' )

#--------------------------------------------------------------
class VTKHyperTreeGridAxisCut(Node, PBVTK_Node):

    bl_idname = 'VTKHyperTreeGridAxisCutType'
    bl_label  = 'vtkHyperTreeGridAxisCut'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PlaneNormalAxis: bpy.props.IntProperty(name='PlaneNormalAxis', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PlanePosition: bpy.props.FloatProperty(name='PlanePosition', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_PlaneNormalAxis','m_PlanePosition',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHyperTreeGridAxisCut )        
TYPENAMES.append('VTKHyperTreeGridAxisCutType' )

#--------------------------------------------------------------
class VTKHyperTreeGridAxisReflection(Node, PBVTK_Node):

    bl_idname = 'VTKHyperTreeGridAxisReflectionType'
    bl_label  = 'vtkHyperTreeGridAxisReflection'
    e_Plane_items=[ (x,x,x) for x in ['XMin', 'YMin', 'ZMin', 'XMax', 'YMax', 'ZMax', 'X', 'Y', 'Z']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Center: bpy.props.FloatProperty(name='Center', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_Plane: bpy.props.EnumProperty(name='Plane', default="XMin", items=e_Plane_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_Center','e_Plane',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHyperTreeGridAxisReflection )        
TYPENAMES.append('VTKHyperTreeGridAxisReflectionType' )

#--------------------------------------------------------------
class VTKHyperTreeGridCellCenters(Node, PBVTK_Node):

    bl_idname = 'VTKHyperTreeGridCellCentersType'
    bl_label  = 'vtkHyperTreeGridCellCenters'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ConvertGhostCellsToGhostPoints: bpy.props.BoolProperty(name='ConvertGhostCellsToGhostPoints', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CopyArrays: bpy.props.BoolProperty(name='CopyArrays', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VertexCells: bpy.props.BoolProperty(name='VertexCells', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ConvertGhostCellsToGhostPoints','m_CopyArrays','m_VertexCells','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHyperTreeGridCellCenters )        
TYPENAMES.append('VTKHyperTreeGridCellCentersType' )

#--------------------------------------------------------------
class VTKHyperTreeGridContour(Node, PBVTK_Node):

    bl_idname = 'VTKHyperTreeGridContourType'
    bl_label  = 'vtkHyperTreeGridContour'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseImplicitArrays: bpy.props.BoolProperty(name='UseImplicitArrays', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfContours: bpy.props.IntProperty(name='NumberOfContours', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_UseImplicitArrays','m_ObjectName','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHyperTreeGridContour )        
TYPENAMES.append('VTKHyperTreeGridContourType' )

#--------------------------------------------------------------
class VTKHyperTreeGridDepthLimiter(Node, PBVTK_Node):

    bl_idname = 'VTKHyperTreeGridDepthLimiterType'
    bl_label  = 'vtkHyperTreeGridDepthLimiter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_JustCreateNewMask: bpy.props.BoolProperty(name='JustCreateNewMask', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Depth: bpy.props.IntProperty(name='Depth', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_JustCreateNewMask','m_ObjectName','m_Depth',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHyperTreeGridDepthLimiter )        
TYPENAMES.append('VTKHyperTreeGridDepthLimiterType' )

#--------------------------------------------------------------
class VTKHyperTreeGridEvaluateCoarse(Node, PBVTK_Node):

    bl_idname = 'VTKHyperTreeGridEvaluateCoarseType'
    bl_label  = 'vtkHyperTreeGridEvaluateCoarse'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Operator: bpy.props.IntProperty(name='Operator', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_Operator',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHyperTreeGridEvaluateCoarse )        
TYPENAMES.append('VTKHyperTreeGridEvaluateCoarseType' )

#--------------------------------------------------------------
class VTKHyperTreeGridExtractGhostCells(Node, PBVTK_Node):

    bl_idname = 'VTKHyperTreeGridExtractGhostCellsType'
    bl_label  = 'vtkHyperTreeGridExtractGhostCells'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputGhostArrayName: bpy.props.StringProperty(name='OutputGhostArrayName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_OutputGhostArrayName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHyperTreeGridExtractGhostCells )        
TYPENAMES.append('VTKHyperTreeGridExtractGhostCellsType' )

#--------------------------------------------------------------
class VTKHyperTreeGridFeatureEdges(Node, PBVTK_Node):

    bl_idname = 'VTKHyperTreeGridFeatureEdgesType'
    bl_label  = 'vtkHyperTreeGridFeatureEdges'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MergePoints: bpy.props.BoolProperty(name='MergePoints', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_MergePoints','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHyperTreeGridFeatureEdges )        
TYPENAMES.append('VTKHyperTreeGridFeatureEdgesType' )

#--------------------------------------------------------------
class VTKHyperTreeGridGenerateFields(Node, PBVTK_Node):

    bl_idname = 'VTKHyperTreeGridGenerateFieldsType'
    bl_label  = 'vtkHyperTreeGridGenerateFields'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeCellCenterArray: bpy.props.BoolProperty(name='ComputeCellCenterArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeCellSizeArray: bpy.props.BoolProperty(name='ComputeCellSizeArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeTotalVisibleVolumeArray: bpy.props.BoolProperty(name='ComputeTotalVisibleVolumeArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeValidCellArray: bpy.props.BoolProperty(name='ComputeValidCellArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CellCenterArrayName: bpy.props.StringProperty(name='CellCenterArrayName', default="CellCenter", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CellSizeArrayName: bpy.props.StringProperty(name='CellSizeArrayName', default="CellSize", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TotalVisibleVolumeArrayName: bpy.props.StringProperty(name='TotalVisibleVolumeArrayName', default="TotalVisibleVolume", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ValidCellArrayName: bpy.props.StringProperty(name='ValidCellArrayName', default="ValidCell", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeCellCenterArray','m_ComputeCellSizeArray','m_ComputeTotalVisibleVolumeArray','m_ComputeValidCellArray','m_CellCenterArrayName','m_CellSizeArrayName','m_ObjectName','m_TotalVisibleVolumeArrayName','m_ValidCellArrayName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHyperTreeGridGenerateFields )        
TYPENAMES.append('VTKHyperTreeGridGenerateFieldsType' )

#--------------------------------------------------------------
class VTKHyperTreeGridGenerateGlobalIds(Node, PBVTK_Node):

    bl_idname = 'VTKHyperTreeGridGenerateGlobalIdsType'
    bl_label  = 'vtkHyperTreeGridGenerateGlobalIds'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHyperTreeGridGenerateGlobalIds )        
TYPENAMES.append('VTKHyperTreeGridGenerateGlobalIdsType' )

#--------------------------------------------------------------
class VTKHyperTreeGridGenerateProcessIds(Node, PBVTK_Node):

    bl_idname = 'VTKHyperTreeGridGenerateProcessIdsType'
    bl_label  = 'vtkHyperTreeGridGenerateProcessIds'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHyperTreeGridGenerateProcessIds )        
TYPENAMES.append('VTKHyperTreeGridGenerateProcessIdsType' )

#--------------------------------------------------------------
class VTKHyperTreeGridGeometry(Node, PBVTK_Node):

    bl_idname = 'VTKHyperTreeGridGeometryType'
    bl_label  = 'vtkHyperTreeGridGeometry'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FillMaterial: bpy.props.BoolProperty(name='FillMaterial', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Merging: bpy.props.BoolProperty(name='Merging', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassThroughCellIds: bpy.props.BoolProperty(name='PassThroughCellIds', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OriginalCellIdArrayName: bpy.props.StringProperty(name='OriginalCellIdArrayName', default="vtkOriginalCellIds", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FillMaterial','m_Merging','m_PassThroughCellIds','m_ObjectName','m_OriginalCellIdArrayName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHyperTreeGridGeometry )        
TYPENAMES.append('VTKHyperTreeGridGeometryType' )

#--------------------------------------------------------------
class VTKHyperTreeGridGhostCellsGenerator(Node, PBVTK_Node):

    bl_idname = 'VTKHyperTreeGridGhostCellsGeneratorType'
    bl_label  = 'vtkHyperTreeGridGhostCellsGenerator'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHyperTreeGridGhostCellsGenerator )        
TYPENAMES.append('VTKHyperTreeGridGhostCellsGeneratorType' )

#--------------------------------------------------------------
class VTKHyperTreeGridGradient(Node, PBVTK_Node):

    bl_idname = 'VTKHyperTreeGridGradientType'
    bl_label  = 'vtkHyperTreeGridGradient'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeDivergence: bpy.props.BoolProperty(name='ComputeDivergence', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeGradient: bpy.props.BoolProperty(name='ComputeGradient', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeQCriterion: bpy.props.BoolProperty(name='ComputeQCriterion', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeVorticity: bpy.props.BoolProperty(name='ComputeVorticity', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ExtensiveComputation: bpy.props.BoolProperty(name='ExtensiveComputation', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DivergenceArrayName: bpy.props.StringProperty(name='DivergenceArrayName', default="Divergence", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GradientArrayName: bpy.props.StringProperty(name='GradientArrayName', default="Gradient", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_QCriterionArrayName: bpy.props.StringProperty(name='QCriterionArrayName', default="QCriterion", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VorticityArrayName: bpy.props.StringProperty(name='VorticityArrayName', default="Vorticity", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Mode: bpy.props.IntProperty(name='Mode', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeDivergence','m_ComputeGradient','m_ComputeQCriterion','m_ComputeVorticity','m_ExtensiveComputation','m_DivergenceArrayName','m_GradientArrayName','m_ObjectName','m_QCriterionArrayName','m_VorticityArrayName','m_Mode',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHyperTreeGridGradient )        
TYPENAMES.append('VTKHyperTreeGridGradientType' )

#--------------------------------------------------------------
class VTKHyperTreeGridOutlineFilter(Node, PBVTK_Node):

    bl_idname = 'VTKHyperTreeGridOutlineFilterType'
    bl_label  = 'vtkHyperTreeGridOutlineFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateFaces: bpy.props.BoolProperty(name='GenerateFaces', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_GenerateFaces','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHyperTreeGridOutlineFilter )        
TYPENAMES.append('VTKHyperTreeGridOutlineFilterType' )

#--------------------------------------------------------------
class VTKHyperTreeGridPlaneCutter(Node, PBVTK_Node):

    bl_idname = 'VTKHyperTreeGridPlaneCutterType'
    bl_label  = 'vtkHyperTreeGridPlaneCutter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Dual: bpy.props.BoolProperty(name='Dual', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Plane: bpy.props.FloatVectorProperty(name='Plane', default=[0.0, 0.0, 0.0, 0.0], size=4, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Dual','m_ObjectName','m_Plane',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHyperTreeGridPlaneCutter )        
TYPENAMES.append('VTKHyperTreeGridPlaneCutterType' )

#--------------------------------------------------------------
class VTKHyperTreeGridRemoveGhostCells(Node, PBVTK_Node):

    bl_idname = 'VTKHyperTreeGridRemoveGhostCellsType'
    bl_label  = 'vtkHyperTreeGridRemoveGhostCells'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHyperTreeGridRemoveGhostCells )        
TYPENAMES.append('VTKHyperTreeGridRemoveGhostCellsType' )

#--------------------------------------------------------------
class VTKHyperTreeGridThreshold(Node, PBVTK_Node):

    bl_idname = 'VTKHyperTreeGridThresholdType'
    bl_label  = 'vtkHyperTreeGridThreshold'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MemoryStrategy: bpy.props.IntProperty(name='MemoryStrategy', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LowerThreshold: bpy.props.FloatProperty(name='LowerThreshold', default=2.2250738585072014e-308, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UpperThreshold: bpy.props.FloatProperty(name='UpperThreshold', default=1e+30, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_MemoryStrategy','m_LowerThreshold','m_UpperThreshold',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHyperTreeGridThreshold )        
TYPENAMES.append('VTKHyperTreeGridThresholdType' )

#--------------------------------------------------------------
class VTKHyperTreeGridToDualGrid(Node, PBVTK_Node):

    bl_idname = 'VTKHyperTreeGridToDualGridType'
    bl_label  = 'vtkHyperTreeGridToDualGrid'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHyperTreeGridToDualGrid )        
TYPENAMES.append('VTKHyperTreeGridToDualGridType' )

#--------------------------------------------------------------
class VTKHyperTreeGridToUnstructuredGrid(Node, PBVTK_Node):

    bl_idname = 'VTKHyperTreeGridToUnstructuredGridType'
    bl_label  = 'vtkHyperTreeGridToUnstructuredGrid'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AddOriginalIds: bpy.props.BoolProperty(name='AddOriginalIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AddOriginalIds','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHyperTreeGridToUnstructuredGrid )        
TYPENAMES.append('VTKHyperTreeGridToUnstructuredGridType' )

#--------------------------------------------------------------
class VTKHyperTreeGridVisibleLeavesSize(Node, PBVTK_Node):

    bl_idname = 'VTKHyperTreeGridVisibleLeavesSizeType'
    bl_label  = 'vtkHyperTreeGridVisibleLeavesSize'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeCellCenterArray: bpy.props.BoolProperty(name='ComputeCellCenterArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeCellSizeArray: bpy.props.BoolProperty(name='ComputeCellSizeArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeTotalVisibleVolumeArray: bpy.props.BoolProperty(name='ComputeTotalVisibleVolumeArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeValidCellArray: bpy.props.BoolProperty(name='ComputeValidCellArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CellCenterArrayName: bpy.props.StringProperty(name='CellCenterArrayName', default="CellCenter", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CellSizeArrayName: bpy.props.StringProperty(name='CellSizeArrayName', default="CellSize", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TotalVisibleVolumeArrayName: bpy.props.StringProperty(name='TotalVisibleVolumeArrayName', default="TotalVisibleVolume", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ValidCellArrayName: bpy.props.StringProperty(name='ValidCellArrayName', default="ValidCell", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeCellCenterArray','m_ComputeCellSizeArray','m_ComputeTotalVisibleVolumeArray','m_ComputeValidCellArray','m_CellCenterArrayName','m_CellSizeArrayName','m_ObjectName','m_TotalVisibleVolumeArrayName','m_ValidCellArrayName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKHyperTreeGridVisibleLeavesSize )        
TYPENAMES.append('VTKHyperTreeGridVisibleLeavesSizeType' )

#--------------------------------------------------------------
class VTKIconGlyphFilter(Node, PBVTK_Node):

    bl_idname = 'VTKIconGlyphFilterType'
    bl_label  = 'vtkIconGlyphFilter'
    e_Gravity_items=[ (x,x,x) for x in ['TopRight', 'TopCenter', 'TopLeft', 'CenterRight', 'CenterCenter', 'CenterLeft', 'BottomRight', 'BottomCenter', 'BottomLeft']]
    e_IconScaling_items=[ (x,x,x) for x in ['ScalingOff', 'ScalingArray']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassScalars: bpy.props.BoolProperty(name='PassScalars', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseIconSize: bpy.props.BoolProperty(name='UseIconSize', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_Gravity: bpy.props.EnumProperty(name='Gravity', default="CenterCenter", items=e_Gravity_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_IconScaling: bpy.props.EnumProperty(name='IconScaling', default="ScalingOff", items=e_IconScaling_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DisplaySize: bpy.props.IntVectorProperty(name='DisplaySize', default=[25, 25], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IconSheetSize: bpy.props.IntVectorProperty(name='IconSheetSize', default=[1, 1], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IconSize: bpy.props.IntVectorProperty(name='IconSize', default=[1, 1], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Offset: bpy.props.IntVectorProperty(name='Offset', default=[0, 0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_PassScalars','m_UseIconSize','m_ObjectName','e_Gravity','e_IconScaling','m_DisplaySize','m_IconSheetSize','m_IconSize','m_Offset',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKIconGlyphFilter )        
TYPENAMES.append('VTKIconGlyphFilterType' )

#--------------------------------------------------------------
class VTKIdFilter(Node, PBVTK_Node):

    bl_idname = 'VTKIdFilterType'
    bl_label  = 'vtkIdFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CellIds: bpy.props.BoolProperty(name='CellIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldData: bpy.props.BoolProperty(name='FieldData', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PointIds: bpy.props.BoolProperty(name='PointIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CellIdsArrayName: bpy.props.StringProperty(name='CellIdsArrayName', default="vtkIdFilter_Ids", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PointIdsArrayName: bpy.props.StringProperty(name='PointIdsArrayName', default="vtkIdFilter_Ids", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CellIds','m_FieldData','m_PointIds','m_CellIdsArrayName','m_ObjectName','m_PointIdsArrayName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKIdFilter )        
TYPENAMES.append('VTKIdFilterType' )

#--------------------------------------------------------------
class VTKImageAnisotropicDiffusion2D(Node, PBVTK_Node):

    bl_idname = 'VTKImageAnisotropicDiffusion2DType'
    bl_label  = 'vtkImageAnisotropicDiffusion2D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Corners: bpy.props.BoolProperty(name='Corners', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Edges: bpy.props.BoolProperty(name='Edges', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Faces: bpy.props.BoolProperty(name='Faces', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GradientMagnitudeThreshold: bpy.props.BoolProperty(name='GradientMagnitudeThreshold', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfIterations: bpy.props.IntProperty(name='NumberOfIterations', default=4, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DiffusionFactor: bpy.props.FloatProperty(name='DiffusionFactor', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DiffusionThreshold: bpy.props.FloatProperty(name='DiffusionThreshold', default=5.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Corners','m_Edges','m_EnableSMP','m_Faces','m_GlobalDefaultEnableSMP','m_GradientMagnitudeThreshold','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfIterations','m_NumberOfThreads','m_DiffusionFactor','m_DiffusionThreshold','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageAnisotropicDiffusion2D )        
TYPENAMES.append('VTKImageAnisotropicDiffusion2DType' )

#--------------------------------------------------------------
class VTKImageAnisotropicDiffusion3D(Node, PBVTK_Node):

    bl_idname = 'VTKImageAnisotropicDiffusion3DType'
    bl_label  = 'vtkImageAnisotropicDiffusion3D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Corners: bpy.props.BoolProperty(name='Corners', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Edges: bpy.props.BoolProperty(name='Edges', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Faces: bpy.props.BoolProperty(name='Faces', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GradientMagnitudeThreshold: bpy.props.BoolProperty(name='GradientMagnitudeThreshold', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfIterations: bpy.props.IntProperty(name='NumberOfIterations', default=4, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DiffusionFactor: bpy.props.FloatProperty(name='DiffusionFactor', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DiffusionThreshold: bpy.props.FloatProperty(name='DiffusionThreshold', default=5.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Corners','m_Edges','m_EnableSMP','m_Faces','m_GlobalDefaultEnableSMP','m_GradientMagnitudeThreshold','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfIterations','m_NumberOfThreads','m_DiffusionFactor','m_DiffusionThreshold','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageAnisotropicDiffusion3D )        
TYPENAMES.append('VTKImageAnisotropicDiffusion3DType' )

#--------------------------------------------------------------
class VTKImageAppend(Node, PBVTK_Node):

    bl_idname = 'VTKImageAppendType'
    bl_label  = 'vtkImageAppend'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PreserveExtents: bpy.props.BoolProperty(name='PreserveExtents', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AppendAxis: bpy.props.IntProperty(name='AppendAxis', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_PreserveExtents','m_ObjectName','m_AppendAxis','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageAppend )        
TYPENAMES.append('VTKImageAppendType' )

#--------------------------------------------------------------
class VTKImageAppendComponents(Node, PBVTK_Node):

    bl_idname = 'VTKImageAppendComponentsType'
    bl_label  = 'vtkImageAppendComponents'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageAppendComponents )        
TYPENAMES.append('VTKImageAppendComponentsType' )

#--------------------------------------------------------------
class VTKImageBSplineCoefficients(Node, PBVTK_Node):

    bl_idname = 'VTKImageBSplineCoefficientsType'
    bl_label  = 'vtkImageBSplineCoefficients'
    e_OutputScalarType_items=[ (x,x,x) for x in ['Float', 'Double']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Bypass: bpy.props.BoolProperty(name='Bypass', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SplineDegree: bpy.props.IntProperty(name='SplineDegree', default=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_OutputScalarType: bpy.props.EnumProperty(name='OutputScalarType', default="Float", items=e_OutputScalarType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Bypass','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','m_SplineDegree','e_OutputScalarType','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['BorderMode', 'ContainerAlgorithm'], []) 
    
add_class( VTKImageBSplineCoefficients )        
TYPENAMES.append('VTKImageBSplineCoefficientsType' )

#--------------------------------------------------------------
class VTKImageButterworthHighPass(Node, PBVTK_Node):

    bl_idname = 'VTKImageButterworthHighPassType'
    bl_label  = 'vtkImageButterworthHighPass'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Order: bpy.props.IntProperty(name='Order', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_XCutOff: bpy.props.FloatProperty(name='XCutOff', default=1e+30, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_YCutOff: bpy.props.FloatProperty(name='YCutOff', default=1e+30, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ZCutOff: bpy.props.FloatProperty(name='ZCutOff', default=1e+30, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CutOff: bpy.props.FloatVectorProperty(name='CutOff', default=[1e+30, 1e+30, 1e+30], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Order','m_XCutOff','m_YCutOff','m_ZCutOff','e_SplitMode','m_MinimumPieceSize','m_CutOff',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageButterworthHighPass )        
TYPENAMES.append('VTKImageButterworthHighPassType' )

#--------------------------------------------------------------
class VTKImageButterworthLowPass(Node, PBVTK_Node):

    bl_idname = 'VTKImageButterworthLowPassType'
    bl_label  = 'vtkImageButterworthLowPass'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Order: bpy.props.IntProperty(name='Order', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_XCutOff: bpy.props.FloatProperty(name='XCutOff', default=1e+30, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_YCutOff: bpy.props.FloatProperty(name='YCutOff', default=1e+30, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ZCutOff: bpy.props.FloatProperty(name='ZCutOff', default=1e+30, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CutOff: bpy.props.FloatVectorProperty(name='CutOff', default=[1e+30, 1e+30, 1e+30], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Order','m_XCutOff','m_YCutOff','m_ZCutOff','e_SplitMode','m_MinimumPieceSize','m_CutOff',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageButterworthLowPass )        
TYPENAMES.append('VTKImageButterworthLowPassType' )

#--------------------------------------------------------------
class VTKImageCacheFilter(Node, PBVTK_Node):

    bl_idname = 'VTKImageCacheFilterType'
    bl_label  = 'vtkImageCacheFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CacheSize: bpy.props.IntProperty(name='CacheSize', default=10, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_CacheSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageCacheFilter )        
TYPENAMES.append('VTKImageCacheFilterType' )

#--------------------------------------------------------------
class VTKImageCast(Node, PBVTK_Node):

    bl_idname = 'VTKImageCastType'
    bl_label  = 'vtkImageCast'
    e_OutputScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Long', 'UnsignedLong', 'Float', 'Double']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ClampOverflow: bpy.props.BoolProperty(name='ClampOverflow', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_OutputScalarType: bpy.props.EnumProperty(name='OutputScalarType', default="Float", items=e_OutputScalarType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ClampOverflow','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','e_OutputScalarType','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageCast )        
TYPENAMES.append('VTKImageCastType' )

#--------------------------------------------------------------
class VTKImageCityBlockDistance(Node, PBVTK_Node):

    bl_idname = 'VTKImageCityBlockDistanceType'
    bl_label  = 'vtkImageCityBlockDistance'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Dimensionality: bpy.props.IntProperty(name='Dimensionality', default=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageCityBlockDistance )        
TYPENAMES.append('VTKImageCityBlockDistanceType' )

#--------------------------------------------------------------
class VTKImageClip(Node, PBVTK_Node):

    bl_idname = 'VTKImageClipType'
    bl_label  = 'vtkImageClip'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ClipData: bpy.props.BoolProperty(name='ClipData', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ClipData','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageClip )        
TYPENAMES.append('VTKImageClipType' )

#--------------------------------------------------------------
class VTKImageConstantPad(Node, PBVTK_Node):

    bl_idname = 'VTKImageConstantPadType'
    bl_label  = 'vtkImageConstantPad'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputNumberOfScalarComponents: bpy.props.IntProperty(name='OutputNumberOfScalarComponents', default=-1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Constant: bpy.props.FloatProperty(name='Constant', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','m_OutputNumberOfScalarComponents','m_Constant','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['OutputWholeExtent', 'ComponentConstants', 'ContainerAlgorithm'], []) 
    
add_class( VTKImageConstantPad )        
TYPENAMES.append('VTKImageConstantPadType' )

#--------------------------------------------------------------
class VTKImageContinuousDilate3D(Node, PBVTK_Node):

    bl_idname = 'VTKImageContinuousDilate3DType'
    bl_label  = 'vtkImageContinuousDilate3D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_KernelSize: bpy.props.IntVectorProperty(name='KernelSize', default=[1, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_KernelSize','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageContinuousDilate3D )        
TYPENAMES.append('VTKImageContinuousDilate3DType' )

#--------------------------------------------------------------
class VTKImageContinuousErode3D(Node, PBVTK_Node):

    bl_idname = 'VTKImageContinuousErode3DType'
    bl_label  = 'vtkImageContinuousErode3D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_KernelSize: bpy.props.IntVectorProperty(name='KernelSize', default=[1, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_KernelSize','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageContinuousErode3D )        
TYPENAMES.append('VTKImageContinuousErode3DType' )

#--------------------------------------------------------------
class VTKImageConvolve(Node, PBVTK_Node):

    bl_idname = 'VTKImageConvolveType'
    bl_label  = 'vtkImageConvolve'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageConvolve )        
TYPENAMES.append('VTKImageConvolveType' )

#--------------------------------------------------------------
class VTKImageCursor3D(Node, PBVTK_Node):

    bl_idname = 'VTKImageCursor3DType'
    bl_label  = 'vtkImageCursor3D'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CursorRadius: bpy.props.IntProperty(name='CursorRadius', default=5, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CursorValue: bpy.props.FloatProperty(name='CursorValue', default=255.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CursorPosition: bpy.props.FloatVectorProperty(name='CursorPosition', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_CursorRadius','m_CursorValue','m_CursorPosition',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageCursor3D )        
TYPENAMES.append('VTKImageCursor3DType' )

#--------------------------------------------------------------
class VTKImageDataGeometryFilter(Node, PBVTK_Node):

    bl_idname = 'VTKImageDataGeometryFilterType'
    bl_label  = 'vtkImageDataGeometryFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputTriangles: bpy.props.BoolProperty(name='OutputTriangles', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ThresholdCells: bpy.props.BoolProperty(name='ThresholdCells', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ThresholdValue: bpy.props.BoolProperty(name='ThresholdValue', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_OutputTriangles','m_ThresholdCells','m_ThresholdValue','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageDataGeometryFilter )        
TYPENAMES.append('VTKImageDataGeometryFilterType' )

#--------------------------------------------------------------
class VTKImageDataOutlineFilter(Node, PBVTK_Node):

    bl_idname = 'VTKImageDataOutlineFilterType'
    bl_label  = 'vtkImageDataOutlineFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateFaces: bpy.props.BoolProperty(name='GenerateFaces', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_GenerateFaces','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageDataOutlineFilter )        
TYPENAMES.append('VTKImageDataOutlineFilterType' )

#--------------------------------------------------------------
class VTKImageDataStreamer(Node, PBVTK_Node):

    bl_idname = 'VTKImageDataStreamerType'
    bl_label  = 'vtkImageDataStreamer'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfStreamDivisions: bpy.props.IntProperty(name='NumberOfStreamDivisions', default=10, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_NumberOfStreamDivisions',]
    def m_connections( self ):
        return (['input'], ['output'], ['ExtentTranslator', 'ContainerAlgorithm'], []) 
    
add_class( VTKImageDataStreamer )        
TYPENAMES.append('VTKImageDataStreamerType' )

#--------------------------------------------------------------
class VTKImageDataToExplicitStructuredGrid(Node, PBVTK_Node):

    bl_idname = 'VTKImageDataToExplicitStructuredGridType'
    bl_label  = 'vtkImageDataToExplicitStructuredGrid'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageDataToExplicitStructuredGrid )        
TYPENAMES.append('VTKImageDataToExplicitStructuredGridType' )

#--------------------------------------------------------------
class VTKImageDataToHyperTreeGrid(Node, PBVTK_Node):

    bl_idname = 'VTKImageDataToHyperTreeGridType'
    bl_label  = 'vtkImageDataToHyperTreeGrid'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DepthMax: bpy.props.IntProperty(name='DepthMax', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NbColors: bpy.props.IntProperty(name='NbColors', default=256, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_DepthMax','m_NbColors',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageDataToHyperTreeGrid )        
TYPENAMES.append('VTKImageDataToHyperTreeGridType' )

#--------------------------------------------------------------
class VTKImageDataToPointSet(Node, PBVTK_Node):

    bl_idname = 'VTKImageDataToPointSetType'
    bl_label  = 'vtkImageDataToPointSet'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageDataToPointSet )        
TYPENAMES.append('VTKImageDataToPointSetType' )

#--------------------------------------------------------------
class VTKImageDataToUniformGrid(Node, PBVTK_Node):

    bl_idname = 'VTKImageDataToUniformGridType'
    bl_label  = 'vtkImageDataToUniformGrid'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Reverse: bpy.props.BoolProperty(name='Reverse', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Reverse','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageDataToUniformGrid )        
TYPENAMES.append('VTKImageDataToUniformGridType' )

#--------------------------------------------------------------
class VTKImageDilateErode3D(Node, PBVTK_Node):

    bl_idname = 'VTKImageDilateErode3DType'
    bl_label  = 'vtkImageDilateErode3D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DilateValue: bpy.props.FloatProperty(name='DilateValue', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ErodeValue: bpy.props.FloatProperty(name='ErodeValue', default=255.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_KernelSize: bpy.props.IntVectorProperty(name='KernelSize', default=[1, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','m_DilateValue','m_ErodeValue','e_SplitMode','m_KernelSize','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageDilateErode3D )        
TYPENAMES.append('VTKImageDilateErode3DType' )

#--------------------------------------------------------------
class VTKImageDivergence(Node, PBVTK_Node):

    bl_idname = 'VTKImageDivergenceType'
    bl_label  = 'vtkImageDivergence'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageDivergence )        
TYPENAMES.append('VTKImageDivergenceType' )

#--------------------------------------------------------------
class VTKImageEuclideanDistance(Node, PBVTK_Node):

    bl_idname = 'VTKImageEuclideanDistanceType'
    bl_label  = 'vtkImageEuclideanDistance'
    e_Algorithm_items=[ (x,x,x) for x in ['SaitoCached', 'Saito']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ConsiderAnisotropy: bpy.props.BoolProperty(name='ConsiderAnisotropy', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Initialize: bpy.props.BoolProperty(name='Initialize', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Dimensionality: bpy.props.IntProperty(name='Dimensionality', default=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumDistance: bpy.props.FloatProperty(name='MaximumDistance', default=2147483647.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_Algorithm: bpy.props.EnumProperty(name='Algorithm', default="Saito", items=e_Algorithm_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ConsiderAnisotropy','m_EnableSMP','m_GlobalDefaultEnableSMP','m_Initialize','m_ObjectName','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','m_MaximumDistance','e_Algorithm','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageEuclideanDistance )        
TYPENAMES.append('VTKImageEuclideanDistanceType' )

#--------------------------------------------------------------
class VTKImageEuclideanToPolar(Node, PBVTK_Node):

    bl_idname = 'VTKImageEuclideanToPolarType'
    bl_label  = 'vtkImageEuclideanToPolar'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ThetaMaximum: bpy.props.FloatProperty(name='ThetaMaximum', default=255.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','m_ThetaMaximum','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageEuclideanToPolar )        
TYPENAMES.append('VTKImageEuclideanToPolarType' )

#--------------------------------------------------------------
class VTKImageExtractComponents(Node, PBVTK_Node):

    bl_idname = 'VTKImageExtractComponentsType'
    bl_label  = 'vtkImageExtractComponents'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageExtractComponents )        
TYPENAMES.append('VTKImageExtractComponentsType' )

#--------------------------------------------------------------
class VTKImageFFT(Node, PBVTK_Node):

    bl_idname = 'VTKImageFFTType'
    bl_label  = 'vtkImageFFT'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Dimensionality: bpy.props.IntProperty(name='Dimensionality', default=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageFFT )        
TYPENAMES.append('VTKImageFFTType' )

#--------------------------------------------------------------
class VTKImageFourierCenter(Node, PBVTK_Node):

    bl_idname = 'VTKImageFourierCenterType'
    bl_label  = 'vtkImageFourierCenter'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Dimensionality: bpy.props.IntProperty(name='Dimensionality', default=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageFourierCenter )        
TYPENAMES.append('VTKImageFourierCenterType' )

#--------------------------------------------------------------
class VTKImageGaussianSmooth(Node, PBVTK_Node):

    bl_idname = 'VTKImageGaussianSmoothType'
    bl_label  = 'vtkImageGaussianSmooth'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Dimensionality: bpy.props.IntProperty(name='Dimensionality', default=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RadiusFactors: bpy.props.FloatVectorProperty(name='RadiusFactors', default=[1.5, 1.5, 1.5], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_StandardDeviations: bpy.props.FloatVectorProperty(name='StandardDeviations', default=[2.0, 2.0, 2.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize','m_RadiusFactors','m_StandardDeviations',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageGaussianSmooth )        
TYPENAMES.append('VTKImageGaussianSmoothType' )

#--------------------------------------------------------------
class VTKImageGradient(Node, PBVTK_Node):

    bl_idname = 'VTKImageGradientType'
    bl_label  = 'vtkImageGradient'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HandleBoundaries: bpy.props.BoolProperty(name='HandleBoundaries', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Dimensionality: bpy.props.IntProperty(name='Dimensionality', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_HandleBoundaries','m_ObjectName','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageGradient )        
TYPENAMES.append('VTKImageGradientType' )

#--------------------------------------------------------------
class VTKImageGradientMagnitude(Node, PBVTK_Node):

    bl_idname = 'VTKImageGradientMagnitudeType'
    bl_label  = 'vtkImageGradientMagnitude'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HandleBoundaries: bpy.props.BoolProperty(name='HandleBoundaries', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Dimensionality: bpy.props.IntProperty(name='Dimensionality', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_HandleBoundaries','m_ObjectName','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageGradientMagnitude )        
TYPENAMES.append('VTKImageGradientMagnitudeType' )

#--------------------------------------------------------------
class VTKImageHSIToRGB(Node, PBVTK_Node):

    bl_idname = 'VTKImageHSIToRGBType'
    bl_label  = 'vtkImageHSIToRGB'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Maximum: bpy.props.FloatProperty(name='Maximum', default=255.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Maximum','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageHSIToRGB )        
TYPENAMES.append('VTKImageHSIToRGBType' )

#--------------------------------------------------------------
class VTKImageHSVToRGB(Node, PBVTK_Node):

    bl_idname = 'VTKImageHSVToRGBType'
    bl_label  = 'vtkImageHSVToRGB'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Maximum: bpy.props.FloatProperty(name='Maximum', default=255.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Maximum','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageHSVToRGB )        
TYPENAMES.append('VTKImageHSVToRGBType' )

#--------------------------------------------------------------
class VTKImageHybridMedian2D(Node, PBVTK_Node):

    bl_idname = 'VTKImageHybridMedian2DType'
    bl_label  = 'vtkImageHybridMedian2D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageHybridMedian2D )        
TYPENAMES.append('VTKImageHybridMedian2DType' )

#--------------------------------------------------------------
class VTKImageIdealHighPass(Node, PBVTK_Node):

    bl_idname = 'VTKImageIdealHighPassType'
    bl_label  = 'vtkImageIdealHighPass'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_XCutOff: bpy.props.FloatProperty(name='XCutOff', default=1e+30, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_YCutOff: bpy.props.FloatProperty(name='YCutOff', default=1e+30, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ZCutOff: bpy.props.FloatProperty(name='ZCutOff', default=1e+30, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CutOff: bpy.props.FloatVectorProperty(name='CutOff', default=[1e+30, 1e+30, 1e+30], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','m_XCutOff','m_YCutOff','m_ZCutOff','e_SplitMode','m_MinimumPieceSize','m_CutOff',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageIdealHighPass )        
TYPENAMES.append('VTKImageIdealHighPassType' )

#--------------------------------------------------------------
class VTKImageIdealLowPass(Node, PBVTK_Node):

    bl_idname = 'VTKImageIdealLowPassType'
    bl_label  = 'vtkImageIdealLowPass'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_XCutOff: bpy.props.FloatProperty(name='XCutOff', default=1e+30, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_YCutOff: bpy.props.FloatProperty(name='YCutOff', default=1e+30, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ZCutOff: bpy.props.FloatProperty(name='ZCutOff', default=1e+30, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CutOff: bpy.props.FloatVectorProperty(name='CutOff', default=[1e+30, 1e+30, 1e+30], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','m_XCutOff','m_YCutOff','m_ZCutOff','e_SplitMode','m_MinimumPieceSize','m_CutOff',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageIdealLowPass )        
TYPENAMES.append('VTKImageIdealLowPassType' )

#--------------------------------------------------------------
class VTKImageIslandRemoval2D(Node, PBVTK_Node):

    bl_idname = 'VTKImageIslandRemoval2DType'
    bl_label  = 'vtkImageIslandRemoval2D'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SquareNeighborhood: bpy.props.BoolProperty(name='SquareNeighborhood', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AreaThreshold: bpy.props.IntProperty(name='AreaThreshold', default=4, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IslandValue: bpy.props.FloatProperty(name='IslandValue', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReplaceValue: bpy.props.FloatProperty(name='ReplaceValue', default=255.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_SquareNeighborhood','m_ObjectName','m_AreaThreshold','m_IslandValue','m_ReplaceValue',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageIslandRemoval2D )        
TYPENAMES.append('VTKImageIslandRemoval2DType' )

#--------------------------------------------------------------
class VTKImageLaplacian(Node, PBVTK_Node):

    bl_idname = 'VTKImageLaplacianType'
    bl_label  = 'vtkImageLaplacian'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Dimensionality: bpy.props.IntProperty(name='Dimensionality', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageLaplacian )        
TYPENAMES.append('VTKImageLaplacianType' )

#--------------------------------------------------------------
class VTKImageLogarithmicScale(Node, PBVTK_Node):

    bl_idname = 'VTKImageLogarithmicScaleType'
    bl_label  = 'vtkImageLogarithmicScale'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Constant: bpy.props.FloatProperty(name='Constant', default=10.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Constant','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageLogarithmicScale )        
TYPENAMES.append('VTKImageLogarithmicScaleType' )

#--------------------------------------------------------------
class VTKImageLuminance(Node, PBVTK_Node):

    bl_idname = 'VTKImageLuminanceType'
    bl_label  = 'vtkImageLuminance'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageLuminance )        
TYPENAMES.append('VTKImageLuminanceType' )

#--------------------------------------------------------------
class VTKImageMagnify(Node, PBVTK_Node):

    bl_idname = 'VTKImageMagnifyType'
    bl_label  = 'vtkImageMagnify'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Interpolate: bpy.props.BoolProperty(name='Interpolate', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MagnificationFactors: bpy.props.IntVectorProperty(name='MagnificationFactors', default=[1, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_Interpolate','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MagnificationFactors','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageMagnify )        
TYPENAMES.append('VTKImageMagnifyType' )

#--------------------------------------------------------------
class VTKImageMagnitude(Node, PBVTK_Node):

    bl_idname = 'VTKImageMagnitudeType'
    bl_label  = 'vtkImageMagnitude'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageMagnitude )        
TYPENAMES.append('VTKImageMagnitudeType' )

#--------------------------------------------------------------
class VTKImageMapToColors(Node, PBVTK_Node):

    bl_idname = 'VTKImageMapToColorsType'
    bl_label  = 'vtkImageMapToColors'
    e_OutputFormat_items=[ (x,x,x) for x in ['Luminance', 'LuminanceAlpha', 'RGB', 'RGBA']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassAlphaToOutput: bpy.props.BoolProperty(name='PassAlphaToOutput', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ActiveComponent: bpy.props.IntProperty(name='ActiveComponent', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_OutputFormat: bpy.props.EnumProperty(name='OutputFormat', default="RGBA", items=e_OutputFormat_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NaNColor: bpy.props.IntVectorProperty(name='NaNColor', default=[0, 0, 0, 0], size=4, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_PassAlphaToOutput','m_ObjectName','m_ActiveComponent','m_DesiredBytesPerPiece','m_NumberOfThreads','e_OutputFormat','e_SplitMode','m_MinimumPieceSize','m_NaNColor',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'LookupTable'], []) 
    
add_class( VTKImageMapToColors )        
TYPENAMES.append('VTKImageMapToColorsType' )

#--------------------------------------------------------------
class VTKImageMapToRGBA(Node, PBVTK_Node):

    bl_idname = 'VTKImageMapToRGBAType'
    bl_label  = 'vtkImageMapToRGBA'
    e_OutputFormat_items=[ (x,x,x) for x in ['Luminance', 'LuminanceAlpha', 'RGB', 'RGBA']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassAlphaToOutput: bpy.props.BoolProperty(name='PassAlphaToOutput', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ActiveComponent: bpy.props.IntProperty(name='ActiveComponent', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_OutputFormat: bpy.props.EnumProperty(name='OutputFormat', default="RGBA", items=e_OutputFormat_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NaNColor: bpy.props.IntVectorProperty(name='NaNColor', default=[0, 0, 0, 0], size=4, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_PassAlphaToOutput','m_ObjectName','m_ActiveComponent','m_DesiredBytesPerPiece','m_NumberOfThreads','e_OutputFormat','e_SplitMode','m_MinimumPieceSize','m_NaNColor',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'LookupTable'], []) 
    
add_class( VTKImageMapToRGBA )        
TYPENAMES.append('VTKImageMapToRGBAType' )

#--------------------------------------------------------------
class VTKImageMapToWindowLevelColors(Node, PBVTK_Node):

    bl_idname = 'VTKImageMapToWindowLevelColorsType'
    bl_label  = 'vtkImageMapToWindowLevelColors'
    e_OutputFormat_items=[ (x,x,x) for x in ['Luminance', 'LuminanceAlpha', 'RGB', 'RGBA']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassAlphaToOutput: bpy.props.BoolProperty(name='PassAlphaToOutput', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ActiveComponent: bpy.props.IntProperty(name='ActiveComponent', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Level: bpy.props.FloatProperty(name='Level', default=127.5, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Window: bpy.props.FloatProperty(name='Window', default=255.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_OutputFormat: bpy.props.EnumProperty(name='OutputFormat', default="RGBA", items=e_OutputFormat_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NaNColor: bpy.props.IntVectorProperty(name='NaNColor', default=[0, 0, 0, 0], size=4, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=14, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_PassAlphaToOutput','m_ObjectName','m_ActiveComponent','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Level','m_Window','e_OutputFormat','e_SplitMode','m_MinimumPieceSize','m_NaNColor',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'LookupTable'], []) 
    
add_class( VTKImageMapToWindowLevelColors )        
TYPENAMES.append('VTKImageMapToWindowLevelColorsType' )

#--------------------------------------------------------------
class VTKImageMarchingCubes(Node, PBVTK_Node):

    bl_idname = 'VTKImageMarchingCubesType'
    bl_label  = 'vtkImageMarchingCubes'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeGradients: bpy.props.BoolProperty(name='ComputeGradients', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeNormals: bpy.props.BoolProperty(name='ComputeNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeScalars: bpy.props.BoolProperty(name='ComputeScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InputMemoryLimit: bpy.props.IntProperty(name='InputMemoryLimit', default=10240, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfContours: bpy.props.IntProperty(name='NumberOfContours', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeGradients','m_ComputeNormals','m_ComputeScalars','m_ObjectName','m_InputMemoryLimit','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageMarchingCubes )        
TYPENAMES.append('VTKImageMarchingCubesType' )

#--------------------------------------------------------------
class VTKImageMaskBits(Node, PBVTK_Node):

    bl_idname = 'VTKImageMaskBitsType'
    bl_label  = 'vtkImageMaskBits'
    e_Operation_items=[ (x,x,x) for x in ['And', 'Or', 'Xor', 'Nand', 'Nor']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_Operation: bpy.props.EnumProperty(name='Operation', default="And", items=e_Operation_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Masks: bpy.props.IntVectorProperty(name='Masks', default=[1000000000, 1000000000, 1000000000, 1000000000], size=4, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','e_Operation','e_SplitMode','m_Masks','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageMaskBits )        
TYPENAMES.append('VTKImageMaskBitsType' )

#--------------------------------------------------------------
class VTKImageMathematics(Node, PBVTK_Node):

    bl_idname = 'VTKImageMathematicsType'
    bl_label  = 'vtkImageMathematics'
    e_Operation_items=[ (x,x,x) for x in ['Add', 'Subtract', 'Multiply', 'Divide', 'Invert', 'Sin', 'Cos', 'Exp', 'Log', 'AbsoluteValue', 'Square', 'SquareRoot', 'Min', 'Max', 'ATAN', 'ATAN2', 'MultiplyByK', 'AddConstant', 'Conjugate', 'ComplexMultiply', 'ReplaceCByK']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DivideByZeroToC: bpy.props.BoolProperty(name='DivideByZeroToC', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ConstantC: bpy.props.FloatProperty(name='ConstantC', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ConstantK: bpy.props.FloatProperty(name='ConstantK', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_Operation: bpy.props.EnumProperty(name='Operation', default="Add", items=e_Operation_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_DivideByZeroToC','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','m_ConstantC','m_ConstantK','e_Operation','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageMathematics )        
TYPENAMES.append('VTKImageMathematicsType' )

#--------------------------------------------------------------
class VTKImageMedian3D(Node, PBVTK_Node):

    bl_idname = 'VTKImageMedian3DType'
    bl_label  = 'vtkImageMedian3D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_KernelSize: bpy.props.IntVectorProperty(name='KernelSize', default=[1, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_KernelSize','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageMedian3D )        
TYPENAMES.append('VTKImageMedian3DType' )

#--------------------------------------------------------------
class VTKImageMirrorPad(Node, PBVTK_Node):

    bl_idname = 'VTKImageMirrorPadType'
    bl_label  = 'vtkImageMirrorPad'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputNumberOfScalarComponents: bpy.props.IntProperty(name='OutputNumberOfScalarComponents', default=-1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','m_OutputNumberOfScalarComponents','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['OutputWholeExtent', 'ContainerAlgorithm'], []) 
    
add_class( VTKImageMirrorPad )        
TYPENAMES.append('VTKImageMirrorPadType' )

#--------------------------------------------------------------
class VTKImageNormalize(Node, PBVTK_Node):

    bl_idname = 'VTKImageNormalizeType'
    bl_label  = 'vtkImageNormalize'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageNormalize )        
TYPENAMES.append('VTKImageNormalizeType' )

#--------------------------------------------------------------
class VTKImageOpenClose3D(Node, PBVTK_Node):

    bl_idname = 'VTKImageOpenClose3DType'
    bl_label  = 'vtkImageOpenClose3D'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CloseValue: bpy.props.FloatProperty(name='CloseValue', default=255.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OpenValue: bpy.props.FloatProperty(name='OpenValue', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_CloseValue','m_OpenValue',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageOpenClose3D )        
TYPENAMES.append('VTKImageOpenClose3DType' )

#--------------------------------------------------------------
class VTKImagePadFilter(Node, PBVTK_Node):

    bl_idname = 'VTKImagePadFilterType'
    bl_label  = 'vtkImagePadFilter'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputNumberOfScalarComponents: bpy.props.IntProperty(name='OutputNumberOfScalarComponents', default=-1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','m_OutputNumberOfScalarComponents','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['OutputWholeExtent', 'ContainerAlgorithm'], []) 
    
add_class( VTKImagePadFilter )        
TYPENAMES.append('VTKImagePadFilterType' )

#--------------------------------------------------------------
class VTKImageQuantizeRGBToIndex(Node, PBVTK_Node):

    bl_idname = 'VTKImageQuantizeRGBToIndexType'
    bl_label  = 'vtkImageQuantizeRGBToIndex'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SortIndexByLuminance: bpy.props.BoolProperty(name='SortIndexByLuminance', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfColors: bpy.props.IntProperty(name='NumberOfColors', default=256, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BuildTreeExecuteTime: bpy.props.FloatProperty(name='BuildTreeExecuteTime', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InitializeExecuteTime: bpy.props.FloatProperty(name='InitializeExecuteTime', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LookupIndexExecuteTime: bpy.props.FloatProperty(name='LookupIndexExecuteTime', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SamplingRate: bpy.props.IntVectorProperty(name='SamplingRate', default=[1, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_SortIndexByLuminance','m_ObjectName','m_NumberOfColors','m_BuildTreeExecuteTime','m_InitializeExecuteTime','m_LookupIndexExecuteTime','m_SamplingRate',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageQuantizeRGBToIndex )        
TYPENAMES.append('VTKImageQuantizeRGBToIndexType' )

#--------------------------------------------------------------
class VTKImageRFFT(Node, PBVTK_Node):

    bl_idname = 'VTKImageRFFTType'
    bl_label  = 'vtkImageRFFT'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Dimensionality: bpy.props.IntProperty(name='Dimensionality', default=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageRFFT )        
TYPENAMES.append('VTKImageRFFTType' )

#--------------------------------------------------------------
class VTKImageRGBToHSI(Node, PBVTK_Node):

    bl_idname = 'VTKImageRGBToHSIType'
    bl_label  = 'vtkImageRGBToHSI'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Maximum: bpy.props.FloatProperty(name='Maximum', default=255.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Maximum','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageRGBToHSI )        
TYPENAMES.append('VTKImageRGBToHSIType' )

#--------------------------------------------------------------
class VTKImageRGBToHSV(Node, PBVTK_Node):

    bl_idname = 'VTKImageRGBToHSVType'
    bl_label  = 'vtkImageRGBToHSV'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Maximum: bpy.props.FloatProperty(name='Maximum', default=255.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Maximum','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageRGBToHSV )        
TYPENAMES.append('VTKImageRGBToHSVType' )

#--------------------------------------------------------------
class VTKImageRGBToXYZ(Node, PBVTK_Node):

    bl_idname = 'VTKImageRGBToXYZType'
    bl_label  = 'vtkImageRGBToXYZ'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageRGBToXYZ )        
TYPENAMES.append('VTKImageRGBToXYZType' )

#--------------------------------------------------------------
class VTKImageRGBToYIQ(Node, PBVTK_Node):

    bl_idname = 'VTKImageRGBToYIQType'
    bl_label  = 'vtkImageRGBToYIQ'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Maximum: bpy.props.FloatProperty(name='Maximum', default=255.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Maximum','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageRGBToYIQ )        
TYPENAMES.append('VTKImageRGBToYIQType' )

#--------------------------------------------------------------
class VTKImageRange3D(Node, PBVTK_Node):

    bl_idname = 'VTKImageRange3DType'
    bl_label  = 'vtkImageRange3D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_KernelSize: bpy.props.IntVectorProperty(name='KernelSize', default=[1, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_KernelSize','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageRange3D )        
TYPENAMES.append('VTKImageRange3DType' )

#--------------------------------------------------------------
class VTKImageResize(Node, PBVTK_Node):

    bl_idname = 'VTKImageResizeType'
    bl_label  = 'vtkImageResize'
    e_ResizeMethod_items=[ (x,x,x) for x in ['OutputDimensions', 'OutputSpacing', 'MagnificationFactors']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Border: bpy.props.BoolProperty(name='Border', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Cropping: bpy.props.BoolProperty(name='Cropping', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Interpolate: bpy.props.BoolProperty(name='Interpolate', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ResizeMethod: bpy.props.EnumProperty(name='ResizeMethod', default="OutputDimensions", items=e_ResizeMethod_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputDimensions: bpy.props.IntVectorProperty(name='OutputDimensions', default=[-1, -1, -1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MagnificationFactors: bpy.props.FloatVectorProperty(name='MagnificationFactors', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputSpacing: bpy.props.FloatVectorProperty(name='OutputSpacing', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Border','m_Cropping','m_EnableSMP','m_GlobalDefaultEnableSMP','m_Interpolate','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','e_ResizeMethod','e_SplitMode','m_MinimumPieceSize','m_OutputDimensions','m_MagnificationFactors','m_OutputSpacing',]
    def m_connections( self ):
        return (['input'], ['output'], ['Interpolator', 'ContainerAlgorithm'], []) 
    
add_class( VTKImageResize )        
TYPENAMES.append('VTKImageResizeType' )

#--------------------------------------------------------------
class VTKImageSeedConnectivity(Node, PBVTK_Node):

    bl_idname = 'VTKImageSeedConnectivityType'
    bl_label  = 'vtkImageSeedConnectivity'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Dimensionality: bpy.props.IntProperty(name='Dimensionality', default=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InputConnectValue: bpy.props.IntProperty(name='InputConnectValue', default=255, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputConnectedValue: bpy.props.IntProperty(name='OutputConnectedValue', default=255, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputUnconnectedValue: bpy.props.IntProperty(name='OutputUnconnectedValue', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_Dimensionality','m_InputConnectValue','m_OutputConnectedValue','m_OutputUnconnectedValue',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageSeedConnectivity )        
TYPENAMES.append('VTKImageSeedConnectivityType' )

#--------------------------------------------------------------
class VTKImageSeparableConvolution(Node, PBVTK_Node):

    bl_idname = 'VTKImageSeparableConvolutionType'
    bl_label  = 'vtkImageSeparableConvolution'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Dimensionality: bpy.props.IntProperty(name='Dimensionality', default=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'XKernel', 'YKernel', 'ZKernel'], []) 
    
add_class( VTKImageSeparableConvolution )        
TYPENAMES.append('VTKImageSeparableConvolutionType' )

#--------------------------------------------------------------
class VTKImageShiftScale(Node, PBVTK_Node):

    bl_idname = 'VTKImageShiftScaleType'
    bl_label  = 'vtkImageShiftScale'
    e_OutputScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Long', 'UnsignedLong', 'Float', 'Double']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ClampOverflow: bpy.props.BoolProperty(name='ClampOverflow', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Scale: bpy.props.FloatProperty(name='Scale', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Shift: bpy.props.FloatProperty(name='Shift', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_OutputScalarType: bpy.props.EnumProperty(name='OutputScalarType', default="Char", items=e_OutputScalarType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ClampOverflow','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Scale','m_Shift','e_OutputScalarType','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageShiftScale )        
TYPENAMES.append('VTKImageShiftScaleType' )

#--------------------------------------------------------------
class VTKImageShrink3D(Node, PBVTK_Node):

    bl_idname = 'VTKImageShrink3DType'
    bl_label  = 'vtkImageShrink3D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Averaging: bpy.props.BoolProperty(name='Averaging', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Maximum: bpy.props.BoolProperty(name='Maximum', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Mean: bpy.props.BoolProperty(name='Mean', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Median: bpy.props.BoolProperty(name='Median', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Minimum: bpy.props.BoolProperty(name='Minimum', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Shift: bpy.props.IntVectorProperty(name='Shift', default=[0, 0, 0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ShrinkFactors: bpy.props.IntVectorProperty(name='ShrinkFactors', default=[1, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Averaging','m_EnableSMP','m_GlobalDefaultEnableSMP','m_Maximum','m_Mean','m_Median','m_Minimum','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize','m_Shift','m_ShrinkFactors',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageShrink3D )        
TYPENAMES.append('VTKImageShrink3DType' )

#--------------------------------------------------------------
class VTKImageSkeleton2D(Node, PBVTK_Node):

    bl_idname = 'VTKImageSkeleton2DType'
    bl_label  = 'vtkImageSkeleton2D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Prune: bpy.props.BoolProperty(name='Prune', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfIterations: bpy.props.IntProperty(name='NumberOfIterations', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_Prune','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfIterations','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageSkeleton2D )        
TYPENAMES.append('VTKImageSkeleton2DType' )

#--------------------------------------------------------------
class VTKImageSlab(Node, PBVTK_Node):

    bl_idname = 'VTKImageSlabType'
    bl_label  = 'vtkImageSlab'
    e_Operation_items=[ (x,x,x) for x in ['Min', 'Max', 'Mean', 'Sum']]
    e_Orientation_items=[ (x,x,x) for x in ['X', 'Y', 'Z']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MultiSliceOutput: bpy.props.BoolProperty(name='MultiSliceOutput', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TrapezoidIntegration: bpy.props.BoolProperty(name='TrapezoidIntegration', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_Operation: bpy.props.EnumProperty(name='Operation', default="Mean", items=e_Operation_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_Orientation: bpy.props.EnumProperty(name='Orientation', default="Z", items=e_Orientation_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SliceRange: bpy.props.IntVectorProperty(name='SliceRange', default=[-1000000000, 1000000000], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_MultiSliceOutput','m_TrapezoidIntegration','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','e_Operation','e_Orientation','e_SplitMode','m_MinimumPieceSize','m_SliceRange',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageSlab )        
TYPENAMES.append('VTKImageSlabType' )

#--------------------------------------------------------------
class VTKImageSobel2D(Node, PBVTK_Node):

    bl_idname = 'VTKImageSobel2DType'
    bl_label  = 'vtkImageSobel2D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageSobel2D )        
TYPENAMES.append('VTKImageSobel2DType' )

#--------------------------------------------------------------
class VTKImageSobel3D(Node, PBVTK_Node):

    bl_idname = 'VTKImageSobel3DType'
    bl_label  = 'vtkImageSobel3D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageSobel3D )        
TYPENAMES.append('VTKImageSobel3DType' )

#--------------------------------------------------------------
class VTKImageSpatialAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKImageSpatialAlgorithmType'
    bl_label  = 'vtkImageSpatialAlgorithm'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageSpatialAlgorithm )        
TYPENAMES.append('VTKImageSpatialAlgorithmType' )

#--------------------------------------------------------------
class VTKImageStencilAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKImageStencilAlgorithmType'
    bl_label  = 'vtkImageStencilAlgorithm'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageStencilAlgorithm )        
TYPENAMES.append('VTKImageStencilAlgorithmType' )

#--------------------------------------------------------------
class VTKImageStencilSource(Node, PBVTK_Node):

    bl_idname = 'VTKImageStencilSourceType'
    bl_label  = 'vtkImageStencilSource'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputWholeExtent: bpy.props.IntVectorProperty(name='OutputWholeExtent', default=[0, -1, 0, -1, 0, -1], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputOrigin: bpy.props.FloatVectorProperty(name='OutputOrigin', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputSpacing: bpy.props.FloatVectorProperty(name='OutputSpacing', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_OutputWholeExtent','m_OutputOrigin','m_OutputSpacing',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageStencilSource )        
TYPENAMES.append('VTKImageStencilSourceType' )

#--------------------------------------------------------------
class VTKImageStencilToImage(Node, PBVTK_Node):

    bl_idname = 'VTKImageStencilToImageType'
    bl_label  = 'vtkImageStencilToImage'
    e_OutputScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Long', 'UnsignedLong', 'Float', 'Double']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InsideValue: bpy.props.FloatProperty(name='InsideValue', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutsideValue: bpy.props.FloatProperty(name='OutsideValue', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_OutputScalarType: bpy.props.EnumProperty(name='OutputScalarType', default="UnsignedChar", items=e_OutputScalarType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_InsideValue','m_OutsideValue','e_OutputScalarType',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageStencilToImage )        
TYPENAMES.append('VTKImageStencilToImageType' )

#--------------------------------------------------------------
class VTKImageThreshold(Node, PBVTK_Node):

    bl_idname = 'VTKImageThresholdType'
    bl_label  = 'vtkImageThreshold'
    e_OutputScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Long', 'UnsignedLong', 'Float', 'Double', 'SignedChar']]
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReplaceIn: bpy.props.BoolProperty(name='ReplaceIn', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReplaceOut: bpy.props.BoolProperty(name='ReplaceOut', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InValue: bpy.props.FloatProperty(name='InValue', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutValue: bpy.props.FloatProperty(name='OutValue', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_OutputScalarType: bpy.props.EnumProperty(name='OutputScalarType', default="Char", items=e_OutputScalarType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ReplaceIn','m_ReplaceOut','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','m_InValue','m_OutValue','e_OutputScalarType','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageThreshold )        
TYPENAMES.append('VTKImageThresholdType' )

#--------------------------------------------------------------
class VTKImageToAMR(Node, PBVTK_Node):

    bl_idname = 'VTKImageToAMRType'
    bl_label  = 'vtkImageToAMR'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumNumberOfBlocks: bpy.props.IntProperty(name='MaximumNumberOfBlocks', default=100, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfLevels: bpy.props.IntProperty(name='NumberOfLevels', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RefinementRatio: bpy.props.IntProperty(name='RefinementRatio', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_MaximumNumberOfBlocks','m_NumberOfLevels','m_RefinementRatio',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageToAMR )        
TYPENAMES.append('VTKImageToAMRType' )

#--------------------------------------------------------------
class VTKImageToImageStencil(Node, PBVTK_Node):

    bl_idname = 'VTKImageToImageStencilType'
    bl_label  = 'vtkImageToImageStencil'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LowerThreshold: bpy.props.FloatProperty(name='LowerThreshold', default=-1e+30, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UpperThreshold: bpy.props.FloatProperty(name='UpperThreshold', default=1e+30, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_LowerThreshold','m_UpperThreshold',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageToImageStencil )        
TYPENAMES.append('VTKImageToImageStencilType' )

#--------------------------------------------------------------
class VTKImageToPolyDataFilter(Node, PBVTK_Node):

    bl_idname = 'VTKImageToPolyDataFilterType'
    bl_label  = 'vtkImageToPolyDataFilter'
    e_ColorMode_items=[ (x,x,x) for x in ['LUT', 'Linear256']]
    e_OutputStyle_items=[ (x,x,x) for x in ['Pixelize', 'Polygonalize', 'RunLength']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Decimation: bpy.props.BoolProperty(name='Decimation', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Smoothing: bpy.props.BoolProperty(name='Smoothing', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Error: bpy.props.IntProperty(name='Error', default=100, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfSmoothingIterations: bpy.props.IntProperty(name='NumberOfSmoothingIterations', default=40, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SubImageSize: bpy.props.IntProperty(name='SubImageSize', default=250, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DecimationError: bpy.props.FloatProperty(name='DecimationError', default=1.5, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ColorMode: bpy.props.EnumProperty(name='ColorMode', default="Linear256", items=e_ColorMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_OutputStyle: bpy.props.EnumProperty(name='OutputStyle', default="Polygonalize", items=e_OutputStyle_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Decimation','m_Smoothing','m_ObjectName','m_Error','m_NumberOfSmoothingIterations','m_SubImageSize','m_DecimationError','e_ColorMode','e_OutputStyle',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'LookupTable'], []) 
    
add_class( VTKImageToPolyDataFilter )        
TYPENAMES.append('VTKImageToPolyDataFilterType' )

#--------------------------------------------------------------
class VTKImageToStructuredGrid(Node, PBVTK_Node):

    bl_idname = 'VTKImageToStructuredGridType'
    bl_label  = 'vtkImageToStructuredGrid'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageToStructuredGrid )        
TYPENAMES.append('VTKImageToStructuredGridType' )

#--------------------------------------------------------------
class VTKImageTranslateExtent(Node, PBVTK_Node):

    bl_idname = 'VTKImageTranslateExtentType'
    bl_label  = 'vtkImageTranslateExtent'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Translation: bpy.props.IntVectorProperty(name='Translation', default=[0, 0, 0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_Translation',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageTranslateExtent )        
TYPENAMES.append('VTKImageTranslateExtentType' )

#--------------------------------------------------------------
class VTKImageVariance3D(Node, PBVTK_Node):

    bl_idname = 'VTKImageVariance3DType'
    bl_label  = 'vtkImageVariance3D'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_KernelSize: bpy.props.IntVectorProperty(name='KernelSize', default=[1, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_KernelSize','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageVariance3D )        
TYPENAMES.append('VTKImageVariance3DType' )

#--------------------------------------------------------------
class VTKImageWeightedSum(Node, PBVTK_Node):

    bl_idname = 'VTKImageWeightedSumType'
    bl_label  = 'vtkImageWeightedSum'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NormalizeByWeight: bpy.props.BoolProperty(name='NormalizeByWeight', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_NormalizeByWeight','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['Weights', 'ContainerAlgorithm'], []) 
    
add_class( VTKImageWeightedSum )        
TYPENAMES.append('VTKImageWeightedSumType' )

#--------------------------------------------------------------
class VTKImageWrapPad(Node, PBVTK_Node):

    bl_idname = 'VTKImageWrapPadType'
    bl_label  = 'vtkImageWrapPad'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputNumberOfScalarComponents: bpy.props.IntProperty(name='OutputNumberOfScalarComponents', default=-1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','m_OutputNumberOfScalarComponents','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['OutputWholeExtent', 'ContainerAlgorithm'], []) 
    
add_class( VTKImageWrapPad )        
TYPENAMES.append('VTKImageWrapPadType' )

#--------------------------------------------------------------
class VTKImageXYZToLAB(Node, PBVTK_Node):

    bl_idname = 'VTKImageXYZToLABType'
    bl_label  = 'vtkImageXYZToLAB'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageXYZToLAB )        
TYPENAMES.append('VTKImageXYZToLABType' )

#--------------------------------------------------------------
class VTKImageYIQToRGB(Node, PBVTK_Node):

    bl_idname = 'VTKImageYIQToRGBType'
    bl_label  = 'vtkImageYIQToRGB'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Maximum: bpy.props.FloatProperty(name='Maximum', default=255.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_ObjectName','m_DesiredBytesPerPiece','m_NumberOfThreads','m_Maximum','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImageYIQToRGB )        
TYPENAMES.append('VTKImageYIQToRGBType' )

#--------------------------------------------------------------
class VTKImplicitModeller(Node, PBVTK_Node):

    bl_idname = 'VTKImplicitModellerType'
    bl_label  = 'vtkImplicitModeller'
    e_OutputScalarType_items=[ (x,x,x) for x in ['Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Long', 'UnsignedLong', 'Float', 'Double']]
    e_ProcessMode_items=[ (x,x,x) for x in ['PerVoxel', 'PerCell']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AdjustBounds: bpy.props.BoolProperty(name='AdjustBounds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Capping: bpy.props.BoolProperty(name='Capping', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScaleToMaximumDistance: bpy.props.BoolProperty(name='ScaleToMaximumDistance', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LocatorMaxLevel: bpy.props.IntProperty(name='LocatorMaxLevel', default=5, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AdjustDistance: bpy.props.FloatProperty(name='AdjustDistance', default=0.0125, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CapValue: bpy.props.FloatProperty(name='CapValue', default=1e+30, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumDistance: bpy.props.FloatProperty(name='MaximumDistance', default=0.1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_OutputScalarType: bpy.props.EnumProperty(name='OutputScalarType', default="Float", items=e_OutputScalarType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ProcessMode: bpy.props.EnumProperty(name='ProcessMode', default="PerCell", items=e_ProcessMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SampleDimensions: bpy.props.IntVectorProperty(name='SampleDimensions', default=[50, 50, 50], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ModelBounds: bpy.props.FloatVectorProperty(name='ModelBounds', default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=14, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AdjustBounds','m_Capping','m_ScaleToMaximumDistance','m_ObjectName','m_LocatorMaxLevel','m_NumberOfThreads','m_AdjustDistance','m_CapValue','m_MaximumDistance','e_OutputScalarType','e_ProcessMode','m_SampleDimensions','m_ModelBounds',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKImplicitModeller )        
TYPENAMES.append('VTKImplicitModellerType' )

#--------------------------------------------------------------
class VTKImplicitTextureCoords(Node, PBVTK_Node):

    bl_idname = 'VTKImplicitTextureCoordsType'
    bl_label  = 'vtkImplicitTextureCoords'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FlipTexture: bpy.props.BoolProperty(name='FlipTexture', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FlipTexture','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'RFunction', 'SFunction', 'TFunction'], []) 
    
add_class( VTKImplicitTextureCoords )        
TYPENAMES.append('VTKImplicitTextureCoordsType' )

#--------------------------------------------------------------
class VTKIntegrateAttributes(Node, PBVTK_Node):

    bl_idname = 'VTKIntegrateAttributesType'
    bl_label  = 'vtkIntegrateAttributes'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DivideAllCellDataByVolume: bpy.props.BoolProperty(name='DivideAllCellDataByVolume', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_DivideAllCellDataByVolume','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['IntegrationStrategy', 'ContainerAlgorithm'], []) 
    
add_class( VTKIntegrateAttributes )        
TYPENAMES.append('VTKIntegrateAttributesType' )

#--------------------------------------------------------------
class VTKInterpolateDataSetAttributes(Node, PBVTK_Node):

    bl_idname = 'VTKInterpolateDataSetAttributesType'
    bl_label  = 'vtkInterpolateDataSetAttributes'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_T: bpy.props.FloatProperty(name='T', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_T',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKInterpolateDataSetAttributes )        
TYPENAMES.append('VTKInterpolateDataSetAttributesType' )

#--------------------------------------------------------------
class VTKKdTreeSelector(Node, PBVTK_Node):

    bl_idname = 'VTKKdTreeSelectorType'
    bl_label  = 'vtkKdTreeSelector'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SingleSelection: bpy.props.BoolProperty(name='SingleSelection', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SelectionFieldName: bpy.props.StringProperty(name='SelectionFieldName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SelectionAttribute: bpy.props.IntProperty(name='SelectionAttribute', default=-1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SingleSelectionThreshold: bpy.props.FloatProperty(name='SingleSelectionThreshold', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_SingleSelection','m_ObjectName','m_SelectionFieldName','m_SelectionAttribute','m_SingleSelectionThreshold',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'KdTree'], []) 
    
add_class( VTKKdTreeSelector )        
TYPENAMES.append('VTKKdTreeSelectorType' )

#--------------------------------------------------------------
class VTKLabelHierarchyAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKLabelHierarchyAlgorithmType'
    bl_label  = 'vtkLabelHierarchyAlgorithm'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKLabelHierarchyAlgorithm )        
TYPENAMES.append('VTKLabelHierarchyAlgorithmType' )

#--------------------------------------------------------------
class VTKLabelSizeCalculator(Node, PBVTK_Node):

    bl_idname = 'VTKLabelSizeCalculatorType'
    bl_label  = 'vtkLabelSizeCalculator'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LabelSizeArrayName: bpy.props.StringProperty(name='LabelSizeArrayName', default="LabelSize", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DPI: bpy.props.IntProperty(name='DPI', default=72, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_LabelSizeArrayName','m_ObjectName','m_DPI',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKLabelSizeCalculator )        
TYPENAMES.append('VTKLabelSizeCalculatorType' )

#--------------------------------------------------------------
class VTKLengthDistribution(Node, PBVTK_Node):

    bl_idname = 'VTKLengthDistributionType'
    bl_label  = 'vtkLengthDistribution'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SortSample: bpy.props.BoolProperty(name='SortSample', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SampleSize: bpy.props.IntProperty(name='SampleSize', default=100000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_SortSample','m_ObjectName','m_SampleSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKLengthDistribution )        
TYPENAMES.append('VTKLengthDistributionType' )

#--------------------------------------------------------------
class VTKLevelIdScalars(Node, PBVTK_Node):

    bl_idname = 'VTKLevelIdScalarsType'
    bl_label  = 'vtkLevelIdScalars'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKLevelIdScalars )        
TYPENAMES.append('VTKLevelIdScalarsType' )

#--------------------------------------------------------------
class VTKLinearCellExtrusionFilter(Node, PBVTK_Node):

    bl_idname = 'VTKLinearCellExtrusionFilterType'
    bl_label  = 'vtkLinearCellExtrusionFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MergeDuplicatePoints: bpy.props.BoolProperty(name='MergeDuplicatePoints', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseUserVector: bpy.props.BoolProperty(name='UseUserVector', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScaleFactor: bpy.props.FloatProperty(name='ScaleFactor', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UserVector: bpy.props.FloatVectorProperty(name='UserVector', default=[0.0, 0.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_MergeDuplicatePoints','m_UseUserVector','m_ObjectName','m_ScaleFactor','m_UserVector',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKLinearCellExtrusionFilter )        
TYPENAMES.append('VTKLinearCellExtrusionFilterType' )

#--------------------------------------------------------------
class VTKLinearExtrusionFilter(Node, PBVTK_Node):

    bl_idname = 'VTKLinearExtrusionFilterType'
    bl_label  = 'vtkLinearExtrusionFilter'
    e_ExtrusionType_items=[ (x,x,x) for x in ['VectorExtrusion', 'NormalExtrusion', 'PointExtrusion']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Capping: bpy.props.BoolProperty(name='Capping', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScaleFactor: bpy.props.FloatProperty(name='ScaleFactor', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ExtrusionType: bpy.props.EnumProperty(name='ExtrusionType', default="NormalExtrusion", items=e_ExtrusionType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ExtrusionPoint: bpy.props.FloatVectorProperty(name='ExtrusionPoint', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Vector: bpy.props.FloatVectorProperty(name='Vector', default=[0.0, 0.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Capping','m_ObjectName','m_ScaleFactor','e_ExtrusionType','m_ExtrusionPoint','m_Vector',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKLinearExtrusionFilter )        
TYPENAMES.append('VTKLinearExtrusionFilterType' )

#--------------------------------------------------------------
class VTKLinearSelector(Node, PBVTK_Node):

    bl_idname = 'VTKLinearSelectorType'
    bl_label  = 'vtkLinearSelector'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IncludeVertices: bpy.props.BoolProperty(name='IncludeVertices', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VertexEliminationTolerance: bpy.props.FloatProperty(name='VertexEliminationTolerance', default=1e-06, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EndPoint: bpy.props.FloatVectorProperty(name='EndPoint', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_StartPoint: bpy.props.FloatVectorProperty(name='StartPoint', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_IncludeVertices','m_ObjectName','m_Tolerance','m_VertexEliminationTolerance','m_EndPoint','m_StartPoint',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'Points'], []) 
    
add_class( VTKLinearSelector )        
TYPENAMES.append('VTKLinearSelectorType' )

#--------------------------------------------------------------
class VTKLinearSubdivisionFilter(Node, PBVTK_Node):

    bl_idname = 'VTKLinearSubdivisionFilterType'
    bl_label  = 'vtkLinearSubdivisionFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CheckForTriangles: bpy.props.BoolProperty(name='CheckForTriangles', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfSubdivisions: bpy.props.IntProperty(name='NumberOfSubdivisions', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CheckForTriangles','m_ObjectName','m_NumberOfSubdivisions',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKLinearSubdivisionFilter )        
TYPENAMES.append('VTKLinearSubdivisionFilterType' )

#--------------------------------------------------------------
class VTKLinearToQuadraticCellsFilter(Node, PBVTK_Node):

    bl_idname = 'VTKLinearToQuadraticCellsFilterType'
    bl_label  = 'vtkLinearToQuadraticCellsFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKLinearToQuadraticCellsFilter )        
TYPENAMES.append('VTKLinearToQuadraticCellsFilterType' )

#--------------------------------------------------------------
class VTKLinkEdgels(Node, PBVTK_Node):

    bl_idname = 'VTKLinkEdgelsType'
    bl_label  = 'vtkLinkEdgels'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GradientThreshold: bpy.props.FloatProperty(name='GradientThreshold', default=0.1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LinkThreshold: bpy.props.FloatProperty(name='LinkThreshold', default=90.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PhiThreshold: bpy.props.FloatProperty(name='PhiThreshold', default=90.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_GradientThreshold','m_LinkThreshold','m_PhiThreshold',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKLinkEdgels )        
TYPENAMES.append('VTKLinkEdgelsType' )

#--------------------------------------------------------------
class VTKLoopSubdivisionFilter(Node, PBVTK_Node):

    bl_idname = 'VTKLoopSubdivisionFilterType'
    bl_label  = 'vtkLoopSubdivisionFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CheckForTriangles: bpy.props.BoolProperty(name='CheckForTriangles', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfSubdivisions: bpy.props.IntProperty(name='NumberOfSubdivisions', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CheckForTriangles','m_ObjectName','m_NumberOfSubdivisions',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKLoopSubdivisionFilter )        
TYPENAMES.append('VTKLoopSubdivisionFilterType' )

#--------------------------------------------------------------
class VTKMapArrayValues(Node, PBVTK_Node):

    bl_idname = 'VTKMapArrayValuesType'
    bl_label  = 'vtkMapArrayValues'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassArray: bpy.props.BoolProperty(name='PassArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InputArrayName: bpy.props.StringProperty(name='InputArrayName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputArrayName: bpy.props.StringProperty(name='OutputArrayName', default="ArrayMap", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldType: bpy.props.IntProperty(name='FieldType', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputArrayType: bpy.props.IntProperty(name='OutputArrayType', default=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FillValue: bpy.props.FloatProperty(name='FillValue', default=-1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_PassArray','m_InputArrayName','m_ObjectName','m_OutputArrayName','m_FieldType','m_OutputArrayType','m_FillValue',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMapArrayValues )        
TYPENAMES.append('VTKMapArrayValuesType' )

#--------------------------------------------------------------
class VTKMarchingContourFilter(Node, PBVTK_Node):

    bl_idname = 'VTKMarchingContourFilterType'
    bl_label  = 'vtkMarchingContourFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeGradients: bpy.props.BoolProperty(name='ComputeGradients', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeNormals: bpy.props.BoolProperty(name='ComputeNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeScalars: bpy.props.BoolProperty(name='ComputeScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfContours: bpy.props.IntProperty(name='NumberOfContours', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeGradients','m_ComputeNormals','m_ComputeScalars','m_ObjectName','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMarchingContourFilter )        
TYPENAMES.append('VTKMarchingContourFilterType' )

#--------------------------------------------------------------
class VTKMarchingCubes(Node, PBVTK_Node):

    bl_idname = 'VTKMarchingCubesType'
    bl_label  = 'vtkMarchingCubes'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeGradients: bpy.props.BoolProperty(name='ComputeGradients', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeNormals: bpy.props.BoolProperty(name='ComputeNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeScalars: bpy.props.BoolProperty(name='ComputeScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfContours: bpy.props.IntProperty(name='NumberOfContours', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeGradients','m_ComputeNormals','m_ComputeScalars','m_ObjectName','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMarchingCubes )        
TYPENAMES.append('VTKMarchingCubesType' )

#--------------------------------------------------------------
class VTKMarchingSquares(Node, PBVTK_Node):

    bl_idname = 'VTKMarchingSquaresType'
    bl_label  = 'vtkMarchingSquares'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfContours: bpy.props.IntProperty(name='NumberOfContours', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMarchingSquares )        
TYPENAMES.append('VTKMarchingSquaresType' )

#--------------------------------------------------------------
class VTKMarkBoundaryFilter(Node, PBVTK_Node):

    bl_idname = 'VTKMarkBoundaryFilterType'
    bl_label  = 'vtkMarkBoundaryFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateBoundaryFaces: bpy.props.BoolProperty(name='GenerateBoundaryFaces', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BoundaryCellsName: bpy.props.StringProperty(name='BoundaryCellsName', default="BoundaryCells", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BoundaryFacesName: bpy.props.StringProperty(name='BoundaryFacesName', default="BoundaryFaces", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BoundaryPointsName: bpy.props.StringProperty(name='BoundaryPointsName', default="BoundaryPoints", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_GenerateBoundaryFaces','m_BoundaryCellsName','m_BoundaryFacesName','m_BoundaryPointsName','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMarkBoundaryFilter )        
TYPENAMES.append('VTKMarkBoundaryFilterType' )

#--------------------------------------------------------------
class VTKMaskFields(Node, PBVTK_Node):

    bl_idname = 'VTKMaskFieldsType'
    bl_label  = 'vtkMaskFields'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMaskFields )        
TYPENAMES.append('VTKMaskFieldsType' )

#--------------------------------------------------------------
class VTKMaskPoints(Node, PBVTK_Node):

    bl_idname = 'VTKMaskPointsType'
    bl_label  = 'vtkMaskPoints'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateVertices: bpy.props.BoolProperty(name='GenerateVertices', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ProportionalMaximumNumberOfPoints: bpy.props.BoolProperty(name='ProportionalMaximumNumberOfPoints', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RandomMode: bpy.props.BoolProperty(name='RandomMode', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SingleVertexPerCell: bpy.props.BoolProperty(name='SingleVertexPerCell', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumNumberOfPoints: bpy.props.IntProperty(name='MaximumNumberOfPoints', default=1000000000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Offset: bpy.props.IntProperty(name='Offset', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OnRatio: bpy.props.IntProperty(name='OnRatio', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RandomModeType: bpy.props.IntProperty(name='RandomModeType', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RandomSeed: bpy.props.IntProperty(name='RandomSeed', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_GenerateVertices','m_ProportionalMaximumNumberOfPoints','m_RandomMode','m_SingleVertexPerCell','m_ObjectName','m_MaximumNumberOfPoints','m_Offset','m_OnRatio','m_RandomModeType','m_RandomSeed',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMaskPoints )        
TYPENAMES.append('VTKMaskPointsType' )

#--------------------------------------------------------------
class VTKMaskPolyData(Node, PBVTK_Node):

    bl_idname = 'VTKMaskPolyDataType'
    bl_label  = 'vtkMaskPolyData'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Offset: bpy.props.IntProperty(name='Offset', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OnRatio: bpy.props.IntProperty(name='OnRatio', default=11, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_Offset','m_OnRatio',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMaskPolyData )        
TYPENAMES.append('VTKMaskPolyDataType' )

#--------------------------------------------------------------
class VTKMatricizeArray(Node, PBVTK_Node):

    bl_idname = 'VTKMatricizeArrayType'
    bl_label  = 'vtkMatricizeArray'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SliceDimension: bpy.props.IntProperty(name='SliceDimension', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_SliceDimension',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMatricizeArray )        
TYPENAMES.append('VTKMatricizeArrayType' )

#--------------------------------------------------------------
class VTKMatrixMathFilter(Node, PBVTK_Node):

    bl_idname = 'VTKMatrixMathFilterType'
    bl_label  = 'vtkMatrixMathFilter'
    e_Operation_items=[ (x,x,x) for x in ['Determinant', 'Eigenvalue', 'Eigenvector', 'Inverse']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_Operation: bpy.props.EnumProperty(name='Operation', default="Determinant", items=e_Operation_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','e_Operation',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMatrixMathFilter )        
TYPENAMES.append('VTKMatrixMathFilterType' )

#--------------------------------------------------------------
class VTKMemoryLimitImageDataStreamer(Node, PBVTK_Node):

    bl_idname = 'VTKMemoryLimitImageDataStreamerType'
    bl_label  = 'vtkMemoryLimitImageDataStreamer'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MemoryLimit: bpy.props.IntProperty(name='MemoryLimit', default=51200, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfStreamDivisions: bpy.props.IntProperty(name='NumberOfStreamDivisions', default=10, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_MemoryLimit','m_NumberOfStreamDivisions',]
    def m_connections( self ):
        return (['input'], ['output'], ['ExtentTranslator', 'ContainerAlgorithm'], []) 
    
add_class( VTKMemoryLimitImageDataStreamer )        
TYPENAMES.append('VTKMemoryLimitImageDataStreamerType' )

#--------------------------------------------------------------
class VTKMergeArrays(Node, PBVTK_Node):

    bl_idname = 'VTKMergeArraysType'
    bl_label  = 'vtkMergeArrays'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMergeArrays )        
TYPENAMES.append('VTKMergeArraysType' )

#--------------------------------------------------------------
class VTKMergeBlocks(Node, PBVTK_Node):

    bl_idname = 'VTKMergeBlocksType'
    bl_label  = 'vtkMergeBlocks'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MergePartitionsOnly: bpy.props.BoolProperty(name='MergePartitionsOnly', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MergePoints: bpy.props.BoolProperty(name='MergePoints', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ToleranceIsAbsolute: bpy.props.BoolProperty(name='ToleranceIsAbsolute', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputDataSetType: bpy.props.IntProperty(name='OutputDataSetType', default=4, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_MergePartitionsOnly','m_MergePoints','m_ToleranceIsAbsolute','m_ObjectName','m_OutputDataSetType','m_Tolerance',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMergeBlocks )        
TYPENAMES.append('VTKMergeBlocksType' )

#--------------------------------------------------------------
class VTKMergeFields(Node, PBVTK_Node):

    bl_idname = 'VTKMergeFieldsType'
    bl_label  = 'vtkMergeFields'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfComponents: bpy.props.IntProperty(name='NumberOfComponents', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_NumberOfComponents',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMergeFields )        
TYPENAMES.append('VTKMergeFieldsType' )

#--------------------------------------------------------------
class VTKMergeTimeFilter(Node, PBVTK_Node):

    bl_idname = 'VTKMergeTimeFilterType'
    bl_label  = 'vtkMergeTimeFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseIntersection: bpy.props.BoolProperty(name='UseIntersection', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseRelativeTolerance: bpy.props.BoolProperty(name='UseRelativeTolerance', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=1e-05, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_UseIntersection','m_UseRelativeTolerance','m_ObjectName','m_Tolerance',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMergeTimeFilter )        
TYPENAMES.append('VTKMergeTimeFilterType' )

#--------------------------------------------------------------
class VTKMergeVectorComponents(Node, PBVTK_Node):

    bl_idname = 'VTKMergeVectorComponentsType'
    bl_label  = 'vtkMergeVectorComponents'
    e_AttributeType_items=[ (x,x,x) for x in ['PointData', 'CellData']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputVectorName: bpy.props.StringProperty(name='OutputVectorName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_XArrayName: bpy.props.StringProperty(name='XArrayName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_YArrayName: bpy.props.StringProperty(name='YArrayName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ZArrayName: bpy.props.StringProperty(name='ZArrayName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_AttributeType: bpy.props.EnumProperty(name='AttributeType', default="PointData", items=e_AttributeType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_OutputVectorName','m_XArrayName','m_YArrayName','m_ZArrayName','e_AttributeType',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMergeVectorComponents )        
TYPENAMES.append('VTKMergeVectorComponentsType' )

#--------------------------------------------------------------
class VTKMeshQuality(Node, PBVTK_Node):

    bl_idname = 'VTKMeshQualityType'
    bl_label  = 'vtkMeshQuality'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LinearApproximation: bpy.props.BoolProperty(name='LinearApproximation', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Ratio: bpy.props.BoolProperty(name='Ratio', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SaveCellQuality: bpy.props.BoolProperty(name='SaveCellQuality', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_LinearApproximation','m_Ratio','m_SaveCellQuality','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['HexQualityMeasure', 'PyramidQualityMeasure', 'QuadQualityMeasure', 'TetQualityMeasure', 'TriangleQualityMeasure', 'WedgeQualityMeasure', 'ContainerAlgorithm'], []) 
    
add_class( VTKMeshQuality )        
TYPENAMES.append('VTKMeshQualityType' )

#--------------------------------------------------------------
class VTKMoleculeAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKMoleculeAlgorithmType'
    bl_label  = 'vtkMoleculeAlgorithm'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMoleculeAlgorithm )        
TYPENAMES.append('VTKMoleculeAlgorithmType' )

#--------------------------------------------------------------
class VTKMoleculeAppend(Node, PBVTK_Node):

    bl_idname = 'VTKMoleculeAppendType'
    bl_label  = 'vtkMoleculeAppend'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MergeCoincidentAtoms: bpy.props.BoolProperty(name='MergeCoincidentAtoms', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_MergeCoincidentAtoms','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMoleculeAppend )        
TYPENAMES.append('VTKMoleculeAppendType' )

#--------------------------------------------------------------
class VTKMoleculeToAtomBallFilter(Node, PBVTK_Node):

    bl_idname = 'VTKMoleculeToAtomBallFilterType'
    bl_label  = 'vtkMoleculeToAtomBallFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RadiusSource: bpy.props.IntProperty(name='RadiusSource', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Resolution: bpy.props.IntProperty(name='Resolution', default=50, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RadiusScale: bpy.props.FloatProperty(name='RadiusScale', default=0.8, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_RadiusSource','m_Resolution','m_RadiusScale',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMoleculeToAtomBallFilter )        
TYPENAMES.append('VTKMoleculeToAtomBallFilterType' )

#--------------------------------------------------------------
class VTKMoleculeToBondStickFilter(Node, PBVTK_Node):

    bl_idname = 'VTKMoleculeToBondStickFilterType'
    bl_label  = 'vtkMoleculeToBondStickFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMoleculeToBondStickFilter )        
TYPENAMES.append('VTKMoleculeToBondStickFilterType' )

#--------------------------------------------------------------
class VTKMoleculeToLinesFilter(Node, PBVTK_Node):

    bl_idname = 'VTKMoleculeToLinesFilterType'
    bl_label  = 'vtkMoleculeToLinesFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMoleculeToLinesFilter )        
TYPENAMES.append('VTKMoleculeToLinesFilterType' )

#--------------------------------------------------------------
class VTKMultiBlockDataGroupFilter(Node, PBVTK_Node):

    bl_idname = 'VTKMultiBlockDataGroupFilterType'
    bl_label  = 'vtkMultiBlockDataGroupFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMultiBlockDataGroupFilter )        
TYPENAMES.append('VTKMultiBlockDataGroupFilterType' )

#--------------------------------------------------------------
class VTKMultiBlockDataSetAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKMultiBlockDataSetAlgorithmType'
    bl_label  = 'vtkMultiBlockDataSetAlgorithm'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMultiBlockDataSetAlgorithm )        
TYPENAMES.append('VTKMultiBlockDataSetAlgorithmType' )

#--------------------------------------------------------------
class VTKMultiBlockMergeFilter(Node, PBVTK_Node):

    bl_idname = 'VTKMultiBlockMergeFilterType'
    bl_label  = 'vtkMultiBlockMergeFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMultiBlockMergeFilter )        
TYPENAMES.append('VTKMultiBlockMergeFilterType' )

#--------------------------------------------------------------
class VTKMultiObjectMassProperties(Node, PBVTK_Node):

    bl_idname = 'VTKMultiObjectMassPropertiesType'
    bl_label  = 'vtkMultiObjectMassProperties'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SkipValidityCheck: bpy.props.BoolProperty(name='SkipValidityCheck', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectIdsArrayName: bpy.props.StringProperty(name='ObjectIdsArrayName', default="ObjectIds", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_SkipValidityCheck','m_ObjectIdsArrayName','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMultiObjectMassProperties )        
TYPENAMES.append('VTKMultiObjectMassPropertiesType' )

#--------------------------------------------------------------
class VTKMultiThreshold(Node, PBVTK_Node):

    bl_idname = 'VTKMultiThresholdType'
    bl_label  = 'vtkMultiThreshold'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKMultiThreshold )        
TYPENAMES.append('VTKMultiThresholdType' )

#--------------------------------------------------------------
class VTKNonOverlappingAMRAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKNonOverlappingAMRAlgorithmType'
    bl_label  = 'vtkNonOverlappingAMRAlgorithm'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKNonOverlappingAMRAlgorithm )        
TYPENAMES.append('VTKNonOverlappingAMRAlgorithmType' )

#--------------------------------------------------------------
class VTKNormalizeMatrixVectors(Node, PBVTK_Node):

    bl_idname = 'VTKNormalizeMatrixVectorsType'
    bl_label  = 'vtkNormalizeMatrixVectors'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VectorDimension: bpy.props.IntProperty(name='VectorDimension', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PValue: bpy.props.FloatProperty(name='PValue', default=2.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_VectorDimension','m_PValue',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKNormalizeMatrixVectors )        
TYPENAMES.append('VTKNormalizeMatrixVectorsType' )

#--------------------------------------------------------------
class VTKOBBDicer(Node, PBVTK_Node):

    bl_idname = 'VTKOBBDicerType'
    bl_label  = 'vtkOBBDicer'
    e_DiceMode_items=[ (x,x,x) for x in ['NumberOfPointsPerPiece', 'SpecifiedNumberOfPieces', 'MemoryLimitPerPiece']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldData: bpy.props.BoolProperty(name='FieldData', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MemoryLimit: bpy.props.IntProperty(name='MemoryLimit', default=51200, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfPieces: bpy.props.IntProperty(name='NumberOfPieces', default=10, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfPointsPerPiece: bpy.props.IntProperty(name='NumberOfPointsPerPiece', default=5000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DiceMode: bpy.props.EnumProperty(name='DiceMode', default="NumberOfPointsPerPiece", items=e_DiceMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FieldData','m_ObjectName','m_MemoryLimit','m_NumberOfPieces','m_NumberOfPointsPerPiece','e_DiceMode',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKOBBDicer )        
TYPENAMES.append('VTKOBBDicerType' )

#--------------------------------------------------------------
class VTKOctreeImageToPointSetFilter(Node, PBVTK_Node):

    bl_idname = 'VTKOctreeImageToPointSetFilterType'
    bl_label  = 'vtkOctreeImageToPointSetFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CreateVerticesCellArray: bpy.props.BoolProperty(name='CreateVerticesCellArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ProcessInputCellArray: bpy.props.BoolProperty(name='ProcessInputCellArray', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CellArrayComponent: bpy.props.IntProperty(name='CellArrayComponent', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CreateVerticesCellArray','m_ProcessInputCellArray','m_ObjectName','m_CellArrayComponent',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKOctreeImageToPointSetFilter )        
TYPENAMES.append('VTKOctreeImageToPointSetFilterType' )

#--------------------------------------------------------------
class VTKOpenGLImageGradient(Node, PBVTK_Node):

    bl_idname = 'VTKOpenGLImageGradientType'
    bl_label  = 'vtkOpenGLImageGradient'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HandleBoundaries: bpy.props.BoolProperty(name='HandleBoundaries', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Dimensionality: bpy.props.IntProperty(name='Dimensionality', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_GlobalDefaultEnableSMP','m_HandleBoundaries','m_ObjectName','m_DesiredBytesPerPiece','m_Dimensionality','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKOpenGLImageGradient )        
TYPENAMES.append('VTKOpenGLImageGradientType' )

#--------------------------------------------------------------
class VTKOrientPolyData(Node, PBVTK_Node):

    bl_idname = 'VTKOrientPolyDataType'
    bl_label  = 'vtkOrientPolyData'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AutoOrientNormals: bpy.props.BoolProperty(name='AutoOrientNormals', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Consistency: bpy.props.BoolProperty(name='Consistency', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FlipNormals: bpy.props.BoolProperty(name='FlipNormals', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NonManifoldTraversal: bpy.props.BoolProperty(name='NonManifoldTraversal', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AutoOrientNormals','m_Consistency','m_FlipNormals','m_NonManifoldTraversal','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKOrientPolyData )        
TYPENAMES.append('VTKOrientPolyDataType' )

#--------------------------------------------------------------
class VTKOutlineCornerFilter(Node, PBVTK_Node):

    bl_idname = 'VTKOutlineCornerFilterType'
    bl_label  = 'vtkOutlineCornerFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CornerFactor: bpy.props.FloatProperty(name='CornerFactor', default=0.2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_CornerFactor',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKOutlineCornerFilter )        
TYPENAMES.append('VTKOutlineCornerFilterType' )

#--------------------------------------------------------------
class VTKOutlineFilter(Node, PBVTK_Node):

    bl_idname = 'VTKOutlineFilterType'
    bl_label  = 'vtkOutlineFilter'
    e_CompositeStyle_items=[ (x,x,x) for x in ['Root', 'Leafs', 'RootAndLeafs', 'SpecifiedIndex']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateFaces: bpy.props.BoolProperty(name='GenerateFaces', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_CompositeStyle: bpy.props.EnumProperty(name='CompositeStyle', default="RootAndLeafs", items=e_CompositeStyle_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_GenerateFaces','m_ObjectName','e_CompositeStyle',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKOutlineFilter )        
TYPENAMES.append('VTKOutlineFilterType' )

#--------------------------------------------------------------
class VTKOverlappingAMRAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKOverlappingAMRAlgorithmType'
    bl_label  = 'vtkOverlappingAMRAlgorithm'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKOverlappingAMRAlgorithm )        
TYPENAMES.append('VTKOverlappingAMRAlgorithmType' )

#--------------------------------------------------------------
class VTKOverlappingAMRLevelIdScalars(Node, PBVTK_Node):

    bl_idname = 'VTKOverlappingAMRLevelIdScalarsType'
    bl_label  = 'vtkOverlappingAMRLevelIdScalars'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKOverlappingAMRLevelIdScalars )        
TYPENAMES.append('VTKOverlappingAMRLevelIdScalarsType' )

#--------------------------------------------------------------
class VTKOverlappingCellsDetector(Node, PBVTK_Node):

    bl_idname = 'VTKOverlappingCellsDetectorType'
    bl_label  = 'vtkOverlappingCellsDetector'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfOverlapsPerCellArrayName: bpy.props.StringProperty(name='NumberOfOverlapsPerCellArrayName', default="NumberOfOverlapsPerCell", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_NumberOfOverlapsPerCellArrayName','m_ObjectName','m_Tolerance',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKOverlappingCellsDetector )        
TYPENAMES.append('VTKOverlappingCellsDetectorType' )

#--------------------------------------------------------------
class VTKPAxisAlignedReflectionFilter(Node, PBVTK_Node):

    bl_idname = 'VTKPAxisAlignedReflectionFilterType'
    bl_label  = 'vtkPAxisAlignedReflectionFilter'
    e_PlaneMode_items=[ (x,x,x) for x in ['Plane', 'XMin', 'YMin', 'ZMin', 'XMax', 'YMax', 'ZMax']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CopyInput: bpy.props.BoolProperty(name='CopyInput', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReflectAllInputArrays: bpy.props.BoolProperty(name='ReflectAllInputArrays', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_PlaneMode: bpy.props.EnumProperty(name='PlaneMode', default="Plane", items=e_PlaneMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CopyInput','m_ReflectAllInputArrays','m_ObjectName','e_PlaneMode',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'ReflectionPlane'], []) 
    
add_class( VTKPAxisAlignedReflectionFilter )        
TYPENAMES.append('VTKPAxisAlignedReflectionFilterType' )

#--------------------------------------------------------------
class VTKPCAAnalysisFilter(Node, PBVTK_Node):

    bl_idname = 'VTKPCAAnalysisFilterType'
    bl_label  = 'vtkPCAAnalysisFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPCAAnalysisFilter )        
TYPENAMES.append('VTKPCAAnalysisFilterType' )

#--------------------------------------------------------------
class VTKPCACurvatureEstimation(Node, PBVTK_Node):

    bl_idname = 'VTKPCACurvatureEstimationType'
    bl_label  = 'vtkPCACurvatureEstimation'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SampleSize: bpy.props.IntProperty(name='SampleSize', default=25, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_SampleSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPCACurvatureEstimation )        
TYPENAMES.append('VTKPCACurvatureEstimationType' )

#--------------------------------------------------------------
class VTKPCANormalEstimation(Node, PBVTK_Node):

    bl_idname = 'VTKPCANormalEstimationType'
    bl_label  = 'vtkPCANormalEstimation'
    e_NormalOrientation_items=[ (x,x,x) for x in ['AsComputed', 'Point', 'GraphTraversal']]
    e_SearchMode_items=[ (x,x,x) for x in ['KNN', 'Radius']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FlipNormals: bpy.props.BoolProperty(name='FlipNormals', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CellGenerationMode: bpy.props.IntProperty(name='CellGenerationMode', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SampleSize: bpy.props.IntProperty(name='SampleSize', default=25, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Radius: bpy.props.FloatProperty(name='Radius', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_NormalOrientation: bpy.props.EnumProperty(name='NormalOrientation', default="Point", items=e_NormalOrientation_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SearchMode: bpy.props.EnumProperty(name='SearchMode', default="KNN", items=e_SearchMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OrientationPoint: bpy.props.FloatVectorProperty(name='OrientationPoint', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FlipNormals','m_ObjectName','m_CellGenerationMode','m_SampleSize','m_Radius','e_NormalOrientation','e_SearchMode','m_OrientationPoint',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPCANormalEstimation )        
TYPENAMES.append('VTKPCANormalEstimationType' )

#--------------------------------------------------------------
class VTKPComputeQuantiles(Node, PBVTK_Node):

    bl_idname = 'VTKPComputeQuantilesType'
    bl_label  = 'vtkPComputeQuantiles'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfIntervals: bpy.props.IntProperty(name='NumberOfIntervals', default=4, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_NumberOfIntervals',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPComputeQuantiles )        
TYPENAMES.append('VTKPComputeQuantilesType' )

#--------------------------------------------------------------
class VTKPComputeQuartiles(Node, PBVTK_Node):

    bl_idname = 'VTKPComputeQuartilesType'
    bl_label  = 'vtkPComputeQuartiles'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfIntervals: bpy.props.IntProperty(name='NumberOfIntervals', default=4, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_NumberOfIntervals',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPComputeQuartiles )        
TYPENAMES.append('VTKPComputeQuartilesType' )

#--------------------------------------------------------------
class VTKPConvertToMultiBlockDataSet(Node, PBVTK_Node):

    bl_idname = 'VTKPConvertToMultiBlockDataSetType'
    bl_label  = 'vtkPConvertToMultiBlockDataSet'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPConvertToMultiBlockDataSet )        
TYPENAMES.append('VTKPConvertToMultiBlockDataSetType' )

#--------------------------------------------------------------
class VTKPExtractDataArraysOverTime(Node, PBVTK_Node):

    bl_idname = 'VTKPExtractDataArraysOverTimeType'
    bl_label  = 'vtkPExtractDataArraysOverTime'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReportStatisticsOnly: bpy.props.BoolProperty(name='ReportStatisticsOnly', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseGlobalIDs: bpy.props.BoolProperty(name='UseGlobalIDs', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldAssociation: bpy.props.IntProperty(name='FieldAssociation', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReportStatisticsOnly','m_UseGlobalIDs','m_ObjectName','m_FieldAssociation',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPExtractDataArraysOverTime )        
TYPENAMES.append('VTKPExtractDataArraysOverTimeType' )

#--------------------------------------------------------------
class VTKPExtractExodusGlobalTemporalVariables(Node, PBVTK_Node):

    bl_idname = 'VTKPExtractExodusGlobalTemporalVariablesType'
    bl_label  = 'vtkPExtractExodusGlobalTemporalVariables'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AutoDetectGlobalTemporalDataArrays: bpy.props.BoolProperty(name='AutoDetectGlobalTemporalDataArrays', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AutoDetectGlobalTemporalDataArrays','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPExtractExodusGlobalTemporalVariables )        
TYPENAMES.append('VTKPExtractExodusGlobalTemporalVariablesType' )

#--------------------------------------------------------------
class VTKPLinearExtrusionFilter(Node, PBVTK_Node):

    bl_idname = 'VTKPLinearExtrusionFilterType'
    bl_label  = 'vtkPLinearExtrusionFilter'
    e_ExtrusionType_items=[ (x,x,x) for x in ['VectorExtrusion', 'NormalExtrusion', 'PointExtrusion']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Capping: bpy.props.BoolProperty(name='Capping', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PieceInvariant: bpy.props.BoolProperty(name='PieceInvariant', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScaleFactor: bpy.props.FloatProperty(name='ScaleFactor', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ExtrusionType: bpy.props.EnumProperty(name='ExtrusionType', default="NormalExtrusion", items=e_ExtrusionType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ExtrusionPoint: bpy.props.FloatVectorProperty(name='ExtrusionPoint', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Vector: bpy.props.FloatVectorProperty(name='Vector', default=[0.0, 0.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Capping','m_PieceInvariant','m_ObjectName','m_ScaleFactor','e_ExtrusionType','m_ExtrusionPoint','m_Vector',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPLinearExtrusionFilter )        
TYPENAMES.append('VTKPLinearExtrusionFilterType' )

#--------------------------------------------------------------
class VTKPMaskPoints(Node, PBVTK_Node):

    bl_idname = 'VTKPMaskPointsType'
    bl_label  = 'vtkPMaskPoints'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateVertices: bpy.props.BoolProperty(name='GenerateVertices', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ProportionalMaximumNumberOfPoints: bpy.props.BoolProperty(name='ProportionalMaximumNumberOfPoints', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RandomMode: bpy.props.BoolProperty(name='RandomMode', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SingleVertexPerCell: bpy.props.BoolProperty(name='SingleVertexPerCell', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumNumberOfPoints: bpy.props.IntProperty(name='MaximumNumberOfPoints', default=1000000000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Offset: bpy.props.IntProperty(name='Offset', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OnRatio: bpy.props.IntProperty(name='OnRatio', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RandomModeType: bpy.props.IntProperty(name='RandomModeType', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RandomSeed: bpy.props.IntProperty(name='RandomSeed', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_GenerateVertices','m_ProportionalMaximumNumberOfPoints','m_RandomMode','m_SingleVertexPerCell','m_ObjectName','m_MaximumNumberOfPoints','m_Offset','m_OnRatio','m_RandomModeType','m_RandomSeed',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPMaskPoints )        
TYPENAMES.append('VTKPMaskPointsType' )

#--------------------------------------------------------------
class VTKPMergeArrays(Node, PBVTK_Node):

    bl_idname = 'VTKPMergeArraysType'
    bl_label  = 'vtkPMergeArrays'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPMergeArrays )        
TYPENAMES.append('VTKPMergeArraysType' )

#--------------------------------------------------------------
class VTKPOutlineCornerFilter(Node, PBVTK_Node):

    bl_idname = 'VTKPOutlineCornerFilterType'
    bl_label  = 'vtkPOutlineCornerFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CornerFactor: bpy.props.FloatProperty(name='CornerFactor', default=0.2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_CornerFactor',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPOutlineCornerFilter )        
TYPENAMES.append('VTKPOutlineCornerFilterType' )

#--------------------------------------------------------------
class VTKPOutlineFilter(Node, PBVTK_Node):

    bl_idname = 'VTKPOutlineFilterType'
    bl_label  = 'vtkPOutlineFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPOutlineFilter )        
TYPENAMES.append('VTKPOutlineFilterType' )

#--------------------------------------------------------------
class VTKPPolyDataNormals(Node, PBVTK_Node):

    bl_idname = 'VTKPPolyDataNormalsType'
    bl_label  = 'vtkPPolyDataNormals'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AutoOrientNormals: bpy.props.BoolProperty(name='AutoOrientNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeCellNormals: bpy.props.BoolProperty(name='ComputeCellNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputePointNormals: bpy.props.BoolProperty(name='ComputePointNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Consistency: bpy.props.BoolProperty(name='Consistency', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FlipNormals: bpy.props.BoolProperty(name='FlipNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NonManifoldTraversal: bpy.props.BoolProperty(name='NonManifoldTraversal', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PieceInvariant: bpy.props.BoolProperty(name='PieceInvariant', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Splitting: bpy.props.BoolProperty(name='Splitting', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FeatureAngle: bpy.props.FloatProperty(name='FeatureAngle', default=30.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AutoOrientNormals','m_ComputeCellNormals','m_ComputePointNormals','m_Consistency','m_FlipNormals','m_NonManifoldTraversal','m_PieceInvariant','m_Splitting','m_ObjectName','m_FeatureAngle',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPPolyDataNormals )        
TYPENAMES.append('VTKPPolyDataNormalsType' )

#--------------------------------------------------------------
class VTKPProjectSphereFilter(Node, PBVTK_Node):

    bl_idname = 'VTKPProjectSphereFilterType'
    bl_label  = 'vtkPProjectSphereFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_KeepPolePoints: bpy.props.BoolProperty(name='KeepPolePoints', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TranslateZ: bpy.props.BoolProperty(name='TranslateZ', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_KeepPolePoints','m_TranslateZ','m_ObjectName','m_Center',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPProjectSphereFilter )        
TYPENAMES.append('VTKPProjectSphereFilterType' )

#--------------------------------------------------------------
class VTKPReflectionFilter(Node, PBVTK_Node):

    bl_idname = 'VTKPReflectionFilterType'
    bl_label  = 'vtkPReflectionFilter'
    e_Plane_items=[ (x,x,x) for x in ['XMin', 'YMin', 'ZMin', 'XMax', 'YMax', 'ZMax', 'X', 'Y', 'Z']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CopyInput: bpy.props.BoolProperty(name='CopyInput', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FlipAllInputArrays: bpy.props.BoolProperty(name='FlipAllInputArrays', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Center: bpy.props.FloatProperty(name='Center', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_Plane: bpy.props.EnumProperty(name='Plane', default="XMin", items=e_Plane_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CopyInput','m_FlipAllInputArrays','m_ObjectName','m_Center','e_Plane',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPReflectionFilter )        
TYPENAMES.append('VTKPReflectionFilterType' )

#--------------------------------------------------------------
class VTKPResampleFilter(Node, PBVTK_Node):

    bl_idname = 'VTKPResampleFilterType'
    bl_label  = 'vtkPResampleFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseInputBounds: bpy.props.BoolProperty(name='UseInputBounds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SamplingDimension: bpy.props.IntVectorProperty(name='SamplingDimension', default=[10, 10, 10], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_UseInputBounds','m_ObjectName','m_SamplingDimension',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPResampleFilter )        
TYPENAMES.append('VTKPResampleFilterType' )

#--------------------------------------------------------------
class VTKPResampleToImage(Node, PBVTK_Node):

    bl_idname = 'VTKPResampleToImageType'
    bl_label  = 'vtkPResampleToImage'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseInputBounds: bpy.props.BoolProperty(name='UseInputBounds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SamplingDimensions: bpy.props.IntVectorProperty(name='SamplingDimensions', default=[10, 10, 10], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_UseInputBounds','m_ObjectName','m_SamplingDimensions',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPResampleToImage )        
TYPENAMES.append('VTKPResampleToImageType' )

#--------------------------------------------------------------
class VTKPTextureMapToSphere(Node, PBVTK_Node):

    bl_idname = 'VTKPTextureMapToSphereType'
    bl_label  = 'vtkPTextureMapToSphere'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AutomaticSphereGeneration: bpy.props.BoolProperty(name='AutomaticSphereGeneration', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PreventSeam: bpy.props.BoolProperty(name='PreventSeam', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AutomaticSphereGeneration','m_PreventSeam','m_ObjectName','m_Center',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPTextureMapToSphere )        
TYPENAMES.append('VTKPTextureMapToSphereType' )

#--------------------------------------------------------------
class VTKPYoungsMaterialInterface(Node, PBVTK_Node):

    bl_idname = 'VTKPYoungsMaterialInterfaceType'
    bl_label  = 'vtkPYoungsMaterialInterface'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AxisSymetric: bpy.props.BoolProperty(name='AxisSymetric', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FillMaterial: bpy.props.BoolProperty(name='FillMaterial', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InverseNormal: bpy.props.BoolProperty(name='InverseNormal', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OnionPeel: bpy.props.BoolProperty(name='OnionPeel', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReverseMaterialOrder: bpy.props.BoolProperty(name='ReverseMaterialOrder', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseAllBlocks: bpy.props.BoolProperty(name='UseAllBlocks', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseFractionAsDistance: bpy.props.BoolProperty(name='UseFractionAsDistance', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfMaterials: bpy.props.IntProperty(name='NumberOfMaterials', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VolumeFractionRange: bpy.props.FloatVectorProperty(name='VolumeFractionRange', default=[0.01, 0.99], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AxisSymetric','m_FillMaterial','m_InverseNormal','m_OnionPeel','m_ReverseMaterialOrder','m_UseAllBlocks','m_UseFractionAsDistance','m_ObjectName','m_NumberOfMaterials','m_VolumeFractionRange',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPYoungsMaterialInterface )        
TYPENAMES.append('VTKPYoungsMaterialInterfaceType' )

#--------------------------------------------------------------
class VTKPackLabels(Node, PBVTK_Node):

    bl_idname = 'VTKPackLabelsType'
    bl_label  = 'vtkPackLabels'
    e_OutputScalarType_items=[ (x,x,x) for x in ['Default', 'UnsignedChar', 'UnsignedShort', 'UnsignedInt', 'UnsignedLong']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassCellData: bpy.props.BoolProperty(name='PassCellData', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassFieldData: bpy.props.BoolProperty(name='PassFieldData', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassPointData: bpy.props.BoolProperty(name='PassPointData', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BackgroundValue: bpy.props.IntProperty(name='BackgroundValue', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SortBy: bpy.props.IntProperty(name='SortBy', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_OutputScalarType: bpy.props.EnumProperty(name='OutputScalarType', default="Default", items=e_OutputScalarType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_PassCellData','m_PassFieldData','m_PassPointData','m_ObjectName','m_BackgroundValue','m_SortBy','e_OutputScalarType',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPackLabels )        
TYPENAMES.append('VTKPackLabelsType' )

#--------------------------------------------------------------
class VTKParallelVectors(Node, PBVTK_Node):

    bl_idname = 'VTKParallelVectorsType'
    bl_label  = 'vtkParallelVectors'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FirstVectorFieldName: bpy.props.StringProperty(name='FirstVectorFieldName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SecondVectorFieldName: bpy.props.StringProperty(name='SecondVectorFieldName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FirstVectorFieldName','m_ObjectName','m_SecondVectorFieldName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKParallelVectors )        
TYPENAMES.append('VTKParallelVectorsType' )

#--------------------------------------------------------------
class VTKPartitionBalancer(Node, PBVTK_Node):

    bl_idname = 'VTKPartitionBalancerType'
    bl_label  = 'vtkPartitionBalancer'
    e_Mode_items=[ (x,x,x) for x in ['Expand', 'Squash']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_Mode: bpy.props.EnumProperty(name='Mode', default="Squash", items=e_Mode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','e_Mode',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPartitionBalancer )        
TYPENAMES.append('VTKPartitionBalancerType' )

#--------------------------------------------------------------
class VTKPassArrays(Node, PBVTK_Node):

    bl_idname = 'VTKPassArraysType'
    bl_label  = 'vtkPassArrays'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RemoveArrays: bpy.props.BoolProperty(name='RemoveArrays', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseFieldTypes: bpy.props.BoolProperty(name='UseFieldTypes', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_RemoveArrays','m_UseFieldTypes','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPassArrays )        
TYPENAMES.append('VTKPassArraysType' )

#--------------------------------------------------------------
class VTKPassInputTypeAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKPassInputTypeAlgorithmType'
    bl_label  = 'vtkPassInputTypeAlgorithm'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPassInputTypeAlgorithm )        
TYPENAMES.append('VTKPassInputTypeAlgorithmType' )

#--------------------------------------------------------------
class VTKPassSelectedArrays(Node, PBVTK_Node):

    bl_idname = 'VTKPassSelectedArraysType'
    bl_label  = 'vtkPassSelectedArrays'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Enabled: bpy.props.BoolProperty(name='Enabled', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Enabled','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPassSelectedArrays )        
TYPENAMES.append('VTKPassSelectedArraysType' )

#--------------------------------------------------------------
class VTKPassThrough(Node, PBVTK_Node):

    bl_idname = 'VTKPassThroughType'
    bl_label  = 'vtkPassThrough'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AllowNullInput: bpy.props.BoolProperty(name='AllowNullInput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DeepCopyInput: bpy.props.BoolProperty(name='DeepCopyInput', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AllowNullInput','m_DeepCopyInput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPassThrough )        
TYPENAMES.append('VTKPassThroughType' )

#--------------------------------------------------------------
class VTKPieceRequestFilter(Node, PBVTK_Node):

    bl_idname = 'VTKPieceRequestFilterType'
    bl_label  = 'vtkPieceRequestFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfPieces: bpy.props.IntProperty(name='NumberOfPieces', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Piece: bpy.props.IntProperty(name='Piece', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_NumberOfPieces','m_Piece',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPieceRequestFilter )        
TYPENAMES.append('VTKPieceRequestFilterType' )

#--------------------------------------------------------------
class VTKPieceScalars(Node, PBVTK_Node):

    bl_idname = 'VTKPieceScalarsType'
    bl_label  = 'vtkPieceScalars'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RandomMode: bpy.props.BoolProperty(name='RandomMode', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_RandomMode','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPieceScalars )        
TYPENAMES.append('VTKPieceScalarsType' )

#--------------------------------------------------------------
class VTKPiecewiseFunctionAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKPiecewiseFunctionAlgorithmType'
    bl_label  = 'vtkPiecewiseFunctionAlgorithm'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPiecewiseFunctionAlgorithm )        
TYPENAMES.append('VTKPiecewiseFunctionAlgorithmType' )

#--------------------------------------------------------------
class VTKPiecewiseFunctionShiftScale(Node, PBVTK_Node):

    bl_idname = 'VTKPiecewiseFunctionShiftScaleType'
    bl_label  = 'vtkPiecewiseFunctionShiftScale'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PositionScale: bpy.props.FloatProperty(name='PositionScale', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PositionShift: bpy.props.FloatProperty(name='PositionShift', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ValueScale: bpy.props.FloatProperty(name='ValueScale', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ValueShift: bpy.props.FloatProperty(name='ValueShift', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_PositionScale','m_PositionShift','m_ValueScale','m_ValueShift',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPiecewiseFunctionShiftScale )        
TYPENAMES.append('VTKPiecewiseFunctionShiftScaleType' )

#--------------------------------------------------------------
class VTKPlaneCutter(Node, PBVTK_Node):

    bl_idname = 'VTKPlaneCutterType'
    bl_label  = 'vtkPlaneCutter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BuildHierarchy: bpy.props.BoolProperty(name='BuildHierarchy', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BuildTree: bpy.props.BoolProperty(name='BuildTree', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeNormals: bpy.props.BoolProperty(name='ComputeNormals', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GeneratePolygons: bpy.props.BoolProperty(name='GeneratePolygons', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InterpolateAttributes: bpy.props.BoolProperty(name='InterpolateAttributes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MergePoints: bpy.props.BoolProperty(name='MergePoints', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_BuildHierarchy','m_BuildTree','m_ComputeNormals','m_GeneratePolygons','m_InterpolateAttributes','m_MergePoints','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['Plane', 'ContainerAlgorithm'], []) 
    
add_class( VTKPlaneCutter )        
TYPENAMES.append('VTKPlaneCutterType' )

#--------------------------------------------------------------
class VTKPointConnectivityFilter(Node, PBVTK_Node):

    bl_idname = 'VTKPointConnectivityFilterType'
    bl_label  = 'vtkPointConnectivityFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPointConnectivityFilter )        
TYPENAMES.append('VTKPointConnectivityFilterType' )

#--------------------------------------------------------------
class VTKPointDataToCellData(Node, PBVTK_Node):

    bl_idname = 'VTKPointDataToCellDataType'
    bl_label  = 'vtkPointDataToCellData'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CategoricalData: bpy.props.BoolProperty(name='CategoricalData', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassPointData: bpy.props.BoolProperty(name='PassPointData', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ProcessAllArrays: bpy.props.BoolProperty(name='ProcessAllArrays', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CategoricalData','m_PassPointData','m_ProcessAllArrays','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPointDataToCellData )        
TYPENAMES.append('VTKPointDataToCellDataType' )

#--------------------------------------------------------------
class VTKPointDensityFilter(Node, PBVTK_Node):

    bl_idname = 'VTKPointDensityFilterType'
    bl_label  = 'vtkPointDensityFilter'
    e_DensityEstimate_items=[ (x,x,x) for x in ['FixedRadius', 'RelativeRadius']]
    e_DensityForm_items=[ (x,x,x) for x in ['VolumeNormalized', 'NumberOfPoints']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeGradient: bpy.props.BoolProperty(name='ComputeGradient', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarWeighting: bpy.props.BoolProperty(name='ScalarWeighting', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AdjustDistance: bpy.props.FloatProperty(name='AdjustDistance', default=0.1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Radius: bpy.props.FloatProperty(name='Radius', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RelativeRadius: bpy.props.FloatProperty(name='RelativeRadius', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DensityEstimate: bpy.props.EnumProperty(name='DensityEstimate', default="RelativeRadius", items=e_DensityEstimate_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_DensityForm: bpy.props.EnumProperty(name='DensityForm', default="NumberOfPoints", items=e_DensityForm_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SampleDimensions: bpy.props.IntVectorProperty(name='SampleDimensions', default=[100, 100, 100], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ModelBounds: bpy.props.FloatVectorProperty(name='ModelBounds', default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeGradient','m_ScalarWeighting','m_ObjectName','m_AdjustDistance','m_Radius','m_RelativeRadius','e_DensityEstimate','e_DensityForm','m_SampleDimensions','m_ModelBounds',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPointDensityFilter )        
TYPENAMES.append('VTKPointDensityFilterType' )

#--------------------------------------------------------------
class VTKPointOccupancyFilter(Node, PBVTK_Node):

    bl_idname = 'VTKPointOccupancyFilterType'
    bl_label  = 'vtkPointOccupancyFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EmptyValue: bpy.props.IntProperty(name='EmptyValue', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OccupiedValue: bpy.props.IntProperty(name='OccupiedValue', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SampleDimensions: bpy.props.IntVectorProperty(name='SampleDimensions', default=[100, 100, 100], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ModelBounds: bpy.props.FloatVectorProperty(name='ModelBounds', default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_EmptyValue','m_OccupiedValue','m_SampleDimensions','m_ModelBounds',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPointOccupancyFilter )        
TYPENAMES.append('VTKPointOccupancyFilterType' )

#--------------------------------------------------------------
class VTKPointSetAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKPointSetAlgorithmType'
    bl_label  = 'vtkPointSetAlgorithm'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPointSetAlgorithm )        
TYPENAMES.append('VTKPointSetAlgorithmType' )

#--------------------------------------------------------------
class VTKPointSetStreamer(Node, PBVTK_Node):

    bl_idname = 'VTKPointSetStreamerType'
    bl_label  = 'vtkPointSetStreamer'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CreateVerticesCellArray: bpy.props.BoolProperty(name='CreateVerticesCellArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BucketId: bpy.props.IntProperty(name='BucketId', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfPointsPerBucket: bpy.props.IntProperty(name='NumberOfPointsPerBucket', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CreateVerticesCellArray','m_ObjectName','m_BucketId','m_NumberOfPointsPerBucket',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPointSetStreamer )        
TYPENAMES.append('VTKPointSetStreamerType' )

#--------------------------------------------------------------
class VTKPointSetToLabelHierarchy(Node, PBVTK_Node):

    bl_idname = 'VTKPointSetToLabelHierarchyType'
    bl_label  = 'vtkPointSetToLabelHierarchy'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BoundedSizeArrayName: bpy.props.StringProperty(name='BoundedSizeArrayName', default="BoundedSize", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IconIndexArrayName: bpy.props.StringProperty(name='IconIndexArrayName', default="IconIndex", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LabelArrayName: bpy.props.StringProperty(name='LabelArrayName', default="LabelText", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OrientationArrayName: bpy.props.StringProperty(name='OrientationArrayName', default="Orientation", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PriorityArrayName: bpy.props.StringProperty(name='PriorityArrayName', default="Priority", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SizeArrayName: bpy.props.StringProperty(name='SizeArrayName', default="LabelSize", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumDepth: bpy.props.IntProperty(name='MaximumDepth', default=5, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TargetLabelCount: bpy.props.IntProperty(name='TargetLabelCount', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_BoundedSizeArrayName','m_IconIndexArrayName','m_LabelArrayName','m_ObjectName','m_OrientationArrayName','m_PriorityArrayName','m_SizeArrayName','m_MaximumDepth','m_TargetLabelCount',]
    def m_connections( self ):
        return (['input'], ['output'], ['TextProperty', 'ContainerAlgorithm'], []) 
    
add_class( VTKPointSetToLabelHierarchy )        
TYPENAMES.append('VTKPointSetToLabelHierarchyType' )

#--------------------------------------------------------------
class VTKPointSetToMoleculeFilter(Node, PBVTK_Node):

    bl_idname = 'VTKPointSetToMoleculeFilterType'
    bl_label  = 'vtkPointSetToMoleculeFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ConvertLinesIntoBonds: bpy.props.BoolProperty(name='ConvertLinesIntoBonds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ConvertLinesIntoBonds','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPointSetToMoleculeFilter )        
TYPENAMES.append('VTKPointSetToMoleculeFilterType' )

#--------------------------------------------------------------
class VTKPointSetToOctreeImageFilter(Node, PBVTK_Node):

    bl_idname = 'VTKPointSetToOctreeImageFilterType'
    bl_label  = 'vtkPointSetToOctreeImageFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeCount: bpy.props.BoolProperty(name='ComputeCount', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeLastValue: bpy.props.BoolProperty(name='ComputeLastValue', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeMax: bpy.props.BoolProperty(name='ComputeMax', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeMean: bpy.props.BoolProperty(name='ComputeMean', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeMin: bpy.props.BoolProperty(name='ComputeMin', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeSum: bpy.props.BoolProperty(name='ComputeSum', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ProcessInputPointArray: bpy.props.BoolProperty(name='ProcessInputPointArray', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfPointsPerCell: bpy.props.IntProperty(name='NumberOfPointsPerCell', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeCount','m_ComputeLastValue','m_ComputeMax','m_ComputeMean','m_ComputeMin','m_ComputeSum','m_ProcessInputPointArray','m_ObjectName','m_NumberOfPointsPerCell',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPointSetToOctreeImageFilter )        
TYPENAMES.append('VTKPointSetToOctreeImageFilterType' )

#--------------------------------------------------------------
class VTKPointSmoothingFilter(Node, PBVTK_Node):

    bl_idname = 'VTKPointSmoothingFilterType'
    bl_label  = 'vtkPointSmoothingFilter'
    e_MotionConstraint_items=[ (x,x,x) for x in ['Unconstrained', 'Plane']]
    e_SmoothingMode_items=[ (x,x,x) for x in ['Default', 'Geometric', 'Uniform', 'Scalars', 'Tensors', 'FrameField']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputePackingRadius: bpy.props.BoolProperty(name='ComputePackingRadius', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableConstraints: bpy.props.BoolProperty(name='EnableConstraints', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateConstraintNormals: bpy.props.BoolProperty(name='GenerateConstraintNormals', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateConstraintScalars: bpy.props.BoolProperty(name='GenerateConstraintScalars', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NeighborhoodSize: bpy.props.IntProperty(name='NeighborhoodSize', default=8, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfIterations: bpy.props.IntProperty(name='NumberOfIterations', default=20, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfSubIterations: bpy.props.IntProperty(name='NumberOfSubIterations', default=10, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AttractionFactor: bpy.props.FloatProperty(name='AttractionFactor', default=0.5, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BoundaryAngle: bpy.props.FloatProperty(name='BoundaryAngle', default=110.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Convergence: bpy.props.FloatProperty(name='Convergence', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FixedAngle: bpy.props.FloatProperty(name='FixedAngle', default=60.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumStepSize: bpy.props.FloatProperty(name='MaximumStepSize', default=0.01, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PackingFactor: bpy.props.FloatProperty(name='PackingFactor', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PackingRadius: bpy.props.FloatProperty(name='PackingRadius', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_MotionConstraint: bpy.props.EnumProperty(name='MotionConstraint', default="Unconstrained", items=e_MotionConstraint_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SmoothingMode: bpy.props.EnumProperty(name='SmoothingMode', default="Default", items=e_SmoothingMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputePackingRadius','m_EnableConstraints','m_GenerateConstraintNormals','m_GenerateConstraintScalars','m_ObjectName','m_NeighborhoodSize','m_NumberOfIterations','m_NumberOfSubIterations','m_AttractionFactor','m_BoundaryAngle','m_Convergence','m_FixedAngle','m_MaximumStepSize','m_PackingFactor','m_PackingRadius','e_MotionConstraint','e_SmoothingMode',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'FrameFieldArray', 'Plane'], []) 
    
add_class( VTKPointSmoothingFilter )        
TYPENAMES.append('VTKPointSmoothingFilterType' )

#--------------------------------------------------------------
class VTKPoissonDiskSampler(Node, PBVTK_Node):

    bl_idname = 'VTKPoissonDiskSamplerType'
    bl_label  = 'vtkPoissonDiskSampler'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Radius: bpy.props.FloatProperty(name='Radius', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_Radius',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPoissonDiskSampler )        
TYPENAMES.append('VTKPoissonDiskSamplerType' )

#--------------------------------------------------------------
class VTKPolyDataAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKPolyDataAlgorithmType'
    bl_label  = 'vtkPolyDataAlgorithm'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPolyDataAlgorithm )        
TYPENAMES.append('VTKPolyDataAlgorithmType' )

#--------------------------------------------------------------
class VTKPolyDataConnectivityFilter(Node, PBVTK_Node):

    bl_idname = 'VTKPolyDataConnectivityFilterType'
    bl_label  = 'vtkPolyDataConnectivityFilter'
    e_ExtractionMode_items=[ (x,x,x) for x in ['PointSeededRegions', 'CellSeededRegions', 'SpecifiedRegions', 'LargestRegion', 'AllRegions', 'ClosestPointRegion']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ColorRegions: bpy.props.BoolProperty(name='ColorRegions', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FullScalarConnectivity: bpy.props.BoolProperty(name='FullScalarConnectivity', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MarkVisitedPointIds: bpy.props.BoolProperty(name='MarkVisitedPointIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarConnectivity: bpy.props.BoolProperty(name='ScalarConnectivity', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ExtractionMode: bpy.props.EnumProperty(name='ExtractionMode', default="LargestRegion", items=e_ExtractionMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ClosestPoint: bpy.props.FloatVectorProperty(name='ClosestPoint', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarRange: bpy.props.FloatVectorProperty(name='ScalarRange', default=[0.0, 1.0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ColorRegions','m_FullScalarConnectivity','m_MarkVisitedPointIds','m_ScalarConnectivity','m_ObjectName','e_ExtractionMode','m_ClosestPoint','m_ScalarRange',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPolyDataConnectivityFilter )        
TYPENAMES.append('VTKPolyDataConnectivityFilterType' )

#--------------------------------------------------------------
class VTKPolyDataNormals(Node, PBVTK_Node):

    bl_idname = 'VTKPolyDataNormalsType'
    bl_label  = 'vtkPolyDataNormals'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AutoOrientNormals: bpy.props.BoolProperty(name='AutoOrientNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeCellNormals: bpy.props.BoolProperty(name='ComputeCellNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputePointNormals: bpy.props.BoolProperty(name='ComputePointNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Consistency: bpy.props.BoolProperty(name='Consistency', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FlipNormals: bpy.props.BoolProperty(name='FlipNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NonManifoldTraversal: bpy.props.BoolProperty(name='NonManifoldTraversal', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Splitting: bpy.props.BoolProperty(name='Splitting', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FeatureAngle: bpy.props.FloatProperty(name='FeatureAngle', default=30.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AutoOrientNormals','m_ComputeCellNormals','m_ComputePointNormals','m_Consistency','m_FlipNormals','m_NonManifoldTraversal','m_Splitting','m_ObjectName','m_FeatureAngle',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPolyDataNormals )        
TYPENAMES.append('VTKPolyDataNormalsType' )

#--------------------------------------------------------------
class VTKPolyDataPlaneCutter(Node, PBVTK_Node):

    bl_idname = 'VTKPolyDataPlaneCutterType'
    bl_label  = 'vtkPolyDataPlaneCutter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeNormals: bpy.props.BoolProperty(name='ComputeNormals', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InterpolateAttributes: bpy.props.BoolProperty(name='InterpolateAttributes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BatchSize: bpy.props.IntProperty(name='BatchSize', default=10000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeNormals','m_InterpolateAttributes','m_ObjectName','m_BatchSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'Plane'], []) 
    
add_class( VTKPolyDataPlaneCutter )        
TYPENAMES.append('VTKPolyDataPlaneCutterType' )

#--------------------------------------------------------------
class VTKPolyDataPointSampler(Node, PBVTK_Node):

    bl_idname = 'VTKPolyDataPointSamplerType'
    bl_label  = 'vtkPolyDataPointSampler'
    e_PointGenerationMode_items=[ (x,x,x) for x in ['Regular', 'Random']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateEdgePoints: bpy.props.BoolProperty(name='GenerateEdgePoints', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateInteriorPoints: bpy.props.BoolProperty(name='GenerateInteriorPoints', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateVertexPoints: bpy.props.BoolProperty(name='GenerateVertexPoints', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateVertices: bpy.props.BoolProperty(name='GenerateVertices', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InterpolatePointData: bpy.props.BoolProperty(name='InterpolatePointData', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Distance: bpy.props.FloatProperty(name='Distance', default=0.01, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_PointGenerationMode: bpy.props.EnumProperty(name='PointGenerationMode', default="Regular", items=e_PointGenerationMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_GenerateEdgePoints','m_GenerateInteriorPoints','m_GenerateVertexPoints','m_GenerateVertices','m_InterpolatePointData','m_ObjectName','m_Distance','e_PointGenerationMode',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPolyDataPointSampler )        
TYPENAMES.append('VTKPolyDataPointSamplerType' )

#--------------------------------------------------------------
class VTKPolyDataSilhouette(Node, PBVTK_Node):

    bl_idname = 'VTKPolyDataSilhouetteType'
    bl_label  = 'vtkPolyDataSilhouette'
    e_Direction_items=[ (x,x,x) for x in ['SpecifiedVector', 'SpecifiedOrigin', 'CameraOrigin', 'CameraVector']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BorderEdges: bpy.props.BoolProperty(name='BorderEdges', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PieceInvariant: bpy.props.BoolProperty(name='PieceInvariant', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableFeatureAngle: bpy.props.IntProperty(name='EnableFeatureAngle', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FeatureAngle: bpy.props.FloatProperty(name='FeatureAngle', default=60.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_Direction: bpy.props.EnumProperty(name='Direction', default="CameraOrigin", items=e_Direction_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Origin: bpy.props.FloatVectorProperty(name='Origin', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Vector: bpy.props.FloatVectorProperty(name='Vector', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_BorderEdges','m_PieceInvariant','m_ObjectName','m_EnableFeatureAngle','m_FeatureAngle','e_Direction','m_Origin','m_Vector',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'Prop3D'], []) 
    
add_class( VTKPolyDataSilhouette )        
TYPENAMES.append('VTKPolyDataSilhouetteType' )

#--------------------------------------------------------------
class VTKPolyDataStreamer(Node, PBVTK_Node):

    bl_idname = 'VTKPolyDataStreamerType'
    bl_label  = 'vtkPolyDataStreamer'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ColorByPiece: bpy.props.BoolProperty(name='ColorByPiece', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfStreamDivisions: bpy.props.IntProperty(name='NumberOfStreamDivisions', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ColorByPiece','m_ObjectName','m_NumberOfStreamDivisions',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPolyDataStreamer )        
TYPENAMES.append('VTKPolyDataStreamerType' )

#--------------------------------------------------------------
class VTKPolyDataTangents(Node, PBVTK_Node):

    bl_idname = 'VTKPolyDataTangentsType'
    bl_label  = 'vtkPolyDataTangents'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeCellTangents: bpy.props.BoolProperty(name='ComputeCellTangents', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputePointTangents: bpy.props.BoolProperty(name='ComputePointTangents', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeCellTangents','m_ComputePointTangents','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPolyDataTangents )        
TYPENAMES.append('VTKPolyDataTangentsType' )

#--------------------------------------------------------------
class VTKPolyDataToImageStencil(Node, PBVTK_Node):

    bl_idname = 'VTKPolyDataToImageStencilType'
    bl_label  = 'vtkPolyDataToImageStencil'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=7.62939453125e-06, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputWholeExtent: bpy.props.IntVectorProperty(name='OutputWholeExtent', default=[0, -1, 0, -1, 0, -1], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputOrigin: bpy.props.FloatVectorProperty(name='OutputOrigin', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputSpacing: bpy.props.FloatVectorProperty(name='OutputSpacing', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableSMP','m_ObjectName','m_Tolerance','m_OutputWholeExtent','m_OutputOrigin','m_OutputSpacing',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPolyDataToImageStencil )        
TYPENAMES.append('VTKPolyDataToImageStencilType' )

#--------------------------------------------------------------
class VTKPolyDataToReebGraphFilter(Node, PBVTK_Node):

    bl_idname = 'VTKPolyDataToReebGraphFilterType'
    bl_label  = 'vtkPolyDataToReebGraphFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FieldId: bpy.props.IntProperty(name='FieldId', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_FieldId',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPolyDataToReebGraphFilter )        
TYPENAMES.append('VTKPolyDataToReebGraphFilterType' )

#--------------------------------------------------------------
class VTKPolyDataToUnstructuredGrid(Node, PBVTK_Node):

    bl_idname = 'VTKPolyDataToUnstructuredGridType'
    bl_label  = 'vtkPolyDataToUnstructuredGrid'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKPolyDataToUnstructuredGrid )        
TYPENAMES.append('VTKPolyDataToUnstructuredGridType' )

#--------------------------------------------------------------
class VTKProcrustesAlignmentFilter(Node, PBVTK_Node):

    bl_idname = 'VTKProcrustesAlignmentFilterType'
    bl_label  = 'vtkProcrustesAlignmentFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_StartFromCentroid: bpy.props.BoolProperty(name='StartFromCentroid', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_StartFromCentroid','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKProcrustesAlignmentFilter )        
TYPENAMES.append('VTKProcrustesAlignmentFilterType' )

#--------------------------------------------------------------
class VTKProgrammableAttributeDataFilter(Node, PBVTK_Node):

    bl_idname = 'VTKProgrammableAttributeDataFilterType'
    bl_label  = 'vtkProgrammableAttributeDataFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKProgrammableAttributeDataFilter )        
TYPENAMES.append('VTKProgrammableAttributeDataFilterType' )

#--------------------------------------------------------------
class VTKProgrammableFilter(Node, PBVTK_Node):

    bl_idname = 'VTKProgrammableFilterType'
    bl_label  = 'vtkProgrammableFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CopyArrays: bpy.props.BoolProperty(name='CopyArrays', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CopyArrays','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKProgrammableFilter )        
TYPENAMES.append('VTKProgrammableFilterType' )

#--------------------------------------------------------------
class VTKProjectPointsToPlane(Node, PBVTK_Node):

    bl_idname = 'VTKProjectPointsToPlaneType'
    bl_label  = 'vtkProjectPointsToPlane'
    e_ProjectionType_items=[ (x,x,x) for x in ['XPlane', 'YPlane', 'ZPlane', 'SpecifiedPlane', 'BestCoordinatePlane', 'BestFitPlane']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ProjectionType: bpy.props.EnumProperty(name='ProjectionType', default="ZPlane", items=e_ProjectionType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Normal: bpy.props.FloatVectorProperty(name='Normal', default=[0.0, 0.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Origin: bpy.props.FloatVectorProperty(name='Origin', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','e_ProjectionType','m_Normal','m_Origin',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKProjectPointsToPlane )        
TYPENAMES.append('VTKProjectPointsToPlaneType' )

#--------------------------------------------------------------
class VTKProjectSphereFilter(Node, PBVTK_Node):

    bl_idname = 'VTKProjectSphereFilterType'
    bl_label  = 'vtkProjectSphereFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_KeepPolePoints: bpy.props.BoolProperty(name='KeepPolePoints', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TranslateZ: bpy.props.BoolProperty(name='TranslateZ', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_KeepPolePoints','m_TranslateZ','m_ObjectName','m_Center',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKProjectSphereFilter )        
TYPENAMES.append('VTKProjectSphereFilterType' )

#--------------------------------------------------------------
class VTKProjectedTexture(Node, PBVTK_Node):

    bl_idname = 'VTKProjectedTextureType'
    bl_label  = 'vtkProjectedTexture'
    e_CameraMode_items=[ (x,x,x) for x in ['Pinhole', 'TwoMirror']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MirrorSeparation: bpy.props.FloatProperty(name='MirrorSeparation', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_CameraMode: bpy.props.EnumProperty(name='CameraMode', default="Pinhole", items=e_CameraMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AspectRatio: bpy.props.FloatVectorProperty(name='AspectRatio', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Position: bpy.props.FloatVectorProperty(name='Position', default=[0.0, 0.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SRange: bpy.props.FloatVectorProperty(name='SRange', default=[0.0, 1.0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TRange: bpy.props.FloatVectorProperty(name='TRange', default=[0.0, 1.0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Up: bpy.props.FloatVectorProperty(name='Up', default=[0.0, 1.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_MirrorSeparation','e_CameraMode','m_AspectRatio','m_Position','m_SRange','m_TRange','m_Up',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKProjectedTexture )        
TYPENAMES.append('VTKProjectedTextureType' )

#--------------------------------------------------------------
class VTKProteinRibbonFilter(Node, PBVTK_Node):

    bl_idname = 'VTKProteinRibbonFilterType'
    bl_label  = 'vtkProteinRibbonFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DrawSmallMoleculesAsSpheres: bpy.props.BoolProperty(name='DrawSmallMoleculesAsSpheres', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SphereResolution: bpy.props.IntProperty(name='SphereResolution', default=20, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SubdivideFactor: bpy.props.IntProperty(name='SubdivideFactor', default=20, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CoilWidth: bpy.props.FloatProperty(name='CoilWidth', default=0.30000001192092896, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HelixWidth: bpy.props.FloatProperty(name='HelixWidth', default=1.2999999523162842, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_DrawSmallMoleculesAsSpheres','m_ObjectName','m_SphereResolution','m_SubdivideFactor','m_CoilWidth','m_HelixWidth',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKProteinRibbonFilter )        
TYPENAMES.append('VTKProteinRibbonFilterType' )

#--------------------------------------------------------------
class VTKQuadRotationalExtrusionFilter(Node, PBVTK_Node):

    bl_idname = 'VTKQuadRotationalExtrusionFilterType'
    bl_label  = 'vtkQuadRotationalExtrusionFilter'
    e_Axis_items=[ (x,x,x) for x in ['X', 'Y', 'Z']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Capping: bpy.props.BoolProperty(name='Capping', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Resolution: bpy.props.IntProperty(name='Resolution', default=12, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DefaultAngle: bpy.props.FloatProperty(name='DefaultAngle', default=360.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DeltaRadius: bpy.props.FloatProperty(name='DeltaRadius', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Translation: bpy.props.FloatProperty(name='Translation', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_Axis: bpy.props.EnumProperty(name='Axis', default="Z", items=e_Axis_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Capping','m_ObjectName','m_Resolution','m_DefaultAngle','m_DeltaRadius','m_Translation','e_Axis',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKQuadRotationalExtrusionFilter )        
TYPENAMES.append('VTKQuadRotationalExtrusionFilterType' )

#--------------------------------------------------------------
class VTKQuadraturePointInterpolator(Node, PBVTK_Node):

    bl_idname = 'VTKQuadraturePointInterpolatorType'
    bl_label  = 'vtkQuadraturePointInterpolator'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKQuadraturePointInterpolator )        
TYPENAMES.append('VTKQuadraturePointInterpolatorType' )

#--------------------------------------------------------------
class VTKQuadraturePointsGenerator(Node, PBVTK_Node):

    bl_idname = 'VTKQuadraturePointsGeneratorType'
    bl_label  = 'vtkQuadraturePointsGenerator'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKQuadraturePointsGenerator )        
TYPENAMES.append('VTKQuadraturePointsGeneratorType' )

#--------------------------------------------------------------
class VTKQuadratureSchemeDictionaryGenerator(Node, PBVTK_Node):

    bl_idname = 'VTKQuadratureSchemeDictionaryGeneratorType'
    bl_label  = 'vtkQuadratureSchemeDictionaryGenerator'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKQuadratureSchemeDictionaryGenerator )        
TYPENAMES.append('VTKQuadratureSchemeDictionaryGeneratorType' )

#--------------------------------------------------------------
class VTKQuadricClustering(Node, PBVTK_Node):

    bl_idname = 'VTKQuadricClusteringType'
    bl_label  = 'vtkQuadricClustering'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AutoAdjustNumberOfDivisions: bpy.props.BoolProperty(name='AutoAdjustNumberOfDivisions', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CopyCellData: bpy.props.BoolProperty(name='CopyCellData', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PreventDuplicateCells: bpy.props.BoolProperty(name='PreventDuplicateCells', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseFeatureEdges: bpy.props.BoolProperty(name='UseFeatureEdges', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseFeaturePoints: bpy.props.BoolProperty(name='UseFeaturePoints', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseInputPoints: bpy.props.BoolProperty(name='UseInputPoints', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseInternalTriangles: bpy.props.BoolProperty(name='UseInternalTriangles', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfXDivisions: bpy.props.IntProperty(name='NumberOfXDivisions', default=50, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfYDivisions: bpy.props.IntProperty(name='NumberOfYDivisions', default=50, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfZDivisions: bpy.props.IntProperty(name='NumberOfZDivisions', default=50, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FeaturePointsAngle: bpy.props.FloatProperty(name='FeaturePointsAngle', default=30.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DivisionOrigin: bpy.props.FloatVectorProperty(name='DivisionOrigin', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DivisionSpacing: bpy.props.FloatVectorProperty(name='DivisionSpacing', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AutoAdjustNumberOfDivisions','m_CopyCellData','m_PreventDuplicateCells','m_UseFeatureEdges','m_UseFeaturePoints','m_UseInputPoints','m_UseInternalTriangles','m_ObjectName','m_NumberOfXDivisions','m_NumberOfYDivisions','m_NumberOfZDivisions','m_FeaturePointsAngle','m_DivisionOrigin','m_DivisionSpacing',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKQuadricClustering )        
TYPENAMES.append('VTKQuadricClusteringType' )

#--------------------------------------------------------------
class VTKQuadricDecimation(Node, PBVTK_Node):

    bl_idname = 'VTKQuadricDecimationType'
    bl_label  = 'vtkQuadricDecimation'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AttributeErrorMetric: bpy.props.BoolProperty(name='AttributeErrorMetric', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MapPointData: bpy.props.BoolProperty(name='MapPointData', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NormalsAttribute: bpy.props.BoolProperty(name='NormalsAttribute', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Regularize: bpy.props.BoolProperty(name='Regularize', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarsAttribute: bpy.props.BoolProperty(name='ScalarsAttribute', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TCoordsAttribute: bpy.props.BoolProperty(name='TCoordsAttribute', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TensorsAttribute: bpy.props.BoolProperty(name='TensorsAttribute', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VectorsAttribute: bpy.props.BoolProperty(name='VectorsAttribute', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VolumePreservation: bpy.props.BoolProperty(name='VolumePreservation', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_WeighBoundaryConstraintsByLength: bpy.props.BoolProperty(name='WeighBoundaryConstraintsByLength', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BoundaryWeightFactor: bpy.props.FloatProperty(name='BoundaryWeightFactor', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumError: bpy.props.FloatProperty(name='MaximumError', default=1e+30, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NormalsWeight: bpy.props.FloatProperty(name='NormalsWeight', default=0.1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Regularization: bpy.props.FloatProperty(name='Regularization', default=0.05, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarsWeight: bpy.props.FloatProperty(name='ScalarsWeight', default=0.1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TCoordsWeight: bpy.props.FloatProperty(name='TCoordsWeight', default=0.1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TargetReduction: bpy.props.FloatProperty(name='TargetReduction', default=0.9, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TensorsWeight: bpy.props.FloatProperty(name='TensorsWeight', default=0.1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VectorsWeight: bpy.props.FloatProperty(name='VectorsWeight', default=0.1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=21, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AttributeErrorMetric','m_MapPointData','m_NormalsAttribute','m_Regularize','m_ScalarsAttribute','m_TCoordsAttribute','m_TensorsAttribute','m_VectorsAttribute','m_VolumePreservation','m_WeighBoundaryConstraintsByLength','m_ObjectName','m_BoundaryWeightFactor','m_MaximumError','m_NormalsWeight','m_Regularization','m_ScalarsWeight','m_TCoordsWeight','m_TargetReduction','m_TensorsWeight','m_VectorsWeight',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKQuadricDecimation )        
TYPENAMES.append('VTKQuadricDecimationType' )

#--------------------------------------------------------------
class VTKQuantizePolyDataPoints(Node, PBVTK_Node):

    bl_idname = 'VTKQuantizePolyDataPointsType'
    bl_label  = 'vtkQuantizePolyDataPoints'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ConvertLinesToPoints: bpy.props.BoolProperty(name='ConvertLinesToPoints', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ConvertPolysToLines: bpy.props.BoolProperty(name='ConvertPolysToLines', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ConvertStripsToPolys: bpy.props.BoolProperty(name='ConvertStripsToPolys', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PieceInvariant: bpy.props.BoolProperty(name='PieceInvariant', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PointMerging: bpy.props.BoolProperty(name='PointMerging', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ToleranceIsAbsolute: bpy.props.BoolProperty(name='ToleranceIsAbsolute', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AbsoluteTolerance: bpy.props.FloatProperty(name='AbsoluteTolerance', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_QFactor: bpy.props.FloatProperty(name='QFactor', default=0.25, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ConvertLinesToPoints','m_ConvertPolysToLines','m_ConvertStripsToPolys','m_PieceInvariant','m_PointMerging','m_ToleranceIsAbsolute','m_ObjectName','m_AbsoluteTolerance','m_QFactor','m_Tolerance',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKQuantizePolyDataPoints )        
TYPENAMES.append('VTKQuantizePolyDataPointsType' )

#--------------------------------------------------------------
class VTKRandomAttributeGenerator(Node, PBVTK_Node):

    bl_idname = 'VTKRandomAttributeGeneratorType'
    bl_label  = 'vtkRandomAttributeGenerator'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AttributesConstantPerBlock: bpy.props.BoolProperty(name='AttributesConstantPerBlock', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateCellArray: bpy.props.BoolProperty(name='GenerateCellArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateCellNormals: bpy.props.BoolProperty(name='GenerateCellNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateCellScalars: bpy.props.BoolProperty(name='GenerateCellScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateCellTCoords: bpy.props.BoolProperty(name='GenerateCellTCoords', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateCellTensors: bpy.props.BoolProperty(name='GenerateCellTensors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateCellVectors: bpy.props.BoolProperty(name='GenerateCellVectors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateFieldArray: bpy.props.BoolProperty(name='GenerateFieldArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GeneratePointArray: bpy.props.BoolProperty(name='GeneratePointArray', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GeneratePointNormals: bpy.props.BoolProperty(name='GeneratePointNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GeneratePointScalars: bpy.props.BoolProperty(name='GeneratePointScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GeneratePointTCoords: bpy.props.BoolProperty(name='GeneratePointTCoords', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GeneratePointTensors: bpy.props.BoolProperty(name='GeneratePointTensors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GeneratePointVectors: bpy.props.BoolProperty(name='GeneratePointVectors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfComponents: bpy.props.IntProperty(name='NumberOfComponents', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfTuples: bpy.props.IntProperty(name='NumberOfTuples', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumComponentValue: bpy.props.FloatProperty(name='MaximumComponentValue', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumComponentValue: bpy.props.FloatProperty(name='MinimumComponentValue', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=20, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AttributesConstantPerBlock','m_GenerateCellArray','m_GenerateCellNormals','m_GenerateCellScalars','m_GenerateCellTCoords','m_GenerateCellTensors','m_GenerateCellVectors','m_GenerateFieldArray','m_GeneratePointArray','m_GeneratePointNormals','m_GeneratePointScalars','m_GeneratePointTCoords','m_GeneratePointTensors','m_GeneratePointVectors','m_ObjectName','m_NumberOfComponents','m_NumberOfTuples','m_MaximumComponentValue','m_MinimumComponentValue',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKRandomAttributeGenerator )        
TYPENAMES.append('VTKRandomAttributeGeneratorType' )

#--------------------------------------------------------------
class VTKRearrangeFields(Node, PBVTK_Node):

    bl_idname = 'VTKRearrangeFieldsType'
    bl_label  = 'vtkRearrangeFields'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKRearrangeFields )        
TYPENAMES.append('VTKRearrangeFieldsType' )

#--------------------------------------------------------------
class VTKRecoverGeometryWireframe(Node, PBVTK_Node):

    bl_idname = 'VTKRecoverGeometryWireframeType'
    bl_label  = 'vtkRecoverGeometryWireframe'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CellIdsAttribute: bpy.props.StringProperty(name='CellIdsAttribute', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CellIdsAttribute','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKRecoverGeometryWireframe )        
TYPENAMES.append('VTKRecoverGeometryWireframeType' )

#--------------------------------------------------------------
class VTKRectilinearGridAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKRectilinearGridAlgorithmType'
    bl_label  = 'vtkRectilinearGridAlgorithm'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKRectilinearGridAlgorithm )        
TYPENAMES.append('VTKRectilinearGridAlgorithmType' )

#--------------------------------------------------------------
class VTKRectilinearGridClip(Node, PBVTK_Node):

    bl_idname = 'VTKRectilinearGridClipType'
    bl_label  = 'vtkRectilinearGridClip'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ClipData: bpy.props.BoolProperty(name='ClipData', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ClipData','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKRectilinearGridClip )        
TYPENAMES.append('VTKRectilinearGridClipType' )

#--------------------------------------------------------------
class VTKRectilinearGridGeometryFilter(Node, PBVTK_Node):

    bl_idname = 'VTKRectilinearGridGeometryFilterType'
    bl_label  = 'vtkRectilinearGridGeometryFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Extent: bpy.props.IntVectorProperty(name='Extent', default=[0, 1000000000, 0, 1000000000, 0, 1000000000], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_Extent',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKRectilinearGridGeometryFilter )        
TYPENAMES.append('VTKRectilinearGridGeometryFilterType' )

#--------------------------------------------------------------
class VTKRectilinearGridOutlineFilter(Node, PBVTK_Node):

    bl_idname = 'VTKRectilinearGridOutlineFilterType'
    bl_label  = 'vtkRectilinearGridOutlineFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKRectilinearGridOutlineFilter )        
TYPENAMES.append('VTKRectilinearGridOutlineFilterType' )

#--------------------------------------------------------------
class VTKRectilinearGridPartitioner(Node, PBVTK_Node):

    bl_idname = 'VTKRectilinearGridPartitionerType'
    bl_label  = 'vtkRectilinearGridPartitioner'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DuplicateNodes: bpy.props.BoolProperty(name='DuplicateNodes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfGhostLayers: bpy.props.IntProperty(name='NumberOfGhostLayers', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfPartitions: bpy.props.IntProperty(name='NumberOfPartitions', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_DuplicateNodes','m_ObjectName','m_NumberOfGhostLayers','m_NumberOfPartitions',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKRectilinearGridPartitioner )        
TYPENAMES.append('VTKRectilinearGridPartitionerType' )

#--------------------------------------------------------------
class VTKRectilinearGridToPointSet(Node, PBVTK_Node):

    bl_idname = 'VTKRectilinearGridToPointSetType'
    bl_label  = 'vtkRectilinearGridToPointSet'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKRectilinearGridToPointSet )        
TYPENAMES.append('VTKRectilinearGridToPointSetType' )

#--------------------------------------------------------------
class VTKRectilinearGridToTetrahedra(Node, PBVTK_Node):

    bl_idname = 'VTKRectilinearGridToTetrahedraType'
    bl_label  = 'vtkRectilinearGridToTetrahedra'
    e_TetraPerCell_items=[ (x,x,x) for x in ['5And12', '5', '6', '12']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RememberVoxelId: bpy.props.BoolProperty(name='RememberVoxelId', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_TetraPerCell: bpy.props.EnumProperty(name='TetraPerCell', default="5", items=e_TetraPerCell_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_RememberVoxelId','m_ObjectName','e_TetraPerCell',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKRectilinearGridToTetrahedra )        
TYPENAMES.append('VTKRectilinearGridToTetrahedraType' )

#--------------------------------------------------------------
class VTKRectilinearSynchronizedTemplates(Node, PBVTK_Node):

    bl_idname = 'VTKRectilinearSynchronizedTemplatesType'
    bl_label  = 'vtkRectilinearSynchronizedTemplates'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeGradients: bpy.props.BoolProperty(name='ComputeGradients', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeNormals: bpy.props.BoolProperty(name='ComputeNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeScalars: bpy.props.BoolProperty(name='ComputeScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateTriangles: bpy.props.BoolProperty(name='GenerateTriangles', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ArrayComponent: bpy.props.IntProperty(name='ArrayComponent', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfContours: bpy.props.IntProperty(name='NumberOfContours', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeGradients','m_ComputeNormals','m_ComputeScalars','m_GenerateTriangles','m_ObjectName','m_ArrayComponent','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKRectilinearSynchronizedTemplates )        
TYPENAMES.append('VTKRectilinearSynchronizedTemplatesType' )

#--------------------------------------------------------------
class VTKRecursiveDividingCubes(Node, PBVTK_Node):

    bl_idname = 'VTKRecursiveDividingCubesType'
    bl_label  = 'vtkRecursiveDividingCubes'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Increment: bpy.props.IntProperty(name='Increment', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Distance: bpy.props.FloatProperty(name='Distance', default=0.1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Value: bpy.props.FloatProperty(name='Value', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_Increment','m_Distance','m_Value',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKRecursiveDividingCubes )        
TYPENAMES.append('VTKRecursiveDividingCubesType' )

#--------------------------------------------------------------
class VTKRedistributeDataSetFilter(Node, PBVTK_Node):

    bl_idname = 'VTKRedistributeDataSetFilterType'
    bl_label  = 'vtkRedistributeDataSetFilter'
    e_BoundaryMode_items=[ (x,x,x) for x in ['AssignToOneRegion', 'AssignToAllIntersectingRegions', 'SplitBoundaryCells']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableDebugging: bpy.props.BoolProperty(name='EnableDebugging', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ExpandExplicitCuts: bpy.props.BoolProperty(name='ExpandExplicitCuts', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateGlobalCellIds: bpy.props.BoolProperty(name='GenerateGlobalCellIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LoadBalanceAcrossAllBlocks: bpy.props.BoolProperty(name='LoadBalanceAcrossAllBlocks', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PreservePartitionsInOutput: bpy.props.BoolProperty(name='PreservePartitionsInOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseExplicitCuts: bpy.props.BoolProperty(name='UseExplicitCuts', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfPartitions: bpy.props.IntProperty(name='NumberOfPartitions', default=-1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_BoundaryMode: bpy.props.EnumProperty(name='BoundaryMode', default="AssignToOneRegion", items=e_BoundaryMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_EnableDebugging','m_ExpandExplicitCuts','m_GenerateGlobalCellIds','m_LoadBalanceAcrossAllBlocks','m_PreservePartitionsInOutput','m_UseExplicitCuts','m_ObjectName','m_NumberOfPartitions','e_BoundaryMode',]
    def m_connections( self ):
        return (['input'], ['output'], ['Strategy', 'ContainerAlgorithm'], []) 
    
add_class( VTKRedistributeDataSetFilter )        
TYPENAMES.append('VTKRedistributeDataSetFilterType' )

#--------------------------------------------------------------
class VTKReflectionFilter(Node, PBVTK_Node):

    bl_idname = 'VTKReflectionFilterType'
    bl_label  = 'vtkReflectionFilter'
    e_Plane_items=[ (x,x,x) for x in ['XMin', 'YMin', 'ZMin', 'XMax', 'YMax', 'ZMax', 'X', 'Y', 'Z']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CopyInput: bpy.props.BoolProperty(name='CopyInput', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FlipAllInputArrays: bpy.props.BoolProperty(name='FlipAllInputArrays', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Center: bpy.props.FloatProperty(name='Center', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_Plane: bpy.props.EnumProperty(name='Plane', default="XMin", items=e_Plane_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CopyInput','m_FlipAllInputArrays','m_ObjectName','m_Center','e_Plane',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKReflectionFilter )        
TYPENAMES.append('VTKReflectionFilterType' )

#--------------------------------------------------------------
class VTKRemoveDuplicatePolys(Node, PBVTK_Node):

    bl_idname = 'VTKRemoveDuplicatePolysType'
    bl_label  = 'vtkRemoveDuplicatePolys'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKRemoveDuplicatePolys )        
TYPENAMES.append('VTKRemoveDuplicatePolysType' )

#--------------------------------------------------------------
class VTKRemoveGhosts(Node, PBVTK_Node):

    bl_idname = 'VTKRemoveGhostsType'
    bl_label  = 'vtkRemoveGhosts'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKRemoveGhosts )        
TYPENAMES.append('VTKRemoveGhostsType' )

#--------------------------------------------------------------
class VTKRemovePolyData(Node, PBVTK_Node):

    bl_idname = 'VTKRemovePolyDataType'
    bl_label  = 'vtkRemovePolyData'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ExactMatch: bpy.props.BoolProperty(name='ExactMatch', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ExactMatch','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['CellIds', 'ContainerAlgorithm', 'PointIds'], []) 
    
add_class( VTKRemovePolyData )        
TYPENAMES.append('VTKRemovePolyDataType' )

#--------------------------------------------------------------
class VTKRemoveUnusedPoints(Node, PBVTK_Node):

    bl_idname = 'VTKRemoveUnusedPointsType'
    bl_label  = 'vtkRemoveUnusedPoints'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateOriginalPointIds: bpy.props.BoolProperty(name='GenerateOriginalPointIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OriginalPointIdsArrayName: bpy.props.StringProperty(name='OriginalPointIdsArrayName', default="vtkOriginalPointIds", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_GenerateOriginalPointIds','m_ObjectName','m_OriginalPointIdsArrayName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKRemoveUnusedPoints )        
TYPENAMES.append('VTKRemoveUnusedPointsType' )

#--------------------------------------------------------------
class VTKResampleToImage(Node, PBVTK_Node):

    bl_idname = 'VTKResampleToImageType'
    bl_label  = 'vtkResampleToImage'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseInputBounds: bpy.props.BoolProperty(name='UseInputBounds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SamplingDimensions: bpy.props.IntVectorProperty(name='SamplingDimensions', default=[10, 10, 10], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_UseInputBounds','m_ObjectName','m_SamplingDimensions',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKResampleToImage )        
TYPENAMES.append('VTKResampleToImageType' )

#--------------------------------------------------------------
class VTKReverseSense(Node, PBVTK_Node):

    bl_idname = 'VTKReverseSenseType'
    bl_label  = 'vtkReverseSense'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReverseCells: bpy.props.BoolProperty(name='ReverseCells', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReverseNormals: bpy.props.BoolProperty(name='ReverseNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ReverseCells','m_ReverseNormals','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKReverseSense )        
TYPENAMES.append('VTKReverseSenseType' )

#--------------------------------------------------------------
class VTKRibbonFilter(Node, PBVTK_Node):

    bl_idname = 'VTKRibbonFilterType'
    bl_label  = 'vtkRibbonFilter'
    e_GenerateTCoords_items=[ (x,x,x) for x in ['Off', 'NormalizedLength', 'UseLength', 'UseScalars']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseDefaultNormal: bpy.props.BoolProperty(name='UseDefaultNormal', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VaryWidth: bpy.props.BoolProperty(name='VaryWidth', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Angle: bpy.props.FloatProperty(name='Angle', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TextureLength: bpy.props.FloatProperty(name='TextureLength', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Width: bpy.props.FloatProperty(name='Width', default=0.5, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_WidthFactor: bpy.props.FloatProperty(name='WidthFactor', default=2.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_GenerateTCoords: bpy.props.EnumProperty(name='GenerateTCoords', default="Off", items=e_GenerateTCoords_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DefaultNormal: bpy.props.FloatVectorProperty(name='DefaultNormal', default=[0.0, 0.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_UseDefaultNormal','m_VaryWidth','m_ObjectName','m_Angle','m_TextureLength','m_Width','m_WidthFactor','e_GenerateTCoords','m_DefaultNormal',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKRibbonFilter )        
TYPENAMES.append('VTKRibbonFilterType' )

#--------------------------------------------------------------
class VTKRotationFilter(Node, PBVTK_Node):

    bl_idname = 'VTKRotationFilterType'
    bl_label  = 'vtkRotationFilter'
    e_Axis_items=[ (x,x,x) for x in ['X', 'Y', 'Z']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CopyInput: bpy.props.BoolProperty(name='CopyInput', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfCopies: bpy.props.IntProperty(name='NumberOfCopies', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Angle: bpy.props.FloatProperty(name='Angle', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_Axis: bpy.props.EnumProperty(name='Axis', default="Z", items=e_Axis_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CopyInput','m_ObjectName','m_NumberOfCopies','m_Angle','e_Axis','m_Center',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKRotationFilter )        
TYPENAMES.append('VTKRotationFilterType' )

#--------------------------------------------------------------
class VTKRotationalExtrusionFilter(Node, PBVTK_Node):

    bl_idname = 'VTKRotationalExtrusionFilterType'
    bl_label  = 'vtkRotationalExtrusionFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Capping: bpy.props.BoolProperty(name='Capping', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Resolution: bpy.props.IntProperty(name='Resolution', default=12, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Angle: bpy.props.FloatProperty(name='Angle', default=360.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DeltaRadius: bpy.props.FloatProperty(name='DeltaRadius', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Translation: bpy.props.FloatProperty(name='Translation', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RotationAxis: bpy.props.FloatVectorProperty(name='RotationAxis', default=[0.0, 0.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Capping','m_ObjectName','m_Resolution','m_Angle','m_DeltaRadius','m_Translation','m_RotationAxis',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKRotationalExtrusionFilter )        
TYPENAMES.append('VTKRotationalExtrusionFilterType' )

#--------------------------------------------------------------
class VTKRuledSurfaceFilter(Node, PBVTK_Node):

    bl_idname = 'VTKRuledSurfaceFilterType'
    bl_label  = 'vtkRuledSurfaceFilter'
    e_RuledMode_items=[ (x,x,x) for x in ['Resample', 'PointWalk']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CloseSurface: bpy.props.BoolProperty(name='CloseSurface', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OrientLoops: bpy.props.BoolProperty(name='OrientLoops', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassLines: bpy.props.BoolProperty(name='PassLines', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Offset: bpy.props.IntProperty(name='Offset', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OnRatio: bpy.props.IntProperty(name='OnRatio', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DistanceFactor: bpy.props.FloatProperty(name='DistanceFactor', default=3.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_RuledMode: bpy.props.EnumProperty(name='RuledMode', default="Resample", items=e_RuledMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Resolution: bpy.props.IntVectorProperty(name='Resolution', default=[1, 1], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CloseSurface','m_OrientLoops','m_PassLines','m_ObjectName','m_Offset','m_OnRatio','m_DistanceFactor','e_RuledMode','m_Resolution',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKRuledSurfaceFilter )        
TYPENAMES.append('VTKRuledSurfaceFilterType' )

#--------------------------------------------------------------
class VTKSMPContourGrid(Node, PBVTK_Node):

    bl_idname = 'VTKSMPContourGridType'
    bl_label  = 'vtkSMPContourGrid'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeNormals: bpy.props.BoolProperty(name='ComputeNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeScalars: bpy.props.BoolProperty(name='ComputeScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateTriangles: bpy.props.BoolProperty(name='GenerateTriangles', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MergePieces: bpy.props.BoolProperty(name='MergePieces', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfContours: bpy.props.IntProperty(name='NumberOfContours', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeNormals','m_ComputeScalars','m_GenerateTriangles','m_MergePieces','m_ObjectName','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKSMPContourGrid )        
TYPENAMES.append('VTKSMPContourGridType' )

#--------------------------------------------------------------
class VTKSampleImplicitFunctionFilter(Node, PBVTK_Node):

    bl_idname = 'VTKSampleImplicitFunctionFilterType'
    bl_label  = 'vtkSampleImplicitFunctionFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeGradients: bpy.props.BoolProperty(name='ComputeGradients', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GradientArrayName: bpy.props.StringProperty(name='GradientArrayName', default="Implicit gradients", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarArrayName: bpy.props.StringProperty(name='ScalarArrayName', default="Implicit scalars", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeGradients','m_GradientArrayName','m_ObjectName','m_ScalarArrayName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'ImplicitFunction'], []) 
    
add_class( VTKSampleImplicitFunctionFilter )        
TYPENAMES.append('VTKSampleImplicitFunctionFilterType' )

#--------------------------------------------------------------
class VTKSelectionAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKSelectionAlgorithmType'
    bl_label  = 'vtkSelectionAlgorithm'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKSelectionAlgorithm )        
TYPENAMES.append('VTKSelectionAlgorithmType' )

#--------------------------------------------------------------
class VTKShepardMethod(Node, PBVTK_Node):

    bl_idname = 'VTKShepardMethodType'
    bl_label  = 'vtkShepardMethod'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumDistance: bpy.props.FloatProperty(name='MaximumDistance', default=0.25, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NullValue: bpy.props.FloatProperty(name='NullValue', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PowerParameter: bpy.props.FloatProperty(name='PowerParameter', default=2.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SampleDimensions: bpy.props.IntVectorProperty(name='SampleDimensions', default=[50, 50, 50], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ModelBounds: bpy.props.FloatVectorProperty(name='ModelBounds', default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_MaximumDistance','m_NullValue','m_PowerParameter','m_SampleDimensions','m_ModelBounds',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKShepardMethod )        
TYPENAMES.append('VTKShepardMethodType' )

#--------------------------------------------------------------
class VTKShrinkFilter(Node, PBVTK_Node):

    bl_idname = 'VTKShrinkFilterType'
    bl_label  = 'vtkShrinkFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ShrinkFactor: bpy.props.FloatProperty(name='ShrinkFactor', default=0.5, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_ShrinkFactor',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKShrinkFilter )        
TYPENAMES.append('VTKShrinkFilterType' )

#--------------------------------------------------------------
class VTKShrinkPolyData(Node, PBVTK_Node):

    bl_idname = 'VTKShrinkPolyDataType'
    bl_label  = 'vtkShrinkPolyData'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ShrinkFactor: bpy.props.FloatProperty(name='ShrinkFactor', default=0.5, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_ShrinkFactor',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKShrinkPolyData )        
TYPENAMES.append('VTKShrinkPolyDataType' )

#--------------------------------------------------------------
class VTKSignedDistance(Node, PBVTK_Node):

    bl_idname = 'VTKSignedDistanceType'
    bl_label  = 'vtkSignedDistance'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Radius: bpy.props.FloatProperty(name='Radius', default=0.1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Dimensions: bpy.props.IntVectorProperty(name='Dimensions', default=[256, 256, 256], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Bounds: bpy.props.FloatVectorProperty(name='Bounds', default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_Radius','m_Dimensions','m_Bounds',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKSignedDistance )        
TYPENAMES.append('VTKSignedDistanceType' )

#--------------------------------------------------------------
class VTKSimpleBondPerceiver(Node, PBVTK_Node):

    bl_idname = 'VTKSimpleBondPerceiverType'
    bl_label  = 'vtkSimpleBondPerceiver'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IsToleranceAbsolute: bpy.props.BoolProperty(name='IsToleranceAbsolute', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=0.44999998807907104, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_IsToleranceAbsolute','m_ObjectName','m_Tolerance',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKSimpleBondPerceiver )        
TYPENAMES.append('VTKSimpleBondPerceiverType' )

#--------------------------------------------------------------
class VTKSimpleElevationFilter(Node, PBVTK_Node):

    bl_idname = 'VTKSimpleElevationFilterType'
    bl_label  = 'vtkSimpleElevationFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Vector: bpy.props.FloatVectorProperty(name='Vector', default=[0.0, 0.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_Vector',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKSimpleElevationFilter )        
TYPENAMES.append('VTKSimpleElevationFilterType' )

#--------------------------------------------------------------
class VTKSpatialRepresentationFilter(Node, PBVTK_Node):

    bl_idname = 'VTKSpatialRepresentationFilterType'
    bl_label  = 'vtkSpatialRepresentationFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateLeaves: bpy.props.BoolProperty(name='GenerateLeaves', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_GenerateLeaves','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'SpatialRepresentation'], []) 
    
add_class( VTKSpatialRepresentationFilter )        
TYPENAMES.append('VTKSpatialRepresentationFilterType' )

#--------------------------------------------------------------
class VTKSpatioTemporalHarmonicsAttribute(Node, PBVTK_Node):

    bl_idname = 'VTKSpatioTemporalHarmonicsAttributeType'
    bl_label  = 'vtkSpatioTemporalHarmonicsAttribute'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKSpatioTemporalHarmonicsAttribute )        
TYPENAMES.append('VTKSpatioTemporalHarmonicsAttributeType' )

#--------------------------------------------------------------
class VTKSphereTreeFilter(Node, PBVTK_Node):

    bl_idname = 'VTKSphereTreeFilterType'
    bl_label  = 'vtkSphereTreeFilter'
    e_ExtractionMode_items=[ (x,x,x) for x in ['Levels', 'Point', 'Line', 'Plane']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TreeHierarchy: bpy.props.BoolProperty(name='TreeHierarchy', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Level: bpy.props.IntProperty(name='Level', default=-1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ExtractionMode: bpy.props.EnumProperty(name='ExtractionMode', default="Levels", items=e_ExtractionMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Normal: bpy.props.FloatVectorProperty(name='Normal', default=[0.0, 0.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Point: bpy.props.FloatVectorProperty(name='Point', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Ray: bpy.props.FloatVectorProperty(name='Ray', default=[1.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_TreeHierarchy','m_ObjectName','m_Level','e_ExtractionMode','m_Normal','m_Point','m_Ray',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'SphereTree'], []) 
    
add_class( VTKSphereTreeFilter )        
TYPENAMES.append('VTKSphereTreeFilterType' )

#--------------------------------------------------------------
class VTKSphericalHarmonics(Node, PBVTK_Node):

    bl_idname = 'VTKSphericalHarmonicsType'
    bl_label  = 'vtkSphericalHarmonics'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKSphericalHarmonics )        
TYPENAMES.append('VTKSphericalHarmonicsType' )

#--------------------------------------------------------------
class VTKSplineFilter(Node, PBVTK_Node):

    bl_idname = 'VTKSplineFilterType'
    bl_label  = 'vtkSplineFilter'
    e_GenerateTCoords_items=[ (x,x,x) for x in ['Off', 'NormalizedLength', 'UseLength', 'UseScalars']]
    e_Subdivide_items=[ (x,x,x) for x in ['Specified', 'Length']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumNumberOfSubdivisions: bpy.props.IntProperty(name='MaximumNumberOfSubdivisions', default=1000000000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfSubdivisions: bpy.props.IntProperty(name='NumberOfSubdivisions', default=100, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Length: bpy.props.FloatProperty(name='Length', default=0.1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TextureLength: bpy.props.FloatProperty(name='TextureLength', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_GenerateTCoords: bpy.props.EnumProperty(name='GenerateTCoords', default="NormalizedLength", items=e_GenerateTCoords_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_Subdivide: bpy.props.EnumProperty(name='Subdivide', default="Specified", items=e_Subdivide_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_MaximumNumberOfSubdivisions','m_NumberOfSubdivisions','m_Length','m_TextureLength','e_GenerateTCoords','e_Subdivide',]
    def m_connections( self ):
        return (['input'], ['output'], ['Spline', 'ContainerAlgorithm'], []) 
    
add_class( VTKSplineFilter )        
TYPENAMES.append('VTKSplineFilterType' )

#--------------------------------------------------------------
class VTKSplitByCellScalarFilter(Node, PBVTK_Node):

    bl_idname = 'VTKSplitByCellScalarFilterType'
    bl_label  = 'vtkSplitByCellScalarFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassAllPoints: bpy.props.BoolProperty(name='PassAllPoints', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_PassAllPoints','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKSplitByCellScalarFilter )        
TYPENAMES.append('VTKSplitByCellScalarFilterType' )

#--------------------------------------------------------------
class VTKSplitColumnComponents(Node, PBVTK_Node):

    bl_idname = 'VTKSplitColumnComponentsType'
    bl_label  = 'vtkSplitColumnComponents'
    e_NamingMode_items=[ (x,x,x) for x in ['NumberWithParens', 'NamesWithParens', 'NumberWithUnderscores', 'NamesWithUnderscores']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CalculateMagnitudes: bpy.props.BoolProperty(name='CalculateMagnitudes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_NamingMode: bpy.props.EnumProperty(name='NamingMode', default="NumberWithParens", items=e_NamingMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CalculateMagnitudes','m_ObjectName','e_NamingMode',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKSplitColumnComponents )        
TYPENAMES.append('VTKSplitColumnComponentsType' )

#--------------------------------------------------------------
class VTKSplitField(Node, PBVTK_Node):

    bl_idname = 'VTKSplitFieldType'
    bl_label  = 'vtkSplitField'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKSplitField )        
TYPENAMES.append('VTKSplitFieldType' )

#--------------------------------------------------------------
class VTKSplitSharpEdgesPolyData(Node, PBVTK_Node):

    bl_idname = 'VTKSplitSharpEdgesPolyDataType'
    bl_label  = 'vtkSplitSharpEdgesPolyData'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FeatureAngle: bpy.props.FloatProperty(name='FeatureAngle', default=30.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_FeatureAngle',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKSplitSharpEdgesPolyData )        
TYPENAMES.append('VTKSplitSharpEdgesPolyDataType' )

#--------------------------------------------------------------
class VTKStaticCleanPolyData(Node, PBVTK_Node):

    bl_idname = 'VTKStaticCleanPolyDataType'
    bl_label  = 'vtkStaticCleanPolyData'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AveragePointData: bpy.props.BoolProperty(name='AveragePointData', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ConvertLinesToPoints: bpy.props.BoolProperty(name='ConvertLinesToPoints', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ConvertPolysToLines: bpy.props.BoolProperty(name='ConvertPolysToLines', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ConvertStripsToPolys: bpy.props.BoolProperty(name='ConvertStripsToPolys', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PieceInvariant: bpy.props.BoolProperty(name='PieceInvariant', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ProduceMergeMap: bpy.props.BoolProperty(name='ProduceMergeMap', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RemoveUnusedPoints: bpy.props.BoolProperty(name='RemoveUnusedPoints', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ToleranceIsAbsolute: bpy.props.BoolProperty(name='ToleranceIsAbsolute', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MergingArray: bpy.props.StringProperty(name='MergingArray', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AbsoluteTolerance: bpy.props.FloatProperty(name='AbsoluteTolerance', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AveragePointData','m_ConvertLinesToPoints','m_ConvertPolysToLines','m_ConvertStripsToPolys','m_PieceInvariant','m_ProduceMergeMap','m_RemoveUnusedPoints','m_ToleranceIsAbsolute','m_MergingArray','m_ObjectName','m_AbsoluteTolerance','m_Tolerance',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKStaticCleanPolyData )        
TYPENAMES.append('VTKStaticCleanPolyDataType' )

#--------------------------------------------------------------
class VTKStaticCleanUnstructuredGrid(Node, PBVTK_Node):

    bl_idname = 'VTKStaticCleanUnstructuredGridType'
    bl_label  = 'vtkStaticCleanUnstructuredGrid'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AveragePointData: bpy.props.BoolProperty(name='AveragePointData', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PieceInvariant: bpy.props.BoolProperty(name='PieceInvariant', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ProduceMergeMap: bpy.props.BoolProperty(name='ProduceMergeMap', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RemoveUnusedPoints: bpy.props.BoolProperty(name='RemoveUnusedPoints', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ToleranceIsAbsolute: bpy.props.BoolProperty(name='ToleranceIsAbsolute', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MergingArray: bpy.props.StringProperty(name='MergingArray', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AbsoluteTolerance: bpy.props.FloatProperty(name='AbsoluteTolerance', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AveragePointData','m_PieceInvariant','m_ProduceMergeMap','m_RemoveUnusedPoints','m_ToleranceIsAbsolute','m_MergingArray','m_ObjectName','m_AbsoluteTolerance','m_Tolerance',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKStaticCleanUnstructuredGrid )        
TYPENAMES.append('VTKStaticCleanUnstructuredGridType' )

#--------------------------------------------------------------
class VTKStitchImageDataWithGhosts(Node, PBVTK_Node):

    bl_idname = 'VTKStitchImageDataWithGhostsType'
    bl_label  = 'vtkStitchImageDataWithGhosts'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BuildIfRequired: bpy.props.BoolProperty(name='BuildIfRequired', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateGlobalIds: bpy.props.BoolProperty(name='GenerateGlobalIds', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateProcessIds: bpy.props.BoolProperty(name='GenerateProcessIds', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SynchronizeOnly: bpy.props.BoolProperty(name='SynchronizeOnly', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseStaticMeshCache: bpy.props.BoolProperty(name='UseStaticMeshCache', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfGhostLayers: bpy.props.IntProperty(name='NumberOfGhostLayers', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_BuildIfRequired','m_GenerateGlobalIds','m_GenerateProcessIds','m_SynchronizeOnly','m_UseStaticMeshCache','m_ObjectName','m_NumberOfGhostLayers',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKStitchImageDataWithGhosts )        
TYPENAMES.append('VTKStitchImageDataWithGhostsType' )

#--------------------------------------------------------------
class VTKStrahlerMetric(Node, PBVTK_Node):

    bl_idname = 'VTKStrahlerMetricType'
    bl_label  = 'vtkStrahlerMetric'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Normalize: bpy.props.BoolProperty(name='Normalize', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Normalize','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKStrahlerMetric )        
TYPENAMES.append('VTKStrahlerMetricType' )

#--------------------------------------------------------------
class VTKStripper(Node, PBVTK_Node):

    bl_idname = 'VTKStripperType'
    bl_label  = 'vtkStripper'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_JoinContiguousSegments: bpy.props.BoolProperty(name='JoinContiguousSegments', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassCellDataAsFieldData: bpy.props.BoolProperty(name='PassCellDataAsFieldData', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassThroughCellIds: bpy.props.BoolProperty(name='PassThroughCellIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassThroughPointIds: bpy.props.BoolProperty(name='PassThroughPointIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumLength: bpy.props.IntProperty(name='MaximumLength', default=1000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_JoinContiguousSegments','m_PassCellDataAsFieldData','m_PassThroughCellIds','m_PassThroughPointIds','m_ObjectName','m_MaximumLength',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKStripper )        
TYPENAMES.append('VTKStripperType' )

#--------------------------------------------------------------
class VTKStructuredDataPlaneCutter(Node, PBVTK_Node):

    bl_idname = 'VTKStructuredDataPlaneCutterType'
    bl_label  = 'vtkStructuredDataPlaneCutter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BuildHierarchy: bpy.props.BoolProperty(name='BuildHierarchy', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BuildTree: bpy.props.BoolProperty(name='BuildTree', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeNormals: bpy.props.BoolProperty(name='ComputeNormals', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GeneratePolygons: bpy.props.BoolProperty(name='GeneratePolygons', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InterpolateAttributes: bpy.props.BoolProperty(name='InterpolateAttributes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BatchSize: bpy.props.IntProperty(name='BatchSize', default=1000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_BuildHierarchy','m_BuildTree','m_ComputeNormals','m_GeneratePolygons','m_InterpolateAttributes','m_ObjectName','m_BatchSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['Plane', 'ContainerAlgorithm', 'SphereTree'], []) 
    
add_class( VTKStructuredDataPlaneCutter )        
TYPENAMES.append('VTKStructuredDataPlaneCutterType' )

#--------------------------------------------------------------
class VTKStructuredGridAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKStructuredGridAlgorithmType'
    bl_label  = 'vtkStructuredGridAlgorithm'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKStructuredGridAlgorithm )        
TYPENAMES.append('VTKStructuredGridAlgorithmType' )

#--------------------------------------------------------------
class VTKStructuredGridAppend(Node, PBVTK_Node):

    bl_idname = 'VTKStructuredGridAppendType'
    bl_label  = 'vtkStructuredGridAppend'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKStructuredGridAppend )        
TYPENAMES.append('VTKStructuredGridAppendType' )

#--------------------------------------------------------------
class VTKStructuredGridClip(Node, PBVTK_Node):

    bl_idname = 'VTKStructuredGridClipType'
    bl_label  = 'vtkStructuredGridClip'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ClipData: bpy.props.BoolProperty(name='ClipData', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ClipData','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKStructuredGridClip )        
TYPENAMES.append('VTKStructuredGridClipType' )

#--------------------------------------------------------------
class VTKStructuredGridGeometryFilter(Node, PBVTK_Node):

    bl_idname = 'VTKStructuredGridGeometryFilterType'
    bl_label  = 'vtkStructuredGridGeometryFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Extent: bpy.props.IntVectorProperty(name='Extent', default=[0, 1000000000, 0, 1000000000, 0, 1000000000], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_Extent',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKStructuredGridGeometryFilter )        
TYPENAMES.append('VTKStructuredGridGeometryFilterType' )

#--------------------------------------------------------------
class VTKStructuredGridOutlineFilter(Node, PBVTK_Node):

    bl_idname = 'VTKStructuredGridOutlineFilterType'
    bl_label  = 'vtkStructuredGridOutlineFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKStructuredGridOutlineFilter )        
TYPENAMES.append('VTKStructuredGridOutlineFilterType' )

#--------------------------------------------------------------
class VTKStructuredGridPartitioner(Node, PBVTK_Node):

    bl_idname = 'VTKStructuredGridPartitionerType'
    bl_label  = 'vtkStructuredGridPartitioner'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DuplicateNodes: bpy.props.BoolProperty(name='DuplicateNodes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfGhostLayers: bpy.props.IntProperty(name='NumberOfGhostLayers', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfPartitions: bpy.props.IntProperty(name='NumberOfPartitions', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_DuplicateNodes','m_ObjectName','m_NumberOfGhostLayers','m_NumberOfPartitions',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKStructuredGridPartitioner )        
TYPENAMES.append('VTKStructuredGridPartitionerType' )

#--------------------------------------------------------------
class VTKSubdivideTetra(Node, PBVTK_Node):

    bl_idname = 'VTKSubdivideTetraType'
    bl_label  = 'vtkSubdivideTetra'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKSubdivideTetra )        
TYPENAMES.append('VTKSubdivideTetraType' )

#--------------------------------------------------------------
class VTKSurfaceNets2D(Node, PBVTK_Node):

    bl_idname = 'VTKSurfaceNets2DType'
    bl_label  = 'vtkSurfaceNets2D'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeScalars: bpy.props.BoolProperty(name='ComputeScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataCaching: bpy.props.BoolProperty(name='DataCaching', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Smoothing: bpy.props.BoolProperty(name='Smoothing', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ArrayComponent: bpy.props.IntProperty(name='ArrayComponent', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfContours: bpy.props.IntProperty(name='NumberOfContours', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfLabels: bpy.props.IntProperty(name='NumberOfLabels', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BackgroundLabel: bpy.props.FloatProperty(name='BackgroundLabel', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeScalars','m_DataCaching','m_Smoothing','m_ObjectName','m_ArrayComponent','m_NumberOfContours','m_NumberOfLabels','m_BackgroundLabel',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKSurfaceNets2D )        
TYPENAMES.append('VTKSurfaceNets2DType' )

#--------------------------------------------------------------
class VTKSurfaceNets3D(Node, PBVTK_Node):

    bl_idname = 'VTKSurfaceNets3DType'
    bl_label  = 'vtkSurfaceNets3D'
    e_OutputMeshType_items=[ (x,x,x) for x in ['Default', 'Triangles', 'Quads']]
    e_OutputStyle_items=[ (x,x,x) for x in ['Default', 'Boundary', 'Selected']]
    e_TriangulationStrategy_items=[ (x,x,x) for x in ['Greedy', 'MinEdge', 'MinArea']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AutomaticSmoothingConstraints: bpy.props.BoolProperty(name='AutomaticSmoothingConstraints', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DataCaching: bpy.props.BoolProperty(name='DataCaching', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OptimizedSmoothingStencils: bpy.props.BoolProperty(name='OptimizedSmoothingStencils', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Smoothing: bpy.props.BoolProperty(name='Smoothing', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ArrayComponent: bpy.props.IntProperty(name='ArrayComponent', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfContours: bpy.props.IntProperty(name='NumberOfContours', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfIterations: bpy.props.IntProperty(name='NumberOfIterations', default=16, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfLabels: bpy.props.IntProperty(name='NumberOfLabels', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BackgroundLabel: bpy.props.FloatProperty(name='BackgroundLabel', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ConstraintDistance: bpy.props.FloatProperty(name='ConstraintDistance', default=0.001, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ConstraintScale: bpy.props.FloatProperty(name='ConstraintScale', default=2.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RelaxationFactor: bpy.props.FloatProperty(name='RelaxationFactor', default=0.5, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_OutputMeshType: bpy.props.EnumProperty(name='OutputMeshType', default="Default", items=e_OutputMeshType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_OutputStyle: bpy.props.EnumProperty(name='OutputStyle', default="Default", items=e_OutputStyle_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_TriangulationStrategy: bpy.props.EnumProperty(name='TriangulationStrategy', default="MinEdge", items=e_TriangulationStrategy_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ConstraintBox: bpy.props.FloatVectorProperty(name='ConstraintBox', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=18, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AutomaticSmoothingConstraints','m_DataCaching','m_OptimizedSmoothingStencils','m_Smoothing','m_ObjectName','m_ArrayComponent','m_NumberOfContours','m_NumberOfIterations','m_NumberOfLabels','m_BackgroundLabel','m_ConstraintDistance','m_ConstraintScale','m_RelaxationFactor','e_OutputMeshType','e_OutputStyle','e_TriangulationStrategy','m_ConstraintBox',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKSurfaceNets3D )        
TYPENAMES.append('VTKSurfaceNets3DType' )

#--------------------------------------------------------------
class VTKSurfaceReconstructionFilter(Node, PBVTK_Node):

    bl_idname = 'VTKSurfaceReconstructionFilterType'
    bl_label  = 'vtkSurfaceReconstructionFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NeighborhoodSize: bpy.props.IntProperty(name='NeighborhoodSize', default=20, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SampleSpacing: bpy.props.FloatProperty(name='SampleSpacing', default=-1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_NeighborhoodSize','m_SampleSpacing',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKSurfaceReconstructionFilter )        
TYPENAMES.append('VTKSurfaceReconstructionFilterType' )

#--------------------------------------------------------------
class VTKSynchronizedTemplates2D(Node, PBVTK_Node):

    bl_idname = 'VTKSynchronizedTemplates2DType'
    bl_label  = 'vtkSynchronizedTemplates2D'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeScalars: bpy.props.BoolProperty(name='ComputeScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ArrayComponent: bpy.props.IntProperty(name='ArrayComponent', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfContours: bpy.props.IntProperty(name='NumberOfContours', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeScalars','m_ObjectName','m_ArrayComponent','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKSynchronizedTemplates2D )        
TYPENAMES.append('VTKSynchronizedTemplates2DType' )

#--------------------------------------------------------------
class VTKTableAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKTableAlgorithmType'
    bl_label  = 'vtkTableAlgorithm'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTableAlgorithm )        
TYPENAMES.append('VTKTableAlgorithmType' )

#--------------------------------------------------------------
class VTKTableFFT(Node, PBVTK_Node):

    bl_idname = 'VTKTableFFTType'
    bl_label  = 'vtkTableFFT'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AverageFft: bpy.props.BoolProperty(name='AverageFft', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CreateFrequencyColumn: bpy.props.BoolProperty(name='CreateFrequencyColumn', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Detrend: bpy.props.BoolProperty(name='Detrend', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Normalize: bpy.props.BoolProperty(name='Normalize', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReturnOnesided: bpy.props.BoolProperty(name='ReturnOnesided', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BlockOverlap: bpy.props.IntProperty(name='BlockOverlap', default=-1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BlockSize: bpy.props.IntProperty(name='BlockSize', default=1024, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalingMethod: bpy.props.IntProperty(name='ScalingMethod', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_WindowingFunction: bpy.props.IntProperty(name='WindowingFunction', default=4, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DefaultSampleRate: bpy.props.FloatProperty(name='DefaultSampleRate', default=10000.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=12, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AverageFft','m_CreateFrequencyColumn','m_Detrend','m_Normalize','m_ReturnOnesided','m_ObjectName','m_BlockOverlap','m_BlockSize','m_ScalingMethod','m_WindowingFunction','m_DefaultSampleRate',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTableFFT )        
TYPENAMES.append('VTKTableFFTType' )

#--------------------------------------------------------------
class VTKTableToPolyData(Node, PBVTK_Node):

    bl_idname = 'VTKTableToPolyDataType'
    bl_label  = 'vtkTableToPolyData'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Create2DPoints: bpy.props.BoolProperty(name='Create2DPoints', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PreserveCoordinateColumnsAsDataArrays: bpy.props.BoolProperty(name='PreserveCoordinateColumnsAsDataArrays', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_XColumn: bpy.props.StringProperty(name='XColumn', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_YColumn: bpy.props.StringProperty(name='YColumn', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ZColumn: bpy.props.StringProperty(name='ZColumn', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_XColumnIndex: bpy.props.IntProperty(name='XColumnIndex', default=-1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_XComponent: bpy.props.IntProperty(name='XComponent', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_YColumnIndex: bpy.props.IntProperty(name='YColumnIndex', default=-1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_YComponent: bpy.props.IntProperty(name='YComponent', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ZColumnIndex: bpy.props.IntProperty(name='ZColumnIndex', default=-1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ZComponent: bpy.props.IntProperty(name='ZComponent', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Create2DPoints','m_PreserveCoordinateColumnsAsDataArrays','m_ObjectName','m_XColumn','m_YColumn','m_ZColumn','m_XColumnIndex','m_XComponent','m_YColumnIndex','m_YComponent','m_ZColumnIndex','m_ZComponent',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTableToPolyData )        
TYPENAMES.append('VTKTableToPolyDataType' )

#--------------------------------------------------------------
class VTKTableToStructuredGrid(Node, PBVTK_Node):

    bl_idname = 'VTKTableToStructuredGridType'
    bl_label  = 'vtkTableToStructuredGrid'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_XColumn: bpy.props.StringProperty(name='XColumn', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_YColumn: bpy.props.StringProperty(name='YColumn', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ZColumn: bpy.props.StringProperty(name='ZColumn', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_XComponent: bpy.props.IntProperty(name='XComponent', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_YComponent: bpy.props.IntProperty(name='YComponent', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ZComponent: bpy.props.IntProperty(name='ZComponent', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_XColumn','m_YColumn','m_ZColumn','m_XComponent','m_YComponent','m_ZComponent',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTableToStructuredGrid )        
TYPENAMES.append('VTKTableToStructuredGridType' )

#--------------------------------------------------------------
class VTKTemporalArrayOperatorFilter(Node, PBVTK_Node):

    bl_idname = 'VTKTemporalArrayOperatorFilterType'
    bl_label  = 'vtkTemporalArrayOperatorFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RelativeMode: bpy.props.BoolProperty(name='RelativeMode', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputArrayNameSuffix: bpy.props.StringProperty(name='OutputArrayNameSuffix', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FirstTimeStepIndex: bpy.props.IntProperty(name='FirstTimeStepIndex', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Operator: bpy.props.IntProperty(name='Operator', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SecondTimeStepIndex: bpy.props.IntProperty(name='SecondTimeStepIndex', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TimeStepShift: bpy.props.IntProperty(name='TimeStepShift', default=-1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_RelativeMode','m_ObjectName','m_OutputArrayNameSuffix','m_FirstTimeStepIndex','m_Operator','m_SecondTimeStepIndex','m_TimeStepShift',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTemporalArrayOperatorFilter )        
TYPENAMES.append('VTKTemporalArrayOperatorFilterType' )

#--------------------------------------------------------------
class VTKTemporalDataSetCache(Node, PBVTK_Node):

    bl_idname = 'VTKTemporalDataSetCacheType'
    bl_label  = 'vtkTemporalDataSetCache'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CacheInMemkind: bpy.props.BoolProperty(name='CacheInMemkind', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IsASource: bpy.props.BoolProperty(name='IsASource', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CacheSize: bpy.props.IntProperty(name='CacheSize', default=10, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CacheInMemkind','m_IsASource','m_ObjectName','m_CacheSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTemporalDataSetCache )        
TYPENAMES.append('VTKTemporalDataSetCacheType' )

#--------------------------------------------------------------
class VTKTemporalInterpolator(Node, PBVTK_Node):

    bl_idname = 'VTKTemporalInterpolatorType'
    bl_label  = 'vtkTemporalInterpolator'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CacheData: bpy.props.BoolProperty(name='CacheData', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ResampleFactor: bpy.props.IntProperty(name='ResampleFactor', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DiscreteTimeStepInterval: bpy.props.FloatProperty(name='DiscreteTimeStepInterval', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CacheData','m_ObjectName','m_ResampleFactor','m_DiscreteTimeStepInterval',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTemporalInterpolator )        
TYPENAMES.append('VTKTemporalInterpolatorType' )

#--------------------------------------------------------------
class VTKTemporalShiftScale(Node, PBVTK_Node):

    bl_idname = 'VTKTemporalShiftScaleType'
    bl_label  = 'vtkTemporalShiftScale'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Periodic: bpy.props.BoolProperty(name='Periodic', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PeriodicEndCorrection: bpy.props.BoolProperty(name='PeriodicEndCorrection', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumNumberOfPeriods: bpy.props.FloatProperty(name='MaximumNumberOfPeriods', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PostShift: bpy.props.FloatProperty(name='PostShift', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PreShift: bpy.props.FloatProperty(name='PreShift', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Scale: bpy.props.FloatProperty(name='Scale', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Periodic','m_PeriodicEndCorrection','m_ObjectName','m_MaximumNumberOfPeriods','m_PostShift','m_PreShift','m_Scale',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTemporalShiftScale )        
TYPENAMES.append('VTKTemporalShiftScaleType' )

#--------------------------------------------------------------
class VTKTemporalSmoothing(Node, PBVTK_Node):

    bl_idname = 'VTKTemporalSmoothingType'
    bl_label  = 'vtkTemporalSmoothing'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TemporalWindowHalfWidth: bpy.props.IntProperty(name='TemporalWindowHalfWidth', default=10, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_TemporalWindowHalfWidth',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTemporalSmoothing )        
TYPENAMES.append('VTKTemporalSmoothingType' )

#--------------------------------------------------------------
class VTKTemporalSnapToTimeStep(Node, PBVTK_Node):

    bl_idname = 'VTKTemporalSnapToTimeStepType'
    bl_label  = 'vtkTemporalSnapToTimeStep'
    e_SnapMode_items=[ (x,x,x) for x in ['Nearest', 'NextBelowOrEqual', 'NextAboveOrEqual']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SnapMode: bpy.props.EnumProperty(name='SnapMode', default="Nearest", items=e_SnapMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','e_SnapMode',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTemporalSnapToTimeStep )        
TYPENAMES.append('VTKTemporalSnapToTimeStepType' )

#--------------------------------------------------------------
class VTKTemporalStatistics(Node, PBVTK_Node):

    bl_idname = 'VTKTemporalStatisticsType'
    bl_label  = 'vtkTemporalStatistics'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeAverage: bpy.props.BoolProperty(name='ComputeAverage', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeMaximum: bpy.props.BoolProperty(name='ComputeMaximum', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeMinimum: bpy.props.BoolProperty(name='ComputeMinimum', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeStandardDeviation: bpy.props.BoolProperty(name='ComputeStandardDeviation', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeAverage','m_ComputeMaximum','m_ComputeMinimum','m_ComputeStandardDeviation','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTemporalStatistics )        
TYPENAMES.append('VTKTemporalStatisticsType' )

#--------------------------------------------------------------
class VTKTensorPrincipalInvariants(Node, PBVTK_Node):

    bl_idname = 'VTKTensorPrincipalInvariantsType'
    bl_label  = 'vtkTensorPrincipalInvariants'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScaleVectors: bpy.props.BoolProperty(name='ScaleVectors', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ScaleVectors','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTensorPrincipalInvariants )        
TYPENAMES.append('VTKTensorPrincipalInvariantsType' )

#--------------------------------------------------------------
class VTKTessellatorFilter(Node, PBVTK_Node):

    bl_idname = 'VTKTessellatorFilterType'
    bl_label  = 'vtkTessellatorFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MergePoints: bpy.props.BoolProperty(name='MergePoints', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumNumberOfSubdivisions: bpy.props.IntProperty(name='MaximumNumberOfSubdivisions', default=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutputDimension: bpy.props.IntProperty(name='OutputDimension', default=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ChordError: bpy.props.FloatProperty(name='ChordError', default=0.001, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_MergePoints','m_ObjectName','m_MaximumNumberOfSubdivisions','m_OutputDimension','m_ChordError',]
    def m_connections( self ):
        return (['input'], ['output'], ['Subdivider', 'Tessellator', 'ContainerAlgorithm'], []) 
    
add_class( VTKTessellatorFilter )        
TYPENAMES.append('VTKTessellatorFilterType' )

#--------------------------------------------------------------
class VTKTextureMapToCylinder(Node, PBVTK_Node):

    bl_idname = 'VTKTextureMapToCylinderType'
    bl_label  = 'vtkTextureMapToCylinder'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AutomaticCylinderGeneration: bpy.props.BoolProperty(name='AutomaticCylinderGeneration', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PreventSeam: bpy.props.BoolProperty(name='PreventSeam', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Point1: bpy.props.FloatVectorProperty(name='Point1', default=[0.0, 0.0, -0.5], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Point2: bpy.props.FloatVectorProperty(name='Point2', default=[0.0, 0.0, 0.5], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AutomaticCylinderGeneration','m_PreventSeam','m_ObjectName','m_Point1','m_Point2',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTextureMapToCylinder )        
TYPENAMES.append('VTKTextureMapToCylinderType' )

#--------------------------------------------------------------
class VTKTextureMapToPlane(Node, PBVTK_Node):

    bl_idname = 'VTKTextureMapToPlaneType'
    bl_label  = 'vtkTextureMapToPlane'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AutomaticPlaneGeneration: bpy.props.BoolProperty(name='AutomaticPlaneGeneration', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Normal: bpy.props.FloatVectorProperty(name='Normal', default=[0.0, 0.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Origin: bpy.props.FloatVectorProperty(name='Origin', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Point1: bpy.props.FloatVectorProperty(name='Point1', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Point2: bpy.props.FloatVectorProperty(name='Point2', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SRange: bpy.props.FloatVectorProperty(name='SRange', default=[0.0, 1.0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TRange: bpy.props.FloatVectorProperty(name='TRange', default=[0.0, 1.0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AutomaticPlaneGeneration','m_ObjectName','m_Normal','m_Origin','m_Point1','m_Point2','m_SRange','m_TRange',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTextureMapToPlane )        
TYPENAMES.append('VTKTextureMapToPlaneType' )

#--------------------------------------------------------------
class VTKTextureMapToSphere(Node, PBVTK_Node):

    bl_idname = 'VTKTextureMapToSphereType'
    bl_label  = 'vtkTextureMapToSphere'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AutomaticSphereGeneration: bpy.props.BoolProperty(name='AutomaticSphereGeneration', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PreventSeam: bpy.props.BoolProperty(name='PreventSeam', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AutomaticSphereGeneration','m_PreventSeam','m_ObjectName','m_Center',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTextureMapToSphere )        
TYPENAMES.append('VTKTextureMapToSphereType' )

#--------------------------------------------------------------
class VTKThreshold(Node, PBVTK_Node):

    bl_idname = 'VTKThresholdType'
    bl_label  = 'vtkThreshold'
    e_ComponentMode_items=[ (x,x,x) for x in ['UseSelected', 'UseAll', 'UseAny']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AllScalars: bpy.props.BoolProperty(name='AllScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Invert: bpy.props.BoolProperty(name='Invert', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseContinuousCellRange: bpy.props.BoolProperty(name='UseContinuousCellRange', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SelectedComponent: bpy.props.IntProperty(name='SelectedComponent', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ThresholdFunction: bpy.props.IntProperty(name='ThresholdFunction', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LowerThreshold: bpy.props.FloatProperty(name='LowerThreshold', default=-1e+30, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UpperThreshold: bpy.props.FloatProperty(name='UpperThreshold', default=1e+30, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ComponentMode: bpy.props.EnumProperty(name='ComponentMode', default="UseSelected", items=e_ComponentMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AllScalars','m_Invert','m_UseContinuousCellRange','m_ObjectName','m_SelectedComponent','m_ThresholdFunction','m_LowerThreshold','m_UpperThreshold','e_ComponentMode',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKThreshold )        
TYPENAMES.append('VTKThresholdType' )

#--------------------------------------------------------------
class VTKThresholdPoints(Node, PBVTK_Node):

    bl_idname = 'VTKThresholdPointsType'
    bl_label  = 'vtkThresholdPoints'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InputArrayComponent: bpy.props.IntProperty(name='InputArrayComponent', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LowerThreshold: bpy.props.FloatProperty(name='LowerThreshold', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UpperThreshold: bpy.props.FloatProperty(name='UpperThreshold', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_InputArrayComponent','m_LowerThreshold','m_UpperThreshold',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKThresholdPoints )        
TYPENAMES.append('VTKThresholdPointsType' )

#--------------------------------------------------------------
class VTKThresholdTextureCoords(Node, PBVTK_Node):

    bl_idname = 'VTKThresholdTextureCoordsType'
    bl_label  = 'vtkThresholdTextureCoords'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TextureDimension: bpy.props.IntProperty(name='TextureDimension', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InTextureCoord: bpy.props.FloatVectorProperty(name='InTextureCoord', default=[0.75, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OutTextureCoord: bpy.props.FloatVectorProperty(name='OutTextureCoord', default=[0.25, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_TextureDimension','m_InTextureCoord','m_OutTextureCoord',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKThresholdTextureCoords )        
TYPENAMES.append('VTKThresholdTextureCoordsType' )

#--------------------------------------------------------------
class VTKToImplicitArrayFilter(Node, PBVTK_Node):

    bl_idname = 'VTKToImplicitArrayFilterType'
    bl_label  = 'vtkToImplicitArrayFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseMaxNumberOfDegreesOfFreedom: bpy.props.BoolProperty(name='UseMaxNumberOfDegreesOfFreedom', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaxNumberOfDegreesOfFreedom: bpy.props.IntProperty(name='MaxNumberOfDegreesOfFreedom', default=100, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TargetReduction: bpy.props.FloatProperty(name='TargetReduction', default=0.1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_UseMaxNumberOfDegreesOfFreedom','m_ObjectName','m_MaxNumberOfDegreesOfFreedom','m_TargetReduction',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'Strategy'], []) 
    
add_class( VTKToImplicitArrayFilter )        
TYPENAMES.append('VTKToImplicitArrayFilterType' )

#--------------------------------------------------------------
class VTKTransformCoordinateSystems(Node, PBVTK_Node):

    bl_idname = 'VTKTransformCoordinateSystemsType'
    bl_label  = 'vtkTransformCoordinateSystems'
    e_InputCoordinateSystem_items=[ (x,x,x) for x in ['Display', 'Viewport', 'World']]
    e_OutputCoordinateSystem_items=[ (x,x,x) for x in ['Display', 'Viewport', 'World']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_InputCoordinateSystem: bpy.props.EnumProperty(name='InputCoordinateSystem', default="World", items=e_InputCoordinateSystem_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_OutputCoordinateSystem: bpy.props.EnumProperty(name='OutputCoordinateSystem', default="Display", items=e_OutputCoordinateSystem_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','e_InputCoordinateSystem','e_OutputCoordinateSystem',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'Viewport'], []) 
    
add_class( VTKTransformCoordinateSystems )        
TYPENAMES.append('VTKTransformCoordinateSystemsType' )

#--------------------------------------------------------------
class VTKTransformFilter(Node, PBVTK_Node):

    bl_idname = 'VTKTransformFilterType'
    bl_label  = 'vtkTransformFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TransformAllInputVectors: bpy.props.BoolProperty(name='TransformAllInputVectors', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_TransformAllInputVectors','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'Transform'], []) 
    
add_class( VTKTransformFilter )        
TYPENAMES.append('VTKTransformFilterType' )

#--------------------------------------------------------------
class VTKTransformPolyDataFilter(Node, PBVTK_Node):

    bl_idname = 'VTKTransformPolyDataFilterType'
    bl_label  = 'vtkTransformPolyDataFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'Transform'], []) 
    
add_class( VTKTransformPolyDataFilter )        
TYPENAMES.append('VTKTransformPolyDataFilterType' )

#--------------------------------------------------------------
class VTKTransformTextureCoords(Node, PBVTK_Node):

    bl_idname = 'VTKTransformTextureCoordsType'
    bl_label  = 'vtkTransformTextureCoords'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FlipR: bpy.props.BoolProperty(name='FlipR', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FlipS: bpy.props.BoolProperty(name='FlipS', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FlipT: bpy.props.BoolProperty(name='FlipT', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Origin: bpy.props.FloatVectorProperty(name='Origin', default=[0.5, 0.5, 0.5], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Position: bpy.props.FloatVectorProperty(name='Position', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Scale: bpy.props.FloatVectorProperty(name='Scale', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FlipR','m_FlipS','m_FlipT','m_ObjectName','m_Origin','m_Position','m_Scale',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTransformTextureCoords )        
TYPENAMES.append('VTKTransformTextureCoordsType' )

#--------------------------------------------------------------
class VTKTransmitImageDataPiece(Node, PBVTK_Node):

    bl_idname = 'VTKTransmitImageDataPieceType'
    bl_label  = 'vtkTransmitImageDataPiece'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CreateGhostCells: bpy.props.BoolProperty(name='CreateGhostCells', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CreateGhostCells','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTransmitImageDataPiece )        
TYPENAMES.append('VTKTransmitImageDataPieceType' )

#--------------------------------------------------------------
class VTKTransmitPolyDataPiece(Node, PBVTK_Node):

    bl_idname = 'VTKTransmitPolyDataPieceType'
    bl_label  = 'vtkTransmitPolyDataPiece'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CreateGhostCells: bpy.props.BoolProperty(name='CreateGhostCells', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CreateGhostCells','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTransmitPolyDataPiece )        
TYPENAMES.append('VTKTransmitPolyDataPieceType' )

#--------------------------------------------------------------
class VTKTransmitRectilinearGridPiece(Node, PBVTK_Node):

    bl_idname = 'VTKTransmitRectilinearGridPieceType'
    bl_label  = 'vtkTransmitRectilinearGridPiece'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CreateGhostCells: bpy.props.BoolProperty(name='CreateGhostCells', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CreateGhostCells','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTransmitRectilinearGridPiece )        
TYPENAMES.append('VTKTransmitRectilinearGridPieceType' )

#--------------------------------------------------------------
class VTKTransmitStructuredDataPiece(Node, PBVTK_Node):

    bl_idname = 'VTKTransmitStructuredDataPieceType'
    bl_label  = 'vtkTransmitStructuredDataPiece'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CreateGhostCells: bpy.props.BoolProperty(name='CreateGhostCells', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CreateGhostCells','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTransmitStructuredDataPiece )        
TYPENAMES.append('VTKTransmitStructuredDataPieceType' )

#--------------------------------------------------------------
class VTKTransmitStructuredGridPiece(Node, PBVTK_Node):

    bl_idname = 'VTKTransmitStructuredGridPieceType'
    bl_label  = 'vtkTransmitStructuredGridPiece'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CreateGhostCells: bpy.props.BoolProperty(name='CreateGhostCells', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CreateGhostCells','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTransmitStructuredGridPiece )        
TYPENAMES.append('VTKTransmitStructuredGridPieceType' )

#--------------------------------------------------------------
class VTKTransmitUnstructuredGridPiece(Node, PBVTK_Node):

    bl_idname = 'VTKTransmitUnstructuredGridPieceType'
    bl_label  = 'vtkTransmitUnstructuredGridPiece'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CreateGhostCells: bpy.props.BoolProperty(name='CreateGhostCells', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CreateGhostCells','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTransmitUnstructuredGridPiece )        
TYPENAMES.append('VTKTransmitUnstructuredGridPieceType' )

#--------------------------------------------------------------
class VTKTransposeTable(Node, PBVTK_Node):

    bl_idname = 'VTKTransposeTableType'
    bl_label  = 'vtkTransposeTable'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AddIdColumn: bpy.props.BoolProperty(name='AddIdColumn', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseIdColumn: bpy.props.BoolProperty(name='UseIdColumn', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IdColumnName: bpy.props.StringProperty(name='IdColumnName', default="ColName", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AddIdColumn','m_UseIdColumn','m_IdColumnName','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTransposeTable )        
TYPENAMES.append('VTKTransposeTableType' )

#--------------------------------------------------------------
class VTKTreeAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKTreeAlgorithmType'
    bl_label  = 'vtkTreeAlgorithm'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTreeAlgorithm )        
TYPENAMES.append('VTKTreeAlgorithmType' )

#--------------------------------------------------------------
class VTKTriangleFilter(Node, PBVTK_Node):

    bl_idname = 'VTKTriangleFilterType'
    bl_label  = 'vtkTriangleFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassLines: bpy.props.BoolProperty(name='PassLines', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassVerts: bpy.props.BoolProperty(name='PassVerts', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PreservePolys: bpy.props.BoolProperty(name='PreservePolys', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Tolerance: bpy.props.FloatProperty(name='Tolerance', default=-1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_PassLines','m_PassVerts','m_PreservePolys','m_ObjectName','m_Tolerance',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTriangleFilter )        
TYPENAMES.append('VTKTriangleFilterType' )

#--------------------------------------------------------------
class VTKTriangleMeshPointNormals(Node, PBVTK_Node):

    bl_idname = 'VTKTriangleMeshPointNormalsType'
    bl_label  = 'vtkTriangleMeshPointNormals'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTriangleMeshPointNormals )        
TYPENAMES.append('VTKTriangleMeshPointNormalsType' )

#--------------------------------------------------------------
class VTKTriangularTCoords(Node, PBVTK_Node):

    bl_idname = 'VTKTriangularTCoordsType'
    bl_label  = 'vtkTriangularTCoords'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTriangularTCoords )        
TYPENAMES.append('VTKTriangularTCoordsType' )

#--------------------------------------------------------------
class VTKTubeBender(Node, PBVTK_Node):

    bl_idname = 'VTKTubeBenderType'
    bl_label  = 'vtkTubeBender'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Radius: bpy.props.FloatProperty(name='Radius', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_Radius',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTubeBender )        
TYPENAMES.append('VTKTubeBenderType' )

#--------------------------------------------------------------
class VTKTubeFilter(Node, PBVTK_Node):

    bl_idname = 'VTKTubeFilterType'
    bl_label  = 'vtkTubeFilter'
    e_GenerateTCoords_items=[ (x,x,x) for x in ['Off', 'NormalizedLength', 'UseLength', 'UseScalars']]
    e_VaryRadius_items=[ (x,x,x) for x in ['VaryRadiusOff', 'VaryRadiusByScalar', 'VaryRadiusByVector', 'VaryRadiusByAbsoluteScalar', 'VaryRadiusByVectorNorm']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Capping: bpy.props.BoolProperty(name='Capping', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SidesShareVertices: bpy.props.BoolProperty(name='SidesShareVertices', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseDefaultNormal: bpy.props.BoolProperty(name='UseDefaultNormal', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfSides: bpy.props.IntProperty(name='NumberOfSides', default=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Offset: bpy.props.IntProperty(name='Offset', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OnRatio: bpy.props.IntProperty(name='OnRatio', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Radius: bpy.props.FloatProperty(name='Radius', default=0.5, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_RadiusFactor: bpy.props.FloatProperty(name='RadiusFactor', default=10.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TextureLength: bpy.props.FloatProperty(name='TextureLength', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_GenerateTCoords: bpy.props.EnumProperty(name='GenerateTCoords', default="Off", items=e_GenerateTCoords_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_VaryRadius: bpy.props.EnumProperty(name='VaryRadius', default="VaryRadiusOff", items=e_VaryRadius_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DefaultNormal: bpy.props.FloatVectorProperty(name='DefaultNormal', default=[0.0, 0.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=14, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Capping','m_SidesShareVertices','m_UseDefaultNormal','m_ObjectName','m_NumberOfSides','m_Offset','m_OnRatio','m_Radius','m_RadiusFactor','m_TextureLength','e_GenerateTCoords','e_VaryRadius','m_DefaultNormal',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKTubeFilter )        
TYPENAMES.append('VTKTubeFilterType' )

#--------------------------------------------------------------
class VTKUncertaintyTubeFilter(Node, PBVTK_Node):

    bl_idname = 'VTKUncertaintyTubeFilterType'
    bl_label  = 'vtkUncertaintyTubeFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfSides: bpy.props.IntProperty(name='NumberOfSides', default=12, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_NumberOfSides',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKUncertaintyTubeFilter )        
TYPENAMES.append('VTKUncertaintyTubeFilterType' )

#--------------------------------------------------------------
class VTKUndirectedGraphAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKUndirectedGraphAlgorithmType'
    bl_label  = 'vtkUndirectedGraphAlgorithm'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKUndirectedGraphAlgorithm )        
TYPENAMES.append('VTKUndirectedGraphAlgorithmType' )

#--------------------------------------------------------------
class VTKUniformGridAMRAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKUniformGridAMRAlgorithmType'
    bl_label  = 'vtkUniformGridAMRAlgorithm'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKUniformGridAMRAlgorithm )        
TYPENAMES.append('VTKUniformGridAMRAlgorithmType' )

#--------------------------------------------------------------
class VTKUniformGridPartitioner(Node, PBVTK_Node):

    bl_idname = 'VTKUniformGridPartitionerType'
    bl_label  = 'vtkUniformGridPartitioner'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DuplicateNodes: bpy.props.BoolProperty(name='DuplicateNodes', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfGhostLayers: bpy.props.IntProperty(name='NumberOfGhostLayers', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfPartitions: bpy.props.IntProperty(name='NumberOfPartitions', default=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_DuplicateNodes','m_ObjectName','m_NumberOfGhostLayers','m_NumberOfPartitions',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKUniformGridPartitioner )        
TYPENAMES.append('VTKUniformGridPartitionerType' )

#--------------------------------------------------------------
class VTKUnsignedDistance(Node, PBVTK_Node):

    bl_idname = 'VTKUnsignedDistanceType'
    bl_label  = 'vtkUnsignedDistance'
    e_OutputScalarType_items=[ (x,x,x) for x in ['Float', 'Double']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AdjustBounds: bpy.props.BoolProperty(name='AdjustBounds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Capping: bpy.props.BoolProperty(name='Capping', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AdjustDistance: bpy.props.FloatProperty(name='AdjustDistance', default=0.0125, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CapValue: bpy.props.FloatProperty(name='CapValue', default=1e+30, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Radius: bpy.props.FloatProperty(name='Radius', default=0.1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_OutputScalarType: bpy.props.EnumProperty(name='OutputScalarType', default="Float", items=e_OutputScalarType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Dimensions: bpy.props.IntVectorProperty(name='Dimensions', default=[256, 256, 256], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Bounds: bpy.props.FloatVectorProperty(name='Bounds', default=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AdjustBounds','m_Capping','m_ObjectName','m_AdjustDistance','m_CapValue','m_Radius','e_OutputScalarType','m_Dimensions','m_Bounds',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKUnsignedDistance )        
TYPENAMES.append('VTKUnsignedDistanceType' )

#--------------------------------------------------------------
class VTKUnstructuredGridAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKUnstructuredGridAlgorithmType'
    bl_label  = 'vtkUnstructuredGridAlgorithm'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKUnstructuredGridAlgorithm )        
TYPENAMES.append('VTKUnstructuredGridAlgorithmType' )

#--------------------------------------------------------------
class VTKUnstructuredGridBaseAlgorithm(Node, PBVTK_Node):

    bl_idname = 'VTKUnstructuredGridBaseAlgorithmType'
    bl_label  = 'vtkUnstructuredGridBaseAlgorithm'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKUnstructuredGridBaseAlgorithm )        
TYPENAMES.append('VTKUnstructuredGridBaseAlgorithmType' )

#--------------------------------------------------------------
class VTKUnstructuredGridGeometryFilter(Node, PBVTK_Node):

    bl_idname = 'VTKUnstructuredGridGeometryFilterType'
    bl_label  = 'vtkUnstructuredGridGeometryFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CellClipping: bpy.props.BoolProperty(name='CellClipping', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DuplicateGhostCellClipping: bpy.props.BoolProperty(name='DuplicateGhostCellClipping', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ExtentClipping: bpy.props.BoolProperty(name='ExtentClipping', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Merging: bpy.props.BoolProperty(name='Merging', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassThroughCellIds: bpy.props.BoolProperty(name='PassThroughCellIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassThroughPointIds: bpy.props.BoolProperty(name='PassThroughPointIds', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PointClipping: bpy.props.BoolProperty(name='PointClipping', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OriginalCellIdsName: bpy.props.StringProperty(name='OriginalCellIdsName', default="vtkOriginalCellIds", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OriginalPointIdsName: bpy.props.StringProperty(name='OriginalPointIdsName', default="vtkOriginalPointIds", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CellMaximum: bpy.props.IntProperty(name='CellMaximum', default=1000000000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CellMinimum: bpy.props.IntProperty(name='CellMinimum', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MatchBoundariesIgnoringCellOrder: bpy.props.IntProperty(name='MatchBoundariesIgnoringCellOrder', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PointMaximum: bpy.props.IntProperty(name='PointMaximum', default=1000000000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PointMinimum: bpy.props.IntProperty(name='PointMinimum', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=16, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CellClipping','m_DuplicateGhostCellClipping','m_ExtentClipping','m_Merging','m_PassThroughCellIds','m_PassThroughPointIds','m_PointClipping','m_ObjectName','m_OriginalCellIdsName','m_OriginalPointIdsName','m_CellMaximum','m_CellMinimum','m_MatchBoundariesIgnoringCellOrder','m_PointMaximum','m_PointMinimum',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKUnstructuredGridGeometryFilter )        
TYPENAMES.append('VTKUnstructuredGridGeometryFilterType' )

#--------------------------------------------------------------
class VTKUnstructuredGridQuadricDecimation(Node, PBVTK_Node):

    bl_idname = 'VTKUnstructuredGridQuadricDecimationType'
    bl_label  = 'vtkUnstructuredGridQuadricDecimation'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarsName: bpy.props.StringProperty(name='ScalarsName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AutoAddCandidates: bpy.props.IntProperty(name='AutoAddCandidates', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfCandidates: bpy.props.IntProperty(name='NumberOfCandidates', default=8, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfEdgesToDecimate: bpy.props.IntProperty(name='NumberOfEdgesToDecimate', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfTetsOutput: bpy.props.IntProperty(name='NumberOfTetsOutput', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AutoAddCandidatesThreshold: bpy.props.FloatProperty(name='AutoAddCandidatesThreshold', default=0.4, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BoundaryWeight: bpy.props.FloatProperty(name='BoundaryWeight', default=100.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TargetReduction: bpy.props.FloatProperty(name='TargetReduction', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=10, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_ScalarsName','m_AutoAddCandidates','m_NumberOfCandidates','m_NumberOfEdgesToDecimate','m_NumberOfTetsOutput','m_AutoAddCandidatesThreshold','m_BoundaryWeight','m_TargetReduction',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKUnstructuredGridQuadricDecimation )        
TYPENAMES.append('VTKUnstructuredGridQuadricDecimationType' )

#--------------------------------------------------------------
class VTKUnstructuredGridToCellGrid(Node, PBVTK_Node):

    bl_idname = 'VTKUnstructuredGridToCellGridType'
    bl_label  = 'vtkUnstructuredGridToCellGrid'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKUnstructuredGridToCellGrid )        
TYPENAMES.append('VTKUnstructuredGridToCellGridType' )

#--------------------------------------------------------------
class VTKUnstructuredGridToExplicitStructuredGrid(Node, PBVTK_Node):

    bl_idname = 'VTKUnstructuredGridToExplicitStructuredGridType'
    bl_label  = 'vtkUnstructuredGridToExplicitStructuredGrid'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKUnstructuredGridToExplicitStructuredGrid )        
TYPENAMES.append('VTKUnstructuredGridToExplicitStructuredGridType' )

#--------------------------------------------------------------
class VTKVectorDot(Node, PBVTK_Node):

    bl_idname = 'VTKVectorDotType'
    bl_label  = 'vtkVectorDot'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MapScalars: bpy.props.BoolProperty(name='MapScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarRange: bpy.props.FloatVectorProperty(name='ScalarRange', default=[-1.0, 1.0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_MapScalars','m_ObjectName','m_ScalarRange',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKVectorDot )        
TYPENAMES.append('VTKVectorDotType' )

#--------------------------------------------------------------
class VTKVectorNorm(Node, PBVTK_Node):

    bl_idname = 'VTKVectorNormType'
    bl_label  = 'vtkVectorNorm'
    e_AttributeMode_items=[ (x,x,x) for x in ['Default', 'UsePointData', 'UseCellData']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Normalize: bpy.props.BoolProperty(name='Normalize', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_AttributeMode: bpy.props.EnumProperty(name='AttributeMode', default="Default", items=e_AttributeMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Normalize','m_ObjectName','e_AttributeMode',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKVectorNorm )        
TYPENAMES.append('VTKVectorNormType' )

#--------------------------------------------------------------
class VTKVertexGlyphFilter(Node, PBVTK_Node):

    bl_idname = 'VTKVertexGlyphFilterType'
    bl_label  = 'vtkVertexGlyphFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKVertexGlyphFilter )        
TYPENAMES.append('VTKVertexGlyphFilterType' )

#--------------------------------------------------------------
class VTKVolumeOfRevolutionFilter(Node, PBVTK_Node):

    bl_idname = 'VTKVolumeOfRevolutionFilterType'
    bl_label  = 'vtkVolumeOfRevolutionFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Resolution: bpy.props.IntProperty(name='Resolution', default=12, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SweepAngle: bpy.props.FloatProperty(name='SweepAngle', default=360.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AxisDirection: bpy.props.FloatVectorProperty(name='AxisDirection', default=[0.0, 0.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AxisPosition: bpy.props.FloatVectorProperty(name='AxisPosition', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_Resolution','m_SweepAngle','m_AxisDirection','m_AxisPosition',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKVolumeOfRevolutionFilter )        
TYPENAMES.append('VTKVolumeOfRevolutionFilterType' )

#--------------------------------------------------------------
class VTKVolumeRayCastSpaceLeapingImageFilter(Node, PBVTK_Node):

    bl_idname = 'VTKVolumeRayCastSpaceLeapingImageFilterType'
    bl_label  = 'vtkVolumeRayCastSpaceLeapingImageFilter'
    e_SplitMode_items=[ (x,x,x) for x in ['Slab', 'Beam', 'Block']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeGradientOpacity: bpy.props.BoolProperty(name='ComputeGradientOpacity', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeMinMax: bpy.props.BoolProperty(name='ComputeMinMax', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EnableSMP: bpy.props.BoolProperty(name='EnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GlobalDefaultEnableSMP: bpy.props.BoolProperty(name='GlobalDefaultEnableSMP', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UpdateGradientOpacityFlags: bpy.props.BoolProperty(name='UpdateGradientOpacityFlags', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DesiredBytesPerPiece: bpy.props.IntProperty(name='DesiredBytesPerPiece', default=65536, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IndependentComponents: bpy.props.IntProperty(name='IndependentComponents', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfThreads: bpy.props.IntProperty(name='NumberOfThreads', default=32, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SplitMode: bpy.props.EnumProperty(name='SplitMode', default="Slab", items=e_SplitMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MinimumPieceSize: bpy.props.IntVectorProperty(name='MinimumPieceSize', default=[16, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TableSize: bpy.props.IntVectorProperty(name='TableSize', default=[0, 0, 0, 0], size=4, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TableScale: bpy.props.FloatVectorProperty(name='TableScale', default=[1.0, 1.0, 1.0, 1.0], size=4, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TableShift: bpy.props.FloatVectorProperty(name='TableShift', default=[0.0, 0.0, 0.0, 0.0], size=4, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=15, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeGradientOpacity','m_ComputeMinMax','m_EnableSMP','m_GlobalDefaultEnableSMP','m_UpdateGradientOpacityFlags','m_ObjectName','m_DesiredBytesPerPiece','m_IndependentComponents','m_NumberOfThreads','e_SplitMode','m_MinimumPieceSize','m_TableSize','m_TableScale','m_TableShift',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'CurrentScalars'], []) 
    
add_class( VTKVolumeRayCastSpaceLeapingImageFilter )        
TYPENAMES.append('VTKVolumeRayCastSpaceLeapingImageFilterType' )

#--------------------------------------------------------------
class VTKVortexCore(Node, PBVTK_Node):

    bl_idname = 'VTKVortexCoreType'
    bl_label  = 'vtkVortexCore'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FasterApproximation: bpy.props.BoolProperty(name='FasterApproximation', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HigherOrderMethod: bpy.props.BoolProperty(name='HigherOrderMethod', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_FasterApproximation','m_HigherOrderMethod','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKVortexCore )        
TYPENAMES.append('VTKVortexCoreType' )

#--------------------------------------------------------------
class VTKVoxelContoursToSurfaceFilter(Node, PBVTK_Node):

    bl_idname = 'VTKVoxelContoursToSurfaceFilterType'
    bl_label  = 'vtkVoxelContoursToSurfaceFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MemoryLimitInBytes: bpy.props.IntProperty(name='MemoryLimitInBytes', default=10000000, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Spacing: bpy.props.FloatVectorProperty(name='Spacing', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=4, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_MemoryLimitInBytes','m_Spacing',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKVoxelContoursToSurfaceFilter )        
TYPENAMES.append('VTKVoxelContoursToSurfaceFilterType' )

#--------------------------------------------------------------
class VTKVoxelGrid(Node, PBVTK_Node):

    bl_idname = 'VTKVoxelGridType'
    bl_label  = 'vtkVoxelGrid'
    e_ConfigurationStyle_items=[ (x,x,x) for x in ['Manual', 'LeafSize', 'Automatic']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfPointsPerBin: bpy.props.IntProperty(name='NumberOfPointsPerBin', default=10, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ConfigurationStyle: bpy.props.EnumProperty(name='ConfigurationStyle', default="Automatic", items=e_ConfigurationStyle_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Divisions: bpy.props.IntVectorProperty(name='Divisions', default=[50, 50, 50], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LeafSize: bpy.props.FloatVectorProperty(name='LeafSize', default=[1.0, 1.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_NumberOfPointsPerBin','e_ConfigurationStyle','m_Divisions','m_LeafSize',]
    def m_connections( self ):
        return (['input'], ['output'], ['Kernel', 'ContainerAlgorithm'], []) 
    
add_class( VTKVoxelGrid )        
TYPENAMES.append('VTKVoxelGridType' )

#--------------------------------------------------------------
class VTKVoxelModeller(Node, PBVTK_Node):

    bl_idname = 'VTKVoxelModellerType'
    bl_label  = 'vtkVoxelModeller'
    e_ScalarType_items=[ (x,x,x) for x in ['Bit', 'Char', 'UnsignedChar', 'Short', 'UnsignedShort', 'Int', 'UnsignedInt', 'Long', 'UnsignedLong', 'Float', 'Double']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BackgroundValue: bpy.props.FloatProperty(name='BackgroundValue', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ForegroundValue: bpy.props.FloatProperty(name='ForegroundValue', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_MaximumDistance: bpy.props.FloatProperty(name='MaximumDistance', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ScalarType: bpy.props.EnumProperty(name='ScalarType', default="Bit", items=e_ScalarType_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SampleDimensions: bpy.props.IntVectorProperty(name='SampleDimensions', default=[50, 50, 50], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_BackgroundValue','m_ForegroundValue','m_MaximumDistance','e_ScalarType','m_SampleDimensions',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKVoxelModeller )        
TYPENAMES.append('VTKVoxelModellerType' )

#--------------------------------------------------------------
class VTKWarpLens(Node, PBVTK_Node):

    bl_idname = 'VTKWarpLensType'
    bl_label  = 'vtkWarpLens'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ImageHeight: bpy.props.IntProperty(name='ImageHeight', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ImageWidth: bpy.props.IntProperty(name='ImageWidth', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FormatHeight: bpy.props.FloatProperty(name='FormatHeight', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FormatWidth: bpy.props.FloatProperty(name='FormatWidth', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_K1: bpy.props.FloatProperty(name='K1', default=-1e-06, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_K2: bpy.props.FloatProperty(name='K2', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Kappa: bpy.props.FloatProperty(name='Kappa', default=-1e-06, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_P1: bpy.props.FloatProperty(name='P1', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_P2: bpy.props.FloatProperty(name='P2', default=0.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Center: bpy.props.FloatVectorProperty(name='Center', default=[0.0, 0.0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PrincipalPoint: bpy.props.FloatVectorProperty(name='PrincipalPoint', default=[0.0, 0.0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=13, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_ImageHeight','m_ImageWidth','m_FormatHeight','m_FormatWidth','m_K1','m_K2','m_Kappa','m_P1','m_P2','m_Center','m_PrincipalPoint',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKWarpLens )        
TYPENAMES.append('VTKWarpLensType' )

#--------------------------------------------------------------
class VTKWarpScalar(Node, PBVTK_Node):

    bl_idname = 'VTKWarpScalarType'
    bl_label  = 'vtkWarpScalar'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateEnclosure: bpy.props.BoolProperty(name='GenerateEnclosure', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseNormal: bpy.props.BoolProperty(name='UseNormal', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_XYPlane: bpy.props.BoolProperty(name='XYPlane', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScaleFactor: bpy.props.FloatProperty(name='ScaleFactor', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Normal: bpy.props.FloatVectorProperty(name='Normal', default=[0.0, 0.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_GenerateEnclosure','m_UseNormal','m_XYPlane','m_ObjectName','m_ScaleFactor','m_Normal',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKWarpScalar )        
TYPENAMES.append('VTKWarpScalarType' )

#--------------------------------------------------------------
class VTKWarpTo(Node, PBVTK_Node):

    bl_idname = 'VTKWarpToType'
    bl_label  = 'vtkWarpTo'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Absolute: bpy.props.BoolProperty(name='Absolute', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScaleFactor: bpy.props.FloatProperty(name='ScaleFactor', default=0.5, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Position: bpy.props.FloatVectorProperty(name='Position', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_Absolute','m_ObjectName','m_ScaleFactor','m_Position',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKWarpTo )        
TYPENAMES.append('VTKWarpToType' )

#--------------------------------------------------------------
class VTKWarpVector(Node, PBVTK_Node):

    bl_idname = 'VTKWarpVectorType'
    bl_label  = 'vtkWarpVector'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScaleFactor: bpy.props.FloatProperty(name='ScaleFactor', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_ScaleFactor',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKWarpVector )        
TYPENAMES.append('VTKWarpVectorType' )

#--------------------------------------------------------------
class VTKWeightedTransformFilter(Node, PBVTK_Node):

    bl_idname = 'VTKWeightedTransformFilterType'
    bl_label  = 'vtkWeightedTransformFilter'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AddInputValues: bpy.props.BoolProperty(name='AddInputValues', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CellDataTransformIndexArray: bpy.props.StringProperty(name='CellDataTransformIndexArray', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CellDataWeightArray: bpy.props.StringProperty(name='CellDataWeightArray', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_TransformIndexArray: bpy.props.StringProperty(name='TransformIndexArray', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_WeightArray: bpy.props.StringProperty(name='WeightArray', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfTransforms: bpy.props.IntProperty(name='NumberOfTransforms', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=8, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AddInputValues','m_CellDataTransformIndexArray','m_CellDataWeightArray','m_ObjectName','m_TransformIndexArray','m_WeightArray','m_NumberOfTransforms',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKWeightedTransformFilter )        
TYPENAMES.append('VTKWeightedTransformFilterType' )

#--------------------------------------------------------------
class VTKWindowedSincPolyDataFilter(Node, PBVTK_Node):

    bl_idname = 'VTKWindowedSincPolyDataFilterType'
    bl_label  = 'vtkWindowedSincPolyDataFilter'
    e_WindowFunction_items=[ (x,x,x) for x in ['Nuttall', 'Blackman', 'Hamming']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_BoundarySmoothing: bpy.props.BoolProperty(name='BoundarySmoothing', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FeatureEdgeSmoothing: bpy.props.BoolProperty(name='FeatureEdgeSmoothing', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateErrorScalars: bpy.props.BoolProperty(name='GenerateErrorScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateErrorVectors: bpy.props.BoolProperty(name='GenerateErrorVectors', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NonManifoldSmoothing: bpy.props.BoolProperty(name='NonManifoldSmoothing', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NormalizeCoordinates: bpy.props.BoolProperty(name='NormalizeCoordinates', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_WeightNonManifoldEdges: bpy.props.BoolProperty(name='WeightNonManifoldEdges', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfIterations: bpy.props.IntProperty(name='NumberOfIterations', default=20, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_EdgeAngle: bpy.props.FloatProperty(name='EdgeAngle', default=15.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FeatureAngle: bpy.props.FloatProperty(name='FeatureAngle', default=45.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassBand: bpy.props.FloatProperty(name='PassBand', default=0.1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_WindowFunction: bpy.props.EnumProperty(name='WindowFunction', default="Nuttall", items=e_WindowFunction_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=14, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_BoundarySmoothing','m_FeatureEdgeSmoothing','m_GenerateErrorScalars','m_GenerateErrorVectors','m_NonManifoldSmoothing','m_NormalizeCoordinates','m_WeightNonManifoldEdges','m_ObjectName','m_NumberOfIterations','m_EdgeAngle','m_FeatureAngle','m_PassBand','e_WindowFunction',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKWindowedSincPolyDataFilter )        
TYPENAMES.append('VTKWindowedSincPolyDataFilterType' )

#--------------------------------------------------------------
class VTKYieldCriteria(Node, PBVTK_Node):

    bl_idname = 'VTKYieldCriteriaType'
    bl_label  = 'vtkYieldCriteria'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScaleVectors: bpy.props.BoolProperty(name='ScaleVectors', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ScaleVectors','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKYieldCriteria )        
TYPENAMES.append('VTKYieldCriteriaType' )

#--------------------------------------------------------------
class VTKYoungsMaterialInterface(Node, PBVTK_Node):

    bl_idname = 'VTKYoungsMaterialInterfaceType'
    bl_label  = 'vtkYoungsMaterialInterface'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AxisSymetric: bpy.props.BoolProperty(name='AxisSymetric', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FillMaterial: bpy.props.BoolProperty(name='FillMaterial', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_InverseNormal: bpy.props.BoolProperty(name='InverseNormal', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_OnionPeel: bpy.props.BoolProperty(name='OnionPeel', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReverseMaterialOrder: bpy.props.BoolProperty(name='ReverseMaterialOrder', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseAllBlocks: bpy.props.BoolProperty(name='UseAllBlocks', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseFractionAsDistance: bpy.props.BoolProperty(name='UseFractionAsDistance', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfMaterials: bpy.props.IntProperty(name='NumberOfMaterials', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VolumeFractionRange: bpy.props.FloatVectorProperty(name='VolumeFractionRange', default=[0.01, 0.99], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AxisSymetric','m_FillMaterial','m_InverseNormal','m_OnionPeel','m_ReverseMaterialOrder','m_UseAllBlocks','m_UseFractionAsDistance','m_ObjectName','m_NumberOfMaterials','m_VolumeFractionRange',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKYoungsMaterialInterface )        
TYPENAMES.append('VTKYoungsMaterialInterfaceType' )

#--------------------------------------------------------------
class VTKmAverageToCells(Node, PBVTK_Node):

    bl_idname = 'VTKmAverageToCellsType'
    bl_label  = 'vtkmAverageToCells'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CategoricalData: bpy.props.BoolProperty(name='CategoricalData', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassPointData: bpy.props.BoolProperty(name='PassPointData', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ProcessAllArrays: bpy.props.BoolProperty(name='ProcessAllArrays', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CategoricalData','m_PassPointData','m_ProcessAllArrays','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKmAverageToCells )        
TYPENAMES.append('VTKmAverageToCellsType' )

#--------------------------------------------------------------
class VTKmAverageToPoints(Node, PBVTK_Node):

    bl_idname = 'VTKmAverageToPointsType'
    bl_label  = 'vtkmAverageToPoints'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PassCellData: bpy.props.BoolProperty(name='PassCellData', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_PieceInvariant: bpy.props.BoolProperty(name='PieceInvariant', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ProcessAllArrays: bpy.props.BoolProperty(name='ProcessAllArrays', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ContributingCellOption: bpy.props.IntProperty(name='ContributingCellOption', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_PassCellData','m_PieceInvariant','m_ProcessAllArrays','m_ObjectName','m_ContributingCellOption',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKmAverageToPoints )        
TYPENAMES.append('VTKmAverageToPointsType' )

#--------------------------------------------------------------
class VTKmCleanGrid(Node, PBVTK_Node):

    bl_idname = 'VTKmCleanGridType'
    bl_label  = 'vtkmCleanGrid'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CompactPoints: bpy.props.BoolProperty(name='CompactPoints', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CompactPoints','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKmCleanGrid )        
TYPENAMES.append('VTKmCleanGridType' )

#--------------------------------------------------------------
class VTKmContour(Node, PBVTK_Node):

    bl_idname = 'VTKmContourType'
    bl_label  = 'vtkmContour'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeGradients: bpy.props.BoolProperty(name='ComputeGradients', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeNormals: bpy.props.BoolProperty(name='ComputeNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeScalars: bpy.props.BoolProperty(name='ComputeScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FastMode: bpy.props.BoolProperty(name='FastMode', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateTriangles: bpy.props.BoolProperty(name='GenerateTriangles', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ArrayComponent: bpy.props.IntProperty(name='ArrayComponent', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfContours: bpy.props.IntProperty(name='NumberOfContours', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=9, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeGradients','m_ComputeNormals','m_ComputeScalars','m_FastMode','m_GenerateTriangles','m_ObjectName','m_ArrayComponent','m_NumberOfContours',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKmContour )        
TYPENAMES.append('VTKmContourType' )

#--------------------------------------------------------------
class VTKmCoordinateSystemTransform(Node, PBVTK_Node):

    bl_idname = 'VTKmCoordinateSystemTransformType'
    bl_label  = 'vtkmCoordinateSystemTransform'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKmCoordinateSystemTransform )        
TYPENAMES.append('VTKmCoordinateSystemTransformType' )

#--------------------------------------------------------------
class VTKmExternalFaces(Node, PBVTK_Node):

    bl_idname = 'VTKmExternalFacesType'
    bl_label  = 'vtkmExternalFaces'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CompactPoints: bpy.props.BoolProperty(name='CompactPoints', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CompactPoints','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKmExternalFaces )        
TYPENAMES.append('VTKmExternalFacesType' )

#--------------------------------------------------------------
class VTKmExtractVOI(Node, PBVTK_Node):

    bl_idname = 'VTKmExtractVOIType'
    bl_label  = 'vtkmExtractVOI'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ForceVTKm: bpy.props.BoolProperty(name='ForceVTKm', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_IncludeBoundary: bpy.props.BoolProperty(name='IncludeBoundary', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SampleRate: bpy.props.IntVectorProperty(name='SampleRate', default=[1, 1, 1], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VOI: bpy.props.IntVectorProperty(name='VOI', default=[0, 1000000000, 0, 1000000000, 0, 1000000000], size=6, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ForceVTKm','m_IncludeBoundary','m_ObjectName','m_SampleRate','m_VOI',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKmExtractVOI )        
TYPENAMES.append('VTKmExtractVOIType' )

#--------------------------------------------------------------
class VTKmGradient(Node, PBVTK_Node):

    bl_idname = 'VTKmGradientType'
    bl_label  = 'vtkmGradient'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeDivergence: bpy.props.BoolProperty(name='ComputeDivergence', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeGradient: bpy.props.BoolProperty(name='ComputeGradient', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeQCriterion: bpy.props.BoolProperty(name='ComputeQCriterion', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeVorticity: bpy.props.BoolProperty(name='ComputeVorticity', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FasterApproximation: bpy.props.BoolProperty(name='FasterApproximation', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ForceVTKm: bpy.props.BoolProperty(name='ForceVTKm', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_DivergenceArrayName: bpy.props.StringProperty(name='DivergenceArrayName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_QCriterionArrayName: bpy.props.StringProperty(name='QCriterionArrayName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ResultArrayName: bpy.props.StringProperty(name='ResultArrayName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_VorticityArrayName: bpy.props.StringProperty(name='VorticityArrayName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ContributingCellOption: bpy.props.IntProperty(name='ContributingCellOption', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ReplacementValueOption: bpy.props.IntProperty(name='ReplacementValueOption', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=14, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ComputeDivergence','m_ComputeGradient','m_ComputeQCriterion','m_ComputeVorticity','m_FasterApproximation','m_ForceVTKm','m_DivergenceArrayName','m_ObjectName','m_QCriterionArrayName','m_ResultArrayName','m_VorticityArrayName','m_ContributingCellOption','m_ReplacementValueOption',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKmGradient )        
TYPENAMES.append('VTKmGradientType' )

#--------------------------------------------------------------
class VTKmHistogram(Node, PBVTK_Node):

    bl_idname = 'VTKmHistogramType'
    bl_label  = 'vtkmHistogram'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CenterBinsAroundMinAndMax: bpy.props.BoolProperty(name='CenterBinsAroundMinAndMax', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseCustomBinRanges: bpy.props.BoolProperty(name='UseCustomBinRanges', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfBins: bpy.props.IntProperty(name='NumberOfBins', default=10, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_CustomBinRange: bpy.props.FloatVectorProperty(name='CustomBinRange', default=[100.0, 0.01], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_CenterBinsAroundMinAndMax','m_UseCustomBinRanges','m_ObjectName','m_NumberOfBins','m_CustomBinRange',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKmHistogram )        
TYPENAMES.append('VTKmHistogramType' )

#--------------------------------------------------------------
class VTKmImageConnectivity(Node, PBVTK_Node):

    bl_idname = 'VTKmImageConnectivityType'
    bl_label  = 'vtkmImageConnectivity'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKmImageConnectivity )        
TYPENAMES.append('VTKmImageConnectivityType' )

#--------------------------------------------------------------
class VTKmLevelOfDetail(Node, PBVTK_Node):

    bl_idname = 'VTKmLevelOfDetailType'
    bl_label  = 'vtkmLevelOfDetail'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfXDivisions: bpy.props.IntProperty(name='NumberOfXDivisions', default=512, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfYDivisions: bpy.props.IntProperty(name='NumberOfYDivisions', default=512, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfZDivisions: bpy.props.IntProperty(name='NumberOfZDivisions', default=512, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=5, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_NumberOfXDivisions','m_NumberOfYDivisions','m_NumberOfZDivisions',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKmLevelOfDetail )        
TYPENAMES.append('VTKmLevelOfDetailType' )

#--------------------------------------------------------------
class VTKmNDHistogram(Node, PBVTK_Node):

    bl_idname = 'VTKmNDHistogramType'
    bl_label  = 'vtkmNDHistogram'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKmNDHistogram )        
TYPENAMES.append('VTKmNDHistogramType' )

#--------------------------------------------------------------
class VTKmPointElevation(Node, PBVTK_Node):

    bl_idname = 'VTKmPointElevationType'
    bl_label  = 'vtkmPointElevation'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ForceVTKm: bpy.props.BoolProperty(name='ForceVTKm', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_HighPoint: bpy.props.FloatVectorProperty(name='HighPoint', default=[0.0, 0.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LowPoint: bpy.props.FloatVectorProperty(name='LowPoint', default=[0.0, 0.0, 0.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScalarRange: bpy.props.FloatVectorProperty(name='ScalarRange', default=[0.0, 1.0], size=2, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ForceVTKm','m_ObjectName','m_HighPoint','m_LowPoint','m_ScalarRange',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKmPointElevation )        
TYPENAMES.append('VTKmPointElevationType' )

#--------------------------------------------------------------
class VTKmPointTransform(Node, PBVTK_Node):

    bl_idname = 'VTKmPointTransformType'
    bl_label  = 'vtkmPointTransform'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=2, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'Transform'], []) 
    
add_class( VTKmPointTransform )        
TYPENAMES.append('VTKmPointTransformType' )

#--------------------------------------------------------------
class VTKmPolyDataNormals(Node, PBVTK_Node):

    bl_idname = 'VTKmPolyDataNormalsType'
    bl_label  = 'vtkmPolyDataNormals'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AutoOrientNormals: bpy.props.BoolProperty(name='AutoOrientNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputeCellNormals: bpy.props.BoolProperty(name='ComputeCellNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ComputePointNormals: bpy.props.BoolProperty(name='ComputePointNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Consistency: bpy.props.BoolProperty(name='Consistency', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FlipNormals: bpy.props.BoolProperty(name='FlipNormals', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ForceVTKm: bpy.props.BoolProperty(name='ForceVTKm', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NonManifoldTraversal: bpy.props.BoolProperty(name='NonManifoldTraversal', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Splitting: bpy.props.BoolProperty(name='Splitting', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_FeatureAngle: bpy.props.FloatProperty(name='FeatureAngle', default=30.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AutoOrientNormals','m_ComputeCellNormals','m_ComputePointNormals','m_Consistency','m_FlipNormals','m_ForceVTKm','m_NonManifoldTraversal','m_Splitting','m_ObjectName','m_FeatureAngle',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKmPolyDataNormals )        
TYPENAMES.append('VTKmPolyDataNormalsType' )

#--------------------------------------------------------------
class VTKmSlice(Node, PBVTK_Node):

    bl_idname = 'VTKmSliceType'
    bl_label  = 'vtkmSlice'
    e_SortBy_items=[ (x,x,x) for x in ['SortByValue', 'SortByCell']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateCutScalars: bpy.props.BoolProperty(name='GenerateCutScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateTriangles: bpy.props.BoolProperty(name='GenerateTriangles', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_NumberOfContours: bpy.props.IntProperty(name='NumberOfContours', default=1, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_SortBy: bpy.props.EnumProperty(name='SortBy', default="SortByValue", items=e_SortBy_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=6, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_GenerateCutScalars','m_GenerateTriangles','m_ObjectName','m_NumberOfContours','e_SortBy',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm', 'CutFunction'], []) 
    
add_class( VTKmSlice )        
TYPENAMES.append('VTKmSliceType' )

#--------------------------------------------------------------
class VTKmThreshold(Node, PBVTK_Node):

    bl_idname = 'VTKmThresholdType'
    bl_label  = 'vtkmThreshold'
    e_ComponentMode_items=[ (x,x,x) for x in ['UseSelected', 'UseAll', 'UseAny']]
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_AllScalars: bpy.props.BoolProperty(name='AllScalars', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ForceVTKm: bpy.props.BoolProperty(name='ForceVTKm', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Invert: bpy.props.BoolProperty(name='Invert', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseContinuousCellRange: bpy.props.BoolProperty(name='UseContinuousCellRange', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_SelectedComponent: bpy.props.IntProperty(name='SelectedComponent', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ThresholdFunction: bpy.props.IntProperty(name='ThresholdFunction', default=0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_LowerThreshold: bpy.props.FloatProperty(name='LowerThreshold', default=-1e+30, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UpperThreshold: bpy.props.FloatProperty(name='UpperThreshold', default=1e+30, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    e_ComponentMode: bpy.props.EnumProperty(name='ComponentMode', default="UseSelected", items=e_ComponentMode_items, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=11, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_AllScalars','m_ForceVTKm','m_Invert','m_UseContinuousCellRange','m_ObjectName','m_SelectedComponent','m_ThresholdFunction','m_LowerThreshold','m_UpperThreshold','e_ComponentMode',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKmThreshold )        
TYPENAMES.append('VTKmThresholdType' )

#--------------------------------------------------------------
class VTKmTriangleMeshPointNormals(Node, PBVTK_Node):

    bl_idname = 'VTKmTriangleMeshPointNormalsType'
    bl_label  = 'vtkmTriangleMeshPointNormals'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ForceVTKm: bpy.props.BoolProperty(name='ForceVTKm', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ForceVTKm','m_ObjectName',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKmTriangleMeshPointNormals )        
TYPENAMES.append('VTKmTriangleMeshPointNormalsType' )

#--------------------------------------------------------------
class VTKmWarpScalar(Node, PBVTK_Node):

    bl_idname = 'VTKmWarpScalarType'
    bl_label  = 'vtkmWarpScalar'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_GenerateEnclosure: bpy.props.BoolProperty(name='GenerateEnclosure', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_UseNormal: bpy.props.BoolProperty(name='UseNormal', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_XYPlane: bpy.props.BoolProperty(name='XYPlane', default=True, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScaleFactor: bpy.props.FloatProperty(name='ScaleFactor', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_Normal: bpy.props.FloatVectorProperty(name='Normal', default=[0.0, 0.0, 1.0], size=3, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=7, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_GenerateEnclosure','m_UseNormal','m_XYPlane','m_ObjectName','m_ScaleFactor','m_Normal',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKmWarpScalar )        
TYPENAMES.append('VTKmWarpScalarType' )

#--------------------------------------------------------------
class VTKmWarpVector(Node, PBVTK_Node):

    bl_idname = 'VTKmWarpVectorType'
    bl_label  = 'vtkmWarpVector'
    
    m_AbortOutput: bpy.props.BoolProperty(name='AbortOutput', default=False, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ObjectName: bpy.props.StringProperty(name='ObjectName', default="", update=PBVTK_Node.outdate_vtk_status) #type: ignore
    m_ScaleFactor: bpy.props.FloatProperty(name='ScaleFactor', default=1.0, update=PBVTK_Node.outdate_vtk_status) #type: ignore
    
    b_properties: bpy.props.BoolVectorProperty(name="", size=3, get=PBVTK_Node.get_b, set=PBVTK_Node.set_b) #type: ignore

    def m_properties( self ):
        return ['m_AbortOutput','m_ObjectName','m_ScaleFactor',]
    def m_connections( self ):
        return (['input'], ['output'], ['ContainerAlgorithm'], []) 
    
add_class( VTKmWarpVector )        
TYPENAMES.append('VTKmWarpVectorType' )

#--------------------------------------------------------------
menu_items = [ NodeItem(x) for x in TYPENAMES ]
CATEGORIES.append( PBVTK_NodeCategory( 'Filter1', 'Filter1', items=menu_items) )