#This module houses functions that may be used in multiple modules

from collections import defaultdict
from textblob import TextBlob
import math

def combine_with_score_weight(*args, relative_points :list): # Can have variable no of arguments
    ## Used as combine_with_score_weight(*args, relative_points = whatever list of points)
    '''Combines multiple lists of two tuple according to the weights provided'''
    if len(args) != len(relative_points): raise AssertionError('Different no of arguments and relative points provided')
    assert args != None
    weighted_list = list()
    for no_list in range(len(args)):
        weighted_list.append(multiplier_list(args[no_list],relative_points[no_list]))
    result = defaultdict(int)
    for new_list in weighted_list:
        for sentence,number in new_list:
            result[sentence]+=number
    return list(result.items())


def multiplier_list(list_of_tuple, points_eq): #Takes a list of two tuples and the points_eq to multiply it with
    '''Returns a new list of two tuples with their accompaning number multiplied with points_eq'''
    result = list()
    for sentence,number in list_of_tuple:
        result.append((sentence,number*points_eq))
    return result

def tf_idf_score(word : str, text:TextBlob):
    ''''''
    tf = text.words.count(word) / len(text.words)
    word_in_text = 1 if word in text else 0
    idf = math.log(2)/(1+word_in_text)
    return tf*idf

def compare_with_list_by_function (query,comparing_list:list, fn:callable):
    ''''''
    value_list = [fn(i) for i in comparing_list]
    check = True
    for j in value_list:
        if fn(query) < j:
            check = False
    return check

def calculate_points(query:list,reference:list):
    ''''''
    return sum([reference[i-1][1] for i in query])

# if __name__ == '__main__':
#     ##For testing
#     print(combine_with_score_weight([(1,2),(2,3),(3,4)],[(1,2),(2,3),(3,4)],relative_points = [5,2]))
