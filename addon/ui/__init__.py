from bpy.utils import register_classes_factory
from . import panel

classes = [panel.TestPanel,]

class_register, class_unregister = register_classes_factory(classes)

def register():
    class_register()

def unregister():
    class_unregister()