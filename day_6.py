import pyqrcode

myEmailID = " namrata4055@gmail.com "
contact_No = "9354964991"

myQrCode = pyqrcode.create(myEmailID+"\n"+contact_No)

myQrCode.svg("MYQRCODE.svg")
print("Your QR code is generated successfully")

