import json
import csv
from datetime import datetime

def timestamp_2_round_time(timestamp):
    dt_object = datetime.fromtimestamp(timestamp)
    time_in_hm = dt_object.strftime("%H:%M")
    time_part = time_in_hm.split(':')
    time_part[0] = int(time_part[0])
    time_part[1] = int(time_part[1])
    if time_part[1] <= 15:
        time_part[1] = '00'
    elif time_part[1] > 15:
        time_part[1] = '30'
    elif time_part[1] > 30:
        time_part[0] += 1 if time_part[0] < 23 else '0'
        time_part[0] = str(time_part[0])
        time_part[1] = '00'
    time_part[0] = str(time_part[0])
    time_part[1] = str(time_part[1])
    return ':'.join(time_part)


with open('./processed.json', encoding='utf-8') as jsonfile:
    data = json.load(jsonfile)

with open('stat-full-with-time.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Fanpage", "Likes", "Comments", "Shares", "Thích",
                     "Thả tim", "Wow", "Haha", "Buồn", "Phẩn nộ", "Thương thương", "Độ dài bài đăng", "Sentiment", "Chủ đề", "Độ dài hình ảnh", "Sentiment Ảnh", "Chủ đề ảnh", "Timing"])
    for post in data:
        page = post
        like = 0
        love = 0
        wow = 0
        support = 0
        haha = 0
        sorry = 0
        anger = 0
        if 'reactions' in page and page['reactions'] is not None:
            like = page['reactions']['like'] if 'like' in page['reactions'] else 0
            love = page['reactions']['love'] if 'love' in page['reactions'] else 0
            wow = page['reactions']['wow'] if 'wow' in page['reactions'] else 0
            support = page['reactions']['support'] if 'support' in page['reactions'] else 0
            haha = page['reactions']['haha'] if 'haha' in page['reactions'] else 0
            sorry = page['reactions']['sorry'] if 'sorry' in page['reactions'] else 0
            anger = page['reactions']['anger'] if 'anger' in page['reactions'] else 0
        img_text_length = page['imgTextLength'] if 'imgTextLength' in page else None
        img_sentiment = page['imgSentiment'] if 'imgSentiment' in page else ''
        img_classification = page['imgClassification'][0] if 'imgClassification' in page else ''
        text_classifcation = page['textClassification'][0] if page['textClassification'] is not None else '_'
        time = timestamp_2_round_time(page['time']) if page['time'] is not None else '00:00'
        writer.writerow([page['tag'], page['totalReactions'], page['totalComments'], page['totalShares'], like, love,
                         wow, haha, sorry, anger, support, page['originalTextLength'], page['textSentiment'], text_classifcation, img_text_length, img_sentiment, img_classification, time])
