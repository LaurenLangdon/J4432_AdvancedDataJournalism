#import is a Python module that lets you download web pages and the csv is the file type
import urllib2, csv
#from will allow you to just download BeautifulSoup in bs4 instead of the entire bs4
from bs4 import BeautifulSoup

#I think outfile is creating a new document/output. I think 'jaildata.csv' is the name of the file and based on the following line, I think the w stands for writer
outfile = open('jaildata.csv', 'w')
#I'm not sure what this means, but maybe it's closing the "open" from the previous statement.
writer = csv.writer(outfile)

#this function calls to a website
url = 'https://report.boonecountymo.org/mrcjava/servlet/SH01_MP.I00290s?max_rows=500'
#this opens the url from the previous line and reads it
html = urllib2.urlopen(url).read()

#this refers to a Python library called Beautiful soup and the specific html.parser
soup = BeautifulSoup(html, "html.parser")

#this says that within the Beautiful Soup go to the table body where the class is stripe
tbody = soup.find('tbody', {'class': 'stripe'})
#this says to return all of the table rows  
rows = tbody.find_all('tr')

#this is storing row as a variable, this creates a loop
for row in rows:

	#in the cells go to the attribute row and the action is to find all the cells
    cells = row.find_all('td')

    #I think this creates a new empty list
    data = []

    #this is storing cells as a variable, this creates another loop
    for cell in cells:
    	#this will adjust the text in the cells
        data.append(cell.text)
    #this refers to the earlier outfile and inputs the empty data list that we made
    writer.writerow(data)