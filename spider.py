import requests
from lxml import etree
from time import sleep

header = {
    "user-agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                   "Chrome/88.0.4324.146 Safari/537.36")
}


# 获取所有待爬取新闻的url
def get_news_url():
    news_list = []
    for i in range(2, 8):
        url = "http://tech.163.com/special/gd2016_%02d/" % i
        response = requests.get(url,headers=header)

        # 解析
        html = etree.HTML(response.text)
        news_ul = html.xpath('//*[@id="news-flow-content"]')[0]
        news_href = news_ul.xpath('//li/div/h3/a/@href')
        news_list += news_href
        sleep(2)

    file = open("news_url.txt", "w+")
    for url in news_list:
        file.write(url + "\n")
    file.close()


def get_news_pages():
    file = open("news_url.txt", "r")
    urls_list = file.read().splitlines()
    file.close()
    for url in urls_list:
        news_pages = requests.get(url, headers=header)
        html = etree.HTML(news_pages.text)
        title = html.xpath('//*[@id="container"]/div[1]/h1')[0].text
        print(title)
        break





if __name__ == "__main__":
    # get_news_url()
    get_news_pages()