from linebot import LineBotApi
from linebot.models import TextSendMessage, StickerSendMessage, ImageSendMessage, LocationSendMessage, VideoSendMessage
from linebot.models import TextSendMessage
line_bot_api = LineBotApi('dJ22CX/oh2y8ggkjD3BUgHqkZLxui+nXKeqYm322EZrSWJ4p2haKSL9+wf3aSGfQ5Z4fpwVSHUHm6cq9kp71Wk2bEJNG1C0gHCLBCxm1AdPWe/83jk9/6DDR4/1ZGuhdfw92PkGBVgPTIr9BqN7TYwdB04t89/1O/w1cDnyilFU=')
UserID = 'U3b9c6123cbe69d98c9317ff7335e2014'

text_message = TextSendMessage(text = 'hello world!')
line_bot_api.push_message(UserID, text_message)

Sticker_message = StickerSendMessage(package_id = '789', sticker_id='10855')
line_bot_api.push_message(UserID, Sticker_message)

image_message = ImageSendMessage(
    original_content_url='https://i.imgur.com/xyPtn4m.jpeg',
    preview_image_url='https://i.imgur.com/xyPtn4m.jpeg')
line_bot_api.push_message(UserID,image_message)
video_message = VideoSendMessage(
    original_content_url='https://i.imgur.com/oRcIXiM.mp4',
    preview_image_url='https://i.imgur.com/xyPtn4m.jpeg'
)
line_bot_api.push_message(UserID,video_message)