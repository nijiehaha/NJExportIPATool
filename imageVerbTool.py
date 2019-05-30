from PIL import Image

def CalculationHeightWidth(imageList):

    targetH, targetW = (0, 0)

    for path in imagelist:

        im = Image.open(path)

        w, h = im.size

        targetW = w
        targetH = targetH + h

    return (targetW, targetH)



def verbImage(imageList):

    size = CalculationHeightWidth(imagelist)

    targetIm = Image.new('RGB', size)

    y = 0

    for path in imagelist:

        i = imagelist.index(path)

        im1 = Image.open(path)

        targetIm.paste(im1, (0, y))

        h = im1.size[1]

        y = y + h

    targetIm.save('myLongImage.jpg')

    print('路小飞，您的图片myLongImage拼接完成！！')

imagelist = ['test1.jpg', 'test2.jpg', 'test3.jpg']

list = verbImage(imagelist)

print(list)




