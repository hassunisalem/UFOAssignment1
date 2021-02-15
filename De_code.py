
import base64
from PIL import Image

image = Image.open("UFOAscii_message.png")


def getbytes(bits):
    done = False
    while not done:
        byte = 0
        for _ in range(0, 8):
            try:
                bit = next(bits)
            except StopIteration:
                bit = 0
                done = True
            byte = (byte << 1) | bit
        yield byte


def getLSB(img, channel, index=0):
    data = img.load()

    channel_index = img.mode.index(channel)

    lsb = []
    for x in range(img.size[0]):
        for y in range(img.size[1]):

            color = data[x, y]

            channel = color[channel_index]

            plane = bin(channel)[2:].zfill(8)

            lsb.append(plane[7])

    print(lsb)

    c = []
    for i in lsb:
        c.append(int(i))

        if (len(c) == 8):

           # print(c)
            c = []


getLSB(image, 'B', 0)
