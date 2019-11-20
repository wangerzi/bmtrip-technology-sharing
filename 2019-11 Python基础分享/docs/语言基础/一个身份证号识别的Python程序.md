# 引子：一个身份证号识别的Python程序

文字识别，OCR（光学字符识别），用于把印在纸上或者写在纸上的文字读取出来；可用于证件识别、银行卡识别、车牌识别、名片识别等。

都知道 Python 在人工智能上边比较厉害，现在假如需要实现这样一个提取身份证号的功能，大概需要几行代码呢？不要几百行，也不要几十行，只要六行代码，如下所示：

`code/ocr-idcard.py`

```python
import pytesseract
import sys
import re
from PIL import Image

print(re.search(r'[\dxX]{18}', pytesseract.image_to_string(Image.open(sys.argv[1])), re.I).group())
```

使用方法：`python3 ocr-idcard.py 图片路径.jpg`

### 如何理解？

目前可以这样理解这个程序：`Python`可以看作是一个手机，`pytesseract`、`re`、`Image` 都可以看做是手机上装好的软件，识别并取出身份证信息可以分为如下三个步骤：

- 用图片查看器(`Image`)  将图片打开
- 让文字识别软件(`pytesseract`) 将图片上所有文字识别出来
- 用检索工具(re) 将文字中符合身份证号规则的数据提取出来