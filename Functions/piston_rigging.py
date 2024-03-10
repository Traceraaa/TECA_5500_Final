import maya.cmds as cmds

from Functions import arm_rig_func
from Utils import ui_helper
from Functions import constraint_func

class PistonRigging(object):
    def __init__(self):
        super(PistonRigging, self).__init__()

    def build_ui(self):
        window_width = 400
        cmds.frameLayout('PistonRigging', w=window_width, cll=True)
        self.ui_layout = cmds.columnLayout()
        cmds.text(l="Piston Rigging")

        cmds.button(l="Parent Constraint", c="_set_parent_constraint()")

        cmds.button(l="Aim Constraint", c="_set_aim_constraint()")

        cmds.button(l="Point Constraint", c="_set_point_constraint()")

def _set_parent_constraint():
    selected_obj = cmds.ls(sl=True)
    selected_parent = selected_obj[0]
    selected_child = selected_obj[1]
    constraint_func.parentConstraint(selected_parent, selected_child, True)

def _set_aim_constraint():
    selected_obj = cmds.ls(sl=True)
    constrainer = selected_obj[0]
    constrainee = selected_obj[1]
    constraint_func.aimConstraint(constrainer, constrainee, True)

def _set_point_constraint():
    selected_obj = cmds.ls(sl=True)
    constrainer = selected_obj[0]
    constrainee = selected_obj[1]
    constraint_func.pointConstraint(constrainer, constrainee, True)
