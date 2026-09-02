def is_divisible_by_3(num):
    """
        This is a sample problem and solution that won't be graded. Its purpose is just to familiarize
        yourself with functions and the format for this homework

        The objective of this sample problem is to determine if the num is divisible by 3, if it is, the function will
        return the string "divisible" otherwise it will return "not divisible"

        We will use the modulo operator "%"  (might come in handy in other homework problems - worth a google search!)
    """

    if num % 3:  # Use modulo operator to get remainder. If it not 0 (which would be interpreted like a 'False' in the if statement, then we know it is not divisible by 3
        return "not divisible"
    else:
        return "divisible"


def get_year_type(year):
    """
    When given a year, determine if the year is even or odd, but if it is a leap year return leap

    To be a leap year, the year number must be divisible by four - except for end-of-century years, which must be divisible by 400. This means that the year 2000 was a leap year, although 1900 was not.

    Odd year: Return a string "odd"
    Even year: Return "even" unless it is leap year, then return a string "leap"
    leap year: Return a string "leap"

    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return "leap"

    if year % 2 == 0:
        return "even"
    else:
        return "odd"


def get_triangular_number_list(given_number):
    """
    When given a number, `given_number`, return a list of all values that are trianglular numbers that are less than or equal to the given_number
    triangle number: https://en.wikipedia.org/wiki/Triangular_number

    Remember you are returning a list of numbers!

    """
    result = []
    current = 0
    add = 1

    while current + add <= given_number:
        current = current + add
        result.append(current)
        add = add + 1

    return result

# When you run this python file you should be able to check your work with these test cases

if __name__ == '__main__':
    # Below are the Test Cases!
    print("\nProblem 0:")
    print("Student answer was:", is_divisible_by_3(1), "    Problem 0 answer correct?",
          is_divisible_by_3(1) == 'not divisible', )
    print("Student answer was:", is_divisible_by_3(2), "    Problem 0 answer correct?",
          is_divisible_by_3(2) == 'not divisible', )
    print("Student answer was:", is_divisible_by_3(3), "    Problem 0 answer correct?",
          is_divisible_by_3(3) == 'divisible', )
    print("Student answer was:", is_divisible_by_3(4), "    Problem 0 answer correct?",
          is_divisible_by_3(4) == 'not divisible', )

    print("\nProblem 1:")
    print("Problem 1 answer correct?", get_year_type(2025) == 'odd', "    Student answer was:", get_year_type(2025))
    print("Problem 1 answer correct?", get_year_type(2024) == 'leap', "    Student answer was:", get_year_type(2024))
    print("Problem 1 answer correct?", get_year_type(2023) == 'odd', "    Student answer was:", get_year_type(2023))
    print("Problem 1 answer correct?", get_year_type(2022) == 'even', "    Student answer was:", get_year_type(2022))
    print("Problem 1 answer correct?", get_year_type(2020) == 'leap', "    Student answer was:", get_year_type(2020))
    print("Problem 1 answer correct?", get_year_type(2000) == 'leap', "    Student answer was:", get_year_type(2000))
    print("Problem 1 answer correct?", get_year_type(1900) == 'even', "    Student answer was:", get_year_type(1900))

    print("\nProblem 2:")
    print("Problem 2 answer correct?", get_triangular_number_list(8) == [1, 3, 6], "      Student answer was:",
          get_triangular_number_list(8))
    print("Problem 2 answer correct?", get_triangular_number_list(10) == [1, 3, 6, 10], "      Student answer was:",
          get_triangular_number_list(10))
    print("Problem 2 answer correct?", get_triangular_number_list(16) == [1, 3, 6, 10, 15], "      Student answer was:",
          get_triangular_number_list(16))
    print("Problem 2 answer correct?", get_triangular_number_list(21) == [1, 3, 6, 10, 15, 21],
          "      Student answer was:", get_triangular_number_list(21))
