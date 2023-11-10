import pyqrcode
import png
from pyqrcode import QRCode

# CODIGO QR ID
contador= 1234

#Creacion del QR
while contador <=1235:
    checo = contador
    id = '71'+str(contador)
    qr= pyqrcode.create(71 and id, error='L')
    #save
    qr.png('G'+str(checo)+'.png', scale=6)
    # Mas Mas
    contador=contador+1

