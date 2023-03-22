from utility import service


def get_team_from_row(row, category, year):
    column = row.find_all('td')

    id = column[1].a['href'][-5:]

    org_id = None

    name = column[1].text.strip()
    country = column[2].text.strip()

    return Team(id, org_id, name, country, category, year)


def get_team_table(category, year):
    team_list_url = "https://firstcycling.com/team.php?d=" + category.__str__() + "&y=" + year.__str__()

    table = service.get_soup(team_list_url).find('table', class_='sortTabell')

    return table
