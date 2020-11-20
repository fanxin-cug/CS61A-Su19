""" Typing Test implementation """

from utils import *
from ucb import main
import datetime
# BEGIN Q1-5
"*** YOUR CODE HERE ***"

def lines_from_file(path):
    file=open(path)
    lst=readlines(file)
    for i in range(len(lst)):
        lst[i]=strip(lst[i])
    close(file)
    return lst

def new_sample(path,i):
    lst=lines_from_file(path)
    return lst[i]

def analyze(sample_paragraph,typed_string,start_time,end_time):
    def words_per_minute():
        words=len(typed_string)/5
        time=(end_time-start_time)/60
        return words/time
    def calc_acc():
        a=split(sample_paragraph)
        b=split(typed_string)
        cnt=0
        s=min(len(a),len(b))
        for i in range(s):
            if a[i]==b[i]:
                cnt+=1
        if s==0:
            return 0.0
        return cnt/s*100
    return [words_per_minute(),calc_acc()]

def pig_latin(s):
    i=0
    while i<len(s):
        if s[i] in "aeiou":
            break
        i+=1
    if i==0:
        return s + "way"
    else:
        return s[i:]+s[:i]+"ay"

def autocorrect(user_input,words_list,score_function):
    if user_input in words_list:
        return user_input
    else:
        return min(words_list, key=lambda x: score_function(user_input, x))

def swap_score(s1,s2):
    if s1=="" or s2=="":
        return 0
    elif s1[0]==s2[0]:
        return swap_score(s1[1:],s2[1:])
    else:
        return 1+swap_score(s1[1:],s2[1:])

# END Q1-5

# Question 6
d={}
def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""
    if (word1,word2) in d:
        return d[(word1,word2)]
    if word1=="" or word2=="": # Fill in the condition
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        if word1!="":
            return len(word1)
        if word2!="":
            return len(word2)
        return 0
        # END Q6

    elif word1[0]==word2[0]: # Feel free to remove or add additional cases
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        d[(word1,word2)]=score_function(word1[1:],word2[1:])
        return d[(word1,word2)]
        # END Q6
    
    else:
        add_char = 1+score_function(word1,word2[1:])  # Fill in these lines
        remove_char = 1+score_function(word1[1:],word2)
        substitute_char = 1+score_function(word1[1:],word2[1:])
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        d[(word1,word2)]=min(add_char,remove_char,substitute_char)
        return d[(word1,word2)]
        # END Q6

KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8
"*** YOUR CODE HERE ***"
def score_function_accurate(s1,s2):
    if score_function(s1,s2)==1:
        if len(s1)==len(s2):
            i=0
            while i<len(s1):
                if s1[i]!=s2[i]:
                    break
                i+=1
            return KEY_DISTANCES[(s1[i],s2[i])]
        else:
            return 1
    else:
        return score_function(s1,s2)

def score_function_final(s1,s2):
    return score_function_accurate(s1, s2)
# END Q7-8
"""
words_list = sorted(lines_from_file('data/words.txt'))
start = datetime.datetime.now()
print(autocorrect("spellin", words_list, score_function_final))
print(autocorrect("abstrction", words_list, score_function_final))
print(autocorrect("wird", words_list, score_function_final))
print(autocorrect("yest", words_list, score_function_final))
print(autocorrect("abreviations", words_list, score_function_final))
end = datetime.datetime.now()
print(end-start)
"""