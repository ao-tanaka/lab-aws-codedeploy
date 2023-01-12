import google
from google.oauth2 import service_account
from googleapiclient import discovery
import datetime

def lambda_handler(event, context):
    scopes = ["https://www.googleapis.com/auth/calendar"]
    credentials = service_account.Credentials.from_service_account_file(
        "novelocr-9f351a9d187a.json", scopes=scopes
    )  # jsonはgoogle cloud platformの鍵のダウンロードで落としたやつ
    service = discovery.build(
        "calendar", "v3", credentials=credentials, cache_discovery=False
    ) # cache_discovery=Falseにしてないとaws lambdaだとエラーが出るらしい

    dt_now = datetime.datetime.now()
    date_now = dt_now.date()
    date_now = str(date_now) + "T23:00:00"
    
    TemHum = '室温:' + str(event['Temperature']) + '度, 湿度:' + str(event['Humidity']) + '%'
    
    event = {
        "summary": TemHum,
        "description": "平均気温と平均湿度",
        "start": {"dateTime": date_now, "timeZone": "Asia/Tokyo",},
        "end": {"dateTime": date_now, "timeZone": "Asia/Tokyo",},
    }

    event = (
        service.events()
        .insert(
            calendarId="*****@group.calendar.google.com",  # 設定>マイカレンダーの設定>カレンダーの等号>カレンダーID
            body=event,
        )
        .execute()
    )
