class AWS():
    def __init__(self, region=None):
        import boto3
        self.service = boto3

    def Comprehend(self, msg):
        import json

        comprehend = self.service.client(service_name="comprehend", region_name='us-east-2')
        if msg == "Hello":
            print("None Input\n")
            return False
        else:
            text = self.Translate(msg)
            sentiment = json.dumps(comprehend.detect_sentiment(Text=text, LanguageCode='en'), sort_keys=True, indent=4)
            temp = json.loads(sentiment)
            print(temp)
            return temp
    def Translate(self, msg="안녕하세요"):
        translate = self.service.client(service_name='translate', region_name='us-east-2', use_ssl=True)
        result = translate.translate_text(Text=msg,
            SourceLanguageCode="ko", TargetLanguageCode="en")
        print('TranslatedText: ' + result.get('TranslatedText'))
        return result.get('TranslatedText')

if __name__ == "__main__":
    aws = AWS()
    print(aws.Comprehend("치킨을 먹었는데 치즈양념이랑 포테이토랑 파랑 양파랑 하나씩 먹어봤는데 맛있다. 얻어먹"
              "은 거라 가격은 모르겠지만 매콤한 거 좋아하면 치즈양념 먹고 달콤한거는 포테이토 "
              "먹는게 맛있다"))