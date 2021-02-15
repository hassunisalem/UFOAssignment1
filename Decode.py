#coding: utf-8
import base64
from PIL import Image

image = Image.open("UFOAscii_message.png")

extracted = ''

pixels = image.load()
# Iterate over pixels of the first row
for x in range(0, image.width):
    for y in range(1, image.height):
        b = pixels[x, y]
        # Store LSB of each color channel of each pixel
        extracted += bin(b)[-1]

chars = []
for i in range(len(extracted)/8):
    byte = extracted[i*8:(i+1)*8]
    chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))

# Don't forget that the message was base64-encoded
flag = base64.b64decode(''.join(chars))
print(flag)
