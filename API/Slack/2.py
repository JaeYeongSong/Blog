import requests

myToken = "your key"

def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )

post_msg = "함수로 보내보았습니다."
post_message(myToken,"#test",post_msg)