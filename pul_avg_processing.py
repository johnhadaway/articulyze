import pandas as pd 
import numpy as np 
import ranking_a as rank
import json 

def add_vectors_ds(dataset): 

    """
    - FUNCTION: modifies the dataset
    - INPUT PARAMETERS: dataset
    - RV: modified dataset
    """
    update = dataset.copy()
    l_articles = update['Text'].tolist()

    article_flesch = []
    sentence_polarity = []
    sentence_subjectivity = []
    article_polarity = []
    article_subjectivity = []
    word_counts = []
    characters = []
    spache_percentages = []
    weasel_percentages = []
    dale_chall_percentages = []
    article_dcs = []

    for article in l_articles:
        sentence_sentiment = rank.tb_sentence_sentiment(article)
        article_sentiment = rank.tb_article_sentiment(article)

        article_flesch.append(rank.flesch_index(article))
        sentence_polarity.append(sentence_sentiment[0])
        sentence_subjectivity.append(sentence_sentiment[1])
        article_polarity.append(article_sentiment[0])
        article_subjectivity.append(article_sentiment[1])
        word_counts.append(rank.word_count(article))
        characters.append(rank.average_characters_per_word(article))
        spache_percentages.append(rank.percentage_spache(article))
        weasel_percentages.append(rank.percentage_weasel(article))
        dale_chall_percentages.append(rank.percentage_dale_chall(article))
        article_dcs.append(rank.dale_chall(article))

    new_data_frame = pd.DataFrame({
        'Flesch': article_flesch,
        'S_Polarity' : sentence_polarity,
        'S_Subjectivity' : sentence_subjectivity,
        'A_Polarity' : article_polarity,
        'A_Subjectivity' : article_subjectivity,
        'Word_Count' : word_counts,
        'Characters' : characters,
        'Spache_Percentage' : spache_percentages,
        'Weasel_Percentage' : weasel_percentages,
        'Dale_Chall_Percentage' : dale_chall_percentages,
        'Dale_Chall' : article_dcs
        })

    return update.join(new_data_frame)

def get_average(dataset, column_name):

    """
    - FUNCTION: returns the average of a column of a dataset
    - INPUT PARAMETERS: dataset (pandas df), column_name (string: column name)
    - RV: the average of a column
    """

    return dataset[column_name].mean()

def get_averages(dataset):

    """
    - FUNCTION: returns the average of all of the relevant columns
    - INPUT PARAMETERS: dataset (pandas df)
    - RV: dictionary mapping column name to its average
    """

    column_averages = {"Flesch" : int, "A_Polarity": int, "A_Subjectivity": int, \
        "S_Polarity" : int, "S_Subjectivity": int, "Word_Count": int, \
        'Characters' : float, 'Spache_Percentage' : float, 'Weasel_Percentage' : float, \
        'Dale_Chall_Percentage' : float, 'Dale_Chall' : float} #still being added to

    for column in column_averages:
        column_averages[column] = get_average(dataset, column)

    return column_averages

def read_pul_averages(pul_ds): 

    """
    - FUNCTION: helper function to compute the averages for the pulitzer dataset
    - INPUT PARAMETERS: pul_ds (pulitzer dataset)
    - RV: dictionary
    """
    pul_ds = add_vectors_ds(pul_ds)
    return get_averages(pul_ds)

def update_json(pul_ds_path):

    """
    - FUNCTION: uses all of the previous functions, generates averages for the pulitzer dataset,
    and saves it as a dictionary in JSON format.
    - INPUT PARAMETERS: path to pulitzer dataset
    - RV: n/a
    """
    #replace encoding with latin1 if utf-8 dnw
    pul_ds = pd.read_csv(pul_ds_path, encoding = 'utf-8').dropna()
    average_dictionary = read_pul_averages(pul_ds)

    with open('data\pul_averages.json', 'w') as f:
        f.write(json.dumps(average_dictionary))

    return None

# update_json("data\pul_dset.csv")








