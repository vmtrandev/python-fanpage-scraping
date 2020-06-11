from underthesea import word_tokenize, sentiment, classify
import os
import time
import json

def text_processing(post):
    print('Start ' + post['tag'])
    # post_id = post['post_id'] if 'post_id' in post else '_blank'
    if 'imgTextLength' in post and post['imgTextLength'] > 0:
      return {
        **post,
        'textSentiment': sentiment(post['cleanedText']),
        'textClassification': classify(post['cleanedText']),
        'imgSentiment': sentiment(post['cleanedImgText']),
        'imgClassification': classify(post['cleanedImgText']),
      }
    
    return {
        **post,
        'textSentiment': sentiment(post['cleanedText']),
        'textClassification': classify(post['cleanedText']),
      }

def main():
    try:
        with open('./_processed.json', encoding='utf-8') as jsonfile:
          data = json.load(jsonfile)
          processed_data = []
        
        for post in data:
          processed_data.append(text_processing(post))

    except Exception as e:
        print(e)
        pass
    finally:
        with open('processed.json', "w", encoding='utf-8') as jsonfile:
            json.dump(processed_data, jsonfile, ensure_ascii=False)


if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end-start)
