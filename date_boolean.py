# Create a boolean column that tells whether the date is in a list of date
dataset['isHoliday'] = dataset['Date'].apply(lambda x: 1 if any(x == d for d in holiday_list.values) else 0)

# Create a boolean column that tells whether the date is between a range of date
 # term is a two-variable dataset that contains the start and end date of school terms
term_date = []
for i in range(len(term)):
  a = list(pd.date_range(start = term['start'][i], end = term['end'][i])) 
  term_date = term_date + a

dataset['isSchoolTerm'] = dataset['Date'].apply(lambda x: 1 if any(x == d for d in term_date) else 0)
