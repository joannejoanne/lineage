from map.models import ShipmentMasterLatLon, Warehouses
import csv
from django.db.models import Sum


with open('REAL_zipcodelistorigin.csv', 'wb') as csvfile: 
	zipcodewriter = csv.writer(csvfile, delimiter=',', lineterminator="\n")
	zipcodewriter.writerow(['zipcoderegion', 'weight', 'totalcube', 'origin'])

	
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
	
