import blenderbim.tool as tool
import ifcopenshell

model = tool.Ifc.get()

annotations = model.by_type('IfcAnnotation')

for annotation in annotations:
    if annotation.ObjectType == 'DRAWING':
        psets = ifcopenshell.util.element.get_psets(annotation)
        pset = psets['EPset_Drawing']
        pset_ifc = model.by_id(pset['id'])
        ifcopenshell.api.run("pset.edit_pset", model, pset = pset_ifc, properties = {
            'Stylesheet' : pset['Stylesheet'].replace('\\', '/'),
            'Markers' : pset['Markers'].replace('\\', '/'),
            'Symbols' : pset['Symbols'].replace('\\', '/'),
            'Patterns' : pset['Patterns'].replace('\\', '/'),
        })

