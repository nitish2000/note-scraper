from flask import Flask, render_template, request
import re, json, requests, urllib2
from bs4 import BeautifulSoup
import sqlite3 as sql
import wolframalpha

# define the User class
class User:

    userName = ""
    password = ""
    table = "websites"

    def description(self):
        desc_str = "%s uses websites in table %s for scraping" % (self.userName, self.table)
        return desc_str

    def setTable():
        self.table = userName+"_websites"

    def getTable(self):
        return self.table
    

def defaultUser():
    default = User()
    default.userName = "User"
    return default
    
