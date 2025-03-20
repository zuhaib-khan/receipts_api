from datetime import datetime, time

def day_check(time_stamp):

    given_time_stamp = datetime.strptime(time_stamp, "%Y-%m-%d")
    day = given_time_stamp.date().day
    return day
        
      
def time_check(time_stamp):

    given_time_stamp = datetime.strptime(time_stamp, '%H:%M').time()
    start_time = time(14,0)
    end_time = time(16,0)
    
    in_between = start_time < given_time_stamp < end_time
    return in_between

def alpha_numeric_counter(retailer_name):
    
    counter = 0
    for alphabet in retailer_name:
        if alphabet.isalnum():
            counter += 1
    
    return counter