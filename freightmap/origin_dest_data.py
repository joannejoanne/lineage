from map.models import ShipmentMasterLatLon, Warehouses
import csv
from django.db.models import Sum


	
	all_objs = ShipmentMasterLatLon.objects.filter(overlap=0, dest_lon__isnull=False, origin_lon__isnull=False)
	for each in all_objs: 
		iata = each.origin_coord_name
		name = 'Origin-' + each.origin_std_city + '-' + each.origin_std_state 
		state = each.origin_std_state
		country = 'USA'
		latitude = each.origin_lat
		longitude = each.origin_lon  
		lineage = 1
		zipregion = each.originzip[:2]
		writer.writerow([iata, name, state, country, latitude, longitude, lineage, zipregion])
	return response	

with open('FULLREAL_ORIGIN.csv', 'wb') as csvfile: 
	infowriter = csv.writer(csvfile, delimiter=',', lineterminator="\n")
	infowriter.writerow(['iata', 'name', 'state', 'country', 'latitude', 'longitude', 'lineage', 'zipregion'])
	all_objs = ShipmentMasterLatLon.objects.filter(overlap=0, dest_lon__isnull=False, origin_lon__isnull=False)

	
	adam = ShipmentMasterLatLon.objects.all().values_list('originzip').distinct()

	zipcodemasterlist = []
	for each in adam: 
		newzip = each[0][:2]
		if newzip not in zipcodemasterlist: 
			zipcodemasterlist.append(newzip)

	for each in zipcodemasterlist: 
		zipcoderegion = each
		weight = ShipmentMasterLatLon.objects.filter(overlap=0, dest_lon__isnull=False, origin_lon__isnull=False, originzip__startswith=zipcoderegion).aggregate(Sum('weight'))
		totalcube = ShipmentMasterLatLon.objects.filter(overlap=0, dest_lon__isnull=False, origin_lon__isnull=False, originzip__startswith=zipcoderegion).aggregate(Sum('totalcube'))
		zipcodewriter.writerow([zipcoderegion, weight, totalcube, 1])
	


# with open('REAL_zipcodelistdest.csv', 'wb') as csvfile: 
# 	zipcodewriter = csv.writer(csvfile, delimiter=',', lineterminator="\n")
# 	zipcodewriter.writerow(['zipcoderegion', 'weight', 'totalcube', 'origin'])

	
# 	adam = ShipmentMasterLatLon.objects.all().values_list('destzip').distinct()

# 	zipcodemasterlist = []
# 	for each in adam: 
# 		newzip = each[0][:2]
# 		if newzip not in zipcodemasterlist: 
# 			zipcodemasterlist.append(newzip)

# 	for each in zipcodemasterlist: 
# 		zipcoderegion = each
# 		weight = ShipmentMasterLatLon.objects.filter(overlap=0, dest_lon__isnull=False, origin_lon__isnull=False, destzip__startswith=zipcoderegion).aggregate(Sum('weight'))
# 		totalcube = ShipmentMasterLatLon.objects.filter(overlap=0, dest_lon__isnull=False, origin_lon__isnull=False, destzip__startswith=zipcoderegion).aggregate(Sum('totalcube'))
# 		zipcodewriter.writerow([zipcoderegion, weight, totalcube, 0])
	
