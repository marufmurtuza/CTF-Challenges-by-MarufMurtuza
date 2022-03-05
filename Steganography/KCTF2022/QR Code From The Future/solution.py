#!/usr/bin/env python3

from PIL import Image
from pyzbar.pyzbar import decode

imageObject = Image.open('QR_Code_From_The_Future.gif')

flag = b''
for frame in range(0, imageObject.n_frames):
    imageObject.seek(frame)
    flag += decode(imageObject)[0].data
print('The Flag: ')
print(flag.decode('utf8'))
