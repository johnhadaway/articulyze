import pandas as pd 
import numpy as np 
import ranking_a as rank
import json 
import os 
import glob

def generate_processed_df(dataset, winning_articles = True): 

	"""
	- FUNCTION: modifies the dataset (assumes that these are winning articles, change parameter if not true)
	- INPUT PARAMETERS: article dataset ('URL', 'Text' columns), winning_articles (option - bool) 
	- RV: modified  dataset
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

	if winning_articles: 
		bin_ = 1
	else: 
		bin_ = 0

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
		'Dale_Chall' : article_dcs,
		})

	new_data_frame["bin"] = [bin_] * len(article_flesch)

	return new_data_frame

def read_files_into_list(path_to_folder): 
	return glob.glob(path_to_folder + '/*.csv')

def process_articles_for_neural_net(paths_to_datasets, 
	winning_articles = True): 

	processed_data_frames = []

	for path in paths_to_datasets: 
		df = pd.read_csv(path, encoding="latin1").dropna()
		df_processed = generate_processed_df(df, winning_articles)
		print(df_processed)
		processed_data_frames.append(df_processed)

	print(processed_data_frames)

	if len(processed_data_frames) > 1: 
		processed_data_frame = pd.concat(processed_data_frames)
		data_frame = processed_data_frame.drop_duplicates(['Flesch'])
	else: 
		data_frame = processed_data_frames[0]

	if winning_articles: 
		file_name = "data_for_neural_net/pulitzer_winning.csv"
	else: 
		file_name = "data_for_neural_net/non_pulitzer_winning.csv"

	with open(file_name, 'a'):
		data_frame.to_csv(file_name, header = True)

	return None

#process_articles_for_neural_net(read_files_into_list("data\countries"), winning_articles = False)
process_articles_for_neural_net(["data\pul_dset.csv"], winning_articles = True)













	





