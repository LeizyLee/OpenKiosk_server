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
            result = [temp['Sentiment'], float(temp['SentimentScore'][temp['Sentiment'].capitalize()])*100]
            return result[0], result[1]
    def Translate(self, msg="안녕하세요"):
        translate = self.service.client(service_name='translate', region_name='us-east-2', use_ssl=True)
        result = translate.translate_text(Text=msg,
            SourceLanguageCode="ko", TargetLanguageCode="en")
        print('TranslatedText: ' + result.get('TranslatedText'))
        return result.get('TranslatedText')

if __name__ == "__main__":
    aws = AWS()
    import pymysql
    _host = '121.154.1.89'
    _user = 'Lazy'
    _password = 'qwe123!!@@'
    _db = 'menu'
    _charset = 'utf8'
    conn = pymysql.connect(host=_host, user=_user, password=_password, db=_db, charset=_charset)
    cur = conn.cursor()

    sql = "UPDATE review SET propensity=%s, percent=%s WHERE rvId=%s"
    cur.execute('SELECT rvId, rvText FROM review')
    rvTemp = cur.fetchall()
    for i in rvTemp:
        prop, percent = aws.Comprehend(msg=i[1])
        cur.execute(sql, (prop, percent, i[0]))
    conn.commit()