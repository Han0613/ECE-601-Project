#! /usr/bin/env python
# python ECE601_project.py {filename}

from google.cloud import language_v1
import sys

# get overall sentiment score and sentence sentiment scores
def get_score(filename):
    # import the review for sentiment score
    with open (filename, "r") as review_file:
        content = review_file.read()

    # request API
    client = language_v1.LanguageServiceClient()
    document = language_v1.Document(content=content, type_=language_v1.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(request={'document': document})

    #calculate the sentiment score
    overall_score = content.sentiment.score # overall sentiment score
    sentence_score = [] # sentence sentiment scores of each sentence in sequence
    for index, sentence in enumerate(annotations.sentences):
        sentence_score = sentence_score.append(sentence.sentiment.score)

    return overall_score, sentence_score

if __name__ == "__main__":
    # input filename
    filename = sys.argv[1]
    # get score
    overall_score, sentence_score = get_score(filename)
    # output
    print("The overall sentiment score is ", overall_score)
    print("Sentence scores are ", sentence_score)
