from PIL import Image, ImageDraw, ImageFont

im = Image.new("RGB", (512, 512), (100, 100, 100))

draw = ImageDraw.Draw(im)

draw.ellipse((220, 100, 320, 200), fill=(255, 255, 255))    #Head
draw.rectangle((220, 210, 320, 400), fill=(255, 255, 255))  #Body
draw.rectangle((330, 210, 400, 250), fill=(255, 255, 255))  #RIght Arm till Elbow
draw.rectangle((360, 210, 400, 120), fill=(255, 255, 255))  #RIght Arm far from elbow
draw.rectangle((10, 210, 210, 250), fill=(255, 255, 255))  #Left Arm

im.show()