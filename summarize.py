#This module is for constructing the actual summary given the tuples formed by points functions in each module

from rank_processing import normalized_points
from processdoc import Textblob_with_file_name


def create_summary(text: Textblob_with_file_name , length_of_summary = None):
    '''Creates the overall summary based on points given for certain criteria'''
    points_list = normalized_points(text)

    if length_of_summary == None:
        length_of_summary = len(points_list)//5

    points_list = sorted(sorted(points_list,key = lambda x:x[1],reverse=True)[:length_of_summary],key= lambda x:x[0])

    for i in range(length_of_summary):
        yield str(text.sentences[points_list[i][0]-1])
