# dealing with u functions in python


def ageCalc(current_year, birth_year):
    """ This function calculates age based on current year and birth year """
    age = current_year - birth_year
    # return age
    return f"You are {age} years old"

ageCalc(2024, 1990)

if __name__ == "__main__":
    print(ageCalc(2024, 1990))

