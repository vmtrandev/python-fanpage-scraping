import underthesea
import os
import glob
import concurrent.futures
import time
import pytesseract
import io
import requests
import json
from PIL import Image
import re

os.environ['OMP_THREAD_LIMIT'] = '1'
 #do sth

def VietnameseStopWords(path='./vietnamese-stopwords.txt'):
    inp_file = os.path.join(path)
    inp_data = open(inp_file, 'r')
    return set(line.strip() for line in inp_data)

def clean_text(text):

    #Define emojis pattern
    emoji_pattern = re.compile("["
        u"\U0001F600-\U0001F64F"
        u"\U0001F300-\U0001F5FF"
        u"\U0001F680-\U0001F6FF"
        u"\U0001F1E0-\U0001F1FF"
                           "]+", flags=re.UNICODE)
    
    #Remove special chars (except emoji)
    vice_clean_text = re.sub('(\\n)|[=):-<>\\"🙂(]|-','', text)
    return emoji_pattern.sub('',vice_clean_text)

def img_post_2_text(post, lang='vie'):
    # post_id = post['post_id'] if 'post_id' in post else '_blank'
    if 'post_id' in post:
        if post['post_id'] is not None:
            post_id = post['post_id']
        else:
            post_id = '_null'
    else:
        post_id = '_blank'
    text = post['text']
    time = post['time']
    likes = post['likes']
    comments = post['comments']
    shares = post['shares']
    img_url = post['image']
    reactions = post['reactions'] if 'reactions' in post else None
    print('Start ' + str(post_id))
    text_clean = clean_text(text)
    
    if (img_url is None):
        return {
            'tag': post['tag'],
            'originalTextLength': len(text),
            'cleanedText': text_clean,
            'time': time,
            'totalReactions': likes,
            'totalComments': comments,
            'totalShares': shares,
            'reactions': reactions
        }

    try:
        response = requests.get(img_url)
        img = Image.open(io.BytesIO(response.content))
        img_text = pytesseract.image_to_string(img, lang=lang)
        img_text_cleaned = clean_text(img_text)

        return {
            'tag': post['tag'],
            'originalTextLength': len(text),
            'cleanedText': text_clean,
            'time': time,
            'totalReactions': likes,
            'totalComments': comments,
            'totalShares': shares,
            'reactions': reactions,
            'imgTextLength': len(img_text_cleaned),
            'cleanedImgText': img_text_cleaned,
            # 'imgSentiment': img_sentiment,
            # 'imgKind': img_kind
        }
    except Exception as e:
        print('Error occured ')
        print(e)
        return {
            'tag': post['tag'],
            'originalTextLength': len(text),
            'cleanedText': text_clean,
            'time': time,
            'totalReactions': likes,
            'totalComments': comments,
            'totalShares': shares,
            'reactions': reactions
        }


def load_data(path, tag):
    with open(path, encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
        for i, elm in enumerate(data):
            data[i]['tag'] = tag
        return data


def main():
    try:
        pool = []
        #Replace your data from scaping.py in the below code
        pool = pool + load_data('./dummies.json', 'DM')
        processed_data = []

        with concurrent.futures.ProcessPoolExecutor(max_workers=8) as executor:
            for modified_post in executor.map(img_post_2_text, pool):
                processed_data.append(modified_post)

    except Exception as e:
        print(e)
        pass
    finally:
        with open('_processed.json', "w", encoding='utf-8') as jsonfile:
            json.dump(processed_data, jsonfile, ensure_ascii=False)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end-start)
