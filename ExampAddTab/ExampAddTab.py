import adsk.core, adsk.fusion, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        # For this example, we are adding the already exisiting 'Extrude' command into a new panel:
        cmdDefinitions = ui.commandDefinitions
        anotherExtrudeCmd = cmdDefinitions.itemById('Extrude')
                
        # For a few months, the customer might run either classic UI or tabbed toolbar UI.
        # Find out what is being used:
        runningTabbedToolbar = ui.isTabbedToolbarUI

        if runningTabbedToolbar:
            # Get all workspaces:
            allWorkspaces = ui.workspaces

            # Get the Design workspace:
            designWorkspace = allWorkspaces.itemById('FusionSolidEnvironment')

            if (designWorkspace):
                # Get all the tabs for the Design workspaces:
                allDesignTabs = designWorkspace.toolbarTabs
                if (allDesignTabs.count > 0):
                    # Add a new tab to the Design workspaces:
                    newDesignTab = allDesignTabs.add('ParkerTongTabId', 'Parker Tong')

                    if (newDesignTab):
                        # Get all of the toolbar panels for the NewDesign tab:
                        allNewDesignTabPanels = newDesignTab.toolbarPanels

                        # Has the panel been added already?
                        # You'll get an error if you try to add this more than once to the tab.
                        brandNewDesignPanel = None
                        brandNewDesignPanel = allNewDesignTabPanels.itemById('UnProjectPanel')

                        if brandNewDesignPanel is None:
                            # We have not added the panel already.  Go ahead and add it.
                            brandNewDesignPanel = allNewDesignTabPanels.add('UnProjectPanle', 'Un-Project')

                        if brandNewDesignPanel:
                            # We want this panel to be visible:
                            brandNewDesignPanel.isVisible = True
                            # Access the controls that belong to the panel:
                            newPanelControls = brandNewDesignPanel.controls

                            # Do we already have this command in the controls?  
                            # You'll get an error if you try to add it more than once to the panel:
                            extrudeCmdControl =  None
                            extrudeCmdControl = newPanelControls.itemById('Extrude')
                            if extrudeCmdControl is None:
                                if anotherExtrudeCmd:
                                    # Go ahead and add the command to the panel:
                                    extrudeCmdControl = newPanelControls.addCommand(anotherExtrudeCmd)
                                    if extrudeCmdControl:
                                        extrudeCmdControl.isVisible = True
                                        extrudeCmdControl.isPromoted = True
                                        extrudeCmdControl.isPromotedByDefault = True

                            else:
                                if brandNewDesignPanel.isVisible:
                                    ui.messageBox('Do you see Best Panel now?')     
                                else:
                                    totalControlsInPanel = newPanelControls.count
                                    if (totalControlsInPanel == 1):
                                        if extrudeCmdControl.isVisible:
                                            ui.messageBox('Not visible control')  

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))