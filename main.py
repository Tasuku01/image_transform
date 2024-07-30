import os
import PySimpleGUI as sg
import display_layout
from image_transform import(
    update_image, handle_error, load_image, resize_image, convert_grayscale, rotate_image,
    flip_image, mirror_image, mosaic_image, reset_image, resize_image, save_image, compress_images_in_directory
)

#GUIタイトルと全体レイアウトをのせたWindowを定義。
#resizableでWindowサイズをマウスで変更できるようになる
window = sg.Window("画像加工アプリ", display_layout.layout, resizable=True)

original_image = None
tmp_image = None

#GUIの表示部分
while True:
    # ウィンドウ表示
    event, values = window.read()
    """
    if event == "圧縮":
        directory = values["-FOLDER-"]
        if directory:
            output_directory = os.path.join(directory, "compressed")
            compress_images_in_directory(directory, output_directory, quality=85)
            sg.popup("画像の圧縮が完了しました。")
    
    """
    
    if event == "圧縮":
        #directory = sg.popup_get_folder("圧縮するディレクトリを選択してください")
        directory = values["-FOLDER-"]
        if directory:
            output_directory = os.path.join(directory, "compressed")
            compress_images_in_directory(directory, output_directory, quality=20)
            sg.popup("画像の圧縮が完了しました。")
    
    
    """   元画像を表示するプログラム   """
    if event == "-FILE-":
        image_file = values["-FILE-"]
        if image_file:
            original_image, tmp_image = load_image(image_file)
            update_image(original_image, "-ORIGINAL-", window)

    if event == "-FOLDER-":
        folder_path = values["-FOLDER-"]
        if folder_path:
            True
            #sg.popup(f"{folder_path}")
    
    if event == "サイズ変更":
        new_image = resize_image(tmp_image)
        if new_image:
            tmp_image = new_image
            update_image(tmp_image, "-TRANSFORM-", window)

    if event == "白黒":
        new_image = convert_grayscale(tmp_image)
        if new_image:
            tmp_image = new_image
            update_image(tmp_image, "-TRANSFORM-", window)
        
    if event == "90°回転":
        new_image = rotate_image(tmp_image)
        if new_image:
            tmp_image = new_image
            update_image(tmp_image, "-TRANSFORM-", window)
            
    if event == "上下反転":
        new_image = flip_image(tmp_image)
        if new_image:
            tmp_image = new_image
            update_image(tmp_image, "-TRANSFORM-", window)

    if event == "左右反転":
        new_image = mirror_image(tmp_image)
        if new_image:
            tmp_image = new_image
            update_image(tmp_image, "-TRANSFORM-", window)

    if event == "モザイク":
        new_image = mosaic_image(tmp_image)
        if new_image:
            tmp_image = new_image
            update_image(tmp_image, "-TRANSFORM-", window)

    if event == "元に戻す":
        new_image = reset_image(original_image)
        if new_image:
            tmp_image = new_image
            update_image(tmp_image, "-TRANSFORM-", window)
    
    if event == "保存":
        save_image(tmp_image, original_image)
            
    if event == "終了" or event is None:
        break

window.close()