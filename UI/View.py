import os

import maya.cmds as cmds
import sys
import importlib

from Functions.arm_rigging import ArmRigging

sys.path.append("C:/Users/weiwe/Documents/maya/2024/scripts/TECA_5500_Final")

from Functions import arm_rig_func
importlib.reload(arm_rig_func)
from Utils import ui_helper
importlib.reload(ui_helper)
from Functions import constraint_func
importlib.reload(constraint_func)

from Functions import arm_rigging
importlib.reload(arm_rigging)
from Functions import piston_rigging
importlib.reload(piston_rigging)
from Functions import chain_rigging
importlib.reload(chain_rigging)
from Functions import tread_rigging
importlib.reload(tread_rigging)


ui_helper_tool = ui_helper
armrig_func = arm_rig_func

# PATHS
USERAPPDIR = cmds.internalVar(userAppDir=True)
VERSION = cmds.about(v=True)
IconPath = os.path.join(USERAPPDIR, VERSION, "/scripts/TECA_5500_Final/UI/")
FunctionPath = os.path.join(USERAPPDIR, VERSION, "/scripts/TECA_5500_Final/Functinos/")
UtilsPath = os.path.join(USERAPPDIR, VERSION, "/scripts/TECA_5500_Final/Utils/")


class View(object):
    def __init__(self):
        super(View, self).__init__()
        self.build_ui()

    def build_ui(self):
        # Delete the window if it already exists
        if cmds.window("myTabbedWindow", exists=True):
            cmds.deleteUI("myTabbedWindow")

        # Create the main window
        window = cmds.window("myTabbedWindow", title="Rigging Tools", widthHeight=(400, 500))

        cmds.columnLayout(mar=10)
        cmds.text(l="Gold Digger Rigging v01", fn="boldLabelFont", bgc=(213,156,255))
        form = cmds.formLayout()

        # Create the tab layout
        tabs = cmds.tabLayout("main_tab", innerMarginWidth=5, innerMarginHeight=5)
        cmds.formLayout(form,
                        edit=True,
                        attachForm=((tabs, 'top', 10), (tabs, 'left', 0), (tabs, 'bottom', 0), (tabs, 'right', 0)))

        # Tabs for arm rig
        child1 = cmds.rowColumnLayout(numberOfColumns=1)
        arm_UI = arm_rigging.ArmRigging()
        arm_UI.build_ui()

        cmds.setParent(child1)
        cmds.setParent(tabs)


        # Tabs for tread
        child2 = cmds.rowColumnLayout(numberOfColumns=1)
        Tread_Tab_UI = tread_rigging.TreadRigging
        Tread_Tab_UI.build_ui(self)
        cmds.setParent(child2)
        cmds.setParent(tabs)

        # Tabs for chains
        child3 = cmds.rowColumnLayout(numberOfColumns=1)
        Tread_Tab_UI = chain_rigging.ChainRigging
        Tread_Tab_UI.build_ui(self)
        cmds.setParent(child3)
        cmds.setParent(tabs)

        # Tabs for Piston
        child4 =cmds.rowColumnLayout(numberOfColumns=1)
        piston_ui = piston_rigging.PistonRigging
        piston_ui.build_ui(self)
        cmds.setParent(child4)
        cmds.setParent(tabs)


        cmds.tabLayout(tabs,
                       edit=True,
                       tabLabel=((child1, '1.Arm'),
                                 (child2, '2.Tread'),
                                 (child3, '3.Chain'),
                                 (child4, '4.Piston'))
                       )


        # Show the window
        cmds.showWindow(window)


Main_UI = View()


