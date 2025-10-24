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
    
friday = friday13(8,2021)
print(friday)