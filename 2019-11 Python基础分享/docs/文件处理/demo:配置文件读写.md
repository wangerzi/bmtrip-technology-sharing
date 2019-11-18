# 配置文件读写

下面以配置文件写入读取为例，展示Python的文件读写能力

```python
def saveConfig(name, password):
    fp = fopen('./config.json', 'w') # 覆盖的方式
    
```

