import maya.cmds as cmds


def make_locator(front_pos, back_pos):

    cmds.spaceLocator(n="CircleLocFront")
    cmds.scale(5, 5, 5)
    cmds.move(front_pos[0], front_pos[1], front_pos[2])
    cmds.setAttr("CircleLocFront.translateX", lock=True)
    cmds.setAttr("CircleLocFront.translateY", lock=True)
    cmds.setAttr("CircleLocFront.translateZ", lock=True)

    cmds.spaceLocator(n="CircleLocBack")
    cmds.scale(5, 5, 5)
    cmds.move(back_pos[0], back_pos[1], back_pos[2])
    cmds.setAttr("CircleLocBack.translateX", lock=True)
    cmds.setAttr("CircleLocBack.translateY", lock=True)
    cmds.setAttr("CircleLocBack.translateZ", lock=True)

    cmds.group("CircleLocFront", "CircleLocBack", n="LocGRP")


def make_curve():
    return None


def use_default_traed():
    return None


def use_custom_tread():
    return None


def adjust_tread_number():
    return None


def update_tread():
    return None


def reset():
    return None


def finalize():
    return None