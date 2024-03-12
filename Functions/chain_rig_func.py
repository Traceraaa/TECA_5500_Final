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

def controller_redo(selected_curve, new_span):
    global selected_curve_name

    try:
        cmds.delete("AllLocators")
    except:
        pass

    cmds.select(selected_curve_name)
    selected_curve = cmds.ls(sl=True)

    cmds.rebuildCurve(selected_curve, rpo=True, kep=True, rt=0, s=new_span)
    cmds.select(selected_curve)
    make_controller()

def make_controller(selected_curve):
    selected_curve = cmds.ls(sl=True)
    EPlist = cmds.ls(selected_curve[0] + ".ep[*]", fl=True)
    chain_count = len(EPlist)
    locList = []
    # now with having those two lists we can create locators and dump them on each point in order
    for ep in EPlist:
        cmds.select(ep, r=True)
        cmds.pointCurveConstraint()
        cmds.CenterPivot()
        locList.append(cmds.rename("EPCTRL1"))
    cmds.select(locList)
    cmds.group(n="AllLocators")
    cmds.select(selected_curve)
    cmds.select(cl=True)
    return chain_count

def make_chain(selected_curve, chain_count):

    selectedOBJ = cmds.ls(sl=True)
    cmds.select(selectedOBJ, r=True)
    cmds.select(selected_curve, add=True)
    cmds.pathAnimation(fm=True, f=True, fa="x", ua="y", wut="vector", wu=(0, 1, 0), inverseFront=False, iu=False,
                       b=False, stu=1, etu=chain_count)
    cmds.select(selectedOBJ, r=True)

    AnimCTList = cmds.ls("EPCTRL*", tr=True)
    cmds.selectKey('motionPath1_uValue', time=(1, chain_count))
    cmds.keyTangent(itt="linear", ott="linear")
    chainLinks = []

    for curkey in range(1, chain_count + 1):
        cmds.currentTime(curkey)
        cmds.select(selectedOBJ, r=True)
        cmds.FreezeTransformations()
        cmds.duplicate()
        cmds.select(AnimCTList[curkey - 1], add=True)
        cmds.parentConstraint(w=1.0)
        chainLinks.append(cmds.rename("CLink1"))

    cmds.select(chainLinks)
    cmds.group(n="AllLinks")
    linksCount = len(chainLinks)

    for i in range(1, linksCount, 2):
        cmds.currentTime(i)
        cmds.select(chainLinks[i])
        cmds.setAttr(chainLinks[i] + ".rx", 90)
    cmds.DeleteMotionPaths()




def make_proxy():
    proxy_geo = cmds.polyTorus(n="ProxyGeo", sa=10, sh=10, sr=0.3)
    edges_to_scale = []
    edges_template = ["pTorus1.e[109]", "pTorus1.e[119]", "pTorus1.e[129]", "pTorus1.e[139]", "pTorus1.e[149]",
                      "pTorus1.e[159]", "pTorus1.e[169]", "pTorus1.e[179]", "pTorus1.e[189]", "pTorus1.e[199]",
                      "pTorus1.e[104]", "pTorus1.e[114]", "pTorus1.e[124]", "pTorus1.e[134]", "pTorus1.e[144]",
                      "pTorus1.e[154]", "pTorus1.e[164]", "pTorus1.e[174]", "pTorus1.e[184]", "pTorus1.e[194]"]

    for edge in edges_template:
        suffix_name = edge.split(".")[-1]
        new_edge_name = "ProxyGeo." + str(suffix_name)
        edges_to_scale.append(new_edge_name)

    cmds.select(cl=True)
    cmds.select(edges_to_scale)
    cmds.scale(0.828, 1, 1, )
    cmds.select(proxy_geo)

def update_chain():

    try:
        cmds.delete("AllLinks")
        cmds.select(user_selected_mesh)
    except:
        pass

    cmds.delete(mp=True)

    if user_selected_mesh == proxy_geo:
        cmds.select(proxy_geo)
        cmds.setAttr(proxy_geo[0] + ".translateX", 0.0)
        cmds.setAttr(proxy_geo[0] + ".translateY", 0.0)
        cmds.setAttr(proxy_geo[0] + ".translateZ", 0.0)
        cmds.setAttr(proxy_geo[0] + ".rotateX", 0.0)
        cmds.setAttr(proxy_geo[0] + ".rotateY", 0.0)
        cmds.setAttr(proxy_geo[0] + ".rotateZ", 0.0)


