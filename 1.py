import werobot
import openai

openai.api_key = "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"

robot = werobot.WeRoBot()

class RobotConfig(object):
    HOST="10.9.100.246"
    PORT= 80
    TOKEN = "123456"# token是微信公众号用来指定接入当前云服务器的服务的凭证，代表是自己人接入的，等一下就有什么用了
    
robot.config.from_object(RobotConfig)

def generate_response(prompt):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    temperature=0.7,
    max_tokens=3000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    message = response.choices[0].text
    return message.strip()



@robot.handler
def hello (messages):
    print(messages.content)
    return generate_response(messages.content)


if __name__ == "__main__":
    robot.run()
