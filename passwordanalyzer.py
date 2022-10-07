import pandas as pd
import re

csv = pd.read_csv('compromisedpasswords.csv', nrows=50)

passwords = csv.values.tolist()




def avg_len(passwords):

    len_under = 0
    len_over = 0
    for i in passwords:
        if len(i[0]) > 8:
        #checks length of each password and if greater than 8 count towards total
            len_over +=1
        else:
            len_under += 1
        percent_len = (len_over / (len(passwords))) * 100
    return percent_len, len_over


def avg_spchars(passwords):
    no_spchars = 0
    yes_spchars = 0



    for i in passwords: 
        if i[0].isalnum():
            no_spchars+=1
        else:
            yes_spchars+=1
    
    percent_spchars = (yes_spchars / (len(passwords))) * 100

    return percent_spchars, yes_spchars


def upper_or_lower(passwords):
    same_case = 0
    both_case = 0
    for i in passwords:

        if i[0].upper() == i[0] or i[0].lower() == i[0] or i[0].isdigit():
            same_case +=1
        else:
            both_case +=1
    percent_case = (both_case / (len(passwords))) * 100
    return percent_case, both_case

