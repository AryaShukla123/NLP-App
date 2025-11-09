import nlpcloud

class API:

    def __init__(self):
        nlpcloud.Client("gpt-oss-120b", "7ec262c99705d1d1cf6398fd0ac27a42573b6680", gpu=True)

    def sentiment_analysis(self,text):

        response = nlpcloud.sentiment(text,target="NLP Cloud")
        return response