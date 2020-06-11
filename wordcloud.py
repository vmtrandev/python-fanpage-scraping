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

def wordcloud(source_file, topic):
  with open(source_file, encoding='utf-8') as jsonfile:
      data = json.load(jsonfile)
  text_data = ''
  for post in data:
    if post['textClassification'] == [topic]:
      for token in word_tokenize(post['cleanedText'].lower()):
        if token not in stopword:
          text += token
  mask = np.array(Image.open('./mask.png'))
  wc = WordCloud(stopwords=set(),
                mask=mask, background_color="white",
                max_words=450, max_font_size=256,
                random_state=42, width=mask.shape[1],
                height=mask.shape[0])
  wc.generate(text_data)
  plt.imshow(wc, interpolation="bilinear")
  plt.axis('off')
  plt.show()

if __name__ == '__main__':
    wordcloud('./sample/processed.json', 'chinh_tri_xa_hoi')
