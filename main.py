from PIL import Image
import numpy as np
import sys

if __name__ == "__main__":

    if len(sys.argv) > 1:
        path = sys.argv[1]
    else:
        sys.exit("No Image Availiable")

    img = Image.open(path)
    img = img.convert("L")

    w, h = img.size

    ar = h/w

    nw = 160
    nh = int(ar * nw * 0.5)
    img = img.resize((nw, nh))
    pixs = np.array(img.getdata())

    #ASCII Characters to represent grey scales, from brightest to the drakest pixel
    ascii_chars = ['@', '#', 'S', '%', '?', '*', '+', ';', ':', ',', '.']

    #Mapping
    ascii_pix = [ascii_chars[pix//25] for pix in pixs]
    ascii_pix = "".join(ascii_pix)

    #Writing pixels into a .txt file
    with open("output.txt", 'w') as f:
        for i in range(0, len(ascii_pix), nw):
            f.write(ascii_pix[i:i+nw] + '\n')
    
    print("You have successfully created an ASCII art!")

    
