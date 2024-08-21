import io
import PySimpleGUI as sg
from PIL import Image, ImageOps, ImageFile

# Pillowのデフォルトのテキストチャンクメモリ制限を変更
ImageFile.LOAD_TRUNCATED_IMAGES = True

def update_image(image, key, window):
    bio = io.BytesIO()
    image.save(bio, format="PNG")
    #image.save(bio, format="jpeg")
    window[key].update(data=bio.getvalue())

def handle_error(message):
    sg.popup_error(message)


def load_image(filepath):
    original_image = Image.open(filepath)
    original_image.thumbnail((450, 450))
    #original_image.thumbnail((500, 500))
    tmp_image = original_image.copy()
    return original_image, tmp_image

def resize_image(tmp_image):
    if tmp_image:
        new_width = sg.popup_get_text("幅を入力してください。")
        new_height = sg.popup_get_text("高さを入力してください。")
        if new_width and new_height:
            try:
                resized_image = tmp_image.resize((int(new_width), int(new_height)))
                return resized_image
            except ValueError:
                handle_error("幅と高さは数値で入力してください。")
        else:
            handle_error("幅と高さを入力してください")
    else:
        handle_error("元画像を選んで下さい。")

def convert_grayscale(tmp_image):
    if tmp_image:
        return tmp_image.convert("L")
    else:
        handle_error("元画像を選んで下さい。")
    return None

def rotate_image(tmp_image):
    if tmp_image:
        return tmp_image.rotate(-90)
    else:
        handle_error("元画像を選んで下さい。")
    return None

def flip_image(tmp_image):
    if tmp_image:
        return ImageOps.flip(tmp_image)
    else:
        handle_error("元画像を選んで下さい。")
    return None

def mirror_image(tmp_image):
    if tmp_image:
        return ImageOps.mirror(tmp_image)
    else:
        handle_error("元画像を選んで下さい。")
    return None

def mosaic_image(tmp_image):
    if tmp_image:
        pixel_size = 7
        return tmp_image.resize((tmp_image.width // pixel_size, tmp_image.height // pixel_size), resample=Image.NEAREST).resize(tmp_image.size, resample=Image.NEAREST)
    else: 
        handle_error("元画像を選んで下さい。")
    return None

def reset_image(original_image):
    if original_image:
        return original_image.copy()
    else:
        handle_error("元画像を選んで下さい。")
    return None

def save_image(tmp_image, original_image):
    if tmp_image and tmp_image != original_image:
        save_path = sg.popup_get_file("保存先を選択して下さい。", save_as=True, file_types=(("PNG Files", "*.png"),))
        if save_path:
            tmp_image.save(save_path)
    else:
        handle_error("元画像を選んで下さい。")