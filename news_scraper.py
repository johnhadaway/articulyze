import json 
import pandas as pd 
import numpy as np 
import datetime
from newspaper import Article
import urllib
import re
import os
import csv
import glob

main_search_queries = {"yemen" : ["https://news.google.com/news?q=yemen%20crisis&output=rss", 
"https://news.google.com/news/?q=yemen+humanitarian&output=rss", "https://news.google.com/news/?q=yemen+suffering&output=rss"],
    "drc" : ["https://news.google.com/news?q=DRC+crisis&output=rss",
    "https://news.google.com/news?q=DRC+humanitarian&output=rss", "https://news.google.com/news?q=DRC+suffering&output=rss"],
    "somalia" : ["https://news.google.com/news?q=somalia+crisis&output=rss",
    "https://news.google.com/news?q=somalia+humanitarian&output=rss", "https://news.google.com/news?q=somalia+suffering&output=rss"],
    "syria" : ["https://news.google.com/news?q=syria+crisis&output=rss",
    "https://news.google.com/news?q=syria+humanitarian&output=rss", "https://news.google.com/news?q=syria+suffering&output=rss"],
    "south+sudan" : ["https://news.google.com/news?q=south+sudan+crisis&output=rss",
    "https://news.google.com/news?q=south+sudan+humanitarian&output=rss", "https://news.google.com/news?q=south+sudan+suffering&output=rss"]
    }

def generate_search_queries(list_countries, list_extensions):

    search_queries = {}

    for country in list_countries:
        queries = []
        for extension in list_extensions:
            if extension == "":
                search_url = "https://news.google.com/news/?q=" + country + "&output=rss"
            else:
                search_url = "https://news.google.com/news/?q=" + country + "+" + extension + "&output=rss"
            queries.append(search_url)
        search_queries[country] = queries

    return search_queries

def search_url_to_list(search_url):
    """

    - FUNCTION: takes a search URL in format news.google.com/news?q=QUERY&output=rss, and
    retrieves a list of article urls.
    - INPUT PARAMETER: search_url (search url string)
    - RV: list of article urls

    """

    page = urllib.request.urlopen(search_url)
    content = str(page.read())
    urls = re.findall(r'url=(.*?)</link>', content)
    clean_urls = []

    for url in urls:
        if "&quot" in url:
            position_terminate = url.find("&quot")
            clean_urls.append(url[:position_terminate])
        else:
            clean_urls.append(url)

    return list(set(clean_urls))

def search_by_country(country, search_queries): 
    """

    - FUNCTION: takes a country name as a parameter, returns a list of article urls pertaining to it based on search_queries dictionary
    - INPUT PARAMETER: country (string)
    - RV: list of article urls

    """

    key = country.lower()
    search_urls = search_queries[key]
    article_urls = []

    for search_url in search_urls:
        article_urls.extend(search_url_to_list(search_url))

    return list(set(article_urls))

def return_text_url_title(article_url):
    """

    - FUNCTION: takes a url, returns the article's text and title
    - INPUT PARAMETER: article url (string)
    - RV: list (text, url, title)

    """

    article = Article(article_url)
    try:
        article.download()
        article.parse()
    except:
        return None
    return [article.text, article.url, article.title]

def csv_articles_for_country(country, search_queries):
    """

    - FUNCTION: takes a country string as a parameter, creates a csv file for the country
    - INPUT PARAMETER: country (string)
    - RV: None

    """

    article_urls = search_by_country(country, search_queries)
    urls = []
    texts = []
    titles = []

    for url in article_urls:
        text_list = return_text_url_title(url)
        if text_list != None:
            texts.append(text_list[0])
            urls.append(text_list[1])
            titles.append(text_list[2])

    new_dataset = pd.DataFrame({
        'Concerning' : [country] * len(urls),
        'URL' : urls,
        'Text' : texts,
        'Title' : titles
        })

    country_csv_filename = "data\countries" + "\\" + country + ".csv"

    if os.path.exists(country_csv_filename):
        with open(country_csv_filename, "a"):
            new_dataset.to_csv(country_csv_filename, header = False)
    else:
        with open(country_csv_filename, "a"):
            new_dataset.to_csv(country_csv_filename, header = True)

    return country_csv_filename


def update_all(search_queries): 

    country_file_names = []

    for country_key in search_queries:
        country_file_name = csv_articles_for_country(country_key, search_queries)
        country_file_names.append(country_file_name)

    return country_file_names


















