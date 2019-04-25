# HTMLOperationScript

> 基于`python3`与`requests`包,可能是用于爆破校内OJ？

## 使用方法

### lojarticals.py

需要安装 `requests` 包
```
pip install requests
```

修改源码

将相关信息填入源码

```
#目标IP
Target_address = '******'

#账号密码
user_data = {'username' : '******', 'password' : '******'}
```
取消要使用的代码块的注释

运行
```
python3 lojarticals.py
```

### StrOption.py
```
#文件名
Filename = '1'
```
将会从`Filename.in`中逐行读取字符串，将`:`前后的内容分别用引号框起来

例如：

Filename.in
```
Host: ***.***.***.***
```
Filename.out
```
'Host' : '***.***.***.***'
```

## 目前已有的功能

### lojarticals.py

- 获取页面
- 自动发帖
- 自动删帖
- 自动回复
- 自动删回复

### StrOption.py

- 将获取的 `headers` 添加引号便于复制进源码

## TODO

- 交互方式
- 将数据与程序分离

