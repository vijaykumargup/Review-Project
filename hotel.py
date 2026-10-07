import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn.model_selection import train_test_split #split data into train and test sets
from sklearn.feature_extraction.text import CountVectorizer #convert text comment into a numeric vector
from sklearn.feature_extraction.text import TfidfTransformer #use TF IDF transformer to change text vector created by count vectorizer
#With Tfidftransformer you will compute word counts using CountVectorizer and then compute the IDF values and only then compute the Tf-idf scores.
#With Tfidfvectorizer you will do all three steps at once.
from sklearn.svm import SVC# Support Vector Machine
from sklearn.pipeline import Pipeline #pipeline to implement steps in series
#from gensim import parsing # To stem data
#Gensim is an open-source library for unsupervised topic modeling and natural language processing, using modern statistical machine learning.
#from joblib import dump, load #save or load model
#from pdftotext import convert_pdf_to_string #converts pdf_to_string
from sklearn.metrics import accuracy_score  #accuracy

#Read the dataset
df = pd.read_csv("dataset.csv", encoding='latin1')

#Split the dataset in x and y
#X, y = df['word'], df['taxonomy']
X, y = df['text'], df['deceptive']   

#Split data in train and test sets.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)
