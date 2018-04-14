# psuedo code
# use scraper to scrape today's relevant news into data/countries 
# call ranking.py on them => save dic as pandas.df for each country
# use sqllite to store pandas.dfs into sql database
# remove items from more than 7 days ago from sql databases, into archive, re-sort sql databases based on scores

import ranking_a as ranker
import news_scraping as scraper
import pandas as pd
import sqlite3 as sqlite
import os

search_countries = ["afghanistan", "burundi", "cameroon", "central+african+republic", "chad", "democratic+republic+of+the+congo", "ethiopia", "haiti", "iraq", "libya", "mali",
    "myanmar", "niger", "nigeria", "palestine", "somalia", "south+sudan", "sudan", "syria", "ukraine", "yemen"]

test_countries = ["afghanistan", "burundi"]
additional_queries = ["", "crisis", "humanitarian"]

def extract_country_from_file_name(file_name):
    # file structure "data\countries\country_name.csv"

    start = file_name.find('countries' + "\\") + 10
    end = file_name.find('.csv', start)
    return file_name[start:end]

def daily_script(): 

    # delete all files in data\countries directory 
    fileList = os.listdir("data/countries")
    for fileName in fileList:
        os.remove("data/countries/"+fileName)

    # generate search queries
    search_queries = scraper.generate_search_queries(test_countries, additional_queries)

    # update all / return file names
    file_names = scraper.update_all(search_queries)

    country_to_articles_dic = {}

    # go through all file names and create dictionary mapping country name to ranked list of lists
    for file_name in file_names:
        ranked_list_of_lists = ranker.ranking(file_name)
        country_name = extract_country_from_file_name(file_name)
        country_to_articles_dic.update({country_name : ranked_list_of_lists})

    # connect to current_database (or create on first run), and create cursor object for it 
    conn_current = sqlite.connect("website\current_unohca.db")
    cursor_current = conn_current.cursor()

    # update / create tables for each country in the database (NOT DONE)

    # remove articles that have been there for more than 7 days and store them in an archive.db / delete duplicates in archive.db 

    # delete duplicates in current tables and re-sort all tables by score 

    return None

daily_script()