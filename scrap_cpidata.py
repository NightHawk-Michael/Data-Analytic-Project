from bs4 import BeautifulSoup
import urllib.request
import pandas as pd

# Read URL
url = "https://www.minneapolisfed.org/community/teaching-aids/cpi-calculator-information/consumer-price-index-1800"
content = urllib.request.urlopen(url).read()

# Put HTML content into soup object
soup = BeautifulSoup(content, 'html.parser')

# Process the soup object to get the CPI data from the table in the html
headers = []
for header in soup.find_all('th'):
	beautified_header = "_".join(header.get_text().replace('\n','').split())
	headers.append(beautified_header)

cpidata = []
for row in soup.find_all('tr'):
	rowdata = []
	for data in row.find_all('td'):
		div_text = data.find('div').get_text().replace(u'\xa0',u'')
		if(div_text != ''):
			div_text = div_text.replace(u'*',u'')
			div_text = div_text.replace(u'%',u'')
			rowdata.append(float(div_text))
		else:
			rowdata.append(None)
	if(len(rowdata) > 0):
		cpidata.append(rowdata)

# Prepare dataframe using pandas
dataframe = pd.DataFrame(cpidata, columns=headers)
dataframe = dataframe.dropna()

# Write to CSV using pandas
path = "/Users/Michael/Documents/CZ4032 Project/csv/cpidata.csv"
dataframe.to_csv(path, encoding='utf-8', index=False)

print("Successfully generated cpidata.csv file...")
