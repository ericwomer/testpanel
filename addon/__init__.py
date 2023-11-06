# import bpy
from . import props
from . import ui

def register():
    ui.register()
    props.register()

def unregister():
    props.unregister()
    ui.unregister()
