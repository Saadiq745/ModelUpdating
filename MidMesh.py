from abaqus import *
from abaqusConstants import *
from odbAccess import *
import __main__
import section
import regionToolset
import displayGroupMdbToolset as dgm
import part
import material
import assembly
import step
import interaction
import load
import mesh
import optimization
import job
import sketch
import visualization
import xyPlot
import displayGroupOdbToolset as dgo
import connectorBehavior
import numpy as np
import os
from driverUtils import executeOnCaeStartup
import xyPlot
rho_1 = 2.71e-9
rho_2 = 2.71e-9
rho_3 = 2.71e-9
rho_4 = 2.71e-9
rho_5 = 2.71e-9
#
E_1 = 69e3
E_2 = 69e3
E_3 = 69e3
E_4 = 69e3
E_5 = 69e3
#  
Thickness_1 = 5.0
Thickness_2 = 5.0
Thickness_3 = 5.0
Thickness_4 = 5.0
Thickness_5 = 5.0
#
#
session.Viewport(name='Viewport: 1', origin=(0.0, 0.0), width=116.682289123535, 
    height=215.951843261719)
session.viewports['Viewport: 1'].makeCurrent()
session.viewports['Viewport: 1'].maximize()
executeOnCaeStartup()
#: A new model database has been created.
#: The model "Model-1" has been created.
session.viewports['Viewport: 1'].setValues(displayedObject=None)
step = mdb.openStep('C:/Users/Saadiq Ahmed/Desktop/Mid.stp', scaleFromFile=OFF)
mdb.models['Model-1'].PartFromGeometryFile(name='Mid', geometryFile=step, 
    combine=True, dimensionality=THREE_D, type=DEFORMABLE_BODY)
p = mdb.models['Model-1'].parts['Mid']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON)
session.viewports['Viewport: 1'].partDisplay.geometryOptions.setValues(
    referenceRepresentation=OFF)
mdb.models['Model-1'].Material(name='Mat-1')
mdb.models['Model-1'].materials['Mat-1'].Density(table=((rho_1, ), ))
mdb.models['Model-1'].materials['Mat-1'].Elastic(table=((E_1, 0.3), ))
mdb.models['Model-1'].Material(name='Mat-2')
mdb.models['Model-1'].materials['Mat-2'].Density(table=((rho_2, ), ))
mdb.models['Model-1'].materials['Mat-2'].Elastic(table=((E_2, 0.3), ))
mdb.models['Model-1'].Material(name='Mat-3')
mdb.models['Model-1'].materials['Mat-3'].Density(table=((rho_3, ), ))
mdb.models['Model-1'].materials['Mat-3'].Elastic(table=((E_3, 0.3), ))
mdb.models['Model-1'].Material(name='Mat-4')
mdb.models['Model-1'].materials['Mat-4'].Density(table=((rho_4, ), ))
mdb.models['Model-1'].materials['Mat-4'].Elastic(table=((E_4, 0.3), ))
mdb.models['Model-1'].Material(name='Mat-5')
mdb.models['Model-1'].materials['Mat-5'].Density(table=((rho_5, ), ))
mdb.models['Model-1'].materials['Mat-5'].Elastic(table=((E_5, 0.3), ))
p = mdb.models['Model-1'].parts['Mid']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#4 ]', ), )
v, e, d = p.vertices, p.edges, p.datums
p.PartitionFaceByShortestPath(point1=v[22], point2=v[19], faces=pickedFaces)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1054.05, 
    farPlane=1553.83, width=373.681, height=194.082, viewOffsetX=-28.4477, 
    viewOffsetY=19.1041)
p = mdb.models['Model-1'].parts['Mid']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#8 ]', ), )
v1, e1, d1 = p.vertices, p.edges, p.datums
p.PartitionFaceByShortestPath(point1=v1[18], point2=v1[23], faces=pickedFaces)
p = mdb.models['Model-1'].parts['Mid']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#10 ]', ), )
v, e, d = p.vertices, p.edges, p.datums
p.PartitionFaceByShortestPath(point1=v[20], point2=v[23], faces=pickedFaces)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1067.25, 
    farPlane=1540.63, width=255.311, height=132.603, viewOffsetX=18.2222, 
    viewOffsetY=-7.07427)
p = mdb.models['Model-1'].parts['Mid']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#20 ]', ), )
v1, e1, d1 = p.vertices, p.edges, p.datums
p.PartitionFaceByShortestPath(point1=v1[10], point2=v1[22], faces=pickedFaces)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1046.73, 
    farPlane=1561.15, width=494.572, height=256.87, viewOffsetX=-16.3561, 
    viewOffsetY=27.9476)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1043.89, 
    farPlane=1563.99, width=493.229, height=256.173, viewOffsetX=22.5107, 
    viewOffsetY=13.8247)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1049.42, 
    farPlane=1664.43, width=495.844, height=257.531, cameraPosition=(1102.31, 
    9.59663, -757.488), cameraUpVector=(-0.280128, 0.924312, 0.259184), 
    cameraTarget=(31.5793, -52.61, -15.9159), viewOffsetX=22.63, 
    viewOffsetY=13.898)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1097.53, 
    farPlane=1621.35, width=518.575, height=269.337, cameraPosition=(868.657, 
    72.8532, -1021.02), cameraUpVector=(-0.34126, 0.903939, 0.257752), 
    cameraTarget=(29.8075, -45.6427, -29.7774), viewOffsetX=23.6674, 
    viewOffsetY=14.5351)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1115.96, 
    farPlane=1602.93, width=302.129, height=156.92, viewOffsetX=-20.2361, 
    viewOffsetY=13.8721)
p = mdb.models['Model-1'].parts['Mid']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#20 ]', ), )
v, e, d = p.vertices, p.edges, p.datums
p.PartitionFaceByShortestPath(point1=v[13], point2=v[14], faces=pickedFaces)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1115.96, 
    farPlane=1602.93, width=302.129, height=156.92, viewOffsetX=-2.99847, 
    viewOffsetY=9.04644)
p = mdb.models['Model-1'].parts['Mid']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#1 ]', ), )
v1, e1, d1 = p.vertices, p.edges, p.datums
p.PartitionFaceByShortestPath(point1=v1[2], point2=v1[9], faces=pickedFaces)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1109.15, 
    farPlane=1609.74, width=409.165, height=212.512, viewOffsetX=-2.98997, 
    viewOffsetY=27.9247)
p = mdb.models['Model-1'].parts['Mid']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#2 ]', ), )
v, e, d = p.vertices, p.edges, p.datums
p.PartitionFaceByShortestPath(point1=v[4], point2=v[9], faces=pickedFaces)
p = mdb.models['Model-1'].parts['Mid']
f = p.faces
pickedFaces = f.getSequenceFromMask(mask=('[#4 ]', ), )
v1, e1, d1 = p.vertices, p.edges, p.datums
p.PartitionFaceByShortestPath(point1=v1[6], point2=v1[9], faces=pickedFaces)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1084.56, 
    farPlane=1634.33, width=656.354, height=340.897, viewOffsetX=-51.5339, 
    viewOffsetY=38.8702)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1262.62, 
    farPlane=1563.53, width=764.11, height=396.863, cameraPosition=(334.103, 
    -352.83, 1334.68), cameraUpVector=(-0.146802, 0.985851, -0.0809084), 
    cameraTarget=(113.655, -47.2196, 86.366), viewOffsetX=-59.9945, 
    viewOffsetY=45.2517)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1171.03, 
    farPlane=1765.01, width=708.683, height=368.075, cameraPosition=(965.214, 
    599.376, 887.841), cameraUpVector=(-0.46157, 0.694197, -0.552308), 
    cameraTarget=(155.337, 18.2101, 47.2288), viewOffsetX=-55.6426, 
    viewOffsetY=41.9692)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1198.91, 
    farPlane=1737.13, width=470.508, height=244.372, viewOffsetX=-35.3628, 
    viewOffsetY=13.0534)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=OFF, 
    engineeringFeatures=OFF, mesh=ON)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=ON)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1187.97, 
    farPlane=1748.07, width=637.847, height=332.281, viewOffsetX=-15.0994, 
    viewOffsetY=16.9984)
p = mdb.models['Model-1'].parts['Mid']
p.seedPart(size=1.0, deviationFactor=0.1, minSizeFactor=0.1)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1191.6, 
    farPlane=1744.44, width=601.413, height=313.301, viewOffsetX=-7.22463, 
    viewOffsetY=13.8467)
p = mdb.models['Model-1'].parts['Mid']
f = p.faces
pickedRegions = f.getSequenceFromMask(mask=('[#7fff ]', ), )
p.setMeshControls(regions=pickedRegions, technique=SWEEP)
p = mdb.models['Model-1'].parts['Mid']
p.generateMesh()
session.viewports['Viewport: 1'].view.setValues(nearPlane=1200.93, 
    farPlane=1735.11, width=541.217, height=281.942, viewOffsetX=26.1383, 
    viewOffsetY=106.503)
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    optimizationTasks=OFF, geometricRestrictions=OFF, stopConditions=OFF)
a = mdb.models['Model-1'].rootAssembly
a.DatumCsysByDefault(CARTESIAN)
p = mdb.models['Model-1'].parts['Mid']
a.Instance(name='Mid-1', part=p, dependent=ON)
session.viewports['Viewport: 1'].partDisplay.setValues(sectionAssignments=ON, 
    engineeringFeatures=ON, mesh=OFF)
session.viewports['Viewport: 1'].partDisplay.meshOptions.setValues(
    meshTechnique=OFF)
p = mdb.models['Model-1'].parts['Mid']
session.viewports['Viewport: 1'].setValues(displayedObject=p)
mdb.models['Model-1'].HomogeneousShellSection(name='Section-1', 
    preIntegrate=OFF, material='Mat-1', thicknessType=UNIFORM, thickness=1.0, 
    thicknessField='', nodalThicknessField='', idealization=NO_IDEALIZATION, 
    poissonDefinition=DEFAULT, thicknessModulus=None, temperature=GRADIENT, 
    useDensity=OFF, integrationRule=SIMPSON, numIntPts=5)
mdb.models['Model-1'].HomogeneousShellSection(name='Section-2', 
    preIntegrate=OFF, material='Mat-2', thicknessType=UNIFORM, thickness=1.0, 
    thicknessField='', nodalThicknessField='', idealization=NO_IDEALIZATION, 
    poissonDefinition=DEFAULT, thicknessModulus=None, temperature=GRADIENT, 
    useDensity=OFF, integrationRule=SIMPSON, numIntPts=5)
mdb.models['Model-1'].HomogeneousShellSection(name='Section-3', 
    preIntegrate=OFF, material='Mat-3', thicknessType=UNIFORM, thickness=1.0, 
    thicknessField='', nodalThicknessField='', idealization=NO_IDEALIZATION, 
    poissonDefinition=DEFAULT, thicknessModulus=None, temperature=GRADIENT, 
    useDensity=OFF, integrationRule=SIMPSON, numIntPts=5)
mdb.models['Model-1'].HomogeneousShellSection(name='Section-4', 
    preIntegrate=OFF, material='Mat-4', thicknessType=UNIFORM, thickness=1.0, 
    thicknessField='', nodalThicknessField='', idealization=NO_IDEALIZATION, 
    poissonDefinition=DEFAULT, thicknessModulus=None, temperature=GRADIENT, 
    useDensity=OFF, integrationRule=SIMPSON, numIntPts=5)
mdb.models['Model-1'].HomogeneousShellSection(name='Section-5', 
    preIntegrate=OFF, material='Mat-5', thicknessType=UNIFORM, thickness=1.0, 
    thicknessField='', nodalThicknessField='', idealization=NO_IDEALIZATION, 
    poissonDefinition=DEFAULT, thicknessModulus=None, temperature=GRADIENT, 
    useDensity=OFF, integrationRule=SIMPSON, numIntPts=5)
#Section thickness
mdb.models['Model-1'].sections['Section-1'].setValues(preIntegrate=OFF, 
    material='Mat-1', thicknessType=UNIFORM, thickness=Thickness_1, thicknessField='', 
    nodalThicknessField='', idealization=NO_IDEALIZATION, 
    integrationRule=SIMPSON, numIntPts=5)
mdb.models['Model-1'].sections['Section-2'].setValues(preIntegrate=OFF, 
    material='Mat-2', thicknessType=UNIFORM, thickness=Thickness_2, thicknessField='', 
    nodalThicknessField='', idealization=NO_IDEALIZATION, 
    integrationRule=SIMPSON, numIntPts=5)
mdb.models['Model-1'].sections['Section-3'].setValues(preIntegrate=OFF, 
    material='Mat-3', thicknessType=UNIFORM, thickness=Thickness_3, thicknessField='', 
    nodalThicknessField='', idealization=NO_IDEALIZATION, 
    integrationRule=SIMPSON, numIntPts=5)
mdb.models['Model-1'].sections['Section-4'].setValues(preIntegrate=OFF, 
    material='Mat-4', thicknessType=UNIFORM, thickness=Thickness_4, thicknessField='', 
    nodalThicknessField='', idealization=NO_IDEALIZATION, 
    integrationRule=SIMPSON, numIntPts=5)
mdb.models['Model-1'].sections['Section-5'].setValues(preIntegrate=OFF, 
    material='Mat-5', thicknessType=UNIFORM, thickness=Thickness_5, thicknessField='', 
    nodalThicknessField='', idealization=NO_IDEALIZATION, 
    integrationRule=SIMPSON, numIntPts=5)
#Section thickness Ends
session.viewports['Viewport: 1'].view.setValues(nearPlane=1165.59, 
    farPlane=1770.45, width=864.332, height=448.916, viewOffsetX=77.6612, 
    viewOffsetY=150.009)
p = mdb.models['Model-1'].parts['Mid']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#888 ]', ), )
region = p.Set(faces=faces, name='Set-2')
p = mdb.models['Model-1'].parts['Mid']
p.SectionAssignment(region=region, sectionName='Section-1', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['Mid']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#4041 ]', ), )
region = p.Set(faces=faces, name='Set-3')
p = mdb.models['Model-1'].parts['Mid']
p.SectionAssignment(region=region, sectionName='Section-2', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['Mid']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#1022 ]', ), )
region = p.Set(faces=faces, name='Set-4')
p = mdb.models['Model-1'].parts['Mid']
p.SectionAssignment(region=region, sectionName='Section-3', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1038.85, 
    farPlane=1416.73, width=770.352, height=400.105, cameraPosition=(-312.527, 
    -479.977, 1112.93), cameraUpVector=(-0.0908976, 0.991728, -0.0906266), 
    cameraTarget=(-22.8233, -126.757, -108.376), viewOffsetX=69.2169, 
    viewOffsetY=133.699)
session.viewports['Viewport: 1'].view.setValues(nearPlane=979.953, 
    farPlane=1523.13, width=726.677, height=377.421, cameraPosition=(-728.674, 
    642.68, 792.83), cameraUpVector=(0.461591, 0.528507, -0.71247), 
    cameraTarget=(-64.7613, -165.081, 13.7123), viewOffsetX=65.2927, 
    viewOffsetY=126.119)
session.viewports['Viewport: 1'].view.setValues(nearPlane=1017.03, 
    farPlane=1497.01, width=754.171, height=391.701, cameraPosition=(-606.012, 
    658.256, 882.856), cameraUpVector=(0.399681, 0.522351, -0.753263), 
    cameraTarget=(-70.3631, -161.354, 21.6934), viewOffsetX=67.763, 
    viewOffsetY=130.891)
p = mdb.models['Model-1'].parts['Mid']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#2404 ]', ), )
region = p.Set(faces=faces, name='Set-5')
p = mdb.models['Model-1'].parts['Mid']
p.SectionAssignment(region=region, sectionName='Section-4', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
p = mdb.models['Model-1'].parts['Mid']
f = p.faces
faces = f.getSequenceFromMask(mask=('[#310 ]', ), )
region = p.Set(faces=faces, name='Set-6')
p = mdb.models['Model-1'].parts['Mid']
p.SectionAssignment(region=region, sectionName='Section-5', offset=0.0, 
    offsetType=MIDDLE_SURFACE, offsetField='', 
    thicknessAssignment=FROM_SECTION)
a = mdb.models['Model-1'].rootAssembly
a.regenerate()
a = mdb.models['Model-1'].rootAssembly
session.viewports['Viewport: 1'].setValues(displayedObject=a)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
mdb.models['Model-1'].FrequencyStep(name='Step-1', previous='Initial', 
    numEigen=26)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(step='Step-1')
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(
    adaptiveMeshConstraints=ON)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=ON, bcs=ON, 
    predefinedFields=ON, connectors=ON, adaptiveMeshConstraints=OFF)
session.viewports['Viewport: 1'].assemblyDisplay.setValues(loads=OFF, bcs=OFF, 
    predefinedFields=OFF, connectors=OFF)
mdb.Job(name='Job-2', model='Model-1', description='', type=ANALYSIS, 
    atTime=None, waitMinutes=0, waitHours=0, queue=None, memory=90, 
    memoryUnits=PERCENTAGE, getMemoryFromAnalysis=True, 
    explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, echoPrint=OFF, 
    modelPrint=OFF, contactPrint=OFF, historyPrint=OFF, userSubroutine='', 
    scratch='', resultsFormat=ODB, multiprocessingMode=DEFAULT, numCpus=1, 
    numGPUs=0)
mdb.jobs['Job-2'].submit(consistencyChecking=OFF)
mdb.jobs['Job-2'].writeInput(consistencyChecking=OFF)
mdb.jobs['Job-2'].waitForCompletion()
#: The job input file "Job-2.inp" has been submitted for analysis.
#: Job Job-2: Analysis Input File Processor completed successfully.
#: Job Job-2: Abaqus/Standard completed successfully.
#: Job Job-2 completed successfully. 
odb = openOdb('Job-2.odb')
xy1 = xyPlot.XYDataFromHistory(name='EIGFREQ Whole Model-1', odb=odb, 
    outputVariableName='Eigenfrequency: EIGFREQ for Whole Model', steps=(
    'Step-1', ), __linkedVpName__='Viewport: 1')
c1 = session.Curve(xyData=xy1)
xyp = session.XYPlot('XYPlot-1')
chartName = xyp.charts.keys()[0]
chart = xyp.charts[chartName]
chart.setValues(curvesToPlot=(c1, ), )
session.viewports['Viewport: 1'].setValues(displayedObject=xyp)
x0 = session.xyDataObjects['_EIGFREQ Whole Model-1']
session.writeXYReport(fileName='abaqus.rpt', xyData=(x0, ))
