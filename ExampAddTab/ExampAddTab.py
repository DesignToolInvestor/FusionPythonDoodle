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
            # Get the Render workspace:
            renderWorkspace = allWorkspaces.itemById('FusionRenderEnvironment')
            # Get the Design workspace:
            designWorkspace = allWorkspaces.itemById('FusionSolidEnvironment')
            if (renderWorkspace and designWorkspace):
                # Get all the tabs for the Render and Design workspaces:
                allRenderTabs = renderWorkspace.toolbarTabs
                allDesignTabs = designWorkspace.toolbarTabs
                if ((allRenderTabs.count > 0) and (allDesignTabs.count > 0)):
                    # Add a new tab to the Render and Design workspaces:
                    newRenderTab = allRenderTabs.add('NewRenderTabHere', 'New Render Tab')
                    newDesignTab = allDesignTabs.add('NewDesignTabHere', 'New Design Tab')
                    if (newRenderTab and newDesignTab):
                        # Get all of the toolbar panels for the NewRender and NewDesign tab:
                        allNewRenderTabPanels = newRenderTab.toolbarPanels
                        allNewDesignTabPanels = newDesignTab.toolbarPanels

                        # Has the panel been added already?
                        # You'll get an error if you try to add this more than once to the tab.
                        brandNewRenderPanel = None
                        brandNewRenderPanel = allNewRenderTabPanels.itemById('bestRenderPanelEverId')
                        if brandNewRenderPanel is None:
                            # We have not added the panel already.  Go ahead and add it.
                            brandNewRenderPanel = allNewRenderTabPanels.add('bestRenderPanelEverId', 'Best Render Panel')

                        if brandNewRenderPanel:
                            # We want this panel to be visible:
                            brandNewRenderPanel.isVisible = True
                            # Access the controls that belong to the panel:
                            newPanelControls = brandNewRenderPanel.controls

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
                                if brandNewRenderPanel.isVisible:
                                    ui.messageBox('Do you see Best Panel now?')     
                                else:
                                    totalControlsInPanel = newPanelControls.count
                                    if (totalControlsInPanel == 1):
                                        if extrudeCmdControl.isVisible:
                                            ui.messageBox('Not visible control')                    

                        brandNewDesignPanel = None
                        brandNewDesignPanel = allNewDesignTabPanels.itemById('bestDesignPanelEverId')
                        if brandNewDesignPanel is None:
                            # We have not added the panel already.  Go ahead and add it.
                            brandNewDesignPanel = allNewDesignTabPanels.add('bestDesignPanelEverId', 'Best Design Panel')

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