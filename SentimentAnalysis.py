import pandas as pd

dataset = pd.read_csv("Restaurant_Reviews.csv", delimiter ="\t", quoting = 3)

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
corpus = []
corp = []
for i in range(0,3013):
    review = re.sub('[^a-zA-Z]', ' ', dataset['Review'][i])
    review = review.lower()
    review = review.split()
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features = 1500)
X = cv.fit_transform(corpus).toarray()
y = dataset.iloc[:,1].values

# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Fitting Naive Bayes to the Training set
from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print ("\n\nConfusion Matrix:\n", cm)
print("Accuracy:", classifier.score(X_test, y_test)*100, "%")

def check(r):
    rev = re.sub('[^a-zA-Z]', ' ', r)
    rev = rev.lower()
    rev = rev.split()
    ps = PorterStemmer()
    rev = [ps.stem(word) for word in rev if not word in set(stopwords.words('english'))]
    rev = ' '.join(rev)
    corpus.append(rev)

    a = cv.fit_transform(corpus).toarray()
    y_new = classifier.predict(a)
    a = y_new[-1]
    return str(a)

Comments = ["Wow... Loved this place.","Not tasty and the texture was just nasty.","The fries were great too."]
l = []
for comm in Comments:
    pred = check(comm)
    new_df = pd.DataFrame()
    print(pred)
    if pred == '0':
        l.append("Negative Comment")
    # positive sentiments are greater than negative sentiments!
    else:
        l.append("Positive Comment")
df = pd.DataFrame({'Sentiment':l})

Positive_Comments = df.Sentiment.map(lambda p: 'Positive Comment' in p).sum()
Negative_Comments = df.Sentiment.map(lambda p: 'Negative Comment' in p).sum()
print("Total Positive Comments are: ",Positive_Comments,", while Total Negative Comments are: ",Negative_Comments)