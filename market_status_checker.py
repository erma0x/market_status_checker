import datetime
import pytz
import holidays
import time
import sys, os


def is_weekend():
    local_timezone = pytz.timezone('Europe/Rome')
    current_datetime = datetime.datetime.now(local_timezone)
    current_day = current_datetime.strftime("%A")
    if current_day in ["Saturday", "Sunday"]:
        return True
    else:
        return False

def is_us_holiday(date, year=2023):
    us_holidays = holidays.US(years=year)
    if date in us_holidays:
        return True
    else:
        return False

def calculate_time_difference(desired_time):
    current_time_utc = datetime.datetime.now(datetime.timezone.utc)
    current_date = datetime.datetime.now().date()
    desired_time_utc = datetime.datetime.combine(current_date, desired_time, tzinfo=datetime.timezone.utc)
    time_difference = desired_time_utc - current_time_utc
    rounded_duration = datetime.timedelta(seconds=int(time_difference.total_seconds()))
    return rounded_duration

def check_market_open():
    local_timezone = pytz.timezone('Europe/Rome')
    current_time = datetime.datetime.now(local_timezone)
    utc_timezone = pytz.utc

    current_time_utc = current_time.astimezone(utc_timezone)

    tomorrow_london = current_time_utc + datetime.timedelta(days=1)

    tomorrow_date_london = tomorrow_london.date()

    opening_markets = datetime.time(9, 30)
    closing_markets = datetime.time(17, 30)

    datetime_opening_markets = datetime.datetime.combine(tomorrow_date_london, opening_markets)
    datetime_closing_markets = datetime.datetime.combine(tomorrow_date_london, closing_markets)

    time_util_the_markets_open = calculate_time_difference(datetime_opening_markets.time())
    current_time = datetime.datetime.now().replace(microsecond=0)

    date_when_the_markets_open = current_time_utc + time_util_the_markets_open
    date_when_the_markets_open = date_when_the_markets_open.replace(microsecond=0)

    current_day = current_time_utc.strftime("%A")
    current_date = datetime.datetime.now().date()

    print(f"\nToday is {current_day} {current_time} \n")

    print(f"Market Open:\t{date_when_the_markets_open}")
    print(f"Hours Remaining:\t{time_util_the_markets_open}\n")


    if datetime_opening_markets <= current_time <= datetime_closing_markets and not is_us_holiday(current_time) and not is_weekend():
        print("The market is open.")
        return True
    
    if is_us_holiday(current_date):
        print("The market is closed. It's a holiday in the US.")
        return False
    
    if current_day == "Saturday":
        print(f"The market is closed. It's Saturday. It will open on Monday at {datetime_opening_markets}.")
        return False

    if current_day == "Sunday":
        print(f"The market is closed. It's Sunday. It will open at {datetime_opening_markets} tomorrow.")
        return False

    if datetime_opening_markets >= current_time or current_time >= datetime_closing_markets and not is_us_holiday(current_time) and not is_weekend():
        print(f"The market is closed.")
        return True


def clear_screen():
    # Clear screen command for different operating systems
    command = "cls" if os.name == "nt" else "clear"

    # Execute the command to clear the screen
    os.system(command)

if __name__ == "__main__":
    while True:

        check_market_open()
        time.sleep(1)
        clear_screen()
