import maya.cmds as cmds


class ChainRigging(object):
    def __init__(self):
        super(ChainRigging, self).__init__()

    def build_ui(self):
        main_layout = cmds.columnLayout(mar=5)
        cmds.rowColumnLayout(numberOfColumns=1)
        cmds.text("Curve Rigger Tool", font="boldLabelFont")
        cmds.separator(w=700, h=10)
        cmds.setParent(main_layout)
        ui_curve_frame = cmds.frameLayout(l="Curve Settings", w=700, cll=True, cl=False)
        ui_curve_layout = cmds.columnLayout()
        cmds.text("Before anything, ensure you have a curve selected to restructure the curve use this slider")
        cmds.setParent(ui_curve_layout)

        curvetype = cmds.radioButtonGrp(label='Type of Curve',
                                        labelArray4=['Linear-1', 'Quadratic-2', 'Cubic-3', 'Quintic-5'],
                                        numberOfRadioButtons=4,
                                        cc1='curvetype()',
                                        cc2='curvetype()',
                                        cc3='curvetype()',
                                        cc4='curvetype()',
                                        en=False)

        cmds.rowLayout(numberOfColumns=2)
        SpanCount = cmds.intSliderGrp(min=3, max=100, v=3, cc="SpanMod()", f=True, en=False)
        cb_use_smooth = cmds.checkBox(l="Adjust Smoothness", cc="NextStep()", en=False)
        cmds.setParent(ui_curve_layout)
        cmds.separator(w=700)

        cmds.text("now if you want to smooth it, use this slider to smooth")
        SmoothNess = cmds.floatSliderGrp(min=0, max=10, v=0, cc="SmoothChange()", f=True, en=False)
        btn_next_to_make_controllers = cmds.button(l="Next", c="expand_controller_section()", en=False)

        cmds.separator(w=700)

        cmds.setParent(main_layout)

        # *****************************************************************************************************************
        ui_controller_frame = cmds.frameLayout(l="Make Controllers", w=700, cll=True, cl=True)
        ui_controller_layout = cmds.columnLayout()
        cmds.text("now if you are done with the curve, use this button to create controllers")
        RedoCTRL = cmds.intSliderGrp(min=3, max=100, v=3, cc="CTRLRedo()", f=True, en=False)
        cmds.rowLayout(numberOfColumns=2)
        btn_cmaker = cmds.button(l="CTRL maker", c="CMaker()", en=False)
        btn_to_final_step = cmds.button(l="Next", c="make_chain_section()", en=False)
        cmds.setParent(ui_controller_layout)
        cmds.separator(w=700)
        cmds.setParent(main_layout)

        # *****************************************************************************************************************
        ui_chain_frame = cmds.frameLayout(l="Make Chains", w=700, cll=True, cl=True)
        ui_chain_layout = cmds.columnLayout()
        cmds.text("now if you are done, select your desired object and click next")
        cmds.rowLayout(numberOfColumns=3)
        btn_make_chain_from_selected_obj = cmds.button(l="Make Chain", c="FinalStep()", en=False)
        btn_make_chain = cmds.button(l="MakeChain Only", c="MakeChain()", en=False)
        cb_make_proxy = cmds.checkBox(l="Use Proxy Geo", cc="make_proxy_geo()", en=False)
        cmds.setParent(ui_chain_layout)
        cmds.setParent(main_layout)


