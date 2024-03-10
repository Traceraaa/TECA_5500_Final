import maya.cmds as cmds


class TreadRigging(object):
    def __init__(self):
        super(TreadRigging, self).__init__()

    def build_ui(self):
        main_layout = cmds.columnLayout()

        UI_WARNING_BGC = [1, 1, 0]
        # Initialize
        uiInitFrame = cmds.frameLayout(l="Initialize", w=500, cll=True)
        uiInitCL = cmds.columnLayout()

        cmds.text(l="Creating two locators in the scene. Front and Back")
        initButton = cmds.button(l="Initialize", c="initFunc()")
        cmds.setParent(main_layout)
        cmds.separator(w=500)

        # Make Curve
        uiCurveFrame = cmds.frameLayout(l="Create Curve", w=500, cll=True, en=False)
        uiCurveCL = cmds.columnLayout()

        cmds.text(l="Requirement!", fn="boldLabelFont", bgc=UI_WARNING_BGC)
        cmds.text(l="Position the two locators at the front and back end of your curve. And then hit the button")
        MakeCurveBTN = cmds.button(l="Make Tread Curve", c="MakeCurve()", en=False)
        cmds.setParent(main_layout)
        cmds.separator(w=500)

        # Create Tread
        uiCreateFrame = cmds.frameLayout(l="Create Tread", w=500, cll=True, en=False)
        uiCreateCL = cmds.columnLayout()

        cmds.text(l="Requirement!", fn="boldLabelFont", bgc=UI_WARNING_BGC)
        cmds.text(l="Select default or pick your own tread peice. Hit the Update button to observe the change")
        peicesel = cmds.radioButtonGrp(label='Pick Tread Peice ',
                                                  labelArray2=['Default', 'Pick your own peice'],
                                                  numberOfRadioButtons=2, sl=1,
                                                  cc1='defaulttread()', cc2='picktread()', en=False)

        ObjText = cmds.textFieldButtonGrp(bl="Pick Tread OBJ", bc="PickingObject()", ed=False, en=False)
        CopyNum = cmds.intSliderGrp(min=10, v=25, cc="numChange()", f=True, en=False)

        cmds.rowLayout(numberOfColumns=2, columnWidth2=(250, 250), adjustableColumn=2, columnAlign=(1, 'right'),
                       columnAttach=[(1, 'both', 0), (2, 'both', 0)])
        makeTread = cmds.button(l="MakeTread", c="MakeTankTread()", en=False)
        updatetreadpeice = cmds.button(l="Update Tread Piece", c="updateTread()", en=False)

        cmds.setParent(main_layout)
        cmds.separator(w=500)

        # Finalize and Reset
        cmds.text(l="")
        cmds.rowLayout(numberOfColumns=2, columnWidth2=(250, 250), adjustableColumn=2, columnAlign=(1, 'right'),
                       columnAttach=[(1, 'both', 0), (2, 'both', 0)])
        FinalizeThread = cmds.button(l="Finalize Tread", c="FinThread()", en=False, h=40, bgc=[0, 0.7, 0])
        ResetBTN = cmds.button(l="Reset All", c="resetAll()", en=False, h=40, bgc=[0.7, 0, 0])