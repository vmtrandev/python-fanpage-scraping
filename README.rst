========================================================
A small project aims at crawling public facebook fanpage 
========================================================

Requirements
----------------------------------------

#python >= 3.6 (some dependencies may not work properly with newer versions, at the time I made this project, underthesea module is not loaded with the latest python version 3.8.3)
* Tesseract client (see: https://github.com/tesseract-ocr/tesseract)
* pytesseract : $ pip install pytesseract
* underthesea: (see https://github.com/undertheseanlp/underthesea)
* wordcloud: $ pip install wordcloud

Project structure
----------------------------------------
|-- .gitignore
|-- sample
    |-- _processed.json
    |-- chinh_tri_xa_hoi.csv
    |-- processed.json
    |-- stat-full.csv
    |-- stat.csv
|-- count_reactions_by_page.py
|-- csv.py
|-- datahandling.py
|-- facebook_scraper.py
|-- mask.png
|-- nlp.py
|-- README.rst
|-- scraping.py
|-- vietnamese-stopwords.txt
|-- wordcloud.py
|-- wordtokens_stat.py
----------------------------------------

* `1. Installation <#1-installation>`_
* `2. Data Scraping <#2-data-scraping>`_
* `3. Text cleaning and Image Text extraction <#2-text-image>`_
* `4. Sentiment and Classification <#4-senti-classi>`_
* `5. Export to CSV <#5-export-to-csv>`_
* `6. Word statistics <#6-word-stat>`_
* `7. WordCloud <#7-wc>`_

****************************************
1. Installation
****************************************

The facebook_scraper.py in this project is a modified version of Kevinzg facecbook-scraper (see at: https://github.com/kevinzg/facebook-scraper)
You can either move this file to your current python's site_packages folder or install the original module and repalce the content of this main module file by this one.
If there is any better workaround, go for it cuz I'm not a pythonworm :(((

For other modules, install all the packages listed in the Requirements section above. You better go to the link I provided to install them correctly.

****************************************
2. Data Scraping
****************************************

Usage
* Open scaping.py and change the final line of code

.. code-block:: python
    extract_page_public_posts('<page name>', <quantity>)

****************************************
3. Text cleaning and Image Text extraction
****************************************

Usage
* Open datahandling.py and change the code in main method

.. code-block:: python
    try:
        pool = []
        #Replace your data from scaping.py in the below code
        pool = pool + load_data('./dummies1.json', 'DM')
        pool = pool + load_data('./dummies2.json', 'DN')
        pool = pool + load_data(<path to fanpage data from scraping.py>, <tag name for fanpage data>)


****************************************
4. Sentiment and Classification
****************************************

Usage
* Run nlp_processing.py
* You don't need to modify any line of code provided that you did't change the output file location or name in step 3.

****************************************
5. Export to csv
****************************************
Usage
* Run export_to_csv.py
* You don't need to modify any line of code provided that you did't change the output file location or name in step 4.
* With the result of this file, you can use any sort of visualization applications or services having csv supported file to analyze your data.

****************************************
6. Word Statistics
****************************************
Usage
* Open wordtokens_stat.py and change the final line code
* Default data file location is: processed.json
* To get topic name: open processed.json and copy the topic name wrapped inside ""

.. code-block:: python
    word_tokens_stat(<path to received file from step 4>, '<topic name>')


****************************************
7. WordCloud
****************************************
Usage
* Open wordcloud.py and change the final line code
* Default data file location is: processed.json
* To get topic name: open processed.json and copy the topic name wrapped inside ""

.. code-block:: python
    word_cloud(<path to received file from step 4>, '<topic name>')

