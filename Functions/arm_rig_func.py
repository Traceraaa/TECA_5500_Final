import maya.cmds as cmds


def make_locator(num_locators):
    locator_list = []
    for i in range(1, num_locators + 2):
        newLoc = cmds.spaceLocator(n="Armlocator_{}".format(i), p=(0, 0, i * 5))
        cmds.scale(3, 3, 3)
        cmds.CenterPivot()
        locator_list.append(newLoc[0])
    print(locator_list)

    return locator_list


def create_rig(loc_list):
    loc_trans = []

    for loc in loc_list:
        print(loc)
        loc_pos = cmds.getAttr(loc + ".wp")
        loc_trans.append(loc_pos[0])
    cmds.select(cl=True)

    joint_list = []
    for i in loc_trans:
        created_joint = cmds.joint(n="ArmJoint_#", p=i)
        joint_list.append(created_joint)

    return joint_list

def create_ik_handle():
    ctrl_list = []

    selectedJoint = []
    selectedJoint = cmds.ls(sl=True)

    # Making IK handle
    new_ik_handle = cmds.ikHandle(n="IKCT", sj=selectedJoint[0], ee=selectedJoint[-1], s=False, snc=False)
    # new_ctrl = cmds.circle(r=4, nr=(0, 1, 0))
    # cmds.matchTransform(new_ctrl, new_ik_handle, pos=True, rot=True)
    # cmds.select(new_ctrl)
    # cmds.FreezeTransformations()
    # cmds.parentConstraint(new_ctrl, new_ik_handle[0], mo=True)
    # ctrl_list.append(new_ctrl[0])

    return new_ik_handle

def finalize_FK(joint_list, option_rig_type):
    # Getting user option of whether you use IK or FK
    user_option = cmds.optionMenuGrp(option_rig_type, query=True, value=True)

    # Options for making FK handles
    if user_option == "FK":
        ctrl_list = []
        # get rid of the ctrl for end joint
        new_jnt_list = joint_list.copy()
        new_jnt_list.pop()

        for jnt in new_jnt_list:
            new_ctrl = cmds.circle(n="{}_ctrl".format(jnt), r=4, nr=(0, 1, 0))
            cmds.matchTransform(new_ctrl, jnt, pos=True, rot=True)
            cmds.select(new_ctrl)
            cmds.FreezeTransformations()
            cmds.parentConstraint(new_ctrl, jnt, mo=True)
            ctrl_list.append(new_ctrl[0])
        # parent constrainting controls
        for i in range(len(ctrl_list)-1):
            cmds.parentConstraint(ctrl_list[i], ctrl_list[i + 1], mo=True)
    return ctrl_list

def finalize_IK(ik_handle):
    ctrl_list = []
    new_ctrl = cmds.circle(r=4, nr=(0, 1, 0))
    cmds.matchTransform(new_ctrl, ik_handle, pos=True, rot=True)
    cmds.select(new_ctrl)
    cmds.FreezeTransformations()
    cmds.parentConstraint(new_ctrl, ik_handle[0], mo=True)
    ctrl_list.append(new_ctrl[0])
    return ctrl_list

def reset(locator_list, joint_list, ctrl_list):

    if locator_list:
        cmds.select(locator_list)
        cmds.delete()
        locator_list.clear()
    if joint_list:
        cmds.select(joint_list)
        cmds.select(joint_list)
        cmds.delete()
        joint_list.clear()
    if ctrl_list:
        cmds.select(ctrl_list)
        cmds.delete()
        ctrl_list.clear()
