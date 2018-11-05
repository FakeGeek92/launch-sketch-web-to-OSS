import requests
import re

def from_url_get_html(url):
    html = requests.get(url)
    html.encoding = 'utf-8'
    html = html.text
    return html

def delete_useless_code(html, title):
    # delete anima script
    # html = re.sub(r'<script>[\s\S]*?</script>', '', html)

    # delete initial scale
    html = re.sub(r'initial-scale=1.0, ', '', html)
    # delete anima-src
    html = re.sub(r'src=data.*?nima-src', 'src', html)
    # delete animation css
    html = re.sub(r'.anima-animate.*}}', '', html)
    # delete author-name
    html = re.sub(r'<meta name=author.*?">', '', html)
    # delete favicon and replace with title
    title = "<title>"+title+"</title>"
    html = re.sub(r'<link rel="shortcut icon".*?.png>', title, html)
    # delete discritions
    html = re.sub(r'<!.*?>', '', html)
    # delete launchpad source code
    html = re.sub(r'<script src="launchpad-js.*?</a>', '', html)
    # replace font serif with sans-serif
    html = re.sub(r'serif', 'sans-serif', html)
    # add font
    html = re.sub(r'\'PingFangSC-Medium\'',
                  '\'PingFangSC-Medium\', \'Noto Sans S Chinese-Bold\', \'Microsoft-YaHei-Bold\'',
                  html)
    html = re.sub(r'\'PingFangSC-Regular\'',
                  '\'PingFangSC-Regular\', \'Noto Sans S Chinese-Regular\', \'Microsoft-YaHei-Regular\'',
                  html)
    html = re.sub(r'\'PingFangSC-Semibold\'',
                  '\'PingFangSC-Medium\', \'Noto Sans S Chinese-Black\', \'Microsoft-YaHei-Bold\'',
                  html)

    return html


def replace_img_url_prefix(old_url, new_url_prefix):
    split_url = old_url.split("/")
    new_url = new_url_prefix + split_url[-1]
    return new_url


def save_html_file(web_file_name, html):
    html_file = open(web_file_name, 'w', encoding='UTF-8')
    html_file.write(html)
    html_file.close()


if __name__ == '__main__':
    url = 'https://launchpad.animaapp.com/preview/soP5X8q/screen1'
    html = from_url_get_html(url)
    print(html)
    html = delete_useless_code(html)
    print(html)