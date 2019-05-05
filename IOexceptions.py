# Author 		: 	John Lee
# Creation Date	: 	4/29/2019
# Last Update		:	4/29/2019
# Purpose		:	Library to test IO operations and return exceptions when fails
# Input			:	file, mode (name of file, file mode)
# Output		:	result (0 is success, 1 is failure)

# import libraries
import os

# define user based exceptions
class Error(Exception):
	"""Base class for other exceptions"""
	pass

class ArgNotString(Error):
	"""Raised when FileName passed in is not a string"""
	pass

class InvalidFileMode(Error):
	"""Raised when mode to open file is invalid"""
	pass

class FileEmptyError(Error):
	"""Raised when file is empty"""
	pass

# define function to open file and return exceptions
def open_file(file, mode):
	try:
		# Verify arguments are strings
		if not isinstance(file, str) or not isinstance(mode, str):
			raise ArgNotString
			return 1

		# Check for empty file if reading file
		if mode == 'r' or  mode == 'rb': 
			if os.stat(file).st_size > 0:
				# Try to open file in specified mode
				opened_file = open(file, mode)

			# If file empty print file is empty
			else:
				raise FileEmptyError
				return 1
		
		# Else just open it
		elif mode == 'w' or mode == 'a' or mode == 'wb' or mode == 'ab':
			opened_file = open(file, mode)

		# invalid mode
		else:
			raise InvalidFileMode
			return 1

	except FileNotFoundError:
		print()
		print('ERROR: File %s not found.' % file)
		print()

	except OSError:
		print()
		print('ERROR: File %s not found.' % file)
		print()

	except IOError:
		print()
		print('ERROR: File %s not found.' % file)
		print()

	except PermissionError:
		print()
		print('ERROR: Insufficient permissions to open %s' % file)
		print()

	except ArgNotString:
		print()
		print('ERROR: Argument must be a string.')
		print()

	except InvalidFileMode:
		print()
		print('ERROR: Invalid file mode. Must be "r" or "w" or "a".')
		print()

	except FileEmptyError:
		print()
		print('ERROR: File %s is empty.' % file)
		print()

	else:
		# If successful return opened_file
		return 0