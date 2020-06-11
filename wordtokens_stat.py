import io
import json
from underthesea import word_tokenize
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import csv


def VietnameseStopWords(path='./vietnamese-stopwords.txt'):
    inp_data = open(path, 'r')
    return set(line.strip() for line in inp_data)

stopword = VietnameseStopWords()

def word_tokens_stat(source_file, topic):
  with open(source_file, encoding='utf-8') as jsonfile:
      data = json.load(jsonfile)
  text_data = []
  for post in data:
    if post['textClassification'] == [topic]:
      for token in word_tokenize(post['cleanedText'].lower()):
        if token not in stopword:
          found = False
          for i,text in enumerate(text_data):
            if text['st'] == token:
              text_data[i]['count'] += 1
              found = True
              break
          if found == False:
            text_data.append({
              'st': token,
              'count': 1
            })
    text_data.sort(key=lambda x: x['count'], reverse=True)

  with open(topic+'.csv', 'w', newline='') as file:
      writer = csv.writer(file)
      writer.writerow(["Word", "Count"])
      for word in text_data:
        writer.writerow([word['st'],word['count']])

if __name__ == '__main__':
    word_tokens_stat('./sample/processed.json', 'chinh_tri_xa_hoi')