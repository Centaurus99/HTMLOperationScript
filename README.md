# HTMLOperationScript

> 基于`python3.7.3`与`requests`包(自动交题功能还需要`requests_toolbelt`包),可能是用于爆破校内OJ？

## 使用方法

### ojscript.py

#### Step1:相关依赖

需要安装 `requests` 包
```
pip install requests
```
如需使用`自动提交`功能还需要`requests_toolbelt`包
```
pip install requests_toolbelt
```

#### Step2:配置文件

将配置填入配置文件，文件名默认为`data.in`

目前已有的配置项（配置项`key`不区分大小写，`val`区分大小写）：

- `TargetAddress`: 目标IP
- `LoginMode`: 登录方式
    - 默认为`default`即账号密码登录（需自行`F12`抓包获得
    - `Cookie`/`cookie`为`Cookie`登录（需自行`F12`抓包获得
- `username`: `default`登录方式下的账号
- `password`: `default`登录方式下的密码
- `Cookie`: `Cookie`登录方式下的`Cookie`

样例配置文件
```
TargetAddress: 127.0.0.1
LoginMode: default
username: ******
password: ******
```

```
TargetAddress: 127.0.0.1
LoginMode: Cookie
Cookie: ******
```

#### Step3:修改代码
取消要使用的代码块的注释

#### Step4:运行
```
python3 ojscript.py
```

#### 自动提交的使用方法
默认从`code.cpp`中读取代码

文件需要为`UTF+8`格式

可以修改`Codename`来更改代码文件名

### StrOption.py - by [zby](https://github.com/hazby2002)
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

### ojscript.py

- 账密与`Cookie`两种登录方式
- 获取页面
- 自动发帖
- 自动删帖
- 自动回复
- 自动删回复
- 自动提交

### StrOption.py

- 将获取的 `headers` 添加引号便于复制进源码

## TODO

- [ ] 交互方式
- [ ] 设定函数参数
- [ ] 其他功能
