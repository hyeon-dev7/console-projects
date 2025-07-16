from math import ceil
import datetime

def speed(start_time, len_user_input):
    end_time = datetime.datetime.now()
    diff = (end_time - start_time).total_seconds()
    return ceil( (len_user_input/diff)*60 )

def count_correct_answers(lyrics, user_input):
    count = 0
    for i in range(len(lyrics)):
        try :
            if lyrics[i] == user_input[i]:
                count += 1
        except IndexError :
            break
    return count


def score(lyrics, user_input):
    count = count_correct_answers(lyrics, user_input)
    return ceil(100* (count/len(lyrics) *100)) /100
