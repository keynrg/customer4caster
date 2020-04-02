# Create a boolean column that tells whether the date is in a list of date
dataset['isHoliday'] = dataset['Date'].apply(lambda x: 1 if any(x == d for d in holiday_list.values) else 0)

# Create a boolean column that tells whether the date is between a range of date
 # term is a two-variable dataset that contains the start and end date of school terms
term_date = []
for i in range(len(term)):
  a = list(pd.date_range(start = term['start'][i], end = term['end'][i])) 
  term_date = term_date + a

dataset['isSchoolTerm'] = dataset['Date'].apply(lambda x: 1 if any(x == d for d in term_date) else 0)

# Create a boolean column that tells whether it is working hour 
dataset['isNotWorkingHour'] = dataset['Time'].apply(lambda x: 0 if (x >= datetime.strptime('09:00:00', '%H:%M:%S').time() and x <=datetime.strptime('18:00:00', '%H:%M:%S').time()) else 1)

def determineSeason(date):
	month = date.month
	if(month == 12 or month == 1 or month == 2):
		return 0 #summer
	elif(month == 3 or month == 4 or month == 5):
		return 1 #autumn
	elif(month == 6 or month == 7 or month == 8):
		return 2 #winter
	else: 
		return 3 #spring
