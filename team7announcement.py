import datetime
import json
import pandas as pd
import requests
import openpyxl
import time
import datetime
from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
import sys, os
import selenium
from pandas import DataFrame
import re
import pickle, progressbar, json, glob, time
from tqdm import tqdm

while True:
    print('1. 카테고리의 ID 한 눈에 보기\n2. 영상을 올린 채널 보기')
    command = input()
    if command == '1':
        print('*카테고리 ID값*')
        print('ID 값 : 10     Music\nID 값 : 17     Sports\nID 값 : 20     Game\nID 값 : 25     News & Politics\nID 값 : 30     Movies')
        time.sleep(1)
        print('카테고리의 ID 값을 확인 했으니 다시 선택지로 돌아겠습니다.')
        time.sleep(1)
        continue

    elif command == '2':
        break

    else:
        print('잘못된 명령어 입니다.')

id_ = input('검색할 id를 입력해주세요.')
url = 'https://www.googleapis.com/youtube/v3/search'
params = {
    'key' : 'AIzaSyC2jF9IjABbBRGLksun6FCf_wSziGmmC04',
    'part' : 'snippet',
    'videoCategoryId' : id_,
    'type' : 'video',
    'regionCode' : 'KR',
    'maxResults' : 50
}
response = requests.get(url, params=params)
data = response.json()
result_list = []
for d in data['items']:
    result_list.append(d['snippet']['channelTitle'])
pd.DataFrame(result_list).to_excel(f'category_{id_}_video.xlsx')
with open(f'category_{id_}_video.txt', 'w', encoding='utf-8') as outfile:
    json.dump(data, outfile, ensure_ascii = False)
print('해당 카테고리를 기준으로 영상을 올린 채널을 나열 하겠습니다.')
time.sleep(1.3)
print(result_list)
print()
zeroindex = result_list[0]

if id_ == '10':
    time.sleep(1)
    print('입력하신 ID값을 분석한 결과 음악 카테고리인 것이 확인 되었습니다.')
    print()
    music = input('1. 음악 차트 순위 가져오기\n2. 유튜브 채널 접속하기')
    print()
    if music == '1':
        now = datetime.datetime.now()
        nowDate = now.strftime('%Y년 %m월 %d일 %H시 %M분 기준의 음원 차트 순위를 가져오겠습니다.')
        time.sleep(1.5)
        print(nowDate)
        time.sleep(1.5)
        plat = input('*음원 차트를 가져올 플랫폼을 입력하시오*\n1. 멜론 순위 보기\n2. 벅스 순위 보기\n3. 지니 순위 보기')
        if plat == '1':
            print('멜론에서 음원 차트 순위를 가져오겠습니다.')
            time.sleep(1)
            browser = webdriver.Chrome("C:\\Users\\SAMSUNG\\chromedriver_win32\\chromedriver.exe")
            url = 'https://www.melon.com/chart/'
            browser.get(url)
            time.sleep(60)
        elif plat == '2':
            print('벅스에서 음원 차트 순위를 가져오겠습니다.')
            time.sleep(1)
            browser = webdriver.Chrome("C:\\Users\\SAMSUNG\\chromedriver_win32\\chromedriver.exe")
            url = 'https://music.bugs.co.kr/chart'
            browser.get(url)
            time.sleep(60)
        elif plat == '3':
            print('지니에서 음원 차트 순위를 가져오겠습니다.')
            time.sleep(1)
            browser = webdriver.Chrome("C:\\Users\\SAMSUNG\\chromedriver_win32\\chromedriver.exe")
            url = 'https://www.genie.co.kr/chart/top200'
            browser.get(url)
            time.sleep(60)
        else:
            print('세 음원 사이트 이외에 다른 사이트 서비스는 지원하지 않습니다.')
    elif music == '2':
        print('0번째 인덱스를 자동으로 검색해 해당 유튜브 채널에 접속하겠습니다.')
        time.sleep(1.5)
        path = "C:\\Users\\SAMSUNG\\chromedriver_win32\\chromedriver.exe"
        driver = webdriver.Chrome(path)
        driver.get("https://www.naver.com")
        time.sleep(2)

        driver.find_element_by_id("query").click()
        element = driver.find_element_by_id("query")
        element.send_keys(zeroindex + '유튜브')
        time.sleep(3)
        driver.find_element_by_id("search_btn").click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="web_1"]/div[1]/div[2]/div[1]/div/a[2]').click()
        time.sleep(60)
    else:
        print('음악 카테고리에서는 두 가지 기능 외 다른 기능은 지원하지 않습니다.')

elif id_ == '17':
    time.sleep(1)
    print('입력하신 ID값을 분석한 결과 스포츠 카테고리인 것이 확인 되었습니다.')
    print()
    sports = input('1. 현재 진행중인 게임 정보를 가져올까요? 네 / 아니요')
    print()
    if sports == '네':
        whatsthegame = input('1. 야구\n2. 축구\n3. 농구')
        if whatsthegame == '야구':
            print('실시간으로 진행중인 게임정보와 게임 일정 정보를 가져오겠습니다.')
            time.sleep(1)
            browser = webdriver.Chrome("C:\\Users\\SAMSUNG\\chromedriver_win32\\chromedriver.exe")
            url = 'https://www.koreabaseball.com/Schedule/Schedule.aspx'
            browser.get(url)
            time.sleep(60)
        elif whatsthegame == '축구':
            print('실시간으로 진행중인 게임정보와 게임 일정 정보를 가져오겠습니다.')
            time.sleep(1)
            browser = webdriver.Chrome("C:\\Users\\SAMSUNG\\chromedriver_win32\\chromedriver.exe")
            url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%ED%95%9C%EA%B5%AD+%EC%B6%95%EA%B5%AC+%EC%9D%BC%EC%A0%95&oquery=%ED%95%9C%EA%B5%AD+%EC%B6%95%EA%B5%AC+%EA%B5%AD%EA%B0%80%EB%8C%80%ED%91%9C+%EC%9D%BC%EC%A0%95&tqi=hjVJPsp0YihssiztbqCssssssEV-316460'
            browser.get(url)
            time.sleep(60)
        elif whatsthegame == '농구':
            print('실시간으로 진행중인 게임정보와 게임 일정 정보를 가져오겠습니다.')
            time.sleep(1)
            browser = webdriver.Chrome("C:\\Users\\SAMSUNG\\chromedriver_win32\\chromedriver.exe")
            url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%ED%95%9C%EA%B5%AD+%EB%86%8D%EA%B5%AC+%EC%9D%BC%EC%A0%95'
            browser.get(url)
            time.sleep(60)

        else:
            print('세 스포츠 외 다른 스포츠 서비스는 지원하지 않습니다.')
    elif sports =='아니요':
        print('서비스를 이용해주셔서 감사합니다.')
elif id_ == '20':
    time.sleep(1)
    print('입력하신 ID값을 분석한 결과 게임 카테고리인 것이 확인 되었습니다.')
    print()
    gameing = input('1. 유튜브 채널 접속하기\n2. pc방 점유율 보기')
    print()
    if gameing == '1':
        print('0번째 인덱스를 자동으로 검색해 해당 유튜브 채널에 접속하겠습니다.')
        time.sleep(1.5)
        path = "C:\\Users\\SAMSUNG\\chromedriver_win32\\chromedriver.exe"
        driver = webdriver.Chrome(path)
        driver.get("https://www.naver.com")
        time.sleep(2)

        driver.find_element_by_id("query").click()
        element = driver.find_element_by_id("query")
        element.send_keys(zeroindex + '유튜브')
        time.sleep(3)
        driver.find_element_by_id("search_btn").click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="web_1"]/div[1]/div[2]/div[1]/div/a[2]').click()
        time.sleep(60)
    elif gameing == '2':
        now = datetime.datetime.now()
        nowDate = now.strftime('%Y년 %m월 %d일 %H시 %M분 기준의 피시방 점유율을 크롤링 해오겠습닌다.')
        time.sleep(1.5)
        print(nowDate)
        time.sleep(1.5)
        print('PC방 게임전문 리서치 서비스에서 피시방 점유율 정보를 크롤링 해왔습니다.')
        time.sleep(1)
        browser = webdriver.Chrome("C:\\Users\\SAMSUNG\\chromedriver_win32\\chromedriver.exe")
        url = 'http://www.gametrics.com/'
        browser.get(url)
        time.sleep(60)
elif id_ == '25':
    time.sleep(1)
    print('입력하신 ID값을 분석한 결과 News & Politics 카테고리인 것이 확인 되었습니다.')
    print()
    newspolitics = input('1. 원하는 언론사의 기사 가져오기\n2. 유튜브 채널 접속하기')
    print()
    if newspolitics == '1':
        time.sleep(1.5)
        print('크롤링을 하기 위해 로딩중입니다...\n' + '-' * 100)
        def crawling_main_text(url):
            req = requests.get(url)
            req.encoding = None
            soup = BeautifulSoup(req.text, 'html.parser')
            # 연합뉴스
            if ('://yna' in url) | ('app.yonhapnews' in url):
                main_article = soup.find('div', {'class': 'story-news article'})
                if main_article == None:
                    main_article = soup.find('div', {'class': 'article-txt'})
                text = main_article.text
            # MBC
            elif '//imnews.imbc' in url:
                text = soup.find('div', {'itemprop': 'articleBody'}).text
            # 매일경제(미라클), req.encoding = None 설정 필요
            elif 'mirakle.mk' in url:
                text = soup.find('div', {'class': 'view_txt'}).text
            # 매일경제, req.encoding = None 설정 필요
            elif 'mk.co' in url:
                text = soup.find('div', {'class': 'art_txt'}).text
            # SBS
            elif 'news.sbs' in url:
                text = soup.find('div', {'itemprop': 'articleBody'}).text
            # KBS
            elif 'news.kbs' in url:
                text = soup.find('div', {'id': 'cont_newstext'}).text
            # JTBC
            elif 'news.jtbc' in url:
                text = soup.find('div', {'class': 'article_content'}).text
            # 그 외
            else:
                text == None
            return text.replace('\n', '').replace('\r', '').replace('<br>', '').replace('\t', '')
        press_nm = input('보고싶은 언론사를 입력 하세요.\n1. 연합뉴스\n2. MBC\n3. 매일경제\n4. SBS\n5. KBS\n6. JTBC')
        print('검색할 언론사 : {}'.format(press_nm))

        query = input('검색할 키워드  : ')
        news_num = int(input('수집 뉴스의 수(숫자만 입력) : '))
        print('\n' + '=' * 100 + '\n')
        chrome_path = "C:\\Users\\SAMSUNG\\chromedriver_win32\\chromedriver.exe"
        browser = webdriver.Chrome(chrome_path)
        news_url = 'https://search.naver.com/search.naver?where=news&query={}'.format(query)
        browser.get(news_url)
        time.sleep(1.3)
        print('설정한 언론사를 선택합니다.\n')
        search_opn_btn = browser.find_element_by_xpath('//a[@class="btn_option _search_option_open_btn"]')
        search_opn_btn.click()
        time.sleep(1.5)
        bx_press = browser.find_element_by_xpath(
            '//div[@role="listbox" and @class="api_group_option_sort _search_option_detail_wrap"]//li[@class="bx press"]')
        press_tablist = bx_press.find_elements_by_xpath('.//div[@role="tablist" and @class="option"]/a')
        press_tablist[1].click()
        time.sleep(1.7)

        bx_group = bx_press.find_elements_by_xpath(
            './/div[@class="api_select_option type_group _category_select_layer"]/div[@class="select_wrap _root"]')[0]
        press_kind_bx = bx_group.find_elements_by_xpath('.//div[@class="group_select _list_root"]')[0]
        press_kind_btn_list = press_kind_bx.find_elements_by_xpath(
            './/ul[@role="tablist" and @class="lst_item _ul"]/li/a')
        for press_kind_btn in press_kind_btn_list:
            press_kind_btn.click()
            time.sleep(1)
            press_slct_bx = bx_group.find_elements_by_xpath('.//div[@class="group_select _list_root"]')[1]
            press_slct_btn_list = press_slct_bx.find_elements_by_xpath(
                './/ul[@role="tablist" and @class="lst_item _ul"]/li/a')
            press_slct_btn_list_nm = [psl.text for psl in press_slct_btn_list]

            press_slct_btn_dict = dict(zip(press_slct_btn_list_nm, press_slct_btn_list))

            if press_nm in press_slct_btn_dict.keys():
                print('<{}> 카테고리에서 <{}>를 찾았으므로 탐색을 종료합니다'.format(press_kind_btn.text, press_nm))
                press_slct_btn_dict[press_nm].click()
                time.sleep(1.3)
                break

        print('\n크롤링을 시작합니다.')
        news_dict = {}
        idx = 1
        cur_page = 1
        pbar = tqdm(total=news_num, leave=True)
        while idx < news_num:
            table = browser.find_element_by_xpath('//ul[@class="list_news"]')
            li_list = table.find_elements_by_xpath('./li[contains(@id, "sp_nws")]')
            area_list = [li.find_element_by_xpath('.//div[@class="news_area"]') for li in li_list]
            a_list = [area.find_element_by_xpath('.//a[@class="news_tit"]') for area in area_list]
            for n in a_list[:min(len(a_list), news_num - idx + 1)]:
                n_url = n.get_attribute('href')
                news_dict[idx] = {'title': n.get_attribute('title'),
                                  'url': n_url,
                                  'text': crawling_main_text(n_url)}
                idx += 1
                pbar.update(1)
            if idx < news_num:
                cur_page += 1
                pages = browser.find_element_by_xpath('//div[@class="sc_page_inner"]')
                next_page_url = [p for p in pages.find_elements_by_xpath('.//a') if p.text == str(cur_page)][
                    0].get_attribute(
                    'href')
                browser.get(next_page_url)
                time.sleep(1)
            else:
                pbar.close()

                print('\n브라우저를 종료합니다.\n' + '=' * 100)
                time.sleep(0.7)
                browser.close()
                break

        news_df = DataFrame(news_dict).T
        folder_path = os.getcwd()
        xlsx_file_name = '네이버뉴스_본문_{}개_{}_{}.xlsx'.format(news_num, query, date)
        news_df.to_excel(xlsx_file_name)
        os.startfile(folder_path)
        news_df

    elif newspolitics == '2':
        print('0번째 인덱스를 자동으로 검색해 해당 유튜브 채널에 접속하겠습니다.')
        time.sleep(1.5)
        path = "C:\\Users\\SAMSUNG\\chromedriver_win32\\chromedriver.exe"
        driver = webdriver.Chrome(path)
        driver.get("https://www.naver.com")
        time.sleep(2)

        driver.find_element_by_id("query").click()
        element = driver.find_element_by_id("query")
        element.send_keys(zeroindex + '유튜브')
        time.sleep(3)
        driver.find_element_by_id("search_btn").click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="web_1"]/div[1]/div[2]/div[1]/div/a[2]').click()
        time.sleep(60)

elif id_ == '30':
    time.sleep(1)
    print('입력하신 ID값을 분석한 결과 영화 카테고리인 것이 확인 되었습니다.')
    print()
    movies = input('1. 영화 순위 및 리뷰 보기\n2. 영화표 예매하기')
    print()
    if movies == '1':
        print('네이버 영화에서 차트 및 순위를 가져오겠습니다.')
        time.sleep(1)
        browser = webdriver.Chrome("C:\\Users\\SAMSUNG\\chromedriver_win32\\chromedriver.exe")
        url = 'https://movie.naver.com/'
        browser.get(url)
        time.sleep(60)

    elif movies == '2':
        print('영화표 예매를 도와드리겠습니다.')
        local = input('사용자가 영화를 볼 지역을 입력하세요.')
        movieT = input('영화관을 입력 하세요.\nex)CGV, 롯데시네마, 메가박스...등')
        print('%s %s를 검색 하겠습니다.'%(local, movieT))
        time.sleep(1.5)
        path = "C:\\Users\\SAMSUNG\\chromedriver_win32\\chromedriver.exe"
        driver = webdriver.Chrome(path)
        driver.get("https://www.naver.com")
        time.sleep(2)

        driver.find_element_by_id("query").click()
        element = driver.find_element_by_id("query")
        time.sleep(3)
        element.send_keys(local + movieT)
        driver.find_element_by_id("search_btn").click()
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="web_1"]/div[1]/div[2]/div[1]/div/a[2]').click()
        time.sleep(60)
else:
    print('다른 카테고리 ID값에 대한 서비스는 지원하지 않습니다.')