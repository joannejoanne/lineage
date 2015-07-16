import csv
with open("destination_data.csv", 'rw') as input, open('temp2.csv', 'w') as output:
	reader = csv.reader(input, delimiter = ',')
	writer = csv.writer(output, delimiter = ',')
	
	all_list = []
	for rec in reader:
		                     
		rec.append(0)
		all_list.append(rec) 
	writer.writerows(all_list)