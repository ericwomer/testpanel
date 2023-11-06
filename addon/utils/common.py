from bpy import context
from bpy.types import AddonPreferences

from .. import props

def module() -> str:
    return props.addon.name

def prefs() -> AddonPreferences:
    return context.preferences.addons[module()].preferences
