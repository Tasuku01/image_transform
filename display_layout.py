import PySimpleGUI as sg
from PIL import Image
import os

#テーマカラーをsg.themeで設定
sg.theme("BlueMono")

#画像を表示するフレームの幅,高さを定義
width = 500
height = 500

"""
#画像を選択するフレーム
frame1 = [sg.Text("画像を選択してください。")]
frame2 = [
          sg.InputText(key='-FILE-', enable_events=True),
          sg.FileBrowse("参照")
          ]

#画像を加工するボタンを表示するフレーム
frame3 = [sg.Text("加工の種類を選んで下さい。")]
frame4 = [
          sg.Button("サイズ変更"),
          sg.Button("白黒"),
          sg.Button("90°回転"),
          sg.Button("上下反転"),
          sg.Button("左右反転"),
          sg.Button("モザイク"),
          sg.Button("元に戻す")
          ]
"""

#画像を選択するフレーム
frame1 = [sg.Text("画像を選択してください。")]
frame2 = [
          sg.InputText(key='-FILE-', enable_events=True),
          sg.FileBrowse("参照")
          ]

#画像を加工するボタンを表示するフレーム
frame3 = [sg.Text("加工の種類を選んで下さい。")]
frame4 = [
          sg.Button("サイズ変更"),
          sg.Button("白黒"),
          sg.Button("90°回転"),
          sg.Button("上下反転"),
          sg.Button("左右反転"),
          sg.Button("モザイク"),
          sg.Button("元に戻す")
          ]


#加工前の元画像を表示するフレーム
frame5 = sg.Frame('',
                  [
                    # テキストレイアウト
                    [sg.Text("元の画像")],
                    #元の画像を表示
                    [sg.Image(key="-ORIGINAL-")]
                  ],
                    size=(width, height)
                  )

#加工後の画像を表示するフレーム
frame6 = sg.Frame('',
                  [
                    [sg.Text("加工後の画像")],
                    [sg.Image(key="-TRANSFORM-")]
                  ], 
                    size=(width, height)
                  )

#保存・終了ボタンを表示するフレーム
frame7 = [sg.Text("これで良ければ保存、終了したい場合は終了ボタンを押して下さい。")]
frame8 = [
          sg.Button("保存"),
          sg.Button("終了"),
          #sg.Button("ディレクトリ圧縮")
          ]
"""
frame9 = [sg.Text("圧縮するフォルダを選択してください。選択したら「圧縮」を押してください。")]
frame10 = [
          sg.InputText(key='-FOLDER-', enable_events=True),
          sg.FolderBrowse("参照"),
          sg.Button("圧縮")
          ]
#frame11 = [sg.Button("圧縮")]
"""

#全体レイアウト
#layout = [[sg.Column(left_column), sg.VSeparator(), sg.Column(right_column)], [frame5, frame6], frame7, frame8]

left_column = [frame1, frame2]
right_column = [frame3, frame4]


#layout = [[frame1, frame2, frame3, frame4, frame5, frame6], frame7, frame8]
#layout = [[sg.Column(left_column), sg.Column(right_column)], [frame5, frame6], frame7, frame8]

layout = [[sg.Column(left_column), sg.Column(right_column)], [frame5, frame6], frame7, frame8]
#layout = [[sg.Column(left_column), sg.Column(right_column)], frame9, frame10, [frame5, frame6], frame7, frame8]
