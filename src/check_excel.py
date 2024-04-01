import time
import requests

import pandas as pd

from utils.utils import *
from colors.colors import *

from datetime import datetime

# Import rich module for progress display
from rich.table import Table
from rich.console import Console
from rich.progress import Progress

# Load console of rich
console = Console()

def excel_token_check(privilege_token, normal_token, file, method):
	