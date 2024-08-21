import PySimpleGUI as sg
import display_layout
from image_transform import(
    update_image, load_image, resize_image, convert_grayscale, rotate_image,
    flip_image, mirror_image, mosaic_image, reset_image, resize_image, save_image
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
    
    """   元画像を表示するプログラム   """
    if event == "-FILE-":
        image_file = values["-FILE-"]
        if image_file:
            original_image, tmp_image = load_image(image_file)
            update_image(original_image, "-ORIGINAL-", window)
            
    """   サイズ変更するプログラム   """
    if event == "サイズ変更":
        new_image = resize_image(tmp_image)
        if new_image:
            tmp_image = new_image
            update_image(tmp_image, "-TRANSFORM-", window)
    
    """   白黒表示するプログラム   """
    if event == "白黒":
        new_image = convert_grayscale(tmp_image)
        if new_image:
            tmp_image = new_image
            update_image(tmp_image, "-TRANSFORM-", window)
    
    """   90°回転するプログラム   """
    if event == "90°回転":
        new_image = rotate_image(tmp_image)
        if new_image:
            tmp_image = new_image
            update_image(tmp_image, "-TRANSFORM-", window)
    
    """   上下反転するプログラム   """        
    if event == "上下反転":
        new_image = flip_image(tmp_image)
        if new_image:
            tmp_image = new_image
            update_image(tmp_image, "-TRANSFORM-", window)

    """   左右反転するプログラム   """
    if event == "左右反転":
        new_image = mirror_image(tmp_image)
        if new_image:
            tmp_image = new_image
            update_image(tmp_image, "-TRANSFORM-", window)

    """   モザイク表示するプログラム   """
    if event == "モザイク":
        new_image = mosaic_image(tmp_image)
        if new_image:
            tmp_image = new_image
            update_image(tmp_image, "-TRANSFORM-", window)

    """   画像を初期状態に戻すプログラム   """
    if event == "元に戻す":
        new_image = reset_image(original_image)
        if new_image:
            tmp_image = new_image
            update_image(tmp_image, "-TRANSFORM-", window)
    
    """   保存   """
    if event == "保存":
        save_image(tmp_image, original_image)
    
    """   終了   """        
    if event == "終了" or event is None:
        break

window.close()