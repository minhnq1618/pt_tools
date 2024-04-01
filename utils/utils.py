import os
import sys
import magic
import argparse
import platform

from colors.colors import *

# Import rich module for some nice table display
from rich.table import Table

# Arguments for the tool
def parse_arguments():
	parser = argparse.ArgumentParser(description="Broken Access Control Check", epilog="Author : Minhg Nguyen Quang")

	parser.add_argument('-pt', '--privilege-token', type=str, default="", help="Privilege Session Token")
	parser.add_argument('-nt', '--normal-token', type=str, default="", help="Normal Session Token")
	parser.add_argument('-pc', '--privilege-cookie', type=str, default="", help="Privilege Session Cookie")
	parser.add_argument('-nc', '--normal-cookie', type=str, default="", help="Privilege Session Cookie")
	parser.add_argument('-f', '--file', type=str, default="", help="File that have the target's urls")
	args = parser.parse_args()
	return args

# Handle error or for other thing if i lazy
def error(string):
	preface = "\n[!] "
	print(R(preface) + string)
	sys.exit(1)

# Clear the cli
def clear():
	if platform.system() == "Linux":
		os.system("clear")
	elif platform.system() == "Windows":
		os.system("cls")

def create_rich_table(description):
	table = Table(
		title=f"{description}"
	)
	table.expand = True
	table.add_column("ID", header_style="bright_green", justify="left", style="green")
	table.add_column("API/URL", header_style="bright_yellow", justify="left", style="yellow")
	table.add_column("Privilege request status code", header_style="bright_blue", justify="left", style="blue")
	table.add_column("Normal request status code", header_style="bright_blue", justify="left", style="blue")

	return table

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
				return 'txt'
			elif mime_check(file) == "excel":
				return 'excel'
			else:
				return False
		else:
			return False
	except Exception as e:
		print(e)

def table_warning(file):
	# Create the table display as warning
	table_warning = Table(style="bright_yellow")
	## Add table column
	table_warning.add_column("Using a plain text file", justify="left", style="bold green")
	table_warning.add_column("WARNING", style="bold red3", justify="left")
	## Add table row
	table_warning.add_row(os.path.abspath(file), "Using a plain text file as input file will only trigger GET request test, if the apis also has other method like POST, PUT, ... Using an excel file as input is better!")

	return table_warning
