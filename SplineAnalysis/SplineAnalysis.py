#Author-KWP
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
  
        sel = ui.selectEntity('Select', 'SketchCurves')
        spline = adsk.fusion.SketchFittedSpline.cast(sel.entity)
  
        selClassType = spline.classType()
        if selClassType != 'adsk::fusion::SketchFittedSpline':
            ui.messageBox('This is not a spline', 'Error')
            raise Exception("Re-Run")

        maxPoint = spline.boundingBox.maxPoint
        minPoint = spline.boundingBox.minPoint

        info = "Bounding Box:\n  " + \
            str(minPoint.x) + " " + str(minPoint.y) + " " + str(minPoint.z) + "\n  " + \
            str(maxPoint.x) + " " + str(maxPoint.y) + " " + str(maxPoint.z) + "\n"

        pointList = spline.fitPoints
        numPoint = pointList.count;
        info += "Fit Points:\n  Num = " + str(numPoint) + "\n"

        for index in range(numPoint):
            point = pointList.item(index)
            geom = point.geometry

            (good, x,y,z) = geom.getData()
            info += "  " + str(x) + " " + str(y) + " " + str(z) + "\n"

            tangent = spline.getTangentHandle(point)
            if tangent == None:
                info += "  no tan\n"
            else:
                info += "  tan len = " + str(tangent.length) + "\n"

        nurb = spline.geometry;
        info += "Geomotery:\n   "
        numControlPoint = nurb.controlPointCount
        info += "  " + str(numControlPoint) + "\n"

        controlPointList = nurb.controlPoints;
        for index in range(numControlPoint):
            point3D = controlPointList[index]
            (good, x,y,z) = point3D.getData()
            info += "(" + str(x) + ", " + str(y) + ", " + str(z) + ")\n"

        info += "Curve Tyep = " + str(nurb.curveType) + "\n"       
        info += "Degree = " + str(nurb.degree) + "\n"    
        if nurb.isRational:
            info += "Is rational\n"
        else:
            info += "Not rational\n"
        info += "Knots:"       
        info += "  Count = " + str(nurb.knotCount) + "\n" 
       
        test(ui, info)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def test(ui, info):
    ui.messageBox(info, 'Title')