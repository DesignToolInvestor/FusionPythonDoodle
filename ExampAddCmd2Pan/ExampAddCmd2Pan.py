##  This adds a command to the bottom of the "ADD-INS   " pull-down panel.
##
##  It must be executed as an add-in.  The thread is never terminated.
##
##  It differes from AddToPanel in that it adds to the panel and that it pops 
##  up a message box rather than create a sketch with a triangle.

import adsk.core, adsk.fusion, adsk.cam, traceback

# Global list to keep all event handlers in scope.
# This is only needed with Python.
handlers = []

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        # Get the CommandDefinitions collection.
        cmdDefs = ui.commandDefinitions
        
        # Create a button command definition.
        unProject2dButton = cmdDefs.itemById('UnProject2dId')
        if unProject2dButton is None:
            unProject2dButton = cmdDefs.addButtonDefinition(
                'UnProject2dId', 'Un-Project 2d', 'Unproject from one plane to another')
        
        # Connect to the command created event.
        unProject2dCreateHandler = unProject2dCreate()
        unProject2dButton.commandCreated.add(unProject2dCreateHandler)
        handlers.append(unProject2dCreateHandler)
        
        # Get the ADD-INS panel in the model workspace.
        addInsPanel = ui.allToolbarPanels.itemById('UnProjectPanelId')
        
        # Add the button to the bottom of the panel.
        buttonControl = addInsPanel.controls.addCommand(unProject2dButton)

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))


# Event handler for the commandCreated event.
class unProject2dCreate(adsk.core.CommandCreatedEventHandler):
    def __init__(self):
        super().__init__()

    def notify(self, args):
        eventArgs = adsk.core.CommandCreatedEventArgs.cast(args)
        cmd = eventArgs.command

        # Connect to the execute event.
        onExecuteHandler = unProject2dExecute()
        cmd.execute.add(onExecuteHandler)
        handlers.append(onExecuteHandler)


# Event handler for the execute event.
class unProject2dExecute(adsk.core.CommandEventHandler):
    def __init__(self):
        super().__init__()

    def notify(self, args):
        eventArgs = adsk.core.CommandEventArgs.cast(args)

        # Code to react to the event.
        app = adsk.core.Application.get()
        ui  = app.userInterface
        ui.messageBox('In command execute event handler.')


def stop(context):
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        
        # Clean up the UI.
        cmdDef = ui.commandDefinitions.itemById('unProject2dId')
        if cmdDef:
            cmdDef.deleteMe()
            
        addinsPanel = ui.allToolbarPanels.itemById('UnProjectPanelId')
        cntrl = addinsPanel.controls.itemById('unProject2dId')
        if cntrl:
            cntrl.deleteMe()
        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))	