from sys import argv


_allowed_day = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


def date(raw_date: str) -> bool:
    """ Simple checking function for date,
    to see if such date can exist.
    Args:
        raw_date (str):
        Get's raw date in DD.MM.YYYY format
    Returns:
        bool: Return's True if such date can exist,
        and False if it can not.
    """
    if len(raw_date) == 0:
        return None
    
    list_date: list[int] = list(map(int, raw_date.split(".")))
    
    if len(list_date) != 3:
        raise Exception("Wrong date format.\nCorrect date format is DD.MM.YYYY")
    
    if 1 <= list_date[2] <= 9999:
        if 1 <= list_date[1] <= 12:
            if list_date[0] in range(_allowed_day.get(list_date[1]) + 1):
                return True
            elif list_date[1] == 2 and _leap_year(list_date[2]) and list_date[0] == 29:
                return True
            else:
                print(f"Date with day {list_date[0]} doesn't exist.")
        else:
            print(f"Date with month {list_date[1]} doesn't exist.")
    else:
        print(f"Date with year {list_date[2]} doesn't exist.")
    
    return False
                

def _leap_year(year: int) -> bool:
    """Function to check if the year is
    a leap year
    Args:
        year (int): Year to check.

    Returns:
        bool: True if year is a leap year.
        False if year is not a leap year.
    """
    if year % 400 == 0:
        return True
    else:
        if year % 4 == 0 and year % 100 != 0:
            return True
    return False


if __name__ == "__main__":
    print(date("11.11.1111"))
    print(date("29.02.2012"))
