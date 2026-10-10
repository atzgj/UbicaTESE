import qrcode

url = "https://atzgj.github.io/UbicaTESE/"
qr = qrcode.make(url)
qr.save("qr_ubicatese.png")
print("QR generado correctamente")