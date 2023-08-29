#!/usr/bin/python3
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

#NOTE  BEFORE, THIS CAME IN A FUNCTION, I REMOVED IT!
message= "hello, my name is wenhe"

df = pd.read_csv('spam_messages.csv')
#if there is an error, with a line number given, this means that one of the added lines are incorrect. sometimes, it can be caused by a line not being added as a new line, but following an old one, or simply because of some comma..

messages = pd.DataFrame(data = df, columns=['rating', 'message'])

message_train = messages['message']
rating_train = messages['rating']

model = CountVectorizer()
#create a dictionary with value of position of word

transformed_message_train = model.fit_transform(message_train)
#create a matrix with frequency of a word and the word

Multi = MultinomialNB()
Multi.fit(transformed_message_train, rating_train)

test_counts = model.transform([message])

final = Multi.predict(test_counts)
chances = round((float(Multi.predict_proba(test_counts)[0][1]*100)),5)

#print(final,type(final),chances,type(chances))

#Prediction is numpy array, another conditionnal to return a string

if final == 'spam':
    return_statement = 'This message is spam.-This message has a probability of {0}% of being spam.'.format(chances)
    final_arg = 'spam'
else:
    return_statement = 'This message is not spam.-This message has a probability of {0}% of being spam.'.format(chances)
    final_arg = 'ham'


import pickle

with open('model_pickle', 'wb') as f:
    #in the statement, I simply write the predictino (in my case, its named final) and the model
    pickle.dump(final, f)
#thiis creates a file named model_pickle

with open('model_pickle', 'rb') as f:
    mp = pickle.load(f)

mp.predict("Hello, my name is wenhe zhang")
