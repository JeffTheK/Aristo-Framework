# coding=utf-8
import os
import time
import qrcode
import color
from color import *

def gen_qrcode():
    url = raw_input(''+T+'' + color.UNDERLINE + 'Website or text>' + color.END)
    print(""+C+"Enter the name of the output file without the extension")
    name = raw_input(''+T+'' + color.UNDERLINE + 'Output>' + color.END)
    qr = qrcode.QRCode(5, error_correction=qrcode.constants.ERROR_CORRECT_L)
    qr.add_data(url)
    qr.make()
    im = qr.make_image()
    time.sleep(1)

    qr_img_path = os.path.join(name + ".png")

    if os.path.isfile(qr_img_path):
        os.remove(qr_img_path)
    # save the image out
    im.save(qr_img_path, format='png')
    # print that its been successful
    print(""+G+"[!] " + color.UNDERLINE + "QRCode has been generated!" + color.END)