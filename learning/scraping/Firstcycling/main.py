from Scrapers import rider_scraper, team_scraper
from Utility import service
from Utility import db

# team categories
categories = {1: "UWT", 2: "PRT"}

# existing_teams = db.create_datastructure()
# print(existing_teams)
existing_teams = []  # temporary


def scrape_riders_for_team(team_id):
    riders = []

    # gets table of riders from a specific teams id
    rider_table = rider_scraper.get_rider_table(team_id).tbody.find_all('tr')

    for row in rider_table:
        # gets rider page url from row info
        rider_page_url = rider_scraper.get_rider_page_url(row)

        # creates rider object from page url and team id
        rider = rider_scraper.get_rider_from_rider_page(rider_page_url, team_id)

        riders.append(rider)
    return riders


def assign_org(team_riders):
    team_rider_ids = [rider.id for rider in team_riders]

    # if org exists, return org_id - else return None
    for this_team in existing_teams:  # current_team is compared against all existing teams (this_team)

        # if a team is found with enough of the same riders
        if service.roster_exists(team_rider_ids, existing_teams[this_team]):
            existing_team_org_id = db.get_org_id_from(this_team)  # if org exists, get their org_id
            return existing_team_org_id


def get_teams_and_riders():
    for category in categories:

        # gets table of teams with given uci category, from given year
        team_table = team_scraper.get_team_table(category, service.year).tbody.find_all('tr')

        for row in team_table:

            # create team object from row information
            team = team_scraper.get_team_from_row(row, categories[category], service.year)
            team.print()

            current_team_riders = scrape_riders_for_team(team.id)

            if int(team.id) in existing_teams:
                print("Team ID already exists\n-")
                # Team/rider info can be updated.
                # Transferred riders can be added.
            else:
                # Will be assigned None if matching team is not found. New org_id will be generated
                team.org_id = assign_org(current_team_riders)
                print("Team has been given org_id:", team.org_id)
                print("-")
                team.print()


get_teams_and_riders()