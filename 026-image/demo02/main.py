from PIL import Image

# 读取图像获得Image对象
image = Image.open('../lrt.jpg')

# 通过Image对象的crop方法指定剪裁区域剪裁图像
image.crop((80, 20, 310, 360)).show()

