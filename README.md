# AZTools for Stable Diffusion

StableDiffusion の便利ツールまとめ

<br>

## git_pull.bat

```
Gitがインストール済みの場合、実行するとこのリポジトリが最新版へ更新されます。
```

<br>

## Python ファイルの使い方

```
このリポジトリを任意の場所に配置して、
Pythonファイルのショートカットを作成して使ってください。

推奨バージョン : Python3.10.6~
```

<br>

## pnginfo.py

#### png 画像のプロンプトを表示

```
注意: Pillowがインストールされていない場合、自動的にインストールを行います。

StableDiffusionのメタデータが含まれているpng画像を
このPythonファイル（のショートカット）にドラッグ＆ドロップするとプロンプトを表示します。

NovelAI製の画像の場合、
Stable Diffusion Web UIのフォーマットへ変換して表示します。
```

![image](https://user-images.githubusercontent.com/56951093/197378895-114a4b70-b357-4155-8507-ffcdbbf524b9.png)

<br>

## resort_img_by_prompt.py

#### 特定のポジティブプロンプトを含む画像をフォルダにまとめる

```
注意: オリジナルの resort_img_by_prompt.py は pnginfo.py と同じディレクトリに配置する必要があります。

フォルダまたはファイルをこのPythonファイル（のショートカット）にドラッグ&ドロップして、
ポジティブプロンプトを入力すると、
そのプロンプトのメタデータが含まれたpng画像のみを一括でフォルダにまとめます。
フォルダ名はプロンプト名になります。

複数のプロンプトに対応しました。
ワードはカンマ（,）で区切ってください。
ワードは部分一致した場合、対象になります。

例
　　検索するプロンプト）girl, best

　対象となるファイル例）1 girl, best quality

対象外となるファイル例）girl, quality, illustration


ファイル（複数）をD&Dした場合、そのファイルのカレントディレクトリにフォルダが作成されます。
フォルダをD&Dした場合、その直下のファイルが検索対象となります。検索対象と同じディレクトリにフォルダが作成されます。
（フォルダとファイルを複数D&Dした場合、ファイルのみが対象となります。）
（フォルダのみを複数D&Dした場合、最初のフォルダが対象となります。）
```

![image](https://user-images.githubusercontent.com/56951093/197391370-e76931be-da6c-4b51-bb83-4f21225997ca.png)

<br>
<br>
