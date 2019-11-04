#Author-KWP
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        
        ##########################################
        ##  Parse existing spline
        sel = ui.selectEntity('Select spline', 'SketchCurves')
        spline = adsk.fusion.SketchFittedSpline.cast(sel.entity)
  
        classType = spline.classType()
        numAttribute = spline.attributes.count
        maxPoint = spline.boundingBox.maxPoint
        minPoint = spline.boundingBox.minPoint

        info = classType + "\n" + str(numAttribute) + "\n" + \
            str(minPoint.x) + " " + str(minPoint.y) + " " + str(minPoint.z) + "\n" + \
            str(maxPoint.x) + " " + str(maxPoint.y) + " " + str(maxPoint.z) + "\n"

        pointList = spline.fitPoints
        numPoint = pointList.count;
        info += "Num of point = " + str(numPoint) + "\n"

        for index in range(numPoint):
            point3D = pointList.item(index).geometry
            (good, x,y,z) = point3D.getData()
            info += str(x) + " " + str(y) + " " + str(z) + "\n"

        ui.messageBox(info, 'Title')

        ##########################################
        ##  Create new spline
        newPointList = adsk.core.ObjectCollection.create()
        for index in range(numPoint):
            point3D = pointList.item(index).geometry
            (good, x,y,z) = point3D.getData()

            newPoint = adsk.core.Point3D.create(x,y, z + index / (numPoint - 1))
            newPointList.add(newPoint)
        
        design = adsk.fusion.Design.cast(app.activeProduct)
        root = design.rootComponent

        newSketch = root.sketches.add(root.yZConstructionPlane)
        newSketch.sketchCurves.sketchFittedSplines.add(newPointList)

        ui.messageBox('Done', 'Title')

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))