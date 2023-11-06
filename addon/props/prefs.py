import bpy

from .. import utils

class TestPanelPrefs(bpy.types.AddonPreferences):
    bl_idname = utils.common.module()

    test_string: bpy.props.StringProperty(
        name='Test String',
        description='String for testing',
        default='Empty String isnt so Empty is it?',
        subtype='DIR_PATH',
    )

    test_bool: bpy.props.BoolProperty(
        name = 'Test Bool',
        description='Bool for testing purposes',
        default=False,
    )

    test_bool_string: bpy.props.StringProperty(
        name='Test Bool String Reveal',
        description='You see this if test_bool is set to true',
        default='Empty String Again?'
    )

    test_bool_bool: bpy.props.BoolProperty(
        name = 'Test Bool Bool',
        description='You see this if test_bool is set to true',
        default=False,
    )

    test_int: bpy.props.IntProperty(
        name='Test Int',
        description='Testing the int property',
        default=2,
        min=1,
        max=60
    )

    test_enum: bpy.props.EnumProperty(
        name='Test Enum',
        items=[
            ('FIRST', 'First Enum', 'The first testing enum'),
            ('SECOND', 'Second Enum', 'The secton testing enum'),
            ('THIRD', 'Third Enum', 'The third testing enum'),
        ],
        default='FIRST',
    )

    def draw(self, context):
        layout = self.layout
        
        utils.ui.draw_prop(layout, 'Test String', self, 'test_string')
        utils.ui.draw_prop(layout, 'Test Bool', self, 'test_bool')

        col = layout.column()
        col.enabled = self.test_bool
        utils.ui.draw_prop(layout, 'Test Bool String', self, 'test_bool_string')

        col = layout.column()
        col.enabled = self.test_bool
        utils.ui.draw_prop(layout, 'Test Bool Bool', self, 'test_bool_bool')

        utils.ui.draw_prop(layout, 'Test Int', self, 'test_int')
        utils.ui.draw_prop(layout, 'Test Enum', self, 'test_enum')

