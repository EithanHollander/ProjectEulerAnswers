if __name__ == '__main__':
    def days_in_month(month, year):
        if month in (4, 6, 9, 11):
            return 30
        if month in (1, 3, 5, 7, 8, 10, 12):
            return 31
        else: # month == 2
            if year % 100 == 0:
                if (year / 400).is_integer():
                    return 29
                return 28
            elif year % 4 == 0:
                return 29
            return 28

    def days_in_year(year):
        days = 0
        for i in range(1,13):
            days += days_in_month(i, year)
        return days

    # Knowing Jan. 1st 1900 was Monday
    first_of_month = 2
    how_many_first_sundays = 0
    for year in range(1900, 2001):
        for month in range(1, 13):
            first_of_month = (first_of_month + (days_in_month(month, year) % 7 + 1)) % 7 + 1
            if first_of_month == 1:
                how_many_first_sundays += 1
                if year == 2000 and month == 12:
                    how_many_first_sundays -= 1

    print(how_many_first_sundays)