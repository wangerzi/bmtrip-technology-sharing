# Python的特性

#### 简单易学

语义比较直接，接近伪代码，比如如下代码：

`code/sum.py`

```python
# 计算 1 到 99 的和
total = 0
for i in range(1, 100):
    total += i
print(total)
```

#### 可扩展

Python 的模块非常的多，包括目前比较火的机器学习、区块链、大数据、数据挖掘、爬虫等都有封装好的库，只需要掌握Python的基础语法之后，即可方便的使用

以简单爬虫的 `requests` 扩展为例，仅需两行代码即可获取 [斑马旅游官网](http://www.bmtrip.com/) 中目的地为日本的所有产品信息

`code/bmtrip-product-list.py`

```python
import requests

print(requests.get('http://www.bmtrip.com/api/v3/m1/product/list?platform=3&type=0&order_by=5&page=1&district_id[]=area_p_19&size=6').json())
```

#### 跨平台可移植

比如现在用 Windows 编写的代码，在Linux上依然可以执行，甚至像 PyQt 之类的GUI项目，可以跨 Windows、Linux、MacOS使用。

