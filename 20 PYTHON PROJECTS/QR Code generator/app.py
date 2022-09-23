# from email.mime import image


# Install all the libraries neeeded
# create a function that collects a text and convert it to a qrcode
# save the grcode as an image
# run the function

import qrcode
def generate_qrcode(text):

    qr =qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color = 'white')
    img.save("qrimgs.png")

url = input("Enter yout url: ")
generate_qrcode(url)

#Conversion of QR code for my users