import pyodbc

from Utility import service

DRIVER_NAME = 'SQL SERVER'
SERVER_NAME = 'DESKTOP-8KEOEI7\\SQLEXPRESS'
DB_NAME = 'team_rider'

conn = pyodbc.connect('Driver=' + DRIVER_NAME + ';'
                                                'Server=' + SERVER_NAME + ';'
                                                                          'Database=' + DB_NAME + ';'
                                                                                                  'Trusted_Connection=yes;')

cursor = conn.cursor()


def get_team_by_team_id(team_id):
    cursor.execute('SELECT team.[name] FROM team WHERE id =' + str(team_id))
    team_name = str(cursor.fetchone())
    return team_name


# husk at rette disse metoder så de fetcher de rigtige fra resultset FUCK JEG ER TRÆT

def get_org_id_from(team_id):
    cursor.execute('SELECT org_id FROM team WHERE id =' + str(team_id))
    org_id = str(cursor.fetchone())
    return org_id


def insert_org():
    cursor.execute("INSERT INTO [org] DEFAULT VALUES")
    cursor.commit()


def insert_team(team):
    if team.org_id is None:
        # If org_id is None, create a new organization and get its id
        cursor.execute("INSERT INTO org DEFAULT VALUES")
        cursor.execute("SELECT SCOPE_IDENTITY()")
        team.org_id = cursor.fetchone()[0]

    print(team.name, team.org_id)

    query = """
        INSERT INTO team (id, org_id, name, country, category, year)
        VALUES (?, ?, ?, ?, ?, ?)
    """
    values = (team.id, team.org_id, team.name, team.country, team.category, team.year)
    cursor.execute(query, values)
    conn.commit()


def insert_rider(rider):
    # check if the rider id already exists
    if rider.id not in service.existing_rider_ids:
        # insert the rider into the database
        query = """
            INSERT INTO rider (id, team_id, firstname, lastname, country, date_of_birth) 
            VALUES (?, ?, ?, ?, ?, ?)
        """
        values = (
            rider.id, rider.team_id, rider.firstname, rider.lastname, rider.country, rider.date_of_birth)
        cursor.execute(query, values)
        conn.commit()

        # add the rider id to the set of existing rider ids
        service.existing_rider_ids.add(rider.id)
        print(' Existing ids:', len(service.existing_rider_ids))
    else:
        print("--------------------")
        print("--------------------")
        print("--------------------")
        print("--------------------")
        print("Rider with id:", rider.id, "already in database")
        print("--------------------")
        print("--------------------")
        print("--------------------")
        print("--------------------")
        # skip insertion for this rider


def create_datastructure():
    team_riders = {}
    query = "SELECT team.id, rider.id FROM team JOIN rider ON team.id = rider.team_id"
    cursor.execute(query)
    for row in cursor:
        team_id = row[0]
        rider_id = row[1]
        if team_id not in team_riders:
            team_riders[team_id] = []
        team_riders[team_id].append(rider_id)

    # for key in team_riders:
    #    print(key)
    #    print(team_riders[key])
    #    print()

    return team_riders
