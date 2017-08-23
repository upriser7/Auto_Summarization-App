# This module looks for sentences that are examples (For example,.....) and also looks for sentences that are summaries (In Conclusion,..)

from textblob import TextBlob
from project_tools import *
from processdoc import ProcessDoc

def example_sentence(text:TextBlob): ## Not quite right, will probably be implemented a different way later on
    '''returns a list of two tuples (# of sentence, 0 if the sentence is not a example sentence and 1 if it is)'''
    set_of_example_phrases = {'example','Eg','said','illustrate','demonstrate','specifically','instance'}
    return [(i+1,len(set_of_example_phrases.intersection(set([j for j in text.sentences[i].words])))) for i in range(len(text.sentences))]


def summary_sentence(text:TextBlob):
    '''returns a list of two tuples (# of sentence, 0 if the sentence is not a summary sentence and 1 if it is)'''
    set_of_summary_phrases = {'in conclusion','therefore','in summary', 'to end','in other words','in short','to sum up'}
    result = list()

    for i in range(len(text.sentences)):
        for phrase in set_of_summary_phrases:
            check = False
            if str(text.sentences[i]).lower().startswith(phrase):
                check = True
        if check:
            result.append((i+1,1))
        else:
            result.append((i+1,0))
    return result
    # return [(i+1,len(set_of_summary_phrases.intersection(set([j for j in text.sentences[i].words])))) for i in range(len(text.sentences))]

def citation_sentence(text:TextBlob):
    '''returns a list of two tuples (# of sentence, 0 if the sentence is not a citation sentence and 1 if it is)'''
    set_of_citation_phrases = {'works cited','cited','bibliography','article','author','state','stated','said'} ## add more here
    result = list()

    for i in range(len(text.sentences)):
        for phrase in set_of_citation_phrases:
            check = False
            if phrase in text.sentences[i].lower():
                check = True
        if check:
            result.append((i+1,1))
        else:
            result.append((i+1,0))
    return result

def points_by_example_and_summary_sentence(text:TextBlob):
    '''Calculates points by example and summary sentences and returns a list of two tuples (# of sentence, no of points)'''
    return combine_with_score_weight(example_sentence(text),summary_sentence(text),citation_sentence(text),relative_points=[-1,2,-1])


# if __name__ == '__main__':
#     ##For testing
#     doc = ProcessDoc('AP Final Draft - Meghana Jain.docx')
#     text = doc.convert_to_textblob()
#     print(example_sentence(text))
#     print()
#     print(summary_sentence(text))
