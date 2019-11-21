# Can run this file from Terminal
# 	1. Open terminal
#	2. Change to this directory with cd ~/Desktop/describing_your_data/wikipedia
#	3. Open ipython with ipython
#	4. Copy code and paste into ipython with %paste

import wptools
import pandas as pd
import csv

# open a csv file called results CHANGE NAME WHEN RUNNING SO IT DOESN'T OVERWRITE
f = open("artandfemWiki3.csv", 'w')
writer = csv.writer(f)
labels = ["title",'infobox','length','wikilinks','editorcount','pageID','aveviews', 'categories']
writer.writerow(labels)

## Sample pages for making sure code works before running on the whole list. 
articles = ['Donna Strickland', 'Nathan Ransom Leonard ', 'Bill Murray']

# making an array from data names 
names = [ ] 

with open('artplusfeminismList_clean.csv') as csvDataFile: 
	csvReader = csv.reader(csvDataFile)
	for row in csvReader:
		names.append(row[0])
print(names)

# adding data for each article 
for a in names:
	# fetch page data
	#	to see what's available, run  page.data.keys() 
	try: 
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
	except:
		print("Page does not exist")
f.close()

#Getting Data about politicians - first pulling names: 

sources = ['List of female United States presidential and vice-presidential candidates', 
			'List of female governors in the United States',
			'Women in the United States House of Representatives',
			'List of female lieutenant governors in the United States',
			'List of female members of the House of Representatives of Puerto Rico',
			'List of female speakers of legislatures in the United States',
			'List of female state attorneys general in the United States',
			'List of female state secretaries of state in the United States',
			'List of female United States Cabinet Secretaries',
			'List of first women mayors in the United States',
			'List of most senior women in the United States Congress',
			'List of female state supreme court justices',
			'Women in the United States Senate']

politics = open("politicians.csv", 'w')
writer = csv.writer(politics)
labels = ["title",'wikilinks']
writer.writerow(labels)

for n in sources:
	try: 
		page = wptools.page(n)
		page.get_parse()
		page.get_query()
		page.get_more()
		title = page.data['title']
		wikilinks = page.data['links']

		row = [title, wikilinks]
		print(row)

		writer.writerow(row)
	except:
		print("PageDoesNotExist")
politics.close

femalepoliticians = pd.read_csv("politicians.csv")

WikiNet = femalepoliticians.apply(net, axis=1)
WikiNet = list(WikiNet)
Network = pd.concat(WikiNet)
Network.columns=['Destination', 'Source']

Network.to_csv("FemalePoliticians.csv")

# First Manual Cleanup -- remove all none humans, then return to download information 

p = open("politicsWiki.csv", 'w')
writer = csv.writer(p)
labels = ["title",'infobox','length','wikilinks','editorcount','pageID','aveviews', 'categories']
writer.writerow(labels)

names = [ ]

with open('FemalePoliticians.csv') as csvDataFile: 
	csvReader = csv.reader(csvDataFile)
	for row in csvReader:
		names.append(row[0])
print(names)

for a in names:
	# fetch page data
	#	to see what's available, run  page.data.keys() 
	try: 
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
	except:
		print("Page does not exist")
p.close()

#Locating page information for athletes 

sources = ['List of sportswomen',
			'List of Olympic medalists in athletics (women)',
			'List of female kickboxers',
			'List of female golfers',
			"List of Women's National Basketball Association players",
			"List of FIFA Women's World Cup goalscorers",
			"Chronological list of women's Grand Slam tennis champions"]

athletes= open("athletes.csv", 'w')
writer = csv.writer(athletes)
labels = ["title",'wikilinks']
writer.writerow(labels)


for n in sources:
	try: 
		page = wptools.page(n)
		page.get_parse()
		page.get_query()
		page.get_more()
		title = page.data['title']
		wikilinks = page.data['links']

		row = [title, wikilinks]
		print(row)

		writer.writerow(row)
	except:
		print("PageDoesNotExist")
athletes.close

femaleathletes = pd.read_csv("athletes.csv")

WikiNet = femaleathletes.apply(net, axis=1)
WikiNet = list(WikiNet)
Network = pd.concat(WikiNet)
Network.columns=['Destination', 'Source']

Network.to_csv("FemaleAthletes.csv")
#Manual Cleanup 

p = open("athletesWiki.csv", 'w')
writer = csv.writer(p)
labels = ["title",'infobox','length','wikilinks','editorcount','pageID','aveviews', 'categories']
writer.writerow(labels)

names = [ ]

with open('FemaleAthletes.csv') as csvDataFile: 
	csvReader = csv.reader(csvDataFile)
	for row in csvReader:
		names.append(row[0])
print(names)

for a in names:
	# fetch page data
	#	to see what's available, run  page.data.keys() 
	try: 
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
	except:
		print("Page does note exist")

p.close()



# How to extract network information 

def net(x):
	row= x.wikilinks
	destination= row.split(",")
	source = x.title
	subdf=pd.DataFrame(destination)
	subdf['source']= source 
	return subdf

sample = pd.read_csv("sample.csv")

WikiNet = sample.apply(net, axis=1)
WikiNet = list(WikiNet)
Network = pd.concat(WikiNet)
Network.columns=["Destination","Source"]

print(Network.head())

Network.to_csv("SampleNet.csv")




