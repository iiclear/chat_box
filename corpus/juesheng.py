import requests
from bs4 import BeautifulSoup


url = 'http://ask.juesheng.com/all/answered/'

def page_url(url):
    urls = []
    pag = 1
    while pag <= 1:
        start_url=url+'/'+'?'+ 'page='+str(pag)
        pag = pag + 1
        web_data = requests.get(start_url).content
        soup = BeautifulSoup(web_data,'lxml')
        items = soup.select('body > div.wrap > div > div.row > div.col-xs-12.col-md-9.main > div.stream-list.question-stream > section > div.summary > div > a')
        #body > div.wrap > div > div.row > div.col-xs-12.col-md-9.main > div.stream-list.question-stream > section > div.summary > div > a
        print(items)
        for item in items:
            urls.append(item.get('href'))
    print(urls,len(urls))
    return urls



def juesheng_data(urls):
    item ={}
    juesheng_list= []
    for url in urls:
        web_data = requests.get(url).content
        soup = BeautifulSoup(web_data,'lxml')
        question  = soup.select_one('body > div.wrap > div > div > div.col-xs-12.col-md-9.main > div.widget-question > h1').get_text().strip()
        print(question)
        answer = soup.select_one('#answer > div.media > div > div.content > p').get_text()
        # answer = soup.select('body > div.wenda_cont > div.con_left > ul:nth-child(3) > li')

        item = {
            'question':question,
            'answer':answer
        }
        print(item)
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

