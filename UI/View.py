import maya.cmds as cmds
import sys
import importlib

sys.path.append("C:/Users/weiwe/Documents/maya/2024/scripts/site-packages/FinalAssignment")

from Functions import arm_rig_func
from Utils import ui_helper

from Functions.arm_rigging import ArmRigging

ui_helper_tool = ui_helper
armrig_func = arm_rig_func




class View:
    def __init__(self):
        super(View, self).__init__()
        self.build_ui()
        # importlib.reload(ArmRigging)
        # importlib.reload(ui_helper)
        # importlib.reload(arm_rig_func)

    def build_ui(self):
        # Delete the window if it already exists
        if cmds.window("myTabbedWindow", exists=True):
            cmds.deleteUI("myTabbedWindow")

        # Create the main window
        window = cmds.window("myTabbedWindow", title="Rigging Tools", widthHeight=(400, 300))




        form = cmds.formLayout()

        # Create the tab layout
        tabs = cmds.tabLayout("main_tab", innerMarginWidth=5, innerMarginHeight=5)
        cmds.formLayout(form,
                        edit=True,
                        attachForm=((tabs, 'top', 0), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)))

        # Tabs for arm rig
        child1 = cmds.rowColumnLayout(numberOfColumns=1)
        arm_UI = ArmRigging.build_ui(self)
        cmds.setParent(child1)
        cmds.setParent(tabs)


        # Tabs for tread
        child2 = cmds.rowColumnLayout(numberOfColumns=2)
        # Tread_Tab_UI = Tread.build_ui(self)
        cmds.setParent(child2)
        cmds.setParent(tabs)

        # Tabs for chains
        child3 = cmds.rowColumnLayout(numberOfColumns=2)
        # Tread_Tab_UI = Tread.build_ui(self)
        cmds.setParent(child3)
        cmds.setParent(tabs)

        cmds.tabLayout(tabs, edit=True, tabLabel=((child1, 'One'), (child2, 'Two'), (child3, 'Three')))


        # Show the window
        cmds.showWindow(window)


