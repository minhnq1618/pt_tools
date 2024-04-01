import os
import magic

from colors.colors import *

file = "test.py1"

def mime_check(file):
	# Get the MIME type of the file
	mime = magic.from_file(file, mime=True)

	# Check if the file has a TXT or Excel MIME type
	if mime.startswith('text/plain'):
		return 'txt'
	elif mime.startswith('application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'):
		return 'excel'
	else:
		return False

def file_check(file):
	try:
		if os.path.exists(file):
			if mime_check(file) == "txt":
				print("txt")
			elif mime_check(file) == "excel":
				print("excel")
			else:
				print(R("File type does not support!"))
		else:
			print(R("File does not exists!"))
	except Exception as e:
		print(e)

file_check(file)
