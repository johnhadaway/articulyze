import ranking_a as ranker
import news_scraping as scraper
import pandas as pd
import sqlite3 as sqlite
import os
import datetime
from datetime import date

first_date = date(2018, 5, 7)

search_countries = ["afghanistan", "burundi", "cameroon", "central+african+republic", "chad", "democratic+republic+of+the+congo", "ethiopia", "haiti", "iraq", "libya", "mali",
    "myanmar", "niger", "nigeria", "palestine", "somalia", "south+sudan", "sudan", "syria", "ukraine", "yemen"]

test_countries = ["afghanistan", "burundi"]
additional_queries = ["", "crisis", "humanitarian"]

def extract_country_from_file_name(file_name):
    # file structure "data\countries\country_name.csv"

    start = file_name.find('countries' + "\\") + 10
    end = file_name.find('.csv', start)
    return file_name[start:end]

def daily_script(day_par):

    # delete all files in data\countries directory 
    fileList = os.listdir("data/countries")
    for fileName in fileList:
        os.remove("data/countries/"+fileName)

    # generate search queries
    search_queries = scraper.generate_search_queries(search_countries, additional_queries)

    # update all / return file names
    file_names = scraper.update_all(search_queries)

    country_to_articles_dic = {}

    # go through all file names and create dictionary mapping country name to ranked list of lists
    for file_name in file_names:
        print(file_name)
        ranked_list_of_lists = ranker.ranking(file_name)
        country_name = extract_country_from_file_name(file_name)
        country_to_articles_dic.update({country_name : ranked_list_of_lists})

    # connect to current_database (or create on first run), and create cursor object for it 
    conn_current = sqlite.connect("website\countries\current_unohca.db")
    cursor_current = conn_current.cursor()

    # update / create tables for each country in the database
    for country in country_to_articles_dic:
        country_name = str(country).replace("+", "")
        cursor_current.execute('create table if not exists [' + country_name + '] (url text, title text, score real, days_in_db integer)')
        conn_current.commit()

    # add one to all current rows in db's days_in_db
    """
    for country in country_to_articles_dic:
        country_name = str(country)
        cursor_current.execute('update ' + country_name + ' set days_in_db = days_in_db + 1')
        conn_current.commit()
    """

    # add new rows for every country
    for country in country_to_articles_dic:
        country_name = str(country).replace("+", "")
        article_info_lists = country_to_articles_dic[country]
        for article_info in article_info_lists:
            insert_sql = (article_info[1], article_info[2], article_info[3], day_par)
            cursor_current.execute('insert into [' + country_name + '] values (?, ?, ?, ?)', insert_sql)
            conn_current.commit()

    conn_current.close()

    return None

def __main__():

    current_date = datetime.date.today()
    delta = current_date - first_date
    day_par = delta.days + 1
    daily_script(day_par)

    print(str(day_par) + ": days in db")

    return None

__main__()
