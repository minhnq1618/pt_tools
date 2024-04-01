#!/usr/bin/env python3

import time
import signal
import requests

# Import this tool's module
from src.check_txt import *
from utils.utils import *
from colors.colors import *

# Suppress the warnings from urllib3
from urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

# Load console of rich
from rich.console import Console
console = Console()

# Load the argurments
args = parse_arguments()

def handler(signal, frame):
	print()
	error(R('You pressed "Ctrl + C", Quitting!'))
signal.signal(signal.SIGINT, handler)

def main():
	privilege_token = f"{args.privilege_token}" 
	normal_token = f"{args.normal_token}"
	privilege_cookie = f"{args.privilege_cookie}"
	normal_cookie = f"{args.normal_cookie}"
	file = f"{args.file}"

	# Create the table display as banner
	table_banner = Table(style="bright_yellow")
	## Add table column
	table_banner.add_column("Broken Access Control Check", justify="left", style="bold green")
	table_banner.add_column(datetime.now().ctime().replace(":", "[blink]:[/]"), style="bold red3", justify="left")
	## Add table row
	table_banner.add_row("Author: Minh Nguyen Quang", "Version: 0.1")

	console.print(table_banner)

	if privilege_token and normal_token and file != "None":
		if file_check(file) == "txt":
			console.print(table_warning(file))
			time.sleep(5)
			txt_token_get(privilege_token, normal_token, file)
		elif file_check(file) == "excel":
			print("excel")
		else:
			print(R("File type does not support!") + Y(" OR ") + R("File does not exists!"))
	else:
		error(R("I don't know what to do"))

if __name__ == '__main__':
	main()
