# psuedo code
# use scraper to scrape today's relevant news into data/countries 
# call ranking.py on them => save dic as pandas.df for each country
# use sqllite to store pandas.dfs into sql database
# remove items from more than 7 days ago from sql databases, into archive, re-sort sql databases based on scores

import ranking_a as ranker
import news_scraping as scraper
import pandas as pd

search_countries = ["afghanistan", "burundi", "cameroon", "central+african+republic", "chad", "democratic+republic+of+the+congo", "ethiopia", "haiti", "iraq", "libya", "mali",
    "myanmar", "niger", "nigeria", "palestine", "somalia", "south+sudan", "sudan", "syria", "ukraine", "yemen"]
additional_queries = ["", "crisis", "humanitarian"]

def extract_country_from_file_name(file_name):
    # file structure "data\countries\country_name.csv"

    start = file_name.find('countries' + "\\") + 10
    end = file_name.find('.csv', start)
    return file_name[start:end]

def daily_script(): 

    # generate search queries
    search_queries = scraper.generate_search_queries(search_countries, additional_queries)

    # update all / return file names
    file_names = scraper.update_all(search_queries)

    ranked_dictionaries = {}

    for file_name in file_names:
        print(file_name)
        ranked_dictionary = ranker.ranking(file_name)
        country_name = extract_country_from_file_name(file_name)
        ranked_dictionaries.update({country_name : ranked_dictionary})

    # store all of the dictionaries into sql database 
    # -> remove items from more than 7 days from database, into archive
    # re-sort all databases by score 

    return None

daily_script()