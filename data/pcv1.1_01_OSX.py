# -*- coding: utf-8 -*-
from PIL import Image
# from pylab import *
from matplotlib.pyplot import *

# 添加中文字體支援
from matplotlib.font_manager import FontProperties
font = FontProperties(fname=r"/System/Library/Fonts/PingFang.ttc", size=14)
figure()

pil_im = Image.open('../data/empire.jpg')
gray()
subplot(121)
title(u'原圖',fontproperties=font)
axis('off')
imshow(pil_im)

pil_im = Image.open('../data/empire.jpg').convert('L')
subplot(122)
title(u'灰階圖',fontproperties=font)
axis('off')
imshow(pil_im)

show()
