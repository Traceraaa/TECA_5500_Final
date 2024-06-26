import maya.cmds as cmds
import importlib
import pprint as p

from Functions import tread_rig_func
importlib.reload(tread_rig_func)
from Utils import ui_helper
importlib.reload(ui_helper)

global frame_locator_layout, frame_curve_layout, frame_tread_layout
global btn_make_locator, btn_make_curve, btn_radio_options, btn_make_tread, btn_update_tread, btn_finalize_thread, btn_reset
global slider_number_treads



class TreadRigging(object):
    def __init__(self):
        # super(TreadRigging, self).__init__()
        pass



    def build_ui(self):
        global frame_locator_layout, frame_curve_layout, frame_tread_layout
        global btn_make_locator, btn_make_curve, btn_radio_options, btn_make_tread, btn_update_tread, btn_finalize_thread, btn_reset
        global slider_number_treads

        main_layout = cmds.columnLayout()

        UI_WARNING_BGC = [1, 1, 0]
        # Initialize
        frame_locator_layout = cmds.frameLayout(l="Initialize", w=500, cll=True)
        cmds.columnLayout()

        cmds.text(l="Creating two locators in the scene. Front and Back")
        btn_make_locator = cmds.button(l="Initialize", c="tread_rigging._make_locator()")
        cmds.setParent(main_layout)
        cmds.separator(w=500)

        # Make Curve
        frame_curve_layout = cmds.frameLayout(l="Create Curve", w=500, cll=True, en=False)
        cmds.columnLayout()

        cmds.text(l="Requirement!", fn="boldLabelFont", bgc=UI_WARNING_BGC)
        cmds.text(l="Position the two locators at the front and back end of your curve. And then hit the button")
        btn_make_curve = cmds.button(l="Make Tread Curve", c="tread_rigging._make_curve()", en=False)
        cmds.setParent(main_layout)
        cmds.separator(w=500)

        # Create Tread
        frame_tread_layout = cmds.frameLayout(l="Create Tread", w=500, cll=True, en=False)
        cmds.columnLayout()

        cmds.text(l="Requirement!", fn="boldLabelFont", bgc=UI_WARNING_BGC)
        cmds.text(l="Select default or pick your own tread peice. Hit the Update button to observe the change")
        btn_radio_options = cmds.radioButtonGrp(label='Pick Tread Peice ',
                                                labelArray2=['Default', 'Pick your own peice'],
                                                numberOfRadioButtons=2,
                                                sl=1,
                                                cc1='tread_rigging._use_default_tread()',
                                                cc2='tread_rigging._use_custom_tread()',
                                                en=False)

        cmds.textFieldButtonGrp(bl="Pick Tread OBJ", bc="PickingObject()", ed=False, en=False)
        slider_number_treads = cmds.intSliderGrp(min=10, v=25, cc="tread_rigging._adjust_tread_number()", f=True, en=False)

        cmds.rowLayout(numberOfColumns=2, columnWidth2=(250, 250), adjustableColumn=2, columnAlign=(1, 'right'),
                       columnAttach=[(1, 'both', 0), (2, 'both', 0)])
        btn_make_tread = cmds.button(l="MakeTread", c="tread_rigging._make_tread()", en=False)
        btn_update_tread = cmds.button(l="Update Tread Piece", c="tread_rigging._update_tread()", en=False)

        cmds.setParent(main_layout)
        cmds.separator(w=500)

        # Finalize and Reset
        cmds.text(l="")
        cmds.rowLayout(numberOfColumns=2, columnWidth2=(250, 250), adjustableColumn=2, columnAlign=(1, 'right'),
                       columnAttach=[(1, 'both', 0), (2, 'both', 0)])
        btn_finalize_thread = cmds.button(l="Finalize Tread", c="tread_rigging._finalize()", en=False, h=40, bgc=[0, 0.7, 0])
        btn_reset = cmds.button(l="Reset All", c="tread_rigging._reset()", en=False, h=40, bgc=[0.7, 0, 0])


def _make_locator():
    global btn_make_locator, frame_locator_layout, frame_curve_layout, btn_make_curve

    wheels = cmds.ls(sl=True)

    # Getting bound size for select object
    bound = cmds.xform(q=True, bbi=True)
    b_xmin = bound[0]
    b_ymin = bound[1]
    b_zmin = bound[2]
    b_xmax = bound[3]
    b_ymax = bound[4]
    b_zmax = bound[5]

    # Math for center point of the object
    front_pos = ((b_xmin + b_xmax) / 2, (b_ymin + b_ymax) / 2, b_zmin)
    back_pos = ((b_xmin + b_xmax) / 2, (b_ymin + b_ymax) / 2, b_zmax)

    tread_rig_func.make_locator(front_pos, back_pos)

    # UI interaction
    ui_helper.disable_btn(btn_make_locator)
    ui_helper.disable_frame_layout(frame_locator_layout)
    ui_helper.enable_frame_layout(frame_curve_layout)
    ui_helper.enable_btn(btn_make_curve)
    # UI interaction End


def _make_curve():
    tread_rig_func.make_curve()

def _use_default_tread():
    tread_rig_func.use_default_traed()

def _use_custom_tread():
    tread_rig_func.use_custom_tread()

def _adjust_tread_number():
    tread_rig_func.adjust_tread_number()


def _make_tread():
    tread_rig_func.make_tread()

def _update_tread():
    tread_rig_func.update_tread()
def _reset():
    tread_rig_func.reset()

def _finalize():
    tread_rig_func.finalize()


