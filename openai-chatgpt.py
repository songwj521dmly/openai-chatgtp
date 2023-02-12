#"-code utf-8"
# 导入openai库
import openai
# 导入os库
import os

# 设置openai的api_key
openai.api_key = "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"

# 打印欢迎语
print("欢迎使用AI聊天机器人")
# 打印提示
print("输入quit退出")

# 无限循环
while True:
    # 输入聊天内容
    text = input("你:")
    # 如果输入quit则退出
    if text == "quit":
        break
    else:
        try:
            # print(text)
            # 调用openai的chat方法，返回聊天内容
            response = openai.Completion.create(
                engine="text-davinci-003", # 使用的引擎
                # model="davinci", # 使用的模型
                # model="text-davinci-003", # 使用的模型
                prompt=text, # 聊天内容
                temperature=1, # 温度
                max_tokens=2048, # 生成的最大token数
                top_p=0.9, # 生成的最大概率
                # frequency_penalty=0, # 频率惩罚
                # presence_penalty=0.6, # 存在惩罚
                # stop=["\n", ]  # 结束符
            )
            # print(response)
            # 等待返回结果
            # response = response["choices"][0]["text"]
            # print(response)

            # 判断返回的聊天内容是否为空
            if response["choices"] == []:
                # 打印聊天内容
                print("AI：", "我不知道")
                continue
            # 打印聊天内容
            print("AI：" + response["choices"][0]["text"])
        except Exception as e:
            print("AI：", e)
            continue