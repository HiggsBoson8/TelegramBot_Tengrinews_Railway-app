import json
import requests
from bs4 import BeautifulSoup
from core.config import URL, DOMEN, HEADERS


def get_html(url, headers=HEADERS):
    response = requests.get(url=URL, headers=HEADERS)
    src = response.text
    
    return src


def get_response(response):
    soup = BeautifulSoup(response, "html.parser")

    news = soup.find_all("div", class_="tn-news-author-list-item")
    teg_image = soup.find_all("div", class_="tn-image-container")

    news_info = []
    for item in news:
        try:
            title = item.find("div", class_="tn-news-author-list-item-text").find("span", class_="tn-news-author-list-title")
            description = item.find("div", class_="tn-news-author-list-item-text").find("p", class_="tn-announce")
            date_time = item.find("div", class_="tn-news-author-list-item-text").find("li")
            news_url = DOMEN + item.find("a").get("href")
            image = item.find("div", class_="tn-image-container").find("img").get("src")
        except:
            image = item.find("div", class_="tn-video-container").find("source").get("src")
            information = {
            "title": title.text,
            "description": description.text,
            "date_time": date_time.text.strip(),
            "image": DOMEN + image,
            "url": news_url
        }
        else:
            information = {
            "title": title.text,
            "description": description.text,
            "date_time": date_time.text.strip(),
            "image": DOMEN + image,
            "url": news_url
        }

        news_info.append(information)
    return news_info


def NewsAlmatyParser():
    response = get_html(url=URL)
    soup = get_response(response)
    
    with open(f"core/json/news_almaty.json", "w", encoding="utf-8") as file:
        json.dump(soup, file, indent=4, ensure_ascii=False)






# import json
# import csv
# import time
# import random
# import datetime
# from os import system

# # downloaded libraries - скачанные библиотеки
# from bs4 import BeautifulSoup
# import requests

# #created module - созданный модуль
# from core.config import URL, DOMEN, HEADERS

# # Сделали headers по умолчанию можно не передавать ее при вызове функции
# def get_response(url_def, headers_def = HEADERS):   
#     # Отправляем get запрос на url
#     response = requests.get(url = url_def, headers = headers_def) 
#     # Указали условие если статус код будет равен 200 
#     if response.status_code == 200:    #хороший get запрос 
#         # Получаем html и другие контенты страницы 
#         src = response.content 
#          # И возвращаем ее 
#         return src 
#     else:
#         return f"Что то пошло не так {response.status_code}" 

# def get_soup(response):
#     soup = BeautifulSoup(response, "lxml")
#     all_news = soup.find_all("div", class_ = "tn-news-author-list-item")

#     news_info = []
#     for item in all_news:
#         try:
#             title = item.find("div", class_ = "tn-news-author-list-item-text").find("span", class_ = "tn-news-author-list-title")  # статья и название статьи
#             description = item.find("div", class_ = "tn-news-author-list-item-text").find("p", class_ = "tn-announce") # статья и содержание статьи
#             date_time = item.find("div", class_ = "tn-news-author-list-item-text").find("li") # статья и дата публикации статьи
#             news_url = DOMEN + item.find("a").get("href") # сссылка на статью
#             image = item.find("div", class_ = "tn-image-container").find("img").get("src") # ссылка на картинку
#         except Exception:
#             image = item.find("div", class_ = "tn-video-container").find("source").get("src") # видео(!)
#             information = {
#             "title": title.text,
#             "description": description.text,
#             "date_time": date_time.text.strip(),
#             "image": DOMEN + image,
#             "url": news_url
#             }
#         else:
#             information = {
#             "title": title.text,
#             "description": description.text,
#             "date_time": date_time.text.strip(),
#             "image": DOMEN + image,
#             "url": news_url
#         }
#         news_info.append(information)
#     return news_info

# def parser():
#     response = get_response(url_def = URL) 
#     soup = get_soup(response)

#     with open(f"core/json/tengrinews.json", "w", encoding = "UTF - 8") as file:
#         json.dump(soup, file, indent = 4, ensure_ascii = False) # отступы и для русского языка

# parser()




