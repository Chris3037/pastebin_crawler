import requests
from bs4 import BeautifulSoup
import time
import os
# import urllib


links = []
titles = []


def GetLinks():
	# archive_url = "https://pastebin.com/archive"
	# response = requests.get(archive_url)
	# Setup connection


	url = "https://pastebin.com/"
	response = requests.get(url)

	html = response.text
	soup = BeautifulSoup(html, 'html.parser')

	# content_div = soup.find(class_='maintable').find_all('tr')
	# Get correct data
	content_div = soup.find(class_='right_menu')


	# Apply Data to variables
	global titles
	global links
	links = []
	titles = []
	for item in content_div.find_all('a'):
		titles.append(item.text)
		links.append(item.get('href'))

def SaveFile(title, link, content):
	# filePath = os.path.dirname(os.path.realpath(__file__)) + "/temp.txt"
	filePath = os.path.dirname(os.path.realpath(__file__)) + "/saved_links.txt"
	# print(filePath)
	with open(filePath, 'a+') as f:
		# f.write("\nTest")
		f.write("\n\n\n\n\n################################\n\n\n\n\nTitle: \"" + str(title) + "\"\nURL: \""+str(link)+"\"\n____________________________________________________________________\n\n\n"+str(content))


def PrintContent(link, title):
	print("#################################")
	print("#################################")
	print("#################################")
	os.system('clear')

	response = requests.get(link)
	html = response.text
	soup = BeautifulSoup(html, 'html.parser')
	print(soup.text)
	print()
	print()
	print()

	PrintInfo(link, soup, title)


def PrintInfo(link, soup, title):
		print()
		print("_________________________________")
		print()
		print(title)
		print(link)
		print()
		print("Press enter to see next paste....")
		print("Or type in 8 char Pastebin URL")
		print("[s] to save. [q] to quit")
		PromptInput(link, soup, title)


def PromptInput(link, soup, title):
	userInput = input()
	print()
	print()
	if str(userInput).lower() == 'q':
		import sys
		sys.exit()
	elif str(userInput).lower() == 's':
		# Save to file
		SaveFile(title, link, soup.text);
		print("Saved...")
		print()
		PrintInfo(link, soup, title)
	elif len(userInput) == 8:
		new_link = "https://pastebin.com/raw/" + str(userInput)
		new_link_orig = "https://pastebin.com/" + str(userInput)
		response = requests.get(new_link_orig)

		if response:
			html = response.text
			soup = BeautifulSoup(html, 'html.parser')
			new_title = soup.find(class_='paste_box_line1').h1.text
			PrintContent(new_link, new_title)
		else:
			print("Invalid URL...")
			print()
			PrintInfo(link, soup, title)




while True:
	GetLinks()
	# already_vistited = []
	print("Refreshing Links...")

	for i in range(0, 8):
		link = "https://pastebin.com/raw" + str(links[i])
		PrintContent(link, titles[i])


# BUGS:
# Some <> characters show incorrectly
	# eg. http://pastebin.com/raw/83fx9W5m