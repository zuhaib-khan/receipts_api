"""
Helper functions for the Receipt Processor API.

This file provides utility functions for:
    Extracting the day from a date string.
    Checking if a given time falls within a bonus time window.
    Counting alphanumeric characters in a retailer name.
"""
from datetime import datetime, time

def day_check(time_stamp):
    """
    Extract the day from a date string.

    Param:
        time_stamp : A date string in the format 'YYYY-MM-DD'.

    Returns:
        The day of the month extracted from the date.
    """
    given_time_stamp = datetime.strptime(time_stamp, "%Y-%m-%d")
    day = given_time_stamp.date().day
    return day
        
      
def time_check(time_stamp):
    """
    Check if the provided time is between 2:00 PM and 4:00 PM.

    Param:
        time_stamp: A time string in the format 'HH:MM'.

    Returns:
        True if the time is between 14:00 and 16:00, False otherwise.
    """
    
    given_time_stamp = datetime.strptime(time_stamp, '%H:%M').time()
    start_time = time(14,0)
    end_time = time(16,0)
    
    in_between = start_time < given_time_stamp < end_time
    return in_between

def alpha_numeric_counter(retailer_name):
    """
    Count the number of alphanumeric characters in the retailer name.

    Param:
        retailer_name: The retailer name.

    Returns:
        The count of alphanumeric characters in the retailer name.
    """
    
    counter = 0
    for alphabet in retailer_name:
        if alphabet.isalnum():
            counter += 1
    
    return counter