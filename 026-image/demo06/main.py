from PIL import Image

# 读取图像获得Image对象
image = Image.open('../lrt.jpg')


for x in range(80, 310):
    for y in range(20, 360):
        # 通过Image对象的putpixel方法修改图像指定像素点
        image.putpixel((x, y), (128, 128, 128))
image.show()