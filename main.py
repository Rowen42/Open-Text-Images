import os
import pandas as pd
import cv2
import pyautogui
from PIL import Image, ImageDraw, ImageFont
import random

font_list = [
    "Rubik-Bold.ttf",
    "NotoSerif-Bold.ttf",
    "ntailu.ttf",
    "LiberationSans-Regular.ttf",
    "GenBasBI.ttf",
    "seguibli.ttf",
    "Carlito-Bold.ttf",
    "Rubik-Regular.ttf",
    "MiriamMonoCLM-Book.ttf",
    "NotoSansArabic-Bold.ttf",
    "mingliub.ttc",
    "FRSCRIPT.TTF",
    "verdanab.ttf",
    "NotoSerifGeorgian-Bold.ttf",
    "Caladea-Italic.ttf",
    "NotoSans-LightItalic.ttf",
    "SpaceClaim ASME.ttf",
    "seguihis.ttf",
    "NotoSansArmenian-Regular.ttf",
    "msjh.ttc",
    "couri.ttf",
    "LiberationMono-BoldItalic.ttf",
    "DejaVuSansMono-Bold.ttf",
    "NotoSerifHebrew-Bold.ttf",
    "framdit.ttf",
    "ANTQUAB.TTF",
    "NotoSans-Condensed.ttf",
    "comicbd.ttf",
    "Caladea-Bold.ttf",
    "LinLibertine_DR_G.ttf",
    "NotoKufiArabic-Regular.ttf",
    "FrankRuehlCLM-MediumOblique.ttf",
    "wingding.ttf",
    "LHANDW.TTF",
    "FrankRuhlHofshi-Regular.otf",
    "MiriamMonoCLM-Bold.ttf",
    "SpaceClaim ISO.ttf",
    "ANTQUAI.TTF",
    "MiriamCLM-Book.ttf",
    "GenBkBasI.ttf",
    "mvboli.ttf",
    "seguisli.ttf",
    "corbelli.ttf",
    "Rubik-BoldItalic.ttf",
    "NotoSerifGeorgian-Regular.ttf",
    "AmiriQuran.ttf",
    "Candara.ttf",
    "SitkaVF-Italic.ttf",
    "GOTHIC.TTF",
    "opens___.ttf",
    "MISTRAL.TTF",
    "NotoSerif-Condensed.ttf",
    "malgun.ttf",
    "phagspa.ttf",
    "taile.ttf",
    "LiberationSansNarrow-BoldItalic.ttf",
    "DavidCLM-Medium.otf",
    "GenBasB.ttf",
    "cambriaz.ttf",
    "corbeli.ttf",
    "calibrib.ttf",
    "verdanai.ttf",
    "FrankRuehlCLM-Medium.ttf",
    "msyhl.ttc",
    "LiberationSansNarrow-Regular.ttf",
    "palab.ttf",
    "NotoSerifHebrew-Regular.ttf",
    "LiberationMono-Italic.ttf",
    "NotoSansLao-Bold.ttf",
    "seguili.ttf",
    "Gabriola.ttf",
    "l_10646.ttf",
    "seguisbi.ttf",
    "seguisb.ttf",
    "himalaya.ttf",
    "NotoSans-CondensedBoldItalic.ttf",
    "NirmalaB.ttf",
    "NotoSerif-LightItalic.ttf",
    "ANTQUABI.TTF",
    "DejaVuSans.ttf",
    "Candaraz.ttf",
    "TEMPSITC.TTF",
    "DUBAI-LIGHT.TTF",
    "comicz.ttf",
    "phagspab.ttf",
    "DUBAI-BOLD.TTF",
    "calibriz.ttf",
    "Candaral.ttf",
    "mmrtextb.ttf",
    "constani.ttf",
    "corbell.ttf",
    "NirmalaS.ttf",
    "NotoSans-CondensedBold.ttf",
    "cambriab.ttf",
    "DejaVuSans-BoldOblique.ttf",
    "LinLibertine_RBI_G.ttf",
    "trebucbd.ttf",
    "msyi.ttf",
    "NotoSans-Italic.ttf",
    "Amiri-Regular.ttf",
    "seguibl.ttf",
    "YuGothB.ttc",
    "constanb.ttf",
    "DejaVuSansMono-BoldOblique.ttf",
    "DUBAI-REGULAR.TTF",
    "mmrtext.ttf",
    "ntailub.ttf",
    "malgunsl.ttf",
    "ReemKufi-Bold.ttf",
    "trebucbi.ttf",
    "segoeuiz.ttf",
    "segoeuii.ttf",
    "LeelaUIb.ttf",
    "comici.ttf",
    "msjhl.ttc",
    "MiriamLibre-Bold.otf",
    "NotoSansHebrew-Regular.ttf",
    "NotoSerif-BoldItalic.ttf",
    "NotoKufiArabic-Bold.ttf",
    "sylfaen.ttf",
    "ariali.ttf",
    "consolai.ttf",
    "LinBiolinum_RI_G.ttf",
    "corbel.ttf",
    "segoeuib.ttf",
    "GOTHICB.TTF",
    "Carlito-Regular.ttf",
    "tahoma.ttf",
    "DejaVuSansCondensed-BoldOblique.ttf",
    "PAPYRUS.TTF",
    "NachlieliCLM-LightOblique.otf",
    "segoeuil.ttf",
    "MiriamMonoCLM-BookOblique.ttf",
    "cambriai.ttf",
    "verdana.ttf",
    "Carlito-Italic.ttf",
    "times.ttf",
    "msgothic.ttc",
    "YuGothM.ttc",
    "JUICE___.TTF",
    "webdings.ttf",
    "Candarali.ttf",
    "Rubik-Italic.ttf",
    "palabi.ttf",
    "msyhbd.ttc",
    "NotoSans-Light.ttf",
    "segoeprb.ttf",
    "NotoSansGeorgian-Bold.ttf",
    "GOTHICBI.TTF",
    "NotoSansArabic-Regular.ttf",
    "GenBasR.ttf",
    "NotoSans-BoldItalic.ttf",
    "Amiri-BoldItalic.ttf",
    "DejaVuSansMono.ttf",
    "lucon.ttf",
    "SitkaVF.ttf",
    "MiriamCLM-Bold.ttf",
    "gadugib.ttf",
    "NotoSerifArmenian-Bold.ttf",
    "corbelb.ttf",
    "pala.ttf",
    "ariblk.ttf",
    "NotoSansArabicUI-Bold.ttf",
    "LiberationSans-BoldItalic.ttf",
    "BRADHITC.TTF",
    "DejaVuSans-ExtraLight.ttf",
    "NotoNaskhArabic-Regular.ttf",
    "LinBiolinum_RB_G.ttf",
    "cour.ttf",
    "WINGDNG2.TTF",
    "simsunb.ttf",
    "georgia.ttf",
    "LiberationSerif-Bold.ttf",
    "LeelUIsl.ttf",
    "tahomabd.ttf",
    "gadugi.ttf",
    "NotoSans-Regular.ttf",
    "YuGothL.ttc",
    "GOTHICI.TTF",
    "FREESCPT.TTF",
    "calibril.ttf",
    "monbaiti.ttf",
    "MiriamMonoCLM-BoldOblique.ttf",
    "timesi.ttf",
    "simsun.ttc",
    "DejaVuSans-Oblique.ttf",
    "DavidLibre-Bold.ttf",
    "FrankRuhlHofshi-Bold.otf",
    "LinLibertine_RZI_G.ttf",
    "cambria.ttc",
    "NotoSerif-CondensedItalic.ttf",
    "courbd.ttf",
    "LinLibertine_RZ_G.ttf",
    "DejaVuSansMono-Oblique.ttf",
    "NotoSerifLao-Regular.ttf",
    "courbi.ttf",
    "timesbi.ttf",
    "GenBkBasR.ttf",
    "framd.ttf",
    "DavidCLM-MediumItalic.otf",
    "LiberationSerif-BoldItalic.ttf",
    "DejaVuSansCondensed-Bold.ttf",
    "WINGDNG3.TTF",
    "SansSerifCollection.ttf",
    "calibri.ttf",
    "DejaVuSans-Bold.ttf",
    "GenBasI.ttf",
    "LinLibertine_RB_G.ttf",
    "DejaVuMathTeXGyre.ttf",
    "impact.ttf",
    "Alef-Bold.ttf",
    "georgiaz.ttf",
    "LiberationSans-Italic.ttf",
    "arialbd.ttf",
    "consolab.ttf",
    "DejaVuSansCondensed-Oblique.ttf",
    "LinLibertine_R_G.ttf",
    "comic.ttf",
    "constan.ttf",
    "NotoSerif-Italic.ttf",
    "Scheherazade-Bold.ttf",
    "Carlito-BoldItalic.ttf",
    "LiberationSansNarrow-Bold.ttf",
    "seguisym.ttf",
    "LeelawUI.ttf",
    "LiberationSans-Bold.ttf",
    "consolaz.ttf",
    "Alef-Regular.ttf",
    "segoeui.ttf",
    "bahnschrift.ttf",
    "holomdl2.ttf",
    "DejaVuSansCondensed.ttf",
    "msjhbd.ttc",
    "Caladea-BoldItalic.ttf",
    "PRISTINA.TTF",
    "Amiri-Italic.ttf",
    "Candarab.ttf",
    "NotoNaskhArabic-Bold.ttf",
    "SegoeIcons.ttf",
    "REFSPCL.TTF",
    "ebrimabd.ttf",
    "NotoNaskhArabicUI-Bold.ttf",
    "NotoNaskhArabicUI-Regular.ttf",
    "Candarai.ttf",
    "NotoSansArabicUI-Regular.ttf",
    "seguiemj.ttf",
    "MTEXTRA.TTF",
    "NotoSansGeorgian-Regular.ttf",
    "NotoSerifArmenian-Regular.ttf",
    "NachlieliCLM-BoldOblique.otf",
    "msyh.ttc",
    "GenBkBasB.ttf",
    "LiberationMono-Regular.ttf",
    "LiberationMono-Bold.ttf",
    "BSSYM7.TTF",
    "ebrima.ttf",
    "NotoSansLao-Regular.ttf",
    "Nirmala.ttf",
    "NotoSerif-Light.ttf",
    "DavidLibre-Regular.ttf",
    "consola.ttf",
    "segoescb.ttf",
    "javatext.ttf",
    "NachlieliCLM-Bold.otf",
    "timesbd.ttf",
    "LEELAWAD.TTF",
    "georgiab.ttf",
    "DavidCLM-BoldItalic.otf",
    "FrankRuehlCLM-BoldOblique.ttf",
    "Caladea-Regular.ttf",
    "trebuc.ttf",
    "NotoSans-CondensedItalic.ttf",
    "ITCKRIST.TTF",
    "taileb.ttf",
    "LEELAWDB.TTF",
    "symbol.ttf",
    "NotoSans-Bold.ttf",
    "arial.ttf",
    "constanz.ttf",
    "LiberationSansNarrow-Italic.ttf",
    "NotoSansArmenian-Bold.ttf",
    "segoesc.ttf",
    "BKANT.TTF",
    "NotoSerifLao-Bold.ttf",
    "LiberationSerif-Italic.ttf",
    "ReemKufi-Regular.ttf",
    "arialbi.ttf",
    "LinLibertine_RI_G.ttf",
    "NotoSansHebrew-Bold.ttf",
    "DavidCLM-Bold.otf",
    "GenBkBasBI.ttf",
    "Scheherazade-Regular.ttf",
    "NachlieliCLM-Light.otf",
    "YuGothR.ttc",
    "georgiai.ttf",
    "Inkfree.ttf",
    "trebucit.ttf",
    "segoeuisl.ttf",
    "Amiri-Bold.ttf",
    "palai.ttf",
    "segmdl2.ttf",
    "segoepr.ttf",
    "MiriamLibre-Regular.otf",
    "REFSAN.TTF",
    "CENTURY.TTF",
    "NotoSerif-Regular.ttf",
    "calibrili.ttf",
    "NotoSansLisu-Regular.ttf",
    "LinBiolinum_R_G.ttf",
    "calibrii.ttf",
    "DUBAI-MEDIUM.TTF",
    "LiberationSerif-Regular.ttf",
    "verdanaz.ttf",
    "NotoMono-Regular.ttf",
    "SegUIVar.ttf",
    "corbelz.ttf",
    "NotoSerif-CondensedBold.ttf",
    "micross.ttf",
    "NotoSerif-CondensedBoldItalic.ttf"
    "malgunbd.ttf",
    "FrankRuehlCLM-Bold.ttf",
]

# Randomly select a font from the compatible list
def get_random_font():
    return random.choice(font_list)

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