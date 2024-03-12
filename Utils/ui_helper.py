import maya.cmds as cmds


def disable_frame_layout(layout):
    cmds.frameLayout(layout, e=True, en=False)


def enable_frame_layout(layout):
    cmds.frameLayout(layout, e=True, en=True)


def enable_btn(btn):
    cmds.button(btn, e=True, en=True)


def disable_btn(btn):
    cmds.button(btn, e=True, en=False)


def enable_int_slider_group(int_slider_group):
    cmds.intSliderGrp(int_slider_group, e=True, en=True)


def disable_int_slider_group(int_slider_group):
    cmds.intSliderGrp(int_slider_group, e=True, en=False)


def enable_float_slider_group(float_slider_group):
    cmds.floatSliderGrp(float_slider_group, e=True, en=True)


def disable_float_slider_group(float_slider_group):
    cmds.floatSliderGrp(float_slider_group, e=True, en=False)

def enable_checkbox(checkbox):
    cmds.checkBox(checkbox, e=True, en=True)


def disable_checkbox(checkbox):
    cmds.checkBox(checkbox, e=True, en=False)

def enable_radio_button(radio_button_grp):
    cmds.radioButtonGrp(radio_button_grp, e=True, en=True)

def disable_radio_button(radio_button_grp):
    cmds.radioButtonGrp(radio_button_grp, e=True, en=False)


def get_value_int_slider(int_slider_group):
    return cmds.intSliderGrp(int_slider_group, q=True, v=True)