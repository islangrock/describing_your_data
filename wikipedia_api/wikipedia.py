# Can run this file from Terminal
# 	1. Open terminal
#	2. Change to this directory with cd ~/Desktop/describing_your_data/wikipedia
#	3. Open ipython with ipython
#	4. Copy code and paste into ipython with %paste

import wptools
import csv

# open a csv file called results CHANGE NAME WHEN RUNNING SO IT DOESN'T OVERWRITE
f = open("allresults.csv", 'w')
writer = csv.writer(f)
labels = ["title",'infobox','length','wikilinks','editorcount','pageID','aveviews', 'categories']
writer.writerow(labels)

## Sample pages for making sure code works before running on the whole list. 
articles = ['Donna Strickland', 'Nathan Ransom Leonard  ']

# making an array from data names 
names = [ ] 

with open('500WomenScientistsList.csv') as csvDataFile: 
	csvReader = csv.reader(csvDataFile)
	for row in csvReader:
		names.append(row[0])
print(names)

# adding data for each article 

for a in names:
	# fetch page data
	#	to see what's available, run  page.data.keys() 
	page = wptools.page(a)
	page.get_parse()
	page.get_query()
	page.get_more()

	# pull out page data into variables
	title = page.data['title']
	infobox = page.data['infobox']
	# infobox_attributes = infobox.keys() # will need to apply to only pages with infoboxes. Now, printing out a blank for those
	pagelength = page.data['length']
	wikilinks = page.data['links']
	editors = page.data['contributors']
	ID = page.data['pageid']
	ave_views = page.data['views']
	categories = page.data['categories']

	# create an array called row with the variables
	row = [title, infobox, pagelength, wikilinks, editors, ID, ave_views, categories]
	print(row)

	# write that row to a csv
	writer.writerow(row)

f.close()




