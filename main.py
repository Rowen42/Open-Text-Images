import os
import pandas as pd
import cv2
import pyautogui
from PIL import Image, ImageDraw, ImageFont
import random
import matplotlib.font_manager as fm

def get_compatible_system_fonts():
    system_fonts = fm.findSystemFonts(fontext='ttf')
    compatible_fonts = []

    for font_path in system_fonts:
        try:
            ImageFont.truetype(font_path, 12)
            compatible_fonts.append(font_path)
        except Exception as e:
            print(f"Font not compatible: {font_path}, Error: {e}")
    return compatible_fonts

# Get the system fonts that are compatible with Pillow
compatible_fonts = get_compatible_system_fonts()

# If no compatible fonts are found, raise an exception
if not compatible_fonts:
    raise Exception("No compatible fonts found on this system.")

# Randomly select a font from the compatible list
def get_random_font():
    return random.choice(compatible_fonts)

def generate_random_colour():
    return tuple(random.randint(0, 255) for _ in range(3))

def create_image_from_text(text, filename, size=(800, 600), font_size=36, default_font_size=36):
    img = Image.new('RGB', size, color=generate_random_colour())
    draw = ImageDraw.Draw(img)

    max_font_size = 200
    text_width, text_height = 0, 0
    font = None

    random_font_path = get_random_font()
    font = ImageFont.truetype(random_font_path, font_size)

    for fs in range(font_size, max_font_size + 1):
        font = ImageFont.truetype(random_font_path, fs)
        bbox = draw.textbbox((0,0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        if text_width > size[0] - 20 and text_height > size[1] - 20:
            break

    if text_width > size[0] - 20 or text_height > size[1] - 20:
        font = ImageFont.truetype(random_font_path, default_font_size)
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

    text_x = (size[0] - text_width) // 2
    text_y = (size[1] - text_height) // 2

    shadow_offset = 10
    draw.text((text_x + shadow_offset, text_y + shadow_offset), text, font=font, fill=generate_random_colour())
    draw.text((text_x, text_y), text, font=font, fill=generate_random_colour(), stroke_width=5, stroke_fill=generate_random_colour())
    img.save(filename)

def display_image_fullscreen(image_path, display_time):
    img = cv2.imread(image_path)

    if img is None:
        print(f"Failed to load image: {image_path}")
        return

    screen_width, screen_height = pyautogui.size()
    img_resized = cv2.resize(img, (screen_width, screen_height))

    cv2.namedWindow("Image", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("Image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    cv2.imshow("Image", img_resized)
    if display_time > 0:
        cv2.waitKey(display_time * 1000)
    else:
        cv2.waitKey(0)


def print_from_csv(filename, directory, image_extensions=['.png','.jpg','.jpeg']):

    image_names = pd.read_csv(filename, encoding='utf-8')

    if 'Image Name' not in image_names.columns:
        print("Image Name column not found in the file.")
        return

    images_in_directory = [f for f in os.listdir(directory)
                           if os.path.splitext(f)[1].lower() in image_extensions]

    for index, row in image_names.iterrows():
        name = row['Image Name']
        display_time = row['Time']
        found = False


        for image_file in images_in_directory:
            if os.path.splitext(image_file)[0] == name:
                image_path = os.path.join(directory, image_file)
                display_image_fullscreen(image_path, display_time)
                found = True
                break

        if not found:
            no_image_path = os.path.join(directory, f"{name}_not_found.png")
            create_image_from_text(f"{name}", no_image_path)
            display_image_fullscreen(no_image_path, display_time)

    cv2.destroyAllWindows()



filename = 'Images_File.csv'
directory = 'images_folder'

print_from_csv(filename, directory)