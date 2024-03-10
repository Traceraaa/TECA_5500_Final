import maya.cmds as cmds


def parentConstraint(parent, child, main_offset):
    cmds.parentConstraint(parent, child, mo=main_offset)


def pointConstraint(constrainer, constrainee, main_offset):
    cmds.pointConstraint(constrainer, constrainee, mo=main_offset)

def aimConstraint(constrainer, constrainee, main_offset):
    cmds.aimConstraint(constrainer, constrainee, mo=main_offset)