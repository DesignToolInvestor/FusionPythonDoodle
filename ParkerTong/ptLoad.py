#Author-KWP
#Description-

import adsk.core, adsk.fusion, adsk.cam, traceback
from . import ptTab

# Global list to keep all event handlers in scope.
# This is only needed with Python.
handlers = []

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        ptTab = ptTab.makePanel()

        addTestCmd(ptTab)
        
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))

def addTestCmd(panel)
    ui = None
    try:
        # Get the CommandDefinitions collection.
        cmdDefs = ui.commandDefinitions
        
        # Create a button command definition.
        buttonUnProject2d = cmdDefs.addButtonDefinition('UnProject2dId', 
                                                   'Un-Project 2d', 
                                                   '2d Un-Project')
        
        # Connect to the command created event.
        buttonUnProject2dCommandCreated = buttonUnProject2dCommandCreatedEventHandler()
        buttonUnProject2d.commandCreated.add(buttonUnProject2dCommandCreated)
        handlers.append(buttonUnProject2dCommandCreated)
        
        # Add the button to the bottom of the panel.
        buttonControl = panel.controls.addCommand(buttonUnProject2d)

# Event handler for the commandCreated event.
class buttonUnProject2dCommandCreatedEventHandler(adsk.core.CommandCreatedEventHandler):
    def __init__(self):
        super().__init__()
    def notify(self, args):
        eventArgs = adsk.core.CommandCreatedEventArgs.cast(args)
        cmd = eventArgs.command

        # Connect to the execute event.
        onExecute = buttonUnProject2dCommandExecuteHandler()
        cmd.execute.add(onExecute)
        handlers.append(onExecute)


# Event handler for the execute event.
class buttonUnProject2dCommandExecuteHandler(adsk.core.CommandEventHandler):
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
        cmdDef = ui.commandDefinitions.itemById('UnProject2dId')
        if cmdDef:
            cmdDef.deleteMe()
            
        
        cntrl = addinsPanel.controls.itemById('UnProject2dId')
        if cntrl:
            cntrl.deleteMe()

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))	