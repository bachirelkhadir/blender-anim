import os
import sys
import hashlib
from pathlib import Path
from random import randint
import bpy
from mathutils import Vector


import src.utils as utils
sys.path.append(utils.get_current_path())

import src.tex_file_writing as tex2bpy



TEX_USE_CTEX = False
TEX_TEXT_TO_REPLACE = "YourTextHere"
RESOLUTION = (800, 600)


CURRENT_PATH = utils.get_current_path()
TEX_DIR = os.path.join(CURRENT_PATH, "temps/")
ASSETS_DIR = os.path.join(CURRENT_PATH, "assets/")
OUTPUTS_DIR = os.path.join(CURRENT_PATH, "outputs/")
TEMPLATE_TEX_FILE = os.path.join(
    ASSETS_DIR,
    "tex_template.tex"
)


RIGHT = Vector([1, 0, 0])
UP = Vector([0, 1, 0])
OUT = Vector([0, 0, 1])
LEFT = -RIGHT
DOWN = -UP
IN = -OUT



for path_dir in (ASSETS_DIR, TEX_DIR, OUTPUTS_DIR):
    utils.create_folder_if_needed(path_dir)
