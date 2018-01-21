#Checks for sentence similarity (and group similar sentences together ??) implement levenstein distance???

from textblob import TextBlob
from project_tools import *
from difflib import SequenceMatcher
from high_frequency_words import high_frequency_words
import re
from collections import Counter

def similarity_by_sequence_matching(s1:str,s2:str):
    '''returns a tuple of which the first element is the similarity of sequence matching'''
    senquence_matcher = SequenceMatcher()
    senquence_matcher.set_seq1(s1)
    senquence_matcher.set_seq2(s2)
    return round(senquence_matcher.ratio(),2)

def sentiment_analysis_of_sentence(s:str):
    '''Uses the stock sentiment analysis in Textblob'''
    text = TextBlob(s)
    return text.sentiment[0],text.sentiment[1]

def cosine_similarity_score(s1:str, s2:str):
    '''finds the cosine similarity on the 2 sentences'''

    def text_to_vector(s: str):
        word = re.compile(r'\w+')
        return Counter(word.findall(s))

    vector1 = text_to_vector(s1)
    vector2 = text_to_vector(s2)

    nom = sum([vector1[i] * vector2[i] for i in set(vector1.keys()) & set(vector2.keys())])

    sum1 = sum([vector1[i]**2 for i in vector1.keys()])
    sum2 = sum([vector2[i]**2 for i in vector2.keys()])

    denom = math.sqrt(sum1)*math.sqrt(sum2)

    return round(float(nom)/denom,2) if denom else 0.0

def similarity_quotient(s1:str,s2:str):
    '''Combines everything in this module together'''
    sequence_match = similarity_by_sequence_matching(s1,s2)
    cosine_match = cosine_similarity_score(s1,s2)
    sentiment_s1 = sentiment_analysis_of_sentence(s1)
    sentiment_s2 = sentiment_analysis_of_sentence(s2)
    if abs(sentiment_s1[0] - sentiment_s2[0]) <= 0.6 and abs(sentiment_s1[1]-sentiment_s2[1]) <= 0.6:
        return round((1*sequence_match + 5*cosine_match)/6,2)
    return 0.0





# if __name__ == '__main__':
#     print(similarity_quotient('This is a sentence','This is a similar sentence'))
#     print(cosine_similarity_score('This is a sentence','Completely different sentence in the context'))
#     print(sentiment_analysis_of_sentence('This is a sentence'),'  --  ',sentiment_analysis_of_sentence('Completely different sentence in the context'))
#     print(similarity_by_sequence_matching('This is a sentence','Completely different sentence in the context'))
