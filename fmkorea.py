#내가 필요한 함수와 라이브러리를 import한다.
from bs4 import BeautifulSoup
from requests import get
from re import compile, findall

#Just a function that turns lists into strings because the re.findall() really annoys me
def lststr(lst):
    string=''
    return string.join(lst)

#이 .py 파일을 실행하면 실행될 main method이다.
def main():
    #혐오 표현을 "게시물 검색"으로 서치하면 나오는 결과 페이지 링크이다.
    link=input("에펨코리아 혐오표현 검색 페이지 링크: ")
    #link=https://www.fmkorea.com/?act=IS&is_keyword=

    #그 페이지의 html을 text로 가져온다.
    html_text=requests.get(link).text

    #그 html 내용을 좀 더 다루기 쉽게 BeautifulSoup로 만든다.
    soup=BeautifulSoup(html_text, 'lxml')
    #원하는 url들이 있는 class를 찾는다.
    sch_list=soup.find_all('a', class_='tit_txt')
    #그 안에서 링크만 쏙 빼오고 싶기 때문에 regular expression(정규 표현)을 사용한다.
    r=re.compile('href="(.*?)"')
    #for loop을 위해 비워둔 리스트
    url_list=[]

    for link in sch_list:
        #re library는 string을 input으로 받아야하기 때문에 str()을 사용한다.
        link=str(link)
        #re library를 사용해 링크 부분만 빼온다. 그러나 findall()은 list를 return한다. ㅜㅜ
        url=r.findall(link)
        #그래서 아까 만들어둔 함수를 사용!!
        url_str=lststr(url)
        url_list.append(url_str)


        #제대로 되었는지 확인하는 for liip
        for url in url_list:
            print(url)
    #main method 실행하도록 한다.
    if __name__=="__main__":
        main()
