
# Blender Libraries 
from bpy.utils import register_classes_factory
from bpy.props import PointerProperty
from bpy.types import WindowManager

# Local Modules
from . import addon
from . import prefs

classes = [addon.TestPanelProps,prefs.TestPanelPrefs,]

class_register, class_unregister = register_classes_factory(classes)

def register():
    class_register()
    WindowManager.testpanel = PointerProperty(type=addon.TestPanelProps)

def unregister():
    del WindowManager.testpanel
    class_unregister()