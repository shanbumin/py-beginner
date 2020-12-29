from PIL import Image
from PIL import ImageFilter
# 读取图像获得Image对象
image = Image.open('../lrt.jpg')


# 使用Image对象的filter方法对图像进行滤镜处理
# ImageFilter模块包含了诸多预设的滤镜也可以自定义滤镜
image.filter(ImageFilter.CONTOUR).show()