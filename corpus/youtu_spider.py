import requests
import re 
import time
from bs4 import BeautifulSoup


url = 'http://www.ccutu.com/wenwen/'
#爬取http://www.ccutu.com/wenwen/2/，http://www.ccutu.com/wenwen/3/
# 像这样的链接里面的问题标题的链接，
# 比如：http://www.ccutu.com/wenwen/answer35435.html
#把这些链接存到一个列表urls里面，返回这个列表
def page_url(url):
    urls = []
    page = 1
    while page <= 1:
        start_url = url + str(page) + '/'
        page = page + 1
        web_data = requests.get(start_url).content
        soup = BeautifulSoup(web_data,'lxml')
        items = soup.select('#form1 > div.wenda_cont > div._cont_left > ul > li > a')
        #'http://www.ccutu.com/wenwen/answer35452.html'
        for item in items:
            urls.append('http://www.ccutu.com'+item.get('href'))
    #print(urls,len(urls))
    return urls


# 参数是page_url()函数返回的列表，从中取出问答的链接，然后爬取问答。
# 把每一对问答存成字典，再把字典存到列表中，返回这个列表
# 可以参考我给你改的youtu()函数中字典的部分
def qa_data(urls):
    item ={}
    qa_list= []
    for url in urls:
        web_data = requests.get(url).content
        soup = BeautifulSoup(web_data,'lxml')
        question  = soup.select_one('body > div.wenda_cont > div.con_left > dl > h1').get_text().strip()
        answer = ''.join(re.findall(r'<p>(.*?)</p>',str(soup.select_one('body > div.wenda_cont > div.con_left > ul > li')))).replace('<br/>','')
        # answer = soup.select('body > div.wenda_cont > div.con_left > ul:nth-child(3) > li')

        item = {
            'question':question,
            'answer':answer
        }

        qa_list.append(item)

    return qa_list

def wirte_to_file(qa_list):
   with open('qa.txt','w') as f:
       for qa in qa_list:
           f.write(qa['question'] + '\n' + qa['answer'] + '\n')
   f.close()

def main():
   urls = page_url(url)
   qa_list = qa_data(urls)
   wirte_to_file(qa_list)


if __name__ == '__main__':
    main()