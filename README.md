# AZTools for Stable Diffusion

StableDiffusionの便利ツールまとめ


### git_pull.bat

```
Gitがインストール済みの場合、実行するとこのリポジトリが最新版へ更新されます。
```

<br>

### Pythonファイルの使い方
```
このリポジトリを任意の場所に配置して、
Pythonファイルのショートカットを作成して使ってください。

対応バージョン : Python3.10.6~
```

<br>

### pnginfo.py

```
注意:Pillowがインストールされていない場合、自動的にインストールを行います。

StableDiffusionのメタデータが含まれているpng画像を
ドラッグ＆ドロップするとプロンプトを表示します。

NovelAI製の画像の場合、
Stable Diffusion Web UIのフォーマットへ変換して表示します。
```
![image](https://user-images.githubusercontent.com/56951093/197378895-114a4b70-b357-4155-8507-ffcdbbf524b9.png)

<br>

### resort_img_by_prompt.py

```
注意:オリジナルのresort_img_by_prompt.pyはpnginfo.pyと同じディレクトリに配置する必要があります。

フォルダまたはファイルをドラッグ&ドロップして、
プロンプト（ポジティブプロンプト・1単語のみ）を入力すると、
そのプロンプトが含まれたpng画像のみを一括でフォルダにまとめます。
フォルダ名はプロンプト名になります。

ファイル（複数）をD&Dした場合、そのファイルのカレントディレクトリにフォルダが作成されます。
フォルダをD&Dした場合、その直下のファイルが検索対象となります。検索対象と同じディレクトリにフォルダが作成されます。
（フォルダとファイルを複数D&Dした場合、ファイルのみが対象となります。）
（フォルダのみを複数D&Dした場合、最初のフォルダが対象となります。）
```
![image](https://user-images.githubusercontent.com/56951093/197391370-e76931be-da6c-4b51-bb83-4f21225997ca.png)

<br>
<br>
