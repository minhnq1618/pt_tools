import time
import requests

from utils.utils import *
from colors.colors import *

from datetime import datetime

# Import rich module for progress display
from rich.table import Table
from rich.console import Console
from rich.progress import Progress

# Load console of rich
console = Console()

def txt_token_get(privilege_token, normal_token, file):
	fl = open(f"{file}", "r", encoding='latin-1')
	l = len(fl.readlines())
	print(G("\n[!] ") + C("Total number of apis: ") + Y(f"{l}\n"))
	with Progress() as progress:
		task = progress.add_task("[bold green]Checking for BAC vuln in the apis ...", total=l)

		table_1 = create_rich_table("BAC vuln in these apis")
		table_2 = create_rich_table("No BAC vuln in these apis")
		table_3 = create_rich_table("Possible BAC vuln or maybe something else in these apis")

		count_1 = 0
		count_2 = 0
		count_3 = 0

		while not progress.finished:
			f = open(f"{file}", "r", encoding='latin-1')
			for line in f:
				## Request using privilege token
				headers_priv = {
				    'Authorization': f'Bearer {privilege_token}'
				}
				
				priv_req = requests.get(
				    f'{line}',
				    headers=headers_priv,
				    verify=False,
				)

				## Request using normal token
				headers_norm = {
				    'Authorization': f'Bearer {normal_token}'
				}

				norm_req = requests.get(
				    f'{line}',
				    headers=headers_norm,
				    verify=False,
				)

				a = priv_req.status_code
				b = norm_req.status_code

				if a == b == 200:
					count_1 += 1
					table_1.add_row(f"{count_1}", f"{line}", f"{a}", f"{b}", end_section=True)
					progress.update(task, advance=1)
					time.sleep(0.02)
				elif a == 200 and b == 403:
					count_2 += 1
					table_2.add_row(f"{count_2}", f"{line}", f"{a}", f"{b}", end_section=True)
					progress.update(task, advance=1)
					time.sleep(0.02)
				else:
					count_3 += 1
					table_3.add_row(f"{count_3}", f"{line}", f"{a}", f"{b}", end_section=True)
					progress.update(task, advance=1)
					time.sleep(0.02)

	console.print(table_1)
	console.print(table_2)
	console.print(table_3)
