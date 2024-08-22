# Shinsplat Tarterbox

"""
@author: Shinsplat
@title: Shinsplat
@nickname: shinsplat
@description:
whatever
@license:
If you infer one you're making a mistake.  Your output belongs to you, the code belongs to, most likely not you.
"""

from .python import *
from .python_more import *
# --------------------------------------------------------------------------------
#
# --------------------------------------------------------------------------------
NODE_CLASS_MAPPINGS = {
    "Python (Shinsplat)": Shinsplat_Python,
    "Python - More Inputs (Shinsplat)": Shinsplat_PythonMore,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "Python (Shinsplat)": "Python (Shinsplat)",
    "Python - More Inputs (Shinsplat)": "Python - More Inputs (Shinsplat)",
}
WEB_DIRECTORY = "./web"
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS', 'WEB_DIRECTORY']
# --------------------------------------------------------------------------------
#
# --------------------------------------------------------------------------------
