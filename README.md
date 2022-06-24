# SentimentAnalysisForInstagramComments
This project focuses on classifying a comment or review into Positive or Negative Comment for an Intagram post. Therefore, implying the sentiment of the reviewer. I have used Naive Bayesian Classifier to do this job. On a impactful level, there are more powerful classifier and models that can score the reviews into a range of scores. The goal of this project is to get familiar with a very basic NLP model and how NLTK modules work as a whole to achieve a bigger goal.

#Restaurant_Reviews.csv:
Training data used to train the model which contains reviews and likes for a Restaurant.

#ScrapeInstagramComment.py:
Used Instagram API call and a short-lived token to scrape through the already logged in User and finding comments from their own profile posts using post ID which is fetched using get_own_post() function and this post ID acts as input for delete_negative_comments() which not really deletes but divides the comments into Positive and Negative comments.

#SentimentAnalysis.py:
Used Naive's Bayesian Classifier to train the model. This file first reads the tsv(tab separated values converted to csv file later) file. Later, PorterStemmer module to find the root word removing morphological affixes from words leaving word stem for eg. A stemming algorithm reduces the words “chocolates”, “chocolatey”, and “choco” to the root word, “chocolate”. Also, used stopwords module from nltk.corpus to remove stop words (commonly used words like 'a', 'an', 'the', 'in') from the text. Finally, check() function which takes a comment as argument is used to classify the comment into Positive and Negative comments through trained model 'classifier'.

Take Away:
1) Got to know some interesting things about the research in Sentiment Analysis and NLP.
2) Got familiar with quite a few but effective applications of NLTK and Pandas modules.
3) Got familiar with Web Scrapping algorithms used world-wide and tools and frameworks that can be used to achieve the same.

Upgradation:
1) Can use better models such as BERT model or HuggingFace Transformers used in Pytorch to make the classifier more efficient and thus increasing the range of sentiment scores.
2) Instagram Web Scrapper code is just a dummy code that needs to be upgraded to a fully-fledged implementation. Will keep upgrading the same project to make it better as I learn and grow.

