# Neko_gptBot

nya~~~~ qwq

## 项目说明
>该项目是一个基于cqhttp框架，由Python开发完成的qq群组机器人，接入了OpenAI的GPT3.5
## 简介
Neko是一只基于GPT3.5的人工智能猫娘（使用猫娘之前需要对其进行人格设置），以下是功能介绍：
### GPT AI对话
在群组中，猫娘可以通过远程OpenAI的api实现私聊和群聊的对话，但是对话会收到OpenAI api的限制，如果需要在同一时间内进行更多响应，可以付费使用OpenAI提供的api
### 天气预报系统（开发中）
通过和风天气的api实现
### 自定义对话
用户可以通过修改hiNeko.py文件，对其进行增删改查实现自定义对话。简单的使用字符串检测即可。
### 关键字检测
为了避免不必要的政治问题以及敏感话题产生，Neko可以在用户端和gpt端进行关键词检测并及时屏蔽敏感信息

## 使用方法

### 一、环境搭建

1.Python3.8及以上

2.pip安装 Flask、openai==0.27.0、Pillow、requests

```bash
pip3.8 install Flask
pip3.8 install openai==0.27.0
pip3.8 install Pillow
pip3.8 install requests
```

### 二、安装、使用cqhttp

#### 标准启动方法

1. 双击`go-cqhttp_*.exe`，根据提示生成运行脚本
2. 双击运行脚本

```text
[WARNING]: 尝试加载配置文件 config.yml 失败: 文件不存在
[INFO]: 默认配置文件已生成,请编辑 config.yml 后重启程序.
```

1. 参照[config.mdopen in new window](https://github.com/Mrs4s/go-cqhttp/blob/master/docs/config.md)和你所用到的插件的 `README` 填入参数
2. 再次双击运行脚本

```text
[INFO]: 登录成功 欢迎使用: balabala
```

如出现需要认证的信息, 请自行认证设备。

此时, 基础配置完成

#### 标准启动方法Linux 标准启动方法

1. 通过 SSH 连接到服务器
2. `cd`到解压目录
3. 输入 `./go-cqhttp`, `Enter`运行 , 此时将提示

```text
[WARNING]: 尝试加载配置文件 config.yml 失败: 文件不存在
[INFO]: 默认配置文件已生成,请编辑 config.yml 后重启程序.
```

1. 参照 [config.mdopen in new window](https://github.com/Mrs4s/go-cqhttp/blob/master/docs/config.md) 和你所用到的插件的 `README` 填入参数
2. 再次输入 `./go-cqhttp`, `Enter`运行

```text
[INFO]: 登录成功 欢迎使用: balabala
```

如出现需要认证的信息, 请自行认证设备。

此时, 基础配置完成

> **注意**
>
> 需要保持 go-cqhttp 在后台持续运行
>
> 请配合 screen 等服务来保证断开 SSH 连接后 go-cqhttp 的持续运行

### 三、开启bot

```bash
python3.8 hiNeko.py
```



## 一些需要注意的事

cqhttp在远程登录时需要保证扫码手机与服务器在同一网络环境，我们可以采取上传token的方式进行登录
