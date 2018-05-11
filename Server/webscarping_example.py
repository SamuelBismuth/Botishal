from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import MySQLdb
# Specifying incognito mode as you launch your browser[OPTIONAL]
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

# Create new Instance of Chrome in incognito mode
browser = webdriver.Chrome(executable_path='/home/ehud/Desktop/chromedriver', chrome_options=option)

# Go to desired website
browser.get("https://meyda.ariel.ac.il/michlol3/StudentPortalWap/Pt_login.aspx")

# Wait 20 seconds for page to load
password = browser.find_element_by_id('ctl00_idMasterContentPlaceHolder_SecretCode_text')
username = browser.find_element_by_id('ctl00_idMasterContentPlaceHolder_IdentityNumber_text')
username.send_keys("314095605")
password.send_keys("9424")
browser.find_element_by_id("ctl00_idMasterContentPlaceHolder_idLogin").click()
browser.implicitly_wait(10)
browser.find_element_by_link_text('מערכת שעות').click()



# Get all of the titles for the pinned repositories
# We are not just getting pure titles but we are getting a selenium object
# with selenium elements of the titles.
titles_element =browser.find_elements_by_xpath("//a/pre")

# find_elements_by_xpath - Returns an array of selenium objects.


# List Comprehension to get the actual repo titles and not the selenium objects.
titles = [x.text for x in titles_element]
titles = list(filter(None, titles))
titles = [w.replace('( רישום על תנאי )','') for w in titles]



# print response in terminal
print('TITLES:')
print(titles, '\n')
for course in titles:
        data = course.split("\n")
        print(data)

db = MySQLdb.connect(host="erlichsefi.mooo.com",    # your host, usually localhost
                     user="remote",         # your username
                     passwd="remotetoor",  # your password
                     db="Hackatton",
                     port=4306)        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()
db.set_character_set('utf8')

# Use all the SQL you like
for course in titles:
        data = course.split("\n")
        data = list(filter(None, data))
        arg=data[1]
        cur.execute("INSERT INTO Teachers (firstName) VALUES(%s)", (arg,))

# print all the first cell of all the rows
for row in cur.fetchall():
    print(row[2])

db.close()
