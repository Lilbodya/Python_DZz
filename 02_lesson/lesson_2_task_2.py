def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


year = 2025
result = is_year_leap(year)

print("год", year, ":", result)
