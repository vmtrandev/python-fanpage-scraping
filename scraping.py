from facebook_scraper import get_posts
import json

def extract_page_public_posts(page_name, count):
    max_total_page = int(count / 2)
    file_path = page_name + '_' + str(count) + '.json'
    print('Saving to ' + file_path + '...')
    data = []
    _count = 0
    try:
        for post in get_posts(page_name, pages=max_total_page, extra_info=True, timeout=15):
            print(post)
            if not (post['fail']):
                del post['fail']
                data.append(post)
                _count = _count+1
                print(_count)
                print('\n')
            if (_count >= count):
                break
    except Exception as e:
        print(e)
    finally:
        with open(file_path, "w", encoding='utf-8') as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False)

if __name__ == '__main__':
    extract_page_public_posts('khongsocho.official', 250)
