# 导入myqr模块
from MyQR import myqr

myqr.run(
    # 生成二维码
    words='https://github.com/wljave/subentry',
    # 将QR二维码图像与一张同目录下的图片相结合，产生一张黑白图片。
    picture='GitHub背景图标.jpg',
    # 使产生的图片由黑白变为彩色的。（布尔值，False表示黑白，True表示彩色）
    colorized=True,
    # 输出文件名，如果不填，默认输出文件名为“qrcode.png”
    save_name='subentry.png'
)
