import json, urllib, requests, pyodbc, datetime


#Notes: Info for each teams roster with Links
#Team ID:
#(1, 'New Jersey Devils')
"https://statsapi.web.nhl.com/api/v1/teams/1/roster"
#(2, 'New York Islanders')
"https://statsapi.web.nhl.com/api/v1/teams/2/roster"
#(3, 'New York Rangers')
"https://statsapi.web.nhl.com/api/v1/teams/3/roster"
#(4, 'Philadelphia Flyers')
"https://statsapi.web.nhl.com/api/v1/teams/4/roster"
#(5, 'Pittsburgh Penguins')
"https://statsapi.web.nhl.com/api/v1/teams/5/roster"
#(6, 'Boston Bruins')
"https://statsapi.web.nhl.com/api/v1/teams/6/roster"
#(7, 'Buffalo Sabres')
"https://statsapi.web.nhl.com/api/v1/teams/7/roster"
#(8, 'Montréal Canadiens')
"https://statsapi.web.nhl.com/api/v1/teams/8/roster"
#(9, 'Ottawa Senators')
"https://statsapi.web.nhl.com/api/v1/teams/9/roster"
#(10, 'Toronto Maple Leafs')
"https://statsapi.web.nhl.com/api/v1/teams/10/roster"
#(12, 'Carolina Hurricanes')
"https://statsapi.web.nhl.com/api/v1/teams/12/roster"
#(13, 'Florida Panthers')
"https://statsapi.web.nhl.com/api/v1/teams/13/roster"
#(14, 'Tampa Bay Lightning')
"https://statsapi.web.nhl.com/api/v1/teams/14/roster"
#(15, 'Washington Capitals')
"https://statsapi.web.nhl.com/api/v1/teams/15/roster"
#(16, 'Chicago Blackhawks')
"https://statsapi.web.nhl.com/api/v1/teams/16/roster"
#(17, 'Detroit Red Wings')
"https://statsapi.web.nhl.com/api/v1/teams/17/roster"
#(18, 'Nashville Predators')
"https://statsapi.web.nhl.com/api/v1/teams/18/roster"
#(19, 'St. Louis Blues')
"https://statsapi.web.nhl.com/api/v1/teams/19/roster"
#(20, 'Calgary Flames')
"https://statsapi.web.nhl.com/api/v1/teams/20/roster"
#(21, 'Colorado Avalanche')
"https://statsapi.web.nhl.com/api/v1/teams/21/roster"
#(22, 'Edmonton Oilers')
"https://statsapi.web.nhl.com/api/v1/teams/22/roster"
#(23, 'Vancouver Canucks')
"https://statsapi.web.nhl.com/api/v1/teams/23/roster"
#(24, 'Anaheim Ducks')
"https://statsapi.web.nhl.com/api/v1/teams/24/roster"
#(25, 'Dallas Stars')
"https://statsapi.web.nhl.com/api/v1/teams/25/roster"
#(26, 'Los Angeles Kings')
"https://statsapi.web.nhl.com/api/v1/teams/26/roster"
#(28, 'San Jose Sharks')
"https://statsapi.web.nhl.com/api/v1/teams/28/roster"
#(29, 'Columbus Blue Jackets')
"https://statsapi.web.nhl.com/api/v1/teams/29/roster"
#(30, 'Minnesota Wild')
"https://statsapi.web.nhl.com/api/v1/teams/30/roster"
#(52, 'Winnipeg Jets')
"https://statsapi.web.nhl.com/api/v1/teams/52/roster"
#(53, 'Arizona Coyotes')
"https://statsapi.web.nhl.com/api/v1/teams/53/roster"
#(54, 'Vegas Golden Knights')
"https://statsapi.web.nhl.com/api/v1/teams/54/roster"


#Example links stored in random variables
url = "https://statsapi.web.nhl.com/api/v1/teams"
prl = "https://statsapi.web.nhl.com/api/v1/teams/3/roster"


#gets data from API
"""
hockeyData = requests.get(url)
teamData = json.loads(hockeyData.text)
#print(teamData)

playerData = requests.get(prl)

#dictionary version of JSON
x = json.loads(playerData.text)
print(type(x))
#print(x)



#String version of JSON
x_json = json.dumps(x)

rid_begin = get_dataList(x, 'roster')
#print(rid_begin) 

get_keys = narrow_list(rid_begin, 'person')
desiredField = narrow_list(get_keys, 'id') 
#print(desiredField)

#print(teamPlayer_stats(desiredField, 20182019))

#print(get_player(8476459))
mikal_stats = (singleSeason_stats(8476459, 20182019))
print(mikal_stats) """

#turns URL into a workable json
def turnURL(newURL):
    requestedURL = requests.get(newURL)
    newData = json.loads(requestedURL.text)
    return newData


#obtains the particular key and value for that key
def get_dataList(dictData, desiredKey): 
    y = ''
    for key, value in dictData.items():
        if key == desiredKey:
            #print(value)
            y = value
    return y


#uses list comprehension to get desired values and returned as list
def narrow_list(list_data, desiredKey):
    wantedInfo = [li[desiredKey] for li in list_data]
    return wantedInfo

#gets ID's for a team using provided link
def transform_Playerlist(newURL):
    newData = turnURL(newURL)
    trim_List = get_dataList(newData, 'roster')
    get_next = narrow_list(trim_List, 'person')
    get_field = narrow_list(get_next, 'id')

    return get_field

#retrieves a players page based on their playerID
def get_player(playerID):
    wantedPlayer = "https://statsapi.web.nhl.com/api/v1/people/" + str(playerID)
    wantedURL = requests.get(wantedPlayer)
    wantedText = json.loads(wantedURL.text)

    return wantedText

# Returns a json of a wanted team
def get_team(teamID):
    wantedTeam = "https://statsapi.web.nhl.com/api/v1/teams/" + str(teamID) + "/roster"
    wantedURL = requests.get(wantedTeam)
    wantedText = json.loads(wantedURL.text)

    return wantedText

#gets a specific piece of info about the player in the people section of the player url
def get_playerInfo(playerID, keyInfo):
    requiredLink = get_player(playerID)
    thin_list = get_dataList(requiredLink, 'people')
    find_info = narrow_list(thin_list, keyInfo)
    
    return find_info[0]

#same as get_playerInfo, but does it for a whole team
def get_teamInfo(teamID, keyInfo):
    newList = []
    requiredLink = get_team(teamID)
    elim_roster = get_dataList(requiredLink, 'roster')
    get_keys = narrow_list(elim_roster, 'person')
    desiredField = narrow_list(get_keys, keyInfo)

    return desiredField
#print(get_teamInfo(3, 'fullName'))

#returns a list of each teams ID
def get_teamIDList(teamID):
    rand_list = get_teamInfo(teamID, 'fullName')
    newList = []
    for i in range(len(rand_list)):
        newList.append(teamID)
    return newList


#retrives a players single season stats based off a given playerID and season
def singleSeason_stats(playerID, season):
    wantedPlayer ="https://statsapi.web.nhl.com/api/v1/people/" + str(playerID) + "/stats?stats=statsSingleSeason&season=" + str(season)
    #print(wantedPlayer)
    wantedURL = requests.get(wantedPlayer)
    wantedText = json.loads(wantedURL.text)
    updateText = get_dataList(wantedText, 'stats')

    updateText = narrow_list(updateText, 'splits')
    return updateText

#same as singleSeason_stats but for a whole team
def teamPlayer_stats(teamURL, season):
    newList = []
    team_IDS = transform_Playerlist(teamURL)
    for i in range(len(team_IDS)):
        newList += singleSeason_stats(team_IDS[i], season)
    return newList
#print(teamPlayer_stats("https://statsapi.web.nhl.com/api/v1/teams/1/roster", 20192020))

#gets a specific stat for a single player for a specific season
"""def get_stat(playerID, season, statName):
    stats_list = singleSeason_stats(playerID, season)[0]
    #print(player_stats)
    updated_stats = narrow_list(stats_list, 'stat')
    player_stat = narrow_list(updated_stats, statName)
    
    return player_stat[0]"""

#gets a specific stat for a player based on playerID, season, and stat desired
def get_stat(playerID, season, statName):
    if singleSeason_stats(playerID, season) == [[]]:
        return 0
    stats_list = singleSeason_stats(playerID, season)[0][0]
    updated_stats = get_dataList(stats_list, 'stat')
    for key, value in updated_stats.items():
        if key == statName:
            return value
    return 0

#s = (singleSeason_stats(8475809, 20192020))
#print([[]] == s)
#print(get_stat(8475809, 20192020, 'games'))

#print(get_teamStat(3, 'goals'))

#prints all the stats for a player
def compile_stats(playerID, season):
    
    stats_list = singleSeason_stats(playerID, season)[0]
    #print(player_stats)
    updated_stats = narrow_list(stats_list, 'stat')
    print(updated_stats)

#fetches a specific team based off a given ID
def get_teamName(desiredTeamID):
    requiredLink = turnURL("https://statsapi.web.nhl.com/api/v1/teams")

    newData = get_dataList(requiredLink, 'teams')
    #print(newData)
    teamList = ["nothing"]
    thin_list = narrow_list(newData, 'name')
    #print(thin_list)
    for i in thin_list:
        teamList.append(i)
    for i in range(len(teamList)):
        if i == desiredTeamID:
            return teamList[i]
    raise Exception("Team not Found")

#returns a list of all the teams from the API
def get_teamList():
    requiredLink = turnURL("https://statsapi.web.nhl.com/api/v1/teams")

    newData = get_dataList(requiredLink, 'teams')
    #print(newData)
    teamList = ["nothing"]
    thin_list = narrow_list(newData, 'name')
    #print(thin_list)
    for i in thin_list:
        teamList.append(i)
    return teamList

#Obtains and returns a players position based on the playerID given
def trim_singlePosition(playerID):
    requiredLink = get_player(playerID)
    thin_list = get_dataList(requiredLink, 'people')
    thin_position = narrow_list(thin_list, 'primaryPosition')
    thin_position = thin_position[0]
    for key, value in thin_position.items():
        if key == 'name':
            return value
    raise Exception("Position not Found")
    
#Determines and returns a value based on the given playerID whether the player is a rookie or not. 1 for rookie, 0 for non-rookie
def determine_rookie(playerID):
    rook = get_playerInfo(playerID, 'rookie')
    if rook == False:
        return 0
    return 1

#returns a list of all team ID's
def get_LeagueIDS():
    requiredLink = turnURL("https://statsapi.web.nhl.com/api/v1/teams")

    newData = get_dataList(requiredLink, 'teams')
    #print(newData)
    team_IDList = []
    thin_list = narrow_list(newData, 'id')
    #print(thin_list)
    for i in thin_list:
        team_IDList.append(i)
    return team_IDList

print(get_LeagueIDS())

#www = (get_LeagueIDS())
#for r in www:
 #   print(r)

#print(determine_rookie(8481559))
#print(get_playerInfo(8481559, 'fullName'))

#teamsList = (get_teamList())
 
#print(trim_position(3, 'type'))

"""print(get_stat(8476459, 20192020, 'games'))
lk = get_teamInfo(3, 'id')
newList = []
for i in lk:
    newList += get_stat(i, 20192020, 'games')
print(newList)"""


#i = 1
"""for i in range(len(teamsList)):
    cursor.execute("INSERT INTO Hockey.dbo.NHL (TeamName) VALUES (?)", teamsList[i])
cnxn.commit()""" 

#print(len(teamsList))


#Inserts teams into sql
#"""
def insertTeams(list_teams):
    cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-V3RT9V4\SQLEXPRESS;'
                      'Database=Hockey;'
                      'Trusted_Connection=yes;')
    print(cnxn)
    cursor = cnxn.cursor()
    cursor.execute('SELECT * FROM Hockey.dbo.NHL')

    #for row in cursor:
        #print(row)
    for i in range(1, len(list_teams)):
        #print(teamsList[i]) 
        cursor.execute("INSERT INTO Hockey.dbo.NHL (TeamName) VALUES (?)", list_teams[i]) 
    cnxn.commit()

insertTeams(get_teamList())

#check duplicates method, not finished

"""
def check_duplicateTeams(team_name):
    checkDupe = "select TeamName from dbo.NHL where TeamName = (?)", team_name
    if checkDupe != team_name:
        print("Duplicate Found")
"""
   



#call to insertTeams method
insertTeams(get_teamList())


#Inserts Players and other key areas into sql(does not include stats)
def insertPlayers_team(players_list, ids_list, teamIDS_list):
    cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-V3RT9V4\SQLEXPRESS;'
                      'Database=Hockey;'
                      'Trusted_Connection=yes;')
    #print(cnxn)
    cursor = cnxn.cursor()
    cursor.fast_executemany = True
    for i in range(len(ids_list)):
        know_position = trim_singlePosition(ids_list[i])
        if know_position != 'Goalie':
            cursor.execute('SELECT * FROM Hockey.dbo.NHLPlayer')
            get_age = get_playerInfo(ids_list[i], 'currentAge')
            get_nation = get_playerInfo(ids_list[i], 'nationality')
            get_rook = determine_rookie(ids_list[i])
            get_position = trim_singlePosition(ids_list[i])
            get_height = get_playerInfo(ids_list[i], 'height')
            get_weight = get_playerInfo(ids_list[i], 'weight')
            print(cursor.executemany("INSERT INTO Hockey.dbo.NHLPlayer (PlayerName, TeamID, Age, Nationality, Rookie, Position, Height, Weight, APIKey) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", players_list[i], teamIDS_list[i], get_age, get_nation, get_rook, get_position, get_height, get_weight, ids_list[i]))
        else:
            cursor.execute('SELECT * FROM Hockey.dbo.NHLGoalies')
            get_age = get_playerInfo(ids_list[i], 'currentAge')
            get_nation = get_playerInfo(ids_list[i], 'nationality')
            get_rook = determine_rookie(ids_list[i])
            get_position = trim_singlePosition(ids_list[i])
            get_height = get_playerInfo(ids_list[i], 'height')
            get_weight = get_playerInfo(ids_list[i], 'weight')
            print(cursor.executemany("INSERT INTO Hockey.dbo.NHLGoalies (PlayerName, TeamID, Age, Nationality, Rookie, Position, Height, Weight, APIKey) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", players_list[i], teamIDS_list[i], get_age, get_nation, get_rook, get_position, get_height, get_weight, ids_list[i]))       
    #for row in cursor:
        #print(row)
    cnxn.commit()


for i in get_LeagueIDS():
    insertPlayers_team(get_teamInfo(i, 'fullName'), get_teamInfo(i, 'id'), get_teamIDList(i))



#print('Hockey.dbo.NHL' + str(20192020))


#Inserts stats into sql for each player through .execute method.
"""
def insert_SeasonStats(players_list, ids_list, season):
    cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-V3RT9V4\SQLEXPRESS;'
                      'Database=Hockey;'
                      'Trusted_Connection=yes;')
    #print(cnxn)
    cursor = cnxn.cursor()
    for i in range(len(ids_list)):
        know_position = trim_singlePosition(ids_list[i])
        if know_position != 'Goalie':
            table_name = 'Hockey.dbo.NHLP' + str(season) 
            cursor.execute('SELECT * FROM ' + table_name)
            get_GP = get_stat(ids_list[i], season, 'games')
            get_Points = get_stat(ids_list[i], season, 'points')
            get_Assists = get_stat(ids_list[i], season, 'assists')
            get_Goals = get_stat(ids_list[i], season, 'goals')
            get_PPPoints = get_stat(ids_list[i], season, 'powerPlayPoints')
            get_PPGoals = get_stat(ids_list[i], season, 'powerPlayGoals')
            get_Shots = get_stat(ids_list[i], season, 'shots')
            get_ShotPer = get_stat(ids_list[i], season, 'shotPct')
            get_FOPer = get_stat(ids_list[i], season, 'faceOffPct')
            get_GWGoals = get_stat(ids_list[i], season, 'gameWinningGoals')
            get_OTGoals = get_stat(ids_list[i], season, 'overTimeGoals')
            get_SHGoals = get_stat(ids_list[i], season, 'shortHandedGoals')
            get_SHPoints = get_stat(ids_list[i], season, 'shortHandedPoints')
            get_PM = get_stat(ids_list[i], season, 'plusMinus')
            get_Shifts = get_stat(ids_list[i], season, 'shifts')
            get_PIM = get_stat(ids_list[i], season, 'pim')
            get_PenMin = get_stat(ids_list[i], season, 'penaltyMinutes')
            get_Hits = get_stat(ids_list[i], season, 'hits')
            get_Blocked = get_stat(ids_list[i], season, 'blocked')
            get_TOI = get_stat(ids_list[i], season, 'timeOnIce')
            get_TOIPG = get_stat(ids_list[i], season, 'timeOnIcePerGame')
            get_PPTOI = get_stat(ids_list[i], season, 'powerPlayTimeOnIce')
            get_PPTOIPG = get_stat(ids_list[i], season, 'powerPlayTimeOnIcePerGame')
            get_EvenTOI = get_stat(ids_list[i], season, 'evenTimeOnIce')
            get_EvenTOIPG = get_stat(ids_list[i], season, 'evenTimeOnIcePerGame')
            get_SHTOI = get_stat(ids_list[i], season, 'shortHandedTimeOnIce')
            get_SHTOIPG = get_stat(ids_list[i], season, 'shortHandedTimeOnIcePerGame')
            cursor.execute("INSERT INTO " + table_name + " (Season, PlayerName, GamesPlayed, Points, Assists, Goals, PowerPlayPoints, PowerPlayGoals, Shots, ShotPercentage, FaceoffPercentage, GameWinningGoals, OvertimeGoals, ShortHandedGoals, ShortHandedPoints, PlusMinus, Shifts, PIM, PenaltyMinutes, Hits, Blocked, TimeOnIce, TimeOnIcePG, PowerPlayTimeOnIce, PowerPlayTimeOnIcePG, EvenTimeOnIce, EvenTimeOnIcePG, ShortHandedTimeOnIce, ShortHandedTimeOnIcePG) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", season, players_list[i], get_GP, get_Points, get_Assists, get_Goals, get_PPPoints, get_PPGoals, get_Shots, get_ShotPer, get_FOPer, get_GWGoals, get_OTGoals, get_SHGoals, get_SHPoints, get_PM, get_Shifts, get_PIM, get_PenMin, get_Hits, get_Blocked, get_TOI, get_TOIPG, get_PPTOI, get_PPTOIPG, get_EvenTOI, get_EvenTOIPG, get_SHTOI, get_SHTOIPG)
        else:
            table_name = 'Hockey.dbo.NHLG' + str(season) 
            cursor.execute('SELECT * FROM ' + table_name)
            get_GP = get_stat(ids_list[i], season, 'games')
            get_GS = get_stat(ids_list[i], season, 'gamesStarted')
            get_Wins = get_stat(ids_list[i], season, 'wins')
            get_Losses = get_stat(ids_list[i], season, 'losses')
            get_Ties = get_stat(ids_list[i], season, 'ties')
            get_ShutOuts = get_stat(ids_list[i], season, 'shutouts')
            get_OTGames = get_stat(ids_list[i], season, 'ot')
            get_SavePER = get_stat(ids_list[i], season, 'savePercentage')
            get_GAA = get_stat(ids_list[i], season, 'goalAgainstAverage')
            get_SA = get_stat(ids_list[i], season, 'shotsAgainst')
            get_GA = get_stat(ids_list[i], season, 'goalsAgainst')
            get_Saves = get_stat(ids_list[i], season, 'saves')
            get_EvenSaves = get_stat(ids_list[i], season, 'evenSaves')
            get_EvenSF = get_stat(ids_list[i], season, 'evenShots')
            get_EvenSavePER = get_stat(ids_list[i], season, 'evenStrengthSavePercentage')
            get_PPSaves = get_stat(ids_list[i], season, 'powerPlaySaves')
            get_PPShots = get_stat(ids_list[i], season, 'powerPlayShots')
            get_PPSavesPER = get_stat(ids_list[i], season, 'powerPlaySavePercentage')
            get_SHSaves = get_stat(ids_list[i], season, 'shortHandedSaves')
            get_SHShots = get_stat(ids_list[i], season, 'shortHandedShots')
            get_SHSavePER = get_stat(ids_list[i], season, 'shortHandedSavePercentage')
            get_TOI = get_stat(ids_list[i], season, 'timeOnIce')
            get_TOIPG = get_stat(ids_list[i], season, 'timeOnIcePerGame')
            cursor.execute("INSERT INTO " + table_name + " (Season, PlayerName, GamesPlayed, GamesStarted, Wins, Losses, Ties, Shutouts, OTGames, SavePercentage, GAA, ShotsAgainst, GoalsAgainst, Saves, EvenSaves, EvenShotsFaced, EvenSavePercentage, PowerPlaySaves, PowerPlayShotsFaced, PowerPlaySavePercentage, ShortHandedSaves, ShortHandedShotsFaced, ShortHandedSavePercentage, TimeOnIce, TimeOnIcePerGame) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", season, players_list[i], get_GP, get_GS, get_Wins, get_Losses, get_Ties, get_ShutOuts, get_OTGames, get_SavePER, get_GAA, get_SA, get_GA, get_Saves, get_EvenSaves, get_EvenSF, get_EvenSavePER, get_PPSaves, get_PPShots, get_PPSavesPER, get_SHSaves, get_SHShots, get_SHSavePER, get_TOI, get_TOIPG)
    cnxn.commit()

for i in get_LeagueIDS():
    insert_SeasonStats(get_teamInfo(i, 'fullName'), get_teamInfo(i, 'id'), 20192020)
    
#"""



#Insets stats for each player into sql using .executemany method.

def insertPlayers_team(players_list, ids_list, teamIDS_list):
    cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-V3RT9V4\SQLEXPRESS;'
                      'Database=Hockey;'
                      'UID=djuser;'
                      'PWD=djuser1;')

    cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-V3RT9V4\SQLEXPRESS;'
                      'Database=Hockey;'
                      'Trusted_Connection=yes;')
    #print(cnxn)
    cursor = cnxn.cursor()
    cursor.fast_executemany = True
    for i in range(len(ids_list)):
        know_position = trim_singlePosition(ids_list[i])
        params = [((players_list[i]), (teamIDS_list[i]), (get_playerInfo(ids_list[i], 'currentAge')), (get_playerInfo(ids_list[i], 'nationality')), (determine_rookie(ids_list[i])), (trim_singlePosition(ids_list[i])), (get_playerInfo(ids_list[i], 'height')), (get_playerInfo(ids_list[i], 'weight')), (ids_list[i]))]
        if know_position != 'Goalie':
            print("Begin insert {playername} ".format(playername = players_list[i]) + str(datetime.datetime.now))
            cursor.execute('SELECT * FROM Hockey.dbo.NHLPlayer')
            #(cursor.executemany("INSERT INTO Hockey.dbo.NHLPlayer (PlayerName, TeamID, Age, Nationality, Rookie, Position, Height, Weight, APIKey) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", params))
            print("End insert {playername} ".format(playername = players_list[i]) + str(datetime.datetime.now))
        else:
            print("Begin insert {playername} ".format(playername = players_list[i]) + str(datetime.datetime.now))
            cursor.execute('SELECT * FROM Hockey.dbo.NHLGoalies')
            #(cursor.executemany("INSERT INTO Hockey.dbo.NHLGoalies (PlayerName, TeamID, Age, Nationality, Rookie, Position, Height, Weight, APIKey) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", params))       
            print("End insert {playername} ".format(playername = players_list[i]) + str(datetime.datetime.now))

    #for row in cursor:
        #print(row)
    cnxn.commit()

for i in get_LeagueIDS():
    insertPlayers_team(get_teamInfo(i, 'fullName'), get_teamInfo(i, 'id'), get_teamIDList(i))

 



"""
#print(get_stat(8470645, 20192020, 'shortHandedSavePercentage'))
#print(get_playerInfo())


#print(get_teamName(3))

#print(transform_list("https://statsapi.web.nhl.com/api/v1/teams/3/roster"))
#print(teamPlayer_stats(prl, 20182019))
#print(get_player(8476459))

#mikal_stats = (singleSeason_stats(8476459, 20192020))
#print(mikal_stats)

#print(get_stat(8476459, 20192020, 'goals'))
#compile_stats(8476459, 20192020)

#print(get_playerInfo(8476459, 'fullName'))

#print(get_teamInfo(3, 'fullName'))
    

#Ignore
"""


"""def insertPlayers_team(players_list, ids_list, teamIDS_list):
    cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ServerXXX;'
                      'Database=Hockey;'
                      'Trusted_Connection=yes;')
    #print(cnxn)
    cursor = cnxn.cursor()
    cursor.execute('SELECT * FROM Hockey.dbo.NHLPlayer')
    #for row in cursor:
        #print(row)
    
    for i in range(len(players_list)):
        
        get_age = get_playerInfo(ids_list[i], 'currentAge')
        get_nation = get_playerInfo(ids_list[i], 'nationality')
        get_rook = determine_rookie(ids_list[i])
        get_position = trim_singlePosition(ids_list[i])
        get_height = get_playerInfo(ids_list[i], 'height')
        get_weight = get_playerInfo(ids_list[i], 'weight')
        cursor.execute("INSERT INTO Hockey.dbo.NHLPlayer (PlayerName, TeamID, Age, Nationality, Rookie, Position, Height, Weight, APIKey) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", players_list[i], teamIDS_list[i], get_age, get_nation, get_rook, get_position, get_height, get_weight, ids_list[i])
    cnxn.commit()


#Ignore
def insert_SeasonStats(players_list, ids_list, season):
    cnxn = pyodbc.connect('Driver={SQL Server};'
                      'Server=ServerXXX;'
                      'Database=Hockey;'
                      'Trusted_Connection=yes;')
    #print(cnxn)
    cursor = cnxn.cursor()
    table_name = 'Hockey.dbo.NHL' + str(season) 
    cursor.execute('SELECT * FROM ' + table_name)

    for i in range(len(players_list)):
        get_GP = get_stat(ids_list[i], season, 'games')
        cursor.execute("INSERT INTO " + table_name + " (Season, PlayerName, GamesPlayed) VALUES (?, ?, ?)", season, players_list[i], get_GP)
    cnxn.commit()"""







 