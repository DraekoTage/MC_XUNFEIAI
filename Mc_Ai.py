from mcpi.minecraft import Minecraft
from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage
from pynput.keyboard import Listener, Key, KeyCode
import os

# 连接到Minecraft游戏
mc = Minecraft.create()

def start_Ai():
    # 定义日志文件路径

#----------更改目录位置logs/latest.log
    logs_path = os.path.join("D:", "game", "mcserver3", "logs", "latest.log")

    # 初始化一个变量来存储结果字符串
    result = ""

    # 确保文件存在
    if os.path.exists(logs_path):
        # 打开文件并读取所有行
        with open(logs_path, "r", encoding='ANSI') as file:
            lines = file.readlines()  # 读取所有行到一个列表中
            if lines:  # 确保文件不为空
                # 从最后一行开始向上遍历
                for i in range(len(lines) - 1, -1, -1):
                    line = lines[i]
                    if "Async" in line:
                        # 找到包含特定字符的行后，提取>之后的所有字符串
                        if ">" in line:
                            result = line.split(">")[-1].strip()
                            break  # 找到后就不需要继续循环了
    else:
        print(f"The file {logs_path} does not exist.")

    # 打印结果变量
    print("Resulting string:", result)


    #星火认知大模型Spark Max的URL值，其他版本大模型URL值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
    SPARKAI_URL = 'wss://spark-api.xf-yun.com/v3.5/chat'
    #星火认知大模型调用秘钥信息，请前往讯飞开放平台控制台（https://console.xfyun.cn/services/bm35）查看
    SPARKAI_APP_ID = ''
    SPARKAI_API_SECRET = ''
    SPARKAI_API_KEY = ''
    #星火认知大模型Spark Max的domain值，其他版本大模型domain值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
    SPARKAI_DOMAIN = 'generalv3.5'
    a = "自我介绍一下"
    print(type(a))
    if __name__ == '__main__':
        spark = ChatSparkLLM(
            spark_api_url=SPARKAI_URL,
            spark_app_id=SPARKAI_APP_ID,
            spark_api_key=SPARKAI_API_KEY,
            spark_api_secret=SPARKAI_API_SECRET,
            spark_llm_domain=SPARKAI_DOMAIN,
            streaming=False,
        )
        messages = [ChatMessage(
            role="user",
            content=result
        )]
        handler = ChunkPrintHandler()

        # 数据清洗
        a = spark.generate([messages])
        b = a.generations[0][0].text
        b_cleaned = b.replace('\n', '')  # 去除换行符，并将结果赋值给新的变量 
        print(b_cleaned)  # 打印清洗后的文本
        mc.postToChat(b_cleaned)  # 将清洗后的文本发送到聊天
        



def on_release(key):
    # 检查是否是i键
    if key == Key.alt_l:
        # 执行start_Ai函数
        start_Ai()
# 设置键盘监听器
with Listener(on_release=on_release) as listener:
    listener.join()