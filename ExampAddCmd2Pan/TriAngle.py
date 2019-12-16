##
##  T r i A n g l e . p y
##
##  This command creates a new sketch on the timeline and places a triangle in 
##  it.

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        des = adsk.fusion.Design.cast(app.activeProduct)        
        
        if des:
            root = des.rootComponent
            sk = root.sketches.add(root.xYConstructionPlane)
            lines = sk.sketchCurves.sketchLines
            l1 = lines.addByTwoPoints(adsk.core.Point3D.create(0,0,0), 
                                      adsk.core.Point3D.create(5,0,0))
            l2 = lines.addByTwoPoints(l1.endSketchPoint,
                                      adsk.core.Point3D.create(2.5,4,0))
            l3 = lines.addByTwoPoints(l2.endSketchPoint, l1.startSketchPoint)

        # adsk.terminate()   # This is no longer needed ???

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))