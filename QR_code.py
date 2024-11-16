import qrcode

data = input("Enter your URL to generate the QR code")
qr = qrcode.QRCode(
    version =3, 
    error_correction = qrcode.constants.ERROR_CORRECT_L, 
    box_size = 15, 
    border=4, 
)
qr.add_data(data) 
qr.make(fit = True)
img = qr.make_image(fill = "black", back_colour = "white") 
img.save("qrcode1.png") 
img.show 