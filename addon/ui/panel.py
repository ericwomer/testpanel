from bpy.types import Panel
from bpy.types import UILayout

from .. import utils

class TestPanel(Panel):
    bl_idname = "VIEW_3D_PT_TestPanel"
    bl_category = "TestPanel"
    bl_label = "TestPanel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self,context):
        layout = self.layout
        column = layout.column()

        if self.is_popover:
            pass

        if not self.is_popover:
            panel_draw(self, column)
        pass

def panel_draw(self, column: UILayout):
    prefs = utils.common.prefs()

    box = column.box().column()
    box.props(prefs, 'test_bool')
    col = box.column()
    col.enabled = prefs.test_bool
    row = col.row(align=True)
    row.prop(prefs, 'test_enum', text='')
    if prefs.test_enum == 'FIRST':
        pass

    column.separator()



    