import requests
import re

def from_url_get_html(url):
    html = requests.get(url)
    html.encoding = 'utf-8'
    html = html.text
    return html

def delete_useless_code(html):
    # delete script
    html = re.sub(r'<script>[\s\S]*?</script>', '', html)
    # delete anima-src
    html = re.sub(r'src=data.*?nima-src', 'src', html)
    # delete animation css
    html = re.sub(r'.anima-animate.*}}', '', html)
    # delete author-name
    html = re.sub(r'<meta name=author.*?">', '', html)
    # delete favicon
    html = re.sub(r'<link rel="shortcut icon".*?.png>', '', html)
    # delete discritions
    html = re.sub(r'<!.*?>', '', html)
    return html

def replace_img_url_prefix(html, url):
    html = re.sub(r'https:.*?img', url, html)
    return html

def save_html_file(web_file_name, html):
    html_file = open(web_file_name, 'w', encoding='UTF-8')
    html_file.write(html)
    html_file.close()

if __name__ == '__main__':
    url = 'https://launchpad.animaapp.com/preview/5mFH3lT/innerpeaceproductintro'
    html = from_url_get_html(url)
    print(html)
    html = delete_useless_code(html)
    print(html)