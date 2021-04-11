# coding=utf-8

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 打开文件
text = open('/2020年11月前/constitution.txt').read()

# 生成对象
wc = WordCloud(width=800, height=600, mode='RGBA', background_color=None).generate(text=text)

# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()

# 保存文件
wc.to_file('wordcloud.png')
