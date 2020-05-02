"""
Student code for Word Wrangler game
"""

import urllib2
import codeskulptor
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """
    new_list = list(list1)
    
    for idx in range(len(list1) - 1):
        if list1[idx] == list1[idx+1]:
            new_list.remove(list1[idx])
            
    return new_list

def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """
    new_list = []
    
    for element in list1:
        if element in list2:
            new_list.append(element)
            
    return new_list

# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing those elements that are in
    either list1 or list2.

    This function can be iterative.
    """
    merged_list = []
    copy_list1 = list(list1)
    copy_list2 = list(list2)
    
    while True:
        if len(copy_list1) != 0 and len(copy_list2) !=0:
            if copy_list1[0] <= copy_list2[0]:
                merged_list.append(copy_list1[0])
                copy_list1.pop(0)
            else:
                merged_list.append(copy_list2[0])
                copy_list2.pop(0)
        elif len(copy_list1) == 0:
            merged_list += copy_list2
            break
        else:
            merged_list += copy_list1
            break
            
        
    return merged_list
 
    
def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    """
    # Base 
    if len(list1) <= 1 or (len(list1) == 2 and list1[0] < list1[1]):
        return list1
    elif len(list1) == 2:
        return list1[::-1]
    
    div_idx = (len(list1) - 1) // 2
    list_half1 = list1[:div_idx]
    list_half2 = list1[div_idx:]
    return merge(merge_sort(list_half1), merge_sort(list_half2))

# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    """
    # Base Case:
    if len(word) == 0:
        return ['']
    elif len(word) < 2:
        return ['', word]
    
    # Recursive Step:
    first = word[0]
    rest = word[1:] 
    rest_strings = gen_all_strings(rest)
        
    new_strings = []
    for string in rest_strings:
        for pos in range(len(string) + 1):
            new_strings.append(string[:pos] + first + string[pos:])
           
    return rest_strings + new_strings

# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    words_list = []
    a_file = urllib2.urlopen(codeskulptor.file2url(filename))
    for line in a_file.readlines():
        words_list.append(line[:-1])
        
    return words_list

def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates, 
                                     intersect, merge_sort, 
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()

    
    