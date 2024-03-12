import maya.cmds as cmds


def curve_type(options):

    curve_type = cmds.radioButtonGrp(options, q=True, sl=True)
    if curve_type == 1:
        cmds.confirmDialog(m="Linear curves can not be smoothened.")
    print(curve_type)
    return curve_type

def span_mod(span_count):
    # cmds.textScrollList(curve_scroll_list, e=True, en=False)
    selected_curve = cmds.ls(sl=True, long=True, type="nurbsCurve")
    print(selected_curve)
    if not selected_curve:
        cmds.warning('Please selected a curve and try again')
        return

    cmds.select(selected_curve)
    selectedCurve = cmds.ls(sl=True)
    cmds.rebuildCurve(selectedCurve, rpo=True, kep=True, rt=0, s=span_count, d=curve_type)
    curve = cmds.select(selectedCurve)
    return curve

def update_smoothness(curve, new_smoothness):
    global isFirstTime
    if not isFirstTime:
        cmds.undo()

    curve = cmds.ls(curve, sl=True)
    cmds.smoothCurve(curve[0] + ".cv[*]", s=new_smoothness)
    cmds.select(curve)
    isFirstTime = False


