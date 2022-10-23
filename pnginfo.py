from pip._internal import main as _pip
import sys
import os
import json
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


def DisplayPrompt(img):
    img = Image.open(img)

    # NovelAI
    Positive_Prompt = ""
    if "Software" in img.text:
        if img.text["Software"] == "NovelAI":
            # print("Software :" + img.text["Software"])

            # if "Source" in img.text:
            #     print("Source :" + img.text["Source"])

            if "Description" in img.text:
                Positive_Prompt = img.text["Description"].replace("{","(")
                Positive_Prompt = Positive_Prompt.replace("}",")")
                Positive_Prompt = Positive_Prompt.replace("\"","")

                if __name__ == '__main__':
                    print(Positive_Prompt)

            if "Comment" in img.text:
                Comment_dict = json.loads(img.text["Comment"])
                if "uc" in Comment_dict:

                    Negative_prompt = Comment_dict["uc"].replace("{","(")
                    Negative_prompt = Negative_prompt.replace("}",")")
                    Negative_prompt = Negative_prompt.replace("\"","")

                    if __name__ == '__main__':
                        print("Negative prompt: " + Negative_prompt)

                    if Comment_dict["sampler"] == "k_euler_ancestral":
                        Sampler = "Euler a"
                    elif Comment_dict["sampler"] == "k_euler":
                        Sampler = "Euler"
                    elif Comment_dict["sampler"] == "k_lms":
                        Sampler = "LMS"
                    elif Comment_dict["sampler"] == "plms":
                        Sampler = "PLMS"
                    elif Comment_dict["sampler"] == "ddim":
                        Sampler = "DDIM"
                    else:
                        Sampler = "Euler a"

                    w, h = img.size
                    img_size = str(w) + "x" + str(h)

                    if __name__ == '__main__':
                        print("Steps: " + str(Comment_dict["steps"]) + ", " +
                            "Sampler: " + Sampler + ", " +
                            "CFG scale: " + str(Comment_dict["scale"]) + ", " +
                            "Seed: " + str(Comment_dict["seed"]) + ", " +
                            "Size: " + img_size + ", " +
                            # "Noise: 不明" + Comment_dict["noise"] ","+
                            "Denoising strength: " + str(Comment_dict["strength"]) + ", " +
                            "Clip skip: 2, " +
                            "ENSD: 31337"
                            )

        else:
            if __name__ == '__main__':
                print("Nothing found in the image.")

    # Stable Diffusion Web UI
    elif "parameters" in img.text:
        if __name__ == '__main__':
            print("Stable Diffusin Web UI")
            print(img.text["parameters"])

        prompt = img.text["parameters"].split("Negative prompt: ")
        Positive_Prompt = prompt[0]


    else:
        if __name__ == '__main__':
            print("Nothing found in the image.")

    return Positive_Prompt


if __name__ == '__main__':

    try:
        img = sys.argv[1]
    except:
        img = r"C:\Users\User\Desktop\test.png"

    DisplayPrompt(img)

    # subprocess.call('PAUSE', shell=True)
    os.system("PAUSE")
