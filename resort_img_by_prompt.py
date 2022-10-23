from pip._internal import main as _pip
import pnginfo
import sys
import os
import json

# Pillowバージョンを指定する場合
pillow_ver = None

try:
    from PIL import Image
    # importlib.import_module("Pillow")

except ImportError:
    try:
        if pillow_ver is None:
            _pip(["install", "Pillow"])
        else:
            _pip(["install", "{}=={}".format("Pillow", pillow_ver)])

        # importlib.import_module("Pillow")
        from PIL import Image

    except:
        print("can't import: {}".format("Pillow"))

def ResortImg():
    img = Image.open(sys.argv[1])