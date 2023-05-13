import qrcode
from PIL import Image
qr_web=qrcode.QRCode(version=2,error_correction=qrcode.constants.ERROR_CORRECT_H,
                     box_size=8,border=2)
#The code creates a new instance of the QRCode class from the qrcode module and assigns it to the variable qr_web.
#The QRCode class is used to generate QR codes, which are two-dimensional barcodes that can be scanned using a smartphone camera or other similar devices.

qr_web.add_data("https://www.youtube.com/@Debayan_Music")

qr_web.make(fit=True)
url_image=qr_web.make_image(fill_color="red",back_color="Pink")
url_image.save("deb_music.png")
