import nltk as nl 
import pandas as pd 
import numpy as np
from textblob import TextBlob  
from collections import Counter
from operator import itemgetter
from nltk.tokenize import RegexpTokenizer
import json
from keras.models import model_from_json
from sklearn import preprocessing
from sklearn.externals import joblib



ds = pd.read_csv('data\pul_dset.csv')
ds = ds.dropna()
l_articles = ds['Text'].tolist() #for testing

spache_words = json.load(open('data\spache_words.json'))
dale_chall_words = json.load(open('data\dale_chall_words.json'))
weasel_words = [word.strip() for word in open('data\weasel_phrases.txt').readlines()]

### AUXILLARY FUNCTIONS ###
###########################

def tokenize_article(article): 

    """
    - FUNCTION: auxillary function to tokenize articles
    - INPUT PARAMETERS: article (string: article text)
    - RV: list of tokens
    """

    return RegexpTokenizer(r'\w+').tokenize(article)

def flesch_index(article): 

    """ 
    - FUNCTION: flesch_index calculation for an article
    - INPUT PARAMETERS: article (string: article text)
    - RV: flesch index
    """

    c = Counter(article) 
    sentence_count = c['.'] + c[':'] + c['!'] + c['?']
    word_count = len(article.split()) 
    syllable_count = 0 

    for word_unit in article.split(): 
        word_c = Counter(word_unit)
        for end in ["es", "ed", "e"]:
            if word_unit.endswith(end):
                syllable_count -= 1
        for vow in ["a", "e", "i", "o", "u"]:
            syllable_count += word_c[vow]
        if word_unit.endswith("le"):
            syllable_count += 1

    return float((206.835 - (1.015*(word_count/sentence_count)) - \
        (84.6*(syllable_count/word_count))))

def tb_sentence_sentiment(article): 

    """
    - FUNCTION: returns the average sentence polarity and subjectivity [TextBlob]
    - INPUT PARAMETERS: article (string: article text)
    - RV: tuple w/ (average sentence polarity, average sentence subjectivity)
    """

    article = TextBlob(article)
    sentence_polarity = []
    sentence_subjectivity = []
    for sentence in article.sentences:
        sentence_polarity.append(sentence.sentiment.polarity)
        sentence_subjectivity.append(sentence.sentiment.subjectivity)
    return (float(sum(sentence_polarity)/len(sentence_polarity)),
        float(sum(sentence_subjectivity)/len(sentence_subjectivity)))

def tb_article_sentiment(article): 

    """
    - FUNCTION: returns the article polarity and subjectivity [TextBlob]
    - INPUT PARAMETERS: article (string: article text)
    - RV: tuple (article polariy, article subjectivity)
    """

    article = TextBlob(article)
    return (article.sentiment.polarity, article.sentiment.subjectivity)

def word_count(article):

    """
    - FUNCTION: returns the word count for an article
    - INPUT PARAMETERS: article (string: article text)
    - RV: int (word count)
    """

    tokens = tokenize_article(article)
    return len(tokens)

def average_characters_per_word(article):

    """
    - FUNCTION: returns the average characters per word for an article
    - INPUT PARAMETERS: article (string: article text)
    - RV: float (average characters per word)
    """

    tokens = tokenize_article(article)
    characters_in_word = [len(word) for word in tokens]
    return sum(characters_in_word)/len(characters_in_word)

def percentage_spache(article): 

    """
    - FUNCTION: returns the percentage of words in an article that are
    spache words (from the Spache Readability Formula)
    - INPUT PARAMETERS: article (string: article text)
    - RV: float (percentage of words in the article that are spache words)
    """

    article = article.lower()
    tokens = tokenize_article(article)
    spache_occurences = 0

    for spache_word in spache_words:
        for token in tokens:
            if spache_word == token:
                spache_occurences +=1

    return float(spache_occurences/len(tokens))

def percentage_weasel(article):

    """
    - FUNCTION: returns the percentage of weasel phrases in an article
    (sources: wikipedia // grammar.about.com // matt.might.net )
    - INPUT PARAMETERS: article (string: article text)
    - RV: float (percentage of weasel phrases in an article)
    """

    article = article.lower()
    tokens = tokenize_article(article)
    weasel_occurences = 0

    for weasel in weasel_words:
        for token in tokens:
            if weasel == token:
                weasel_occurences += 1

    return float(weasel_occurences/len(RegexpTokenizer(r'\w+').
        tokenize(article)))

def percentage_dale_chall(article): 

    """
    - FUNCTION: returns the percentage of dale chall familiar words in an article
    - INPUT PARAMETERS: article (string: article text)
    - RV: float (percentage of dale chall words in an article)
    """

    article = article.lower()
    tokens = tokenize_article(article)
    dale_chall_occurences = 0

    for dale_chall in dale_chall_words:
        for token in tokens:
            if dale_chall == token:
                dale_chall_occurences += 1

    return float(dale_chall_occurences/len(tokens))

def dale_chall(article): 

    """
    - FUNCTION: returns the dale chall score of an article (source for equation: wikipedia)
    - INPUT PARAMETERS: article (string: article text)
    - RV: float (dale_chall score)
    """

    article = article.lower()
    tokens = tokenize_article(article)
    c = Counter(article)
    sentence_count = c['.'] + c[':'] + c['!'] + c['?']
    non_dale_chall_occurences = 0

    for token in tokens:
        if token not in dale_chall_words:
            non_dale_chall_occurences += 1

    difficult_words_p = (non_dale_chall_occurences / len(tokens)) * 100

    if difficult_words_p > 5:
        return ((0.1579)*(difficult_words_p)) + \
        ((0.0496)*(len(tokens)/sentence_count)) + 3.6365
    else:
        return ((0.1579)*(difficult_words_p)) + \
        ((0.0496)*(len(tokens)/sentence_count))

### RANKING ALGORITHIM ### 
##########################

def similarity(new_article, pul_averages): 
    """
    - FUNCTION: returns the similairty of a single article to the pulitzer articles
    - INPUT PARAMETERS: new_article (str: non-pulitzer article text), column_averages (dictionary passed from get_averages)
    - RV: similarity score (absolute value of average deviation from pulitzer averages)
    """

    new_sentence_sentiment = tb_sentence_sentiment(new_article)
    new_article_sentiment = tb_article_sentiment(new_article)


    # dictionary mapping index to tuple containing (article score, weight for metric)
    new_article_values = {'Flesch' : (flesch_index(new_article), 1),
        'S_Polarity' : (new_sentence_sentiment[0], 1),
        'S_Subjectivity' : (new_sentence_sentiment[1], 1),
        'A_Polarity' : (new_article_sentiment[0], 0.1),
        'A_Subjectivity' : (new_article_sentiment[1], 0.1),
        'Word_Count' : (word_count(new_article), 1),
        'Characters' : (average_characters_per_word(new_article), 1),
        'Spache_Percentage' : (percentage_spache(new_article), 1),
        'Weasel_Percentage' : (percentage_weasel(new_article), 1),
        'Dale_Chall_Percentage' : (percentage_dale_chall(new_article), 1),
        'Dale_Chall' : (dale_chall(new_article), 1)
        }

    deviations = []
    weights = []

    for key,value in new_article_values.items():
        p_deviation = ((new_article_values[key][0] - pul_averages[key])/pul_averages[key])
        deviations.append(p_deviation * new_article_values[key][1])
        weights.append(new_article_values[key][1])

    return abs((sum(deviations)/len(deviations)))

def similarity2(new_article): 
    """
    - FUNCTION: returns the similairty of a single article to the pulitzer articles
    - INPUT PARAMETERS: new_article (str: non-pulitzer article text), column_averages (dictionary passed from get_averages)
    - RV: similarity score (absolute value of average deviation from pulitzer averages)
    """

    new_sentence_sentiment = tb_sentence_sentiment(new_article)
    new_article_sentiment = tb_article_sentiment(new_article)
    # dictionary mapping index to tuple containing (article score, weight for metric)

    new_article_values = np.array([[
    	new_article_sentiment[0],
    	new_article_sentiment[1],
    	average_characters_per_word(new_article),
    	dale_chall(new_article), 
    	percentage_dale_chall(new_article),
    	flesch_index(new_article),
    	new_sentence_sentiment[0],
    	new_sentence_sentiment[1],
    	percentage_spache(new_article),
    	percentage_weasel(new_article),
    	word_count(new_article)]])

    print(new_article_values)

    json_file = open('data_for_neural_net/model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("data_for_neural_net/model.h5")
    print("Loaded model from disk")
    loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

    '''
    min_max_scaler = joblib.load("data_for_neural_net/scaler.save")
    scaled_X = min_max_scaler.fit_transform(new_article_values)
    '''

    predictions = loaded_model.predict(new_article_values)
    return predictions.item(0)

def ranking(path, num_to_return = None, threshold = None):
    """
    - FUNCTION: takes a dataset of non-Pulitzer-winning articles and ranks them acc. to
    similarity to Pulitzer-winning articles
    - INPUT PARAMETERS: path to article dataset (article dataset), num_to_return (optional int: number of articles to return)
    - RV: list of lists [[article text, url, similarity score]] ordered by similarity score,
    length dependent on num_to_return parameter
    """

    pul_averages = json.load(open('data\pul_averages.json'))
    article_ds = pd.read_csv(path,
        encoding = 'latin1').dropna().drop_duplicates(subset = ['URL', 'Text'])
    article_score_list = []

    for index, row in article_ds.iterrows():
        article_score_list.append([row['Text'][0], row['URL'],
            (1 - similarity(str(row['Text']), pul_averages))])

    if (num_to_return != None) & (threshold == None):
        return sorted(article_score_list, key = itemgetter(2),
            reverse = True)[0:num_to_return]
    elif (threshold != None) & (num_to_return == None):
        threshold_list = []
        for article in article_score_list:
            if article[2] >= threshold:
                threshold_list.append(article)
        return sorted(threshold_list, key = itemgetter(2),
            reverse = True)[0:len(threshold_list)]
    elif (num_to_return == None) & (threshold == None):
        num_to_return = len(article_score_list)
        return sorted(article_score_list, key = itemgetter(2),
            reverse = True)[0:num_to_return]
    else:
        raise Exception("ERROR: invalid parameters")
        return None


# print(ranking("data\g_test_yemen2.csv"))

print(len(l_articles))
a = similarity2(l_articles[80])
print(a)
