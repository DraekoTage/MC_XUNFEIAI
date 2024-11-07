# MC_XUNFEIAI
MC + 讯飞AI 实现游戏聊天显示大模型对话


## 准备工作

#### 构建服务器

在文件中Server目录中，如需构建其他版本的核心请前往[SpigotMC - High Performance Minecraft](https://www.spigotmc.org/?page=2)

#### 讯飞星火API申请

申请详情[星火认知大模型Web API文档 | 讯飞开放平台文档中心](https://www.xfyun.cn/doc/spark/Web.html)

#### 安装插件

plugins目录里这里选择的是1.12.1的插件版本

如需其他版本插件请到

https://github.com/zhuowei/RaspberryJuice

#### vscode python环境

## 开始

### 服务器的搭建

构建好后会在目录中生成plugins的目录

将插件文件.jar后缀的文件放入已经构建好的服务器目录的plugins目录中

在cmd中开启服务器, 执行命令

其中

-Xmx2g 代表最大分配内存空间,按照自己配置需求来

```
"JDk位置" -Xmx2G -jar spigot文件名 nogui
```

例如

```
"D:\Program Files\Java\jdk-17.0.3.1\bin\java" -Xmx2G -jar spigot-1.19.3.jar nogui
```

第一次需要eula同意协议

同意后执行第二次上述操作即可

如命令末尾显示"help"则代码服务器创建成功

访问127.0.0.1进行访问

### python连接MC

终端cmd安装python中

```
pip install mcpi
```

测试是否能够进行连接

运行项目文件中test_mcpi.py 运行成功后会在mc的玩家附近生成8*8羊毛方形火柴盒

则代表你已经连接成功

### 大模型API获取

编辑Mc_AI.py文件

这里使用的是星火，如果使用其他的大模型可以对def start_Ai()函数内容进行修改

编辑start_Ai.py填入在官网获取的API密钥

​    SPARKAI_URL = ''
​    SPARKAI_APP_ID = ''
​    SPARKAI_API_SECRET = ''
​    SPARKAI_API_KEY = ''

如果不知道API密钥是否成功可以先填入xhAI_test.py去测试一下看有无输出结果

## 进行

代码中if key == Key.alt_l: 代表游戏中触发Ai对话按键，如果不按还是可以正常的在游戏里面交流

这里我设置的是左Alt，可以让自己喜欢修改

执行mc_Ai.py所有代码

访问游戏，在聊天框输入对话发送，后按下alt键触发对话Ai机制，如弹出语言则代表成功 例图succeed.png
