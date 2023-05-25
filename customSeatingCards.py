#! python3
# customSeatingCards.py - creates a custom seating card for each guest in
# the 'guests.txt' file.

from PIL import Image, ImageDraw, ImageFont
import os


os.makedirs('seatingCards', exist_ok=True)

guestFile = open('guests.txt', 'r')
guests = guestFile.read().splitlines()

cardImW, cardImH = (288, 360)

for guest in guests:
    cardIm = Image.new('RGBA', (cardImW, cardImH), 'white')

    flowerIm = Image.open('pinkRose.png')
    cardIm.paste(flowerIm, (73, 60), flowerIm)

    draw = ImageDraw.Draw(cardIm)
    draw.line([(0, 0), (287, 0), (287, 359), (0, 359), (0, 0)], fill='black')

    fontsFolder = 'C:\Windows\Fonts'
    segoeFont = ImageFont.truetype(os.path.join(fontsFolder, 'segoeprb.ttf'), 32)

    nameText = f'{guest}'
    nameTextW, nameTextH = draw.textsize(nameText, font=segoeFont)
    draw.text(((cardImW-nameTextW)/2, 20),
                nameText, fill='black', font=segoeFont)

    cardIm.save(os.path.join('seatingCards', f'Seating Card - {guest}.png'))


