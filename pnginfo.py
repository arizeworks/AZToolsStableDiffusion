from pip._internal import main as _pip
import sys
import os
# import subprocess
# import importlib

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


try:
    img = Image.open(sys.argv[1])
    if img.text["parameters"]:
        print(img.text["parameters"])
except:
    print("Nothing found in the image.")

# subprocess.call('PAUSE', shell=True)
os.system("PAUSE")
