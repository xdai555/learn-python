from dingtalkchatbot.chatbot import DingtalkChatbot

from django.conf import settings

def send_msg(message, at_mobiles=[]):
    # 引用 settings 里面的 webhook 配置地址
    webhook = settings.DINGTALK_WEBHOOK
    secret = settings.DINGTALK_SECRET
    # 初始化一个机器人
    bot = DingtalkChatbot(webhook)
    # 示例2：如果机器人勾选了“加签”，需要传入 secret
    bot2 = DingtalkChatbot(webhook=webhook,secret=secret)

    bot.send_text(message, at_mobiles=at_mobiles,is_at_all=True)