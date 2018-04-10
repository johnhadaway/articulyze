# Predicting Pultizers
This file is a way to keep track of progress.

## Logistic Regression
training size: 500
testing size: 250

### Word Count
Using Logistic Regression with just word counts gets you ~87% accuracy on predicting Pulitzers, high of 89%.

### Word Count, Flesch
Over 10 runs averages ~87% accuracy, high of 90%.

### (Na) 2 node output 
With 2 node output, accuracy 87%, 7 percent miss rate when applied to pulitzer-winning dataset

## After normalizing data:
the accurate is always 90%+, will test more in depth later

## 4/8/18: updates: website / scraping algorithim 
scraping algorithim: now also gets article title 
website: more design elements etc... waiting on website designer (my sister lol) to send  stuff

# 4/10/18: updates: 
progress started on main_script -- will fix sql interaction soon / figure out how to link that w the website
fixed other modules, ranking and scraping, to work with main_script 
no progress on website - waiting on sister / busy w research this week. 
tenative launch date: april 27. 

# LONG TERM: note on things to do re algorithim (less important immediately): 
try removing word count + scaling data 
with removed word count in one node model, 79% accuracy.
