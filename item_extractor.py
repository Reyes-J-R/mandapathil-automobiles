# import PyPDF2

# with open('parts_catalogue.pdf', 'rb') as itemfile:
# 	reader = PyPDF2.PdfFileReader(itemfile)
# 	page1 = reader.getPage(1)
# 	total_text = ""
# 	for n in range(1, reader.numPages):
# 		print(f"Extracting page {n}")
# 		page = reader.getPage(n)
# 		text = page.extractText()
# 		total_text += text
# 	total_lst = total_text.splitlines()
# 	new = []
# 	for item in total_lst:
# 		if item in total_lst[:16]:
# 			continue
# 		if len(item) < 1:
# 			continue
# 		if item[0].isalpha() and ' ' not in item:
# 			continue
# 		if not item[0].isalpha():
# 			continue		
# 		new.append(item)
# 	print(new)
# 	print(f"\n extraction Completed with {len(new)}")

with open("items.txt", 'r') as file:
	items = file.read().split("\n")
	res = []
	for item in items:
		if len(item) > 0:
			if item[0].isnumeric():
				add = " ".join(item.split()[:-1])
				add = " ".join(add.split()[2:])
				res.append(add)

	for item in res:
		for _ in range(res.count(item) - 1):
			res.remove(item)

with open("./Records/items.json", 'w') as file:
	result = "{"
	for index, item in enumerate(res, 1):
		result += f'"{item}": {index},\n'
	result += "}"
	file.write(result)