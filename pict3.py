from PIL import Image, ImageDraw, ImageFont

im = Image.new("RGB", (512, 512), (128, 128, 128))

draw = ImageDraw.Draw(im)

#draw.line((0, im.height, im.width, 0), fill=(255, 0, 0), width=8)
#draw.rectangle((100, 100, 200, 200), fill=(0, 255, 0))
draw.ellipse((220, 100, 320, 200), fill=(255, 255, 255))    #Head
draw.rectangle((220, 210, 320, 400), fill=(255, 255, 255))  #Body
draw.rectangle((330, 250, 370, 40), fill=(255, 255, 255))  #RIght Arm
draw.rectangle((170, 210, 210, 420), fill=(255, 255, 255))  #Left Arm

im.show()