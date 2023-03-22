from Utility import service


class Rider:
    def __init__(self, id, team_id, firstname, lastname, country, date_of_birth):
        self.id = id
        self.team_id = team_id
        self.firstname = firstname
        self.lastname = lastname
        self.country = country
        self.date_of_birth = date_of_birth

    def print(self):
        print('           id:', self.id)
        print('      team_id:', self.team_id)
        print('         name:', self.firstname, self.lastname)
        print('      country:', self.country)
        print('date_of_birth:', self.date_of_birth)
        print('               -')


def get_rider_page_url(row):
    column = row.find_all('td')

    rider_page_url = column[0].a['href'][:-7]

    return "https://firstcycling.com/" + rider_page_url + "&y=" + service.year.__str__()


def get_rider_from_rider_page(rider_page_url, team_id):
    soup = service.get_soup(rider_page_url)

    # Find the start and end index of the substring we want to extract
    start_index = rider_page_url.index("rider.php?r=") + len("rider.php?r=")
    end_index = rider_page_url.index("&y=")

    # Extract the substring between start_index and end_index
    id = rider_page_url[start_index:end_index]

    # Full name of rider is stored in the page header
    header = soup.find('h1')
    name = header.text

    # Name is split into first and last name for the database. Firstname is the first word, lastname is the rest
    firstname, lastname = name.split(maxsplit=1)

    # Target the place with all the information from the rider page
    side_box = soup.find('div', {'class': 'cont320h'})
    information = side_box.find('h3', text='Information')

    # Get the 3 tags coming after the information header: country, date_of_birth respectively
    tags = information.find_all_next('p', limit=3)

    country = tags[0].text.strip().split(', ')[0]
    date_of_birth = service.parse_date(tags[1].text.strip())

    return Rider(id, team_id, firstname, lastname, country, date_of_birth)


def get_rider_table(team_id):
    # concatenate url for this teams list of riders page
    rider_list_url = "https://firstcycling.com/team.php?l=" + team_id + "&riders=2"

    # get the specific table of riders from the page
    table = service.get_soup(rider_list_url).find('table', class_='sortTabell')

    return table
