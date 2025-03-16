import hou
import random

def merge_tool():
    result, name = hou.ui.readInput("Enter a name:", buttons=("OK", "Cancel"))
    color = hou.ui.selectColor()
    
    
    sel = hou.selectedNodes()
    root = sel[0].parent()
    
    node_pos = []
    mid_pos = 0
    p_pos=[]
    for p in sel:
        p_pos = p.position()
        node_pos.append(p_pos[0])
        mid_pos = (node_pos[0]+node_pos[-1])*0.5
    
    
    
    if(result==1):
        exit
    else:
        merge = root.createNode("object_merge", name + "_merge")
        merge.parm("numobj").set(len(sel))
        merge.setPosition(hou.Vector2(mid_pos, p_pos[1]-4))
        merge.setColor(color)
        
        
        
        count = 1
        for i in sel:
            null = root.createNode("null", name+ "_null_" + str(count))
            null_pos = i.position()
            null.setInput(0,i)
            null.setColor(color)
            null.setPosition(hou.Vector2(null_pos[0], null_pos[1]-1.5))
            
            
            op = null.path()
            op = "../" + op.split("/")[-1]
            merge.parm("objpath"+str(count)).set(op)
            count+=1

merge_tool()
