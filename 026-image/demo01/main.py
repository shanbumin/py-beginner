
# Pillow中最为重要的是Image类，可以通过Image模块的open函数来读取图像并获得Image类型的对象。
# 1.读取和显示图像

from PIL import Image

# 读取图像获得Image对象
image = Image.open('../lrt.jpg')

# 通过Image对象的format属性获得图像的格式
print(image.format) # JPEG

# 通过Image对象的size属性获得图像的尺寸
print(image.size)   # (640, 716)


# 通过Image对象的mode属性获取图像的模式
print(image.mode)   # RGB


# 通过Image对象的show方法显示图像
image.show()