bl_info = {
    "name": "Test Panel",
    "author": "EWomer",
    "version": (0,0,1),
    "blender": (3,0,0),
    "location": "Unknown",
    "category": "Development",
}

import bpy
from . import addon

def register():
    addon.register() 

def unregister():
    addon.unregister()

if __name__=="__main__":
    register()
