# importing required library
import pandas as pd
import requests
import SentimentAnalysis
# making a variable for received access token

access_token = '8911134469.1efef08.29bd2a882e594528b11ac2aaa137adf9'
# setting the base url that is to be used everywhere
base_url = 'https://api.instagram.com/v1/'
def get_own_post():
    # setting up endpoint url and accessing json object
    request_url = (base_url + 'users/self/media/recent/?access_token=%s') % access_token
    own_media = requests.get(request_url).json()
    # if request is successful
    if own_media['meta']['code'] == 200: #Status_Code=200 means Success Status
        # if some posts exist
        if len(own_media['data']):
            c = True
            x = 1
            # loop to avoid crashes on invalid insertion
            while c:
                x = 1
                c = False

            # downloading the post

            if own_media['data'][x - 1]['type'] == 'image':
                post_name = own_media['data'][x - 1]['id']

                # request unsuccessful
    else:
        print('Status code other than 200 received!')
    return (post_name)


def delete_negative_comment():
    # calling the function for getting media id
    media_id = get_own_post()
    df = pd.DataFrame()
    # setting endpoint url and accessing json object
    request_url = (base_url + 'media/%s/comments/?access_token=%s') % (media_id, access_token)
    comment_info = requests.get(request_url).json()
    # if request successful
    if comment_info['meta']['code'] == 200:
        # if comment exists
        if len(comment_info['data']):
            # iterating over all comments
            for x in range(0, len(comment_info['data'])):
                # getting comment id
                comment_id = comment_info['data'][x]['id']
                # getting comment text
                comment_text = comment_info['data'][x]['text']
                # analysing comment by 'TextBlob'
                pred = SentimentAnalysis.check(comment_text)
                df['comment_text'] = comment_text
                # checking whether sentiments of comment are more negative than positive
                if pred == '0':
                    df['Sentiment'] = "Negative Comment"
                # positive sentiments are greater than negative sentiments!
                else:
                    df['Sentiment'] = "Positive Comment"
        else:
            print("There are no comments on this post yet.")
    # request unsuccessful
    else:
        print("Status code other than 200 received.")

    return df

df = delete_negative_comment()
print(df.head(10))
Positive_Comments = df.Sentiments.map(lambda p: 'Positive Comment' in p).sum()
Negative_Comments = df.Sentiments.map(lambda p: 'Negative Comment' in p).sum()
print("Total Positive Comments are: ",Positive_Comments,", while Total Negative Comments are: ",Negative_Comments)
