'''
Program: set_membership.py
Author: Joshua M McGinley
Last Date Modified: 10/19/2022

Write a program that prompts the user for test scores, stores them in a dictionary, and averages the scores.

    Write a function get_test_scores()
        Create an empty dictionary scores_dict = dict()
        Prompt the user to input the number of test scores, store in num_scores
        Write a loop to get each of the num_scores test scores
        Prompt the user to input each test score and store in score. (Validate the input!)
        Add score to scores_dict  # HINT: update the dictionary
    Write a second function average_scores() that accepts the dictionary as the only parameter and returns the average scores
        Use len() to determine your num_scores for calculation
        Note a dictionary is a set of key, value pairs.
            You can get the keys with .keys() function
            You can access the value using a key variable scores_dict.get(k)
    What about testing?
        Write a main to test your functions
        Unit Tests can also help test average_scores()

Sumit this before moving on to writing the unit tests for average_scores() in the next assignment.
This is worth 10 points.
'''

def get_test_scores():
    scores_dict = dict()
    num_scores = int(input('How many test scores will you enter? '))
    index = 0
    while (index < num_scores):
        score = int(input('Enter score: '))
        ver_key = str('score' + str(index + 1))
        scores_dict.update({ver_key:score})
        index = index + 1
    return scores_dict

def average_scores(scores_dict):
    x = len(scores_dict)
    accum = 0
    for value in scores_dict.values():
        accum = accum + value
    average = accum / x
    return average



if __name__=='__main__':
    my_grades = get_test_scores()
    print(my_grades)
    scores_dict = average_scores(my_grades)
    print(scores_dict)
