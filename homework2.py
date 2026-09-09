from typing import List, Tuple

def histogram(input_dictionary: dict) -> list:
    # data is a dictionary that contains the following keys: 'data', 'n', 'min_val', 'max_val'
    # n is an integer
    # min_val and max_val are floats
    # data is a list

    # Write your code here

    data = input_dictionary['data']
    n = input_dictionary['n']
    min_val = input_dictionary['min_val']
    max_val = input_dictionary['max_val']

    if n <= 0:
        return []

    if min_val == max_val:
        print('Error: min_val and max_val are the same value')
        return []

    if min_val > max_val:
        temp = min_val
        min_val = max_val
        max_val = temp

    histogram = [0] * n
    width = (max_val - min_val) / n

    for val in data:
        if val > min_val:
            if val < max_val:
                index = int((val - min_val) / width)
                if 0 <= index:
                    if n > index:
                        histogram[index] += 1

    return histogram

    # return the variable storing the histogram
    # Output should be a list


# Here, the function first checks if the lower and upper bounds are the same, 
# if they are it prints an error message and returns an empty list. 
# If lower bound is greater than upper bound, it swaps their values. 
# If number of bins is less than or equal to 0, it returns an empty list. 
# Then it initializes an empty list hist of length n and calculates the width of each bin. 
# Then it iterates through the data, 
# and for each value checks if it is within the range of the histogram and if it is, 
# it increments the bin it belongs to. Finally, it returns the histogram.

def combine_birthday_data(person_to_day: List[Tuple[str, int]], 
                          person_to_month: List[Tuple[str, int]], 
                          person_to_year: List[Tuple[str, int]]) -> dict:
    #person_to_day, person_to_month, person_to_year are list of tuples

    # Write your code here

    currentYear = 2026

    month_to_people_data = {}

    for name, month in person_to_month:

        day = 0
        for d in person_to_day:
            if d[0] == name:
                day = d[1]

        year = 0
        for y in person_to_year:
            if y[0] == name:
                year = y[1]

        age = currentYear - year
        person_info = (name, day, year, age)

        if month in month_to_people_data:
            val = month_to_people_data[month]
            if type(val) == list:
                val.append(person_info)
            else:
                month_to_people_data[month] = [val, person_info]
        else:
            month_to_people_data[month] = person_info

    return month_to_people_data

    # return the variable storing output
    # Output should be a dictionary

# We first define the current year as 2026, which will be used to calculate the age of each person later on.
# We create an empty dictionary month_to_people_data that will store the final data in the format specified in the problem statement.
# We iterate over the both values in the tuple of the person_to_month list (note that person_to_month is a list of tuples, which means each item in the list is a tuple) 
# using a for loop. For each iteration, we extract the corresponding day, year and age values from the person_to_day and person_to_year lists using the current name as the "key".
# We then use the current month as the key and a tuple of (name, day, year, age) as the value to update the month_to_people_data dictionary.
# Only change the value to a list data type, when there are multiple entries with the same key. This will help append for other tuples to the same month.
# Finally, we return the month_to_people_data dictionary as the output of the function.
