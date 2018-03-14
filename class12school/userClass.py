# define the User class

class User:
    def __init__(self):
        self.userName = ""
        self.password = ""
        self.table = "websites"

    def description(self):
        desc_str = "%s uses websites in table %s for scraping" % (self.userName, self.table)
        return desc_str

    def setTable(self):
        self.table = self.userName+"_websites"

    def getTable(self):
        return self.table
    

def defaultUser():
    default = User()
    default.userName = "User"
    return default
    
