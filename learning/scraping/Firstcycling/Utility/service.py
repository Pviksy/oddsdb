import datetime
import re
import requests
from bs4 import BeautifulSoup
from Utility import db

# current year
year = datetime.date.today().year

# list of rider ids already in the database to avoid duplicates
existing_rider_ids = set()


def get_soup(url):
    req = requests.get(url)
    html = req.content
    soup = BeautifulSoup(html, 'html5lib')
    return soup


def roster_exists(list_of_current_team, list_of_existing_team):
    # define a threshold of similarity (amount of matching rider ids)
    threshold = 15

    # get the set of rider ids for the current team
    current_set = set([str(x) for x in list_of_current_team])

    # get the set of rider ids for the existing team being compared now
    existing_set = set([str(x) for x in list_of_existing_team])

    # get the intersection of the two sets
    intersection_set = current_set.intersection(existing_set)

    matched_riders = len(intersection_set)

    # check if the size of the intersection set meets the threshold
    if matched_riders >= threshold:
        print("    Matched riders:", matched_riders)
        print("Transferred riders:", len(list_of_current_team) - matched_riders)
        return True
    else:
        if matched_riders > 0:
            print("Transferred riders:", matched_riders)
        return False


def parse_date(unparsed_date):
    # Remove the irrelevant part of the string
    date_str = unparsed_date.split(" (")[0]

    day = get_day(date_str)
    month = get_month(date_str)
    year = date_str.split(' ')[2]

    # Create datetime object
    date_obj = datetime.datetime(int(year), int(month), int(day))

    # Format date for SQL Server
    formatted_date = date_obj.strftime('%Y-%m-%d')

    return formatted_date


def get_day(date_str):
    # Regular expression pattern to match all integers in the string
    pattern = r"\d+"

    # Find all matches of the pattern in the string
    matches = re.findall(pattern, date_str.split(' ')[0])

    day = ''.join(matches)

    return day


def get_month(date_str):
    # Get the month name from the date string
    month_name = date_str.split(' ')[1]

    # Convert month name to number using datetime module
    month = datetime.datetime.strptime(month_name, "%B").month

    return month
