from pip._internal import main as _pip
import pnginfo
import sys
import os
import glob
import shutil

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


# def CheckImg(target_files, prompt):
#     prompt_list = []
#     if prompt.find(","):
#         prompt_list = prompt.split(",")
#     else:
#         prompt_list.append(prompt)

#     file_num = 0
#     for file in target_files:
#         if file.endswith(".png"):
#             Positive_Prompt = pnginfo.DisplayPrompt(file).lower()

#             for prompt_word in prompt_list:
#                 if Positive_Prompt.find(prompt_word) > -1:
#                     prompt_exist = True
#                 else:
#                     prompt_exist = False

#             if prompt_exist:
#                 file_num += 1
#     return file_num


def ResortImg(target_files, prompt, check_only=True):

    prompt_list = []
    if prompt.find(","):
        prompt = prompt.replace(" ","")
        prompt_list = prompt.split(",")
    else:
        prompt_list.append(prompt)

    target_dir = os.path.abspath(os.path.join(target_files[0], os.pardir))

    file_num = 0
    for file in target_files:
        if file.endswith(".png"):

            # print("Load Prompt")
            # print(file)
            Positive_Prompt = pnginfo.DisplayPrompt(file).lower()
            Positive_Prompt = Positive_Prompt.replace(" ", "")
            Positive_Prompt_list = Positive_Prompt.split(",")

            # 部分一致
            prompt_exist = 0
            for prompt_word in prompt_list:

                # 重複チェック
                prompt_exist_check_double = 0

                for Positive_Prompt_word in Positive_Prompt_list:
                    if Positive_Prompt_word.find(prompt_word) > -1:
                        prompt_exist_check_double += 1

                if prompt_exist_check_double > 0:
                    prompt_exist += 1


            # 完全一致
            # if prompt_word in Positive_Prompt_list:
            #     prompt_exist += 1
            #     print(prompt_word)
            # else:
            #     pass

            if prompt_exist == len(prompt_list):
                file_num += 1
                if not check_only:
                    # print(file + " True")
                    new_dir = target_dir + "\\" + prompt
                    if not os.path.exists(new_dir):
                        os.mkdir(new_dir)
                    shutil.move(file, new_dir + "\\" + os.path.basename(file))

    return file_num


if __name__ == '__main__':

    target_files = []
    # D&Dのファイルを全てリストに格納

    target_files = sys.argv[1:]
    # target_files.append(r"E:\GitHub\stable-diffusion-webui\outputs\txt2img-images\test.png")

    len_target_files = len(target_files)

    # すべてフォルダの場合、最初のフォルダの中身を対象にする
    all_dir = 0
    for target_file in target_files:
        if os.path.isdir(target_file):
            all_dir += 1

    if len(target_files) == all_dir:
        target_dir = target_files[0]
        target_files = glob.glob(target_files[0] + "/*")
    else:
        target_dir = os.path.abspath(os.path.join(target_files[0], os.pardir))

    # フォルダを対象から外す
    for target_file in target_files:
        if os.path.isdir(target_file):
            target_files.remove(target_file)

    # 対象のファイルを列挙
    file_num = 0
    print("選択ファイル:")
    for target_file in target_files:
        if target_file.endswith(".png"):
            print(target_file)
            file_num += 1
    print("対象フォルダ:" + os.path.basename(target_dir) + "  選択ファイル数:" + str(file_num))

    if all_dir > 1:
        if len_target_files == all_dir:
            print("複数フォルダがドロップされたため、最初のフォルダ( " + os.path.basename(target_dir) + " )内のファイルのみ対象としました")
        else:
            print("複数のフォルダとファイルがドロップされたため、フォルダを除外しました")

    # 作成するディレクトリの場所
    target_dir = os.path.abspath(os.path.join(target_files[0], os.pardir))

    target_prompt = input("検索するポジティブプロンプトを入力してください:")
    file_num = ResortImg(target_files, target_prompt, True)
    print("該当ファイル数:" + str(file_num))
    if file_num > 0:
        print(target_dir + "\\" + target_prompt)
        if input("該当ファイルを上記のフォルダへ移動します。よろしいですか？ Y/n:").lower() == "Y".lower():

            file_num = ResortImg(target_files, target_prompt, False)
            print(str(file_num) + "のファイルをフォルダ( " + target_prompt + " )へ移動しました")

        else:
            print("キャンセルされました")
    else:
        print("該当ファイルはありませんでした")

    os.system("PAUSE")
