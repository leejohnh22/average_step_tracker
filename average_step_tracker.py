# John Lee		4/11/2019
# Last updated	5/3/2019
# Program Exercise 6-12
# Calculate the average of steps taken each month and print to standard out

# Input
#	steps_text
# Output
#	steps_in_month

# Import libraries
import os
import IOExceptions

# Define Constants
MONTHS_IN_YEAR = 12

def main():
	# Initialize variables
	text_file = 'steps.txt'
	open_mode = 'r'
	open_result = 1
	num_months_in_file = 0
	cur_month = 1
	day_count = 0
	total_line_counter = 0
	num_steps = 0
	num_total_steps = 0
	average_step_count = 0
	year = 0
	leap_year = False

	days_in_year = 365

	# Define dictionary to hold average number of steps taken each month
	steps_in_month = {
	1 : 0,
	2 : 0,
	3 : 0,
	4 : 0,
	5 : 0,
	6 : 0,
	7 : 0,
	8 : 0,
	9 : 0,
	10 : 0,
	11 : 0,
	12 : 0
	}

	# Define dictionary that holds number of days for each month
	days_in_month = {
	1 : 31,
	2 : 28,
	3 : 31,
	4 : 30,
	5 : 31,
	6 : 30,
	7 : 31,
	8 : 31,
	9 : 30,
	10 : 31,
	11 : 30,
	12 : 31
	}

	cumulative_days_by_month = {
	1 : 31,
	2 : 59,
	3 : 90,
	4 : 120,
	5 : 151,
	6 : 181,
	7 : 212,
	8 : 243,
	9 : 273,
	10 : 304,
	11 : 334,
	12 : 365
	}

	# Ask user for year
	year = input("Enter year : ")

	# Error check
	while year.isdigit() == False:
		year = input("Please enter a valid year : ")

	# Convert year to int
	year = int(year)

	# Check if year is leap year
	if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
		leap_year = True

	# If year input is leap year, adjust days per month in dict
	if leap_year == True:
		for month in range(2, len(cumulative_days_by_month)):
			cumulative_days_by_month[month] += 1

		days_in_month[2] += 1

		days_in_year += 1

	# Try to open the file and capture any exceptions
	open_result = IOExceptions.open_file(text_file, open_mode)

	# If open attempt is successful with no exceptions, open file
	if open_result == 0 :
		# Calculate number of lines
		with open(text_file, open_mode) as file:
			num_lines = sum(1 for line in file)

			# Calculate number of months data in file if number of lines is less than 12 months
			for i in range(1, len(cumulative_days_by_month) + 1):
				if i < len(cumulative_days_by_month):
					if (num_lines > cumulative_days_by_month[i]) and (num_lines < cumulative_days_by_month[i + 1]):
						num_months_in_file = i
				# else we know that there are at least 11 months of data
				else:
					num_months_in_file = len(cumulative_days_by_month)

		with open(text_file, 'r') as step_file:
			# While month_count is less than months_in_year
			while cur_month <= num_months_in_file:
				# While day_count is less than days_in_month of current month read line in file, strip \n, convert to int
				while day_count <= days_in_month[cur_month]:
					line = step_file.readline()
					# If not an empty string process it
					if line.strip():
						num_steps = int(line.strip())

					# Add steps taken that day to total step count
					num_total_steps += num_steps

					# Increment day_count by one for each line read
					day_count += 1

				# When current month is done being counted, calculate average step count and store in average_step_count
				average_step_count = calc_avg_step_in_month(days_in_month[cur_month], num_total_steps)
				steps_in_month[cur_month] = average_step_count

				# Increment month count
				cur_month += 1

				# Reset day count and step count
				day_count = 0
				num_steps = 0
				num_total_steps = 0
		# File Closed

		# Format output
		print()
		# Output WARNING if number of days in file is less than one year
		if num_lines < days_in_year:
			print("\tWARNING:\tNumber of days in %s contains less than the number of days in a year (%i)." % (text_file, days_in_year))
			print("\t\t\tTable below may contain inaccurate averages.")
		# Output WARNING if number of days in file is more than one year
		elif num_lines > days_in_year:
			print("\tWARNING:\tNumber of days in %s contains more than the number of days in a year." % text_file)
			print("\t\t\tTable below will contain averages for the first %i days." % days_in_year)

		# Print monthly averages to stdout
		print_step_average_monthly(steps_in_month[1], steps_in_month[2], steps_in_month[3], steps_in_month[4], steps_in_month[5], steps_in_month[6], steps_in_month[7], steps_in_month[8], steps_in_month[9], steps_in_month[10], steps_in_month[11], steps_in_month[12])

# Define function to calculate average steps for the month
def calc_avg_step_in_month(num_days, total_steps):
	try:
		# Calculate average step count
		average_step_count = total_steps / num_days

		# Return average step count
		return average_step_count

	# Raise exception if float conversion fails
	except FloatingPointError:
		print("File must contain numerical values only.")

	# Raise exception if count is 0
	except ZeroDivisionError:
		print("File must contain more than one number.")

# Define function to print out average number of steps for each month, format as integer with comma seperators
def print_step_average_monthly(jan_step_avg, feb_step_avg, mar_step_avg, apr_step_avg, may_step_avg, jun_step_avg, jul_step_avg, aug_step_avg, sep_step_avg, oct_step_avg, nov_step_avg, dec_step_avg):
	print()
	print("\tAverage Step Count for each Month : ")
	print("\t____________________________________")
	print()
	print("\tJanuary\t\t", format(jan_step_avg, ',.0f'))
	print("\tFebruary\t", format(feb_step_avg, ',.0f'))
	print("\tMarch\t\t", format(mar_step_avg, ',.0f'))
	print("\tApril\t\t", format(apr_step_avg, ',.0f'))
	print("\tMay\t\t", format(may_step_avg, ',.0f'))
	print("\tJune\t\t", format(jun_step_avg, ',.0f'))
	print("\tJuly\t\t", format(jul_step_avg, ',.0f'))
	print("\tAugust\t\t", format(aug_step_avg, ',.0f'))
	print("\tSeptember\t", format(sep_step_avg, ',.0f'))
	print("\tNovember\t", format(nov_step_avg, ',.0f'))
	print("\tDecember\t", format(dec_step_avg, ',.0f'))
	print()

main()
# END OF PROGRAM