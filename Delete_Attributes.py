# Delete Prims Attributes
node = hou.pwd()
geo = node.geometry()


prim_attribs = geo.primAttribs()

for attr in prim_attribs:
    if attr.dataType() != hou.attribData.String:
        continue
    allValues = set(geo.primStringAttribValues(attr.name()))
    if allValues == set([""]):
        attr.destroy()
