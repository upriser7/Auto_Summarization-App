#This module is for identifying high freuency words and scoring sentences with these words higher

from textblob import TextBlob
from collections import defaultdict
from processdoc import ProcessDoc
from project_tools import *
import math

def high_frequency_words(text: TextBlob) -> set:
    '''returns a set of the 100 most used words'''
    words = defaultdict(int)
    for word in text.words:
        words[str(word)] += 1
    words_list = sorted(list(words.items()), key=lambda x: x[1], reverse=True)[:100]
    return set([word for word, number in words_list])

def high_tfidf_words(text:TextBlob) -> set:
    '''returns a set of the 100 most important words'''
    return set(sorted(list(text.words.lower()), key = lambda x : tf_idf_score(x,text))[:100])


def no_of_high_frequency_words(text:TextBlob):
    '''returns a list of two tuples (# of sentence, no of high frequency words)'''
    set_of_high_frequency_words = high_frequency_words(text)
    return [(i+1,len(set_of_high_frequency_words.intersection(set([j for j in text.sentences[i].words])))) for i in range(len(text.sentences))]

def no_of_high_tfidf_words(text:TextBlob):
    '''returns a list of two tuples (# of sentence, no of high tfidf words)'''
    set_of_high_tfidf_words = high_tfidf_words(text)
    return [(i+1,len(set_of_high_tfidf_words.intersection(set([j for j in text.sentences[i].words.lower()])))) for i in range(len(text.sentences))]



def points_by_high_frequency_words(text:TextBlob): # Use tf-idf calculations too?
    '''Calculates points by high frequency words and returns a list of two tuples (# of sentence, no of points)'''
    return combine_with_score_weight(no_of_high_frequency_words(text),no_of_high_tfidf_words(text),relative_points=[1,1])


# if __name__ == '__main__':
#     ##For testing
#     doc = ProcessDoc('AP Final Draft - Meghana Jain.docx')
#     text = doc.convert_to_textblob()
#     print(high_frequency_words(text))
#     print()
#     print(tf_idf_score('their',text))
#     print(tf_idf_score('would', text))
#     print(tf_idf_score('them', text))
#     print(tf_idf_score('have', text))
