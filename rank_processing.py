# This Module ranks all of the sentences after normalizating with similar sentences

from examples_and_summary_phrases import points_by_example_and_summary_sentence
from first_last import points_by_topic_first_last
from length_and_distance_from_begining import points_by_length_and_distance_from_begining
from high_frequency_words import points_by_high_frequency_words
from project_tools import combine_with_score_weight, calculate_points
from sentence_similarity import *
from processdoc import Textblob_with_file_name
from textblob import TextBlob


def points_with_all_modules(text:TextBlob): ## decide relative point worth
    '''calculates points with all modules except similarity caluculation'''
    return combine_with_score_weight(points_by_topic_first_last(text),
                                     points_by_length_and_distance_from_begining(text),
                                     points_by_high_frequency_words(text),
                                     points_by_example_and_summary_sentence(text),
                                     relative_points=[1,0.5,0.3,0.7])

def similar_sentences(text:TextBlob):
    '''finds a list of similar sentence to every sentence'''
    clusters_of_similar_sentences = list()
    for i in range(len(text.sentences)):
        similar_sentence_list = list()
        for j in range(len(text.sentences)):
            if similarity_quotient(str(text.sentences[i]),str(text.sentences[j])) >= 0.50:
                similar_sentence_list.append(j+1)
        clusters_of_similar_sentences.append((i+1,similar_sentence_list))
    return clusters_of_similar_sentences

def points_by_similarity(text:TextBlob):
    '''calculates points by similarity'''
    cluster = similar_sentences(text)
    sim_points_list = list()
    points_list = points_with_all_modules(text)
    for i in range(len(text.sentences)):
        sim_points_list.append((i+1, calculate_points(cluster[i][1],points_list)))
    return sim_points_list

def normalized_points(text:Textblob_with_file_name):
    '''final poins after calcualting with all modules'''
    return combine_with_score_weight(points_by_topic_first_last(text),
                                     points_by_length_and_distance_from_begining(text),
                                     points_by_high_frequency_words(text),
                                     points_by_example_and_summary_sentence(text),
                                     points_by_similarity(text),
                                     relative_points=[1,0.5,0.3,0.7,1.5])


if __name__ == '__main__':
    doc = Textblob_with_file_name('AP Final Draft - Meghana Jain.docx')
    print(normalized_points(doc))