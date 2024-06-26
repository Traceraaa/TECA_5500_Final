import maya.cmds as cmds

from Functions import chain_rig_func
from Utils import ui_helper

global frame_layout_curve, frame_layout_controller, frame_layout_chain
global slider_int_span_count, slider_float_smoothness, slider_int_redo_controller
global btn_radio_curve_options, cb_use_smooth, btn_next_to_make_controllers, btn_make_controller, btn_to_final_step
global btn_finalize, btn_make_chain, cb_make_proxy, btn_update

global curve_type_picked, is_first_time, selected_curve, chain_count


class ChainRigging(object):
    def __init__(self):
        # super(ChainRigging, self).__init__()
        global is_first_time
        is_first_time = True

    def build_ui(self):
        main_layout = cmds.columnLayout(mar=5)
        cmds.rowColumnLayout(numberOfColumns=1)
        cmds.text("Curve Rigger Tool", font="boldLabelFont")
        cmds.separator(w=700, h=10)
        cmds.setParent(main_layout)
        frame_layout_curve = cmds.frameLayout(l="Curve Settings", w=700, cll=True, cl=False)
        ui_curve_layout = cmds.columnLayout()
        cmds.text("Before anything, ensure you have a curve selected to restructure the curve use this slider")
        cmds.setParent(ui_curve_layout)

        btn_radio_curve_options = cmds.radioButtonGrp(label='Type of Curve',
                                        labelArray4=['Linear-1', 'Quadratic-2', 'Cubic-3', 'Quintic-5'],
                                        numberOfRadioButtons=4,
                                        cc1='chain_rigging._curve_type()',
                                        cc2='chain_rigging._curve_type()',
                                        cc3='chain_rigging._curve_type()',
                                        cc4='chain_rigging._curve_type()',
                                        en=False)

        cmds.rowLayout(numberOfColumns=2)
        slider_int_span_count = cmds.intSliderGrp(min=3, max=100, v=3, cc="chain_rigging._span_mod()", f=True, en=False)
        cb_use_smooth = cmds.checkBox(l="Adjust Smoothness", cc="chain_rigging._adjust_smoothness()", en=False)
        cmds.setParent(ui_curve_layout)
        cmds.separator(w=700)

        cmds.text("now if you want to smooth it, use this slider to smooth")
        slider_float_smoothness = cmds.floatSliderGrp(min=0, max=10, v=0, cc="chain_rigging._update_smoothness()", f=True, en=False)
        btn_next_to_make_controllers = cmds.button(l="Next", c="chain_rigging.expand_controller_section()", en=False)

        cmds.separator(w=700)
        cmds.setParent(main_layout)

        # *****************************************************************************************************************
        frame_layout_controller = cmds.frameLayout(l="Make Controllers", w=700, cll=True, cl=True)
        ui_controller_layout = cmds.columnLayout()
        cmds.text("now if you are done with the curve, use this button to create controllers")
        slider_int_redo_controller = cmds.intSliderGrp(min=3, max=100, v=3, cc="chain_rigging._controller_redo()", f=True, en=False)
        cmds.rowLayout(numberOfColumns=3)
        btn_make_controller = cmds.button(l="CTRL maker", c="chain_rigging._make_controller()", en=False)
        btn_to_final_step = cmds.button(l="Next", c="chain_rigging._make_chain_section()", en=False)
        btn_update = cmds.button(l="Update Chain", c="chain_rigging._update_chain()", en=False)
        cmds.setParent(ui_controller_layout)
        cmds.separator(w=700)
        cmds.setParent(main_layout)

        # *****************************************************************************************************************
        frame_layout_chain = cmds.frameLayout(l="Make Chains", w=700, cll=True, cl=True)
        ui_chain_layout = cmds.columnLayout()
        cmds.text("now if you are done, select your desired object and click next")
        cmds.rowLayout(numberOfColumns=3)
        btn_make_chain = cmds.button(l="MakeChain", c="chain_rigging._make_chain()", en=False)
        cb_make_proxy = cmds.checkBox(l="Use Proxy Geo", cc="chain_rigging._make_proxy()", en=False)
        cmds.setParent(ui_chain_layout)
        cmds.setParent(main_layout)


def _curve_type():
    global btn_radio_curve_options, slider_int_span_count, slider_float_smoothness, cb_use_smooth, curve_type_picked
    curve_type_picked = chain_rig_func.curve_type(btn_radio_curve_options)

    # UI Interaction
    ui_helper.enable_int_slider_group(slider_int_span_count)
    ui_helper.disable_float_slider_group(slider_float_smoothness)
    ui_helper.disable_checkbox(cb_use_smooth)
    # UI Interaction End


def _span_mod():
    global curve_type_picked, cb_use_smooth, is_first_time, btn_radio_curve_options, btn_next_to_make_controllers

    # UI
    if curve_type_picked == 4:
        curve_type_picked = 5
    if curve_type_picked == 1:
        ui_helper.disable_checkbox(cb_use_smooth)
    else:
        ui_helper.enable_checkbox(cb_use_smooth)

    if not is_first_time:
        cmds.undo()

    # UI Interaction
    ui_helper.disable_radio_button(btn_radio_curve_options)
    ui_helper.enable_btn(btn_next_to_make_controllers)
    # UI Interaction End

    span_value = cmds.intSliderGrp(slider_int_span_count, q=True, v=True)
    selected_curve = chain_rig_func.span_mod(span_value)
    is_first_time = False



def _toggle_smoothness_slider():

    # UI Interaction
    ui_helper.disable_int_slider_group(slider_int_span_count)
    ui_helper.enable_float_slider_group(slider_float_smoothness)
    # UI Interaction End


def _update_smoothness():
    global is_first_time, btn_next_to_make_controllers, slider_float_smoothness, selected_curve
    new_smoothness_value = cmds.floatSliderGrp(slider_float_smoothness, q=True, v=True)
    chain_rig_func.update_smoothness(selected_curve, new_smoothness_value)

    # UI Interaction
    ui_helper.enable_btn(btn_next_to_make_controllers)
    # UI Interaction End


def expand_controller_section():
    global frame_layout_curve, frame_layout_controller

    # UI Interaction
    ui_helper.disable_frame_layout(frame_layout_curve)
    ui_helper.enable_frame_layout(frame_layout_controller)
    # UI Interaction End


def _controller_redo():
    global selected_curve, slider_int_redo_controller
    new_span = cmds.intSliderGrp(slider_int_redo_controller, q=True, v=True)
    chain_rig_func.controller_redo(selected_curve, new_span)

def _make_controller():
    global selected_curve, chain_count
    chain_rig_func.make_controller(selected_curve)

    # UI Interaction
    ui_helper.disable_float_slider_group(slider_float_smoothness)
    ui_helper.disable_int_slider_group(slider_int_redo_controller)
    ui_helper.enable_btn(btn_to_final_step)
    ui_helper.enable_int_slider_group(slider_int_redo_controller)
    ui_helper.disable_btn(btn_make_chain)
    # UI Interaction End

def _make_chain_section():
    global frame_layout_controller, frame_layout_chain

    # UI Interaction
    ui_helper.disable_frame_layout(frame_layout_controller)
    ui_helper.enable_frame_layout(frame_layout_chain)
    # UI Interaction End


def _update_chain():

    chain_rig_func.update_chain()

    # UI Interaction
    ui_helper.disable_btn(btn_to_final_step)
    # UI Interaction End

    _controller_redo()

    cmds.select(selected_curve)

    _make_chain()

def _make_chain():
    global chain_count, selected_curve
    user_selected_mesh = cmds.ls(sl=True)
    if user_selected_mesh:
        chain_rig_func.make_chain(selected_curve, chain_count)

        # UI Interaction
        ui_helper.enable_btn(btn_update)
        ui_helper.disable_btn(btn_make_chain)
        ui_helper.enable_int_slider_group(slider_int_redo_controller)
        ui_helper.disable_checkbox(cb_make_proxy)
        # UI Interaction End





def _make_proxy():
    chain_rig_func.make_proxy()