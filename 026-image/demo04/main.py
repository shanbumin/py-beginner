from PIL import Image



# 读取骆昊的照片获得Image对象
luohao_image = Image.open('luohao.png')
# 读取吉多的照片获得Image对象
guido_image = Image.open('guido.jpg')


# 从吉多的照片上剪裁出吉多的头
guido_head = guido_image.crop((80, 20, 310, 360))
width, height = guido_head.size


# 使用Image对象的resize方法修改图像的尺寸
# 使用Image对象的paste方法将吉多的头粘贴到骆昊的照片上
luohao_image.paste(guido_head.resize((int(width / 1.5), int(height / 1.5))), (172, 40))
luohao_image.show()






