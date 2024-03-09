import maya.cmds as cmds

from Functions import arm_rig_func
from Utils import ui_helper


global btn_make_locater
global btn_create_rig
global btn_create_ik_handle
global btn_finalize
global btn_reset
global slider_total_pieces
global frame_initialize
global frame_create_rig
global frame_IK_creater
global option_rig_type

global locator_list
global joint_list
global ctrl_list
global ik_handle



class ArmRigging(object):
    def __init__(self):
        super(ArmRigging, self).__init__()
        global btn_make_locater
        global btn_create_rig
        global btn_create_ik_handle
        global btn_finalize
        global btn_reset
        global slider_total_pieces
        global frame_initialize
        global frame_create_rig
        global frame_IK_creater

    def build_ui(self):
        global btn_make_locater, btn_create_rig, btn_finalize, btn_reset, frame_initialize, frame_create_rig, \
            frame_IK_creater, slider_total_pieces, option_rig_type

        # region UI
        window_width = 400
        color_warning = [1, 1, 0]

        self.main_layout = cmds.columnLayout()

        frame_initialize = cmds.frameLayout(l="Initialize", w=window_width, cll=True)
        cmds.columnLayout()

        cmds.text(l="Requirement!", fn="boldLabelFont", bgc=color_warning)
        cmds.text(l="Please input how many pieces the arm has.")
        slider_total_pieces = cmds.intSliderGrp(l="Total Pieces: ", min=2, v=3, field=True)
        cmds.separator(h=15)
        btn_make_locater = cmds.button(l="Initialize", w=window_width / 4, c="_make_locator()")
        cmds.setParent(frame_initialize)
        cmds.setParent(self.main_layout)
        cmds.separator(h=15)

        frame_create_rig = cmds.frameLayout(l="Rig", w=window_width, cll=True, en=False)
        cmds.columnLayout()
        cmds.text(l="Requirement!", fn="boldLabelFont", bgc=color_warning)
        cmds.text(l="Please position the locators where you want the joints to be created.")
        cmds.separator(h=15)

        option_rig_type = cmds.optionMenuGrp(l="FK/IK Mode:")
        cmds.menuItem(l="FK")
        cmds.menuItem(l="IK")
        cmds.separator(h=15)
        btn_create_rig = cmds.button(l="Create Rig", w=window_width / 4, c="_create_rig()")


        cmds.setParent(self.main_layout)

        frame_IK_creater = cmds.frameLayout(l="IK Creator", w=window_width, cll=True, en=False)
        self.uiIKCL = cmds.columnLayout()

        cmds.text(l="Requirement!", fn="boldLabelFont", bgc=color_warning)
        cmds.text(
            l="Please select start and end joints that you want an IK Handle for, then click \"Create IK\" button.")
        cmds.separator(h=15)
        cmds.button(l="Create IK Handle", w=window_width / 4, c="_make_ik_handle()")

        cmds.setParent(self.main_layout)

        cmds.separator(h=25)
        cmds.text(l="Please select all arm peices and then click \"Finalize\" button.")
        cmds.rowLayout(nc=2)
        btn_finalize = cmds.button(l="Finalize", w=window_width / 4, c="_finalize()", en=False)
        btn_reset = cmds.button(l="Reset", w=window_width / 4, c="_reset()", en=False)
        cmds.setParent(self.main_layout)

def _create_rig():
    global joint_list, locator_list

    joint_list = arm_rig_func.create_rig(locator_list)
    print("Joint List created : {}".format(joint_list))

    mode = cmds.optionMenuGrp(option_rig_type, q=True, v=True)

    if (mode == "FK"):
        ui_helper.enable_btn(btn_finalize)
    elif (mode == "IK"):
        ui_helper.enable_frame_layout(frame_IK_creater)

    ui_helper.enable_btn(btn_reset)
    ui_helper.disable_frame_layout(frame_create_rig)


def _make_locator():
    global slider_total_pieces, locator_list

    number_of_locator = ui_helper.get_value_int_slider(slider_total_pieces)
    locator_list = arm_rig_func.make_locator(number_of_locator)
    print("Locator List created : {}".format(locator_list))

    ui_helper.disable_frame_layout(frame_initialize)
    ui_helper.enable_frame_layout(frame_create_rig)
    ui_helper.enable_btn(btn_reset)

def _make_ik_handle():
    global joint_list, locator_list, ik_handle
    ik_handle = arm_rig_func.create_ik_handle()

    ui_helper.disable_frame_layout(frame_IK_creater)
    ui_helper.enable_btn(btn_finalize)
    ui_helper.enable_btn(btn_reset)

def _reset():
    global locator_list, joint_list, ctrl_list
    arm_rig_func.reset(locator_list, joint_list, ctrl_list)

    ui_helper.disable_frame_layout(frame_IK_creater)
    ui_helper.disable_frame_layout(frame_create_rig)
    ui_helper.enable_frame_layout(frame_initialize)
    ui_helper.disable_btn(btn_reset)
    ui_helper.disable_btn(btn_finalize)

def _finalize():
    global locator_list, joint_list, option_rig_type, ctrl_list, ik_handle

    rig_option = cmds.optionMenuGrp(option_rig_type, q=True, v=True)

    if rig_option == "FK":
        ctrl_list = arm_rig_func.finalize_FK(joint_list, option_rig_type)

        joint_list = []
        ctrl_list = []
        arm_rig_func.reset(locator_list, joint_list, ctrl_list)



    elif rig_option == "IK":
        ctrl_list = arm_rig_func.finalize_IK(ik_handle)
        joint_list = []
        ctrl_list = []
        arm_rig_func.reset(locator_list, joint_list, ctrl_list)

    ui_helper.disable_frame_layout(frame_IK_creater)
    ui_helper.disable_frame_layout(frame_create_rig)
    ui_helper.enable_frame_layout(frame_initialize)
    ui_helper.disable_btn(btn_reset)
    ui_helper.disable_btn(btn_finalize)




