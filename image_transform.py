import PySimpleGUI as sg
from PIL import Image, ImageOps
import io
import display_layout

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
            # 元画像を表示
            original_image = Image.open(image_file)
            tmp_image = original_image
            #print(tmp_image)
            bio = io.BytesIO()
            original_image.thumbnail((450, 450))  # 画像サイズを調整
            original_image.save(bio, format="PNG")
            window["-ORIGINAL-"].update(data=bio.getvalue())
    
    """   サイズ変更のプログラム   """
    if event == "サイズ変更":
        if tmp_image is not None:
            # 画像をリサイズ
            new_width = sg.popup_get_text("幅を入力して下さい。")
            new_height = sg.popup_get_text("高さを入力して下さい。")
            #print(new_width)
            #print(new_height)
            if new_width and new_height:
                try:
                    transform_image = tmp_image.resize((int(new_width), int(new_height)))
                    tmp_image = transform_image
                    bio = io.BytesIO()
                    tmp_image.save(bio, format="PNG")
                    window['-TRANSFORM-'].update(data=bio.getvalue())
                    print("サイズが変更されました")
                except ValueError:
                   sg.popup_error('幅と高さは数値で入力して下さい。') 
            else:
                sg.popup_error("幅・高さを入力して下さい。")
        else:
            sg.popup_error("元画像を選んで下さい。")
    
    """   白黒のプログラム   """            
    if event == "白黒":
        if tmp_image is not None:
             # 画像をグレースケールに変換
            transform_image = tmp_image.convert("L")
            tmp_image = transform_image
            #print(tmp_image)
            bio = io.BytesIO()
            tmp_image.save(bio, format="PNG")
            window["-TRANSFORM-"].update(data=bio.getvalue())
        else:
            sg.popup_error("元画像を選んで下さい。")
        
    """   90°回転のプログラム   """    
    if event == "90°回転":
        if tmp_image is not None:
            transform_image = tmp_image.rotate(-90)
            tmp_image = transform_image
            #print(tmp_image)
            bio = io.BytesIO()
            tmp_image.save(bio, format="PNG")
            window['-TRANSFORM-'].update(data=bio.getvalue())
        else:
            sg.popup_error("元画像を選んで下さい。")
        
    """   上下反転のプログラム   """    
    if event == "上下反転":
        if tmp_image is not None:
            transform_image = ImageOps.flip(tmp_image)
            tmp_image = transform_image
            #print(tmp_image)
            bio = io.BytesIO()
            tmp_image.save(bio, format="PNG")
            window['-TRANSFORM-'].update(data=bio.getvalue())
        else:
            sg.popup_error("元画像を選んで下さい。")
        
    """   左右反転のプログラム   """    
    if event == "左右反転":
        if tmp_image is not None:
            transform_image = ImageOps.mirror(tmp_image)
            tmp_image = transform_image
            #print(tmp_image)
            bio = io.BytesIO()
            tmp_image.save(bio, format="PNG")
            window['-TRANSFORM-'].update(data=bio.getvalue())
        else:
            sg.popup_error("元画像を選んで下さい。")
        
    """   モザイクのプログラム   """
    if event == "モザイク":
        if tmp_image is not None:
            #モザイク度合いを調整
            pixel_size = 10
            transform_image = tmp_image.resize(
                (tmp_image.width // pixel_size, tmp_image.height // pixel_size),
                resample=Image.NEAREST
            ).resize(tmp_image.size, resample=Image.NEAREST)
            tmp_image = transform_image
            #print(tmp_image)
            bio = io.BytesIO()
            tmp_image.save(bio, format="PNG")
            window['-TRANSFORM-'].update(data=bio.getvalue())
        else:
            sg.popup_error("元画像を選んで下さい。")
        
    """   元に戻すプログラム   """
    if event == "元に戻す":
        if tmp_image is not None:
            # 元画像を表示
            tmp_image = Image.open(image_file)
            #print(tmp_image)
            bio = io.BytesIO()
            tmp_image.thumbnail((450, 450))  # 画像サイズを調整
            tmp_image.save(bio, format="PNG")
            window["-TRANSFORM-"].update(data=bio.getvalue())
        else:
            sg.popup_error("元画像を選んで下さい。")
        
    """   保存のプログラム   """
    if event == "保存":
        if tmp_image is not None:
            if tmp_image == original_image:
                sg.popup_error("画像が加工されていません。")
                #print(tmp_image)
            else:    
                save_path = sg.popup_get_file("保存先を選択して下さい。", save_as=True, file_types=(("PNG Files", "*.png"),))
                if save_path:
                    tmp_image.save(save_path)
        else:
            sg.popup_error("加工後の画像がありません。")
        
    """   終了のプログラム   """
    if event == "終了":
        window.close()
    
    #クローズボタンの処理
    if event is None:
        print("exit")
        break

window.close()