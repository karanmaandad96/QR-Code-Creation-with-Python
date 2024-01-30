# (Little Advance Mini Project) to Create a QR with Python:

import qrcode as qr
from PIL import Image, ImageDraw
import qrcode_terminal as qrt

def custom_qr(data, filename, color = 'black', backgroud = 'white', version = 1, box_size = 10, border = 4):
    yt = qr.QRCode(version=version, error_correction=qr.constants.ERROR_CORRECT_L, box_size =box_size, border = border,)

    yt.add_data("https://www.instagram.com/karan.maandad/")
    yt.make(fit = True)

    img = yt.make_image(fill_color=color, back_color=backgroud)

    # add some for features:
    draw = ImageDraw.Draw(img)
    draw.rectangle([10, 10, 50, 50], outline= 'red')

    # save image
    img.save(filename)

    # # Generate ASCII art representation of the QR code
    # qr_console = yt.make_image().get_image()
    #
    # # display qrcode in to console
    # qrt.draw(qr_console)

if __name__  == "__main__":
    data_to_encode = "Hello, OR Code!"
    output_filename = "Insta_QRcode.png"

    custom_qr(data_to_encode, output_filename, color='blue', backgroud= 'yellow' )

    print(data_to_encode)

