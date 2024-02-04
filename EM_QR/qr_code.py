#from https://realpython.com/python-generate-qr-code/
#wide_border_qrcode.py

import segno


qrcode = segno.make_qr("https://cbdm-01.zdv.uni-mainz.de/~muro/")
qrcode.save(
    "./emuro_qrHomePage.png",
    scale=5,
    border=10,
)
