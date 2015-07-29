from map.models import ShipmentMasterLatLon, Warehouses
import csv



customer = []
all_customers = ShipmentMasterLatLon.objects.filter(overlap=0, dest_lon__isnull=False, origin_lon__isnull=False).values('custname' ).distinct()
for each in all_customers: 
	cust_name = str(each['custname'])
	customer.append(cust_name) 

with open('customer_directory.csv', 'wb') as csvfile: 
	infowriter = csv.writer(csvfile, delimiter=',', lineterminator="\n")
	for each in customer: 
		instance = ShipmentMasterLatLon.objects.filter(overlap=0, dest_lon__isnull=False, origin_lon__isnull=False, custname = each)
		for indiv in instance:
			o_city = indiv.origin_std_city
			o_state = indiv.origin_std_state
			o_lat = indiv.origin_lat 
			o_lon = indiv.origin_lon 
			dest_city = indiv.dest_std_city
			dest_state = indiv.dest_std_state
			dest_lat = indiv.dest_lat 
			dest_lon = indiv.dest_lon 
			infowriter.writerow([each, o_city, o_state, o_lat, o_lon, dest_city, dest_state, dest_lat, dest_lon, indiv.weight])


				
