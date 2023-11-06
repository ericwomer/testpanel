# import bpy
from . import ui
from . import props

def register():
    ui.register()
    props.register()

def unregister():
    props.unregister()
    ui.unregister()
