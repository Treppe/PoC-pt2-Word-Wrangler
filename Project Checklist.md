# Project Checklist

[Phase 1 - List Mutating Functions](#Phase 1 - List Mutating Functions)

[Phase 2 -  Merge Sorting](#Phase 2 -  Merge Sorting)

[Phase 3 - All Strings Generator](#Phase 3 - All Strings Generator)

[Final Touch](#Final Touch)

## Phase 1 - List Mutating Functions

You should first write the functions $\color{red}{\verb|remove_duplicates(list1)|}$ and $\color{red}{\verb|intersect(list1, list2)|}$. These functions can both be written iteratively (using loops, not recursion). All of the arguments to these functions are lists in ascending order. Both functions should return new sorted lists.

### 1. def remove_duplicates(list1)

Should return a new sorted list with the same elements as the input, $\color{red}{\verb|list1|}$, but without any duplicate elements.

- [x] Implement test for function
- [x] Implement function
- [x] Test function
- [x] Fix bugs
- [x] Commit changes

### 2. def intersect(list1, list2)

 Should return a new sorted list that contains only the elements that are in both input lists, $\color{red}{\verb|list1|}$ and $\color{red}{\verb|list2|}$.

- [x] Implement test for function
- [x] Implement function
- [x] Test function
- [x] Fix bugs
- [x] Commit changes



> Remember that the input lists will already be sorted. You should exploit this fact to make these functions simpler to write than if you had to handle arbitrary lists.

## Phase 2 -  Merge Sorting

You should next implement merge sorting. To do so, you will need to write two functions, $\color{red}{\verb|merge(list1, list2)|}$ and $\color{red}{\verb|merge_sort(list1)|}$. The input lists to $\color{red}{\verb|merge|}$ will both be lists in ascending order. The input to $\color{red}{\verb|merge_sort|}$ will be an unsorted list. While you could write $\color{red}{\verb|merge|}$ recursively, you should write it iteratively because it will generate too many recursive calls for reasonably sized lists. However, you must write $\color{red}{\verb|merge_sort|}$ recursively.

### 1. def merge(list1, list2)

Should return a new sorted list that contains all of the elements in either $\color{red}{\verb|list1|}$ and $\color{red}{\verb|list2|}$.

- [x] Implement test for function
- [x] Implement function
- [x] Test function
- [x] Fix bugs
- [x] Commit changes

### 2. def merge_sort(list1)

Should return a new sorted list that contains all of the elements in $\color{red}{\verb|list1|}$ sorted in ascending order.

- [x] Implement test for function
- [x] Implement function
- [x] Test function
- [x] Fix bugs
- [ ] Commit changes

> Again, remember that the input lists to \merge will already be sorted. You should exploit this fact to make it simpler to write. Further, merge_sort should *use* merge to help sort the list!



## Phase 3 - All Strings Generator

Now, you should implement $\color{red}{\verb|gen_all_strings(word)|}$. This function is the heart of the word wrangler game. It takes a string as input and returns a list of strings. It should return *all* possible strings that can be constructed from the letters in the input $\color{red}{\verb|word|}$. More formally, it should return all strings of length 0 to $\color{red}{\verb|len(word)|}$ that can be composed of the letters that occur in $\color{red}{\verb|word|}$, in any order. Further, each letter should be considered distinct, so if the same letter appears twice in the word, then the output will have duplicate strings.

For example, if $\color{red}{\verb|word|}$ is $\color{red}{\verb|"aab"|}$, $\color{red}{\verb|gen_all_strings|}$ would return $\color{red}{\verb|["", "b", "a", "ab", "ba", "a", "ab", "ba", "aa", "aa", "aab", "aab", "aba", "aba", "baa", "baa"]|}$. Notice that the string $\color{red}{\verb|"aa"|}$ appears twice in the output. This is because each $\color{red}{\verb|a|}$ is considered distinct, so these two strings correspond to the two different orderings of the two $\color{red}{\verb|a|}$ letters in the input word. Note that it does not matter in what order the strings appear in the list. The functions you have already written will be used afterwards to sort and remove duplicates from the final lists (you should *not* do this within $\color{red}{\verb|gen_all_strings|}$).

Note that this function is similar (but *not* identical) to something that you have previously written in this course. This time, however, ordering of the output list is not important, duplicates are allowed, and you must write it recursively. The basic idea is as follows:

- [x] Implement test for function
- [x] Implement function
  - [x] Split the input $\color{red}{\verb|word|}$ into two parts: the first character ($\color{red}{\verb|first|}$) and the remaining part ($\color{red}{\verb|rest|}$).
  - [x] Use $\color{red}{\verb|gen_all_strings|}$ to generate all appropriate strings for $\color{red}{\verb|rest|}$. Call this list $\color{red}{\verb|rest_strings|}$.
  - [x] For each string in $\color{red}{\verb|rest_strings|}$, generate new strings by inserting the initial character, $\color{red}{\verb|first|}$, in all possible positions within the string.
  - [x] Return a list containing the strings in $\color{red}{\verb|rest_strings|}$ as well as the new strings generated in step 3.
- [x] Test function
- [x] Fix bugs
- [x] Commit changes

## Final Touches

Finally, you should implement $\color{red}{\verb|load_words(filename)|}$ which will load a "dictionary" (not a Python dictionary, but rather a conventional dictionary with valid English language words) from a file. The dictionary file is simply one string per line, where each string is a valid word in the game. You can see the dictionary file [here](http://codeskulptor-assets.commondatastorage.googleapis.com/assets_scrabble_words3.txt). You may use either $\color{red}{\verb|urllib2.urlopen|}$urllib2.urlopen (either in CodeSkulptor or locally) or $\color{red}{\verb|open|}$ (only if you are running locally and have downloaded the file) to open the file. Note that this function will not be tested. You only need implement it if you wish to play the word wrangler game using the provided GUI.