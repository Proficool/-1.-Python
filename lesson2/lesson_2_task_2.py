year_input = input("Введите год:")
selected_year = int(year_input)

def is_year_leap(year):
    return year % 4 == 0

leap_year_result = is_year_leap(selected_year)

print("год " + str(selected_year) + ": " + str(leap_year_result))