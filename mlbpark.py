from bs4 import BeautifulSoup
from requests import get
from re import compile, findall

def lststr(lst):
    string=''
    return string.join(lst)

def main():
    link=input("오늘의 유머 혐오표현 검색 페이지 링크: ")
    #link=?? 뭔데
    html_text=requests.get(link).text
    soup=BeautifulSoup(html_text, 'lxml')
    sch_list=soup.find_all('a', class_='tit_txt')
    r=re.compile('href="(.*?)"')
    url_list=[]

    for link in sch_list:
        link=str(link)
        url=r.findall(link)
        url_str=lststr(url)
        url_list.append(url_str)

        for url in url_list:
            print(url)

    if __name__=="__main__":
        main()
