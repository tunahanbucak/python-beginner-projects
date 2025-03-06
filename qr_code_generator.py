import qrcode

data = input("Metni veya URL'yi girin: ").strip()
filename = input(
    "Dosya adını ve türünü girin:(QR kod için jpg yada png olabilir): "
).strip()
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)
print(f"QR kodu şu şekilde kaydedildi: {filename}")
