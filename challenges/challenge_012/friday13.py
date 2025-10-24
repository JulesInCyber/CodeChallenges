from datetime import datetime

def friday13(month, year):
    day = 13
    dt = datetime(month=month, year=year, day=day)
    dow = dt.strftime('%A')

    # Checking if Friday
    if dow == "Friday":
        return True
    else:
        return False

if __name__ == "__main__":
    user_month = int(input("Please enter a month: "))
    user_year = int(input("Please enter a year: "))

    result = friday13(user_month, user_year)
    print(result)
