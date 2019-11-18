import adsk.core, adsk.fusion, traceback

def ptMakeTab():
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
         
        # For a few months, the customer might run either classic UI or tabbed toolbar UI.
        # Find out what is being used:
        runningTabbedToolbar = ui.isTabbedToolbarUI

        if not runningTabbedToolbar:
            ui.messageBox('This package requires the new UI (i.e., the tabbed UI)')

        else:
            # Get all workspaces:
            allWorkspaces = ui.workspaces

            # Get the Design workspace:
            designWorkspace = allWorkspaces.itemById('FusionSolidEnvironment')

            # Get all the tabs for the Render and Design workspaces:
            allDesignTabs = designWorkspace.toolbarTabs

            # Add a new tab to the Render and Design workspaces:
            ptTab = allDesignTabs.add('ParkerTongTabId', 'Parker Tong')

            # Get all of the toolbar panels for the NewRender and NewDesign tab:
            allPtTabPanels = ptTab.toolbarPanels

            unProjectPanel = None
            unProjectPanel = allptTabPanels.itemById('ptUnProjectPanId')

            if unProjectPanel is None:
                # We have not added the panel already.  Go ahead and add it.
                unProjectPanel = allptTabPanels.add('ptUnProjectPanId', 'Un-Project')

            return unProjectPanel

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))