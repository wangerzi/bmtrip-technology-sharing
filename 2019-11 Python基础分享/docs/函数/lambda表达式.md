# lambda 表达式

lambda表达式是一个简短的匿名函数，可以省去冗长的函数命名过程；主要用于使用过程中只在一处需要用到的函数，无需为取名问题烦恼。

格式： lambda 参数列表:返回值

```python
g = lambda x,y:2*x+y
ans = g(1, 2)
print(ans) # 4
```

