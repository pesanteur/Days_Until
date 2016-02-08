from datetime import datetime, timedelta 
import timestring

def days_until(date): 
	date = timestring.Date(date)
	date_string = str(date)
	date_string_split = date_string.split(' ')
	real_date = datetime.strptime(date_string_split[0], '%Y-%m-%d')
	today = datetime.now()
	diff = real_date - today
	return diff
	