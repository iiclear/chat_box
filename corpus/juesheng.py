import requests
import re 
from bs4 import BeautifulSoup


url = 'http://ask.juesheng.com/all/answered/'
#爬取http://www.ccutu.com/wenwen/2/，http://www.ccutu.com/wenwen/3/
# 像这样的链接里面的问题标题的链接，
# 比如：http://www.ccutu.com/wenwen/answer35435.html
#把这些链接存到一个列表urls里面，返回这个列表
def page_url(url):
    urls = []
    pag = 1
    while pag <= 1:
        start_url=url+'/'+'?'+ 'page='+str(pag)
        pag = pag + 1
        web_data = requests.get(start_url).content
        soup = BeautifulSoup(web_data,'lxml')
        items = soup.select('#f1  > div.title> div.description > ul> a')
        #'http://www.ccutu.com/wenwen/answer35452.html'
        for item in items:
            urls.append('http://ask.juesheng.com'+item.get('href'))
    #print(urls,len(urls))
    return urls


# 参数是page_url()函数返回的列表，从中取出问答的链接，然后爬取问答。
# 把每一对问答存成字典，再把字典存到列表中，返回这个列表
# 可以参考我给你改的youtu()函数中字典的部分
def juesheng_data(urls):
    item ={}
    juesheng_list= []
    for url in urls:
        web_data = requests.get(url).content
        soup = BeautifulSoup(web_data,'lxml')
        question  = soup.select_one('body > div.title >  div.description > a > h').get_text().strip()
        answer = ''.join(re.findall(r'<p>(.*?)</p>',str(soup.select_one('body  > div.title > div.description > p')))).replace('<br/>','')
        # answer = soup.select('body > div.wenda_cont > div.con_left > ul:nth-child(3) > li')

        item = {
            'question':question,
            'answer':answer
        }

        juesheng_list.append(item)

    return juesheng_list

def wirte_to_file(juesheng_list):
   with open('juesheng.txt','w') as f:
       for js in juesheng_list:
           f.write(js['question'] + '\n' + js['answer'] + '\n')
   f.close()

def main():
   urls = page_url(url)
   juesheng_list = juesheng_data(urls)
   wirte_to_file(juesheng_list)

if __name__ == '__main__':
    main()
