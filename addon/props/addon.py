from bpy.types import AddonPreferences
from bpy.types import PropertyGroup
from bpy.props import StringProperty

from typing import Tuple

from .. import ui 
from .. import utils 

name = __name__.partition('.')[0]

class TestPanelProps(PropertyGroup):
    addon: StringProperty(
        name='Addon',
        description='TestPanel Module',
        default=name,
        )
    
    @property
    def prefs(self) -> AddonPreferences:
        return utils.common.prefs() 

    @staticmethod
    def draw(self, column):
        ui.panel.panel_draw(self, column)
