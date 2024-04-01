import pandas as pd
file_location = "try.xlsx"
sheet = pd.read_excel(file_location)
a = sheet['URL']
b = sheet['Method']

c = a.map(str) + " " +  b.map(str)
for d in c:
	e = list(d.split(" "))
	method = e[1]
	if method == "GET":
		print(e[0])
		print(e[1] + "\n")
