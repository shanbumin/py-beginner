from PIL import Image

# 读取图像获得Image对象
image = Image.open('../lrt.jpg')
# 通过Image对象的thumbnail方法生成指定尺寸的缩略图
image.thumbnail((128, 128))
image.show()

