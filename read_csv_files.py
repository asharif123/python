import csv, os
os.chdir('C:/Users/Awad')
print (os.getcwd())
##with open('company_sales_data.csv') as csv_file:
##    contents = csv.reader(csv_file)
##    for row in contents:
##        print (row)

with open('sitka_weather_07_2014.csv') as csv_file:
    read_file = csv.reader(csv_file)
#use 'next()' to print the column names!
    header_row = next(read_file)
###use index and column name to print name and index associated with each col name!
##    for index, column_name in enumerate(header_row):
##        print (index, column_name)

##read data from the first column (dates) second column (max_temperatures column!)
    highs = []
    dates = []
    for row in read_file:
        dates.append(row[0])
        highs.append(int(row[1]))
    print (highs,dates)


>>> with open('sitka_weather_07_2014.csv') as csv_file:
	read_file = csv.reader(csv_file)
	dates = []
	highs = []
#use 'enumerate()' to extract index and row from read csv_file
#use strptime from datetime to format date to proper format
#here are strptime formats:
#%A - weekday
#%B - Month name spelled out (ex: January)
#%m - month in number (01 to 12)
#%d - day of month (01 to 31)
#%Y - year in four digit (2019)
#%y - year in 2 digits (19)
#%H - Hour, (01 to 24)
#%I - 12 Hour format (01 to 12)
#%P - AM or PM
#%M - Minutes (0 to 59)
#%S - Seconds (00 to 61)

##skip header row (ex: index == 0)
	for index, row in enumerate(read_file):
		if (index == 0):
			continue
		current_date = datetime.strptime(row[0],'%m/%d/%Y')
		dates.append(current_date)
		highs.append(row[1])

		
>>> plt.xlabel('Dates',fontsize=10)
Text(0.5, 0, 'Dates')
>>> plt.ylabel('Temperatures',fontsize=10)
Text(0, 0.5, 'Temperatures')
>>> plt.title('Plot of High Temperatures of 2014',fontsize=15)
Text(0.5, 1.0, 'Plot of High Temperatures of 2014')
>>> plt.plot(dates,highs,color='red')

>>> plt.show()
plt.plot(dates,lows,color='blue')

>>> plt.plot(dates,highs,color='red')
#.fill_between() fills color btwn graphs(x-axis, y1-axis, y2-sxis
#alpha ranges transparency to opague (0 to 1)
>>> plt.fill_between(dates,highs,lows,color='green',alpha=0.4)

    

    
