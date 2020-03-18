# Please Note: This code is referenced from Nikos Koufos' Medium Article
# titled "Create your own Twitter Dataset with this Simple Python Scraper".
# Link to the Article: https://medium.com/analytics-vidhya/create-your-own-twitter-dataset-with-this-simple-python-scraper-710bf7c5dc04

import time 
from selenium import webdriver
import chromedriver_binary # Adds the chromedriver binary to path
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

# Setting up the Chrome Driver
browser = webdriver.Chrome()
driver.get("http://www.python.org")
assert "Python" in driver.title

# Grabbing all tweets that fall under the "forest fire acre" query
base_url = "https://twitter.com/search?q="
query = "forest fire acre"
url = base_url + query
num_of_tweets = 1000

# Grabbing the url and using the timer function
browser.get(url)
time.sleep(1)

# Function to get the tweets 
def get_tweets(browser):
    body = browser.find_element_by_tag_name('body')
    tweets = []
    while len(tweets) < num_of_tweets: 
        for _ in range(5):
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(1)
        tweets = browser.find_elements_by_class_name('content')

    return tweets

# Function to parse through tweets
def parse_and_save(tweets, num_of_tweets, query): 
    counter = 0 
    column_separator = ","
    tags_separator = '|'
    with open(query+"_tweets.csv", 'w', errors='ignore') as f: 
        f.write("Username" + column_separator + "Text" + column_separator + "Reply"\
                + column_separator + "Retweet" + column_separator + "Favorite"\
                + column_separator + "RefUsers" + column_separator + "Hashtags\n")
        
        for tweet in tweets: 
            if counter == num_of_tweets: 
                break; 
            user = tweet.find_element_by_class_name('username').text
            # new line
            text = tweet.find_element_by_class_name('tweet-text').text.replace('\n', ' ').replace(',',' ')
            stats = tweet.find_elements_by_class_name('ProfileTweet-actionCountForPresentation')

            reply = stats[0].text
            if not len(reply): 
                reply = '0'

            retweet = stats[1].text
            if not len(retweet): 
                retweet = '0'

            favorite = stats[3].text
            if not len(favorite): 
                favorite = '0'

            ref_users = '' 
            for user_ref in tweet.find_elements_by_class_name('twitter-atreply'): 
                ref_users += user_ref.text + tags_separator
            ref_users = ref_users[:-len(tags_separator)]
            if not len(ref_users):
                ref_users = '-'

            hashtags = ''
            for hashtag in tweet.find_elements_by_class_name('twitter-hashtag'):
                hashtags += hashtag.text + tags_separator
            hashtags = hashtags[:-len(tags_separator)]
            if len(hashtags) == 0: 
                hashtags = '-'

            line = user + column_separator + text + column_separator + reply \
                    + column_separator + retweet + column_separator + favorite \
                    + column_separator + ref_users + column_separator + hashtags + '\n'
            f.write(line)
            counter += 1 

# End of Twitter scraper 
browser.close()

