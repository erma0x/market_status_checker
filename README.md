Market Status Checker

This Python script checks the status of the market based on the current time, US holidays, and weekends. It provides information on whether the market is open or closed, as well as the remaining hours until the market opens.
Prerequisites

    Python 3.x
    pytz library (can be installed via pip install pytz)
    holidays library (can be installed via pip install holidays)

Usage

    Ensure you have Python 3.x installed on your system.
    Install the required libraries by running the following commands:
        pip install pytz
        pip install holidays
    Open a terminal or command prompt and navigate to the directory where the script is located.
    Run the script using the following command: python market_status_checker.py
    The script will continuously display the market status, updating every second. Press Ctrl+C to stop the script.

Description

This script performs the following functions:

    is_weekend(): Checks if the current day is a weekend (Saturday or Sunday).

    is_us_holiday(date, year=2023): Checks if the provided date is a US holiday. By default, it checks for holidays in the year 2023.

    calculate_time_difference(desired_time): Calculates the time difference between the current UTC time and a desired time. It returns a rounded duration in seconds.

    check_market_open(): Determines whether the market is open based on the current time, US holidays, and weekends. It prints the current day, current time, market opening time, and remaining hours if the market is open or closed. It returns True if the market is open, False otherwise.

    clear_screen(): Clears the terminal screen. Works on different operating systems.

Main Execution

The code enters the main execution block when executed as a standalone script. It continuously calls the check_market_open() function in an infinite loop, sleeping for 1 second between each iteration. The clear_screen() function is called to clear the terminal screen before each iteration.

Feel free to modify the code according to your requirements and run it to check the market status in real-time.
