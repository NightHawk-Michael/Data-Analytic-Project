import pandas as pd
import math

# Reading data from movie_metadata.csv
data = pd.read_csv("/Users/Michael/Documents/CZ4032 Project/csv/movie_metadata.csv",header = 0)
data = data[['movie_title','title_year','budget']]
movie_data = data.values.tolist()

# Reading data from cpidata.csv
cpidata = pd.read_csv("/Users/Michael/Documents/CZ4032 Project/csv/cpidata.csv", header = 0)
cpidata = cpidata.dropna()
years = cpidata.Year.tolist()
annual_avg = cpidata.Annual_Average.tolist()
cpi = {} 
for i in range(0, len(years)):
	cpi[years[i]] = annual_avg[i]	

# Process data by converting all budgets from the past years to 2017 budget
movie_budget_2017 = []
for i in range(0, len(movie_data)):
	movie_title = movie_data[i][0]
	movie_year = movie_data[i][1]
	movie_budget = movie_data[i][2]
	new_budget = 'nan' 
	if((not math.isnan(movie_year)) and (not math.isnan(movie_budget))):
		new_budget = movie_budget*(cpi[2017.0]/cpi[movie_year])
	temp = []
	temp.append(movie_title)
	temp.append(new_budget)
	movie_budget_2017.append(temp)

# Write data back to csv file
headers = ['movie_title','budget_2017']
budget_data = pd.DataFrame(movie_budget_2017, columns = headers)
budget_data.to_csv("/Users/Michael/Documents/CZ4032 Project/csv/budget_data.csv", encoding='utf-8',index=False)
print("Successfully read and process %s data from movie_metadata.csv ..." % len(data))

