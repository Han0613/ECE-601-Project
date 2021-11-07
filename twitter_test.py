# The test bench will the limit of keywords input
# And check the special characters of inputs
# And make sure the last num of inputs is digit.

import sys
import string
import twitter

usr_input = sys.argv[1:]

# limit to 3 keywords
def keyword_limit():
    assert len(usr_input) <= 4, "Too many inputs!"

# make sure no special characters in user input
# special character list: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
def special_char():
    for keyword in usr_input:
        string_set = set(keyword)
        punctuation_set = set(string.punctuation)
        assert not string_set.intersection(punctuation_set),"Special characters are found!"

# test the last number search number of tweets
def tweet_num():
    assert usr_input[-1].isnumeric(),"Not a number!"

if __name__ == '__main__':
    keyword_limit()
    special_char()
    tweet_num()
    twitter.sentiment_analyze(usr_input)
