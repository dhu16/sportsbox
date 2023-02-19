#User profile stuff

class User:
    def __init__(self, username, displayname, theme):
        self.username = username
        self.displayname = displayname
        self.theme = theme #color of UI
        self.sports = [] #cannot be empty, just nba for now
        self.favoriteplayers = [] #must always have at least 1
        self.favoriteteams = [] #must always have at least 1

    #Getters
    def getUser(self):
        return self.username   
    def getFavoritePlayers(self):
        return self.favoriteplayers
    def getFavoriteTeams(self):
        return self.favoriteteams

    #Setters
    def setUser(self, id):
        self.username=id
    def setDisplayName(self, name):
        self.displayname=name
    def setTheme(self, color): #set to color scheme of favorite team
        self.theme=color
    def addPlayer(self, player):
        self.favoriteplayers.append(player)
    def addTeam(self, team):
        self.favoriteteams.append(team) 
