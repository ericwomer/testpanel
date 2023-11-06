# import bpy

def draw_prop(layout, text, data, prop):
    row = layout.row()
    row.label(text=text)
    row.prop(data, prop, text='')