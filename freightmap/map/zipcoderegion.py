from map.models import ShipmentMasterLatLon, Warehouses
import csv


response = HttpResponse(content_type='text/csv')
response['Content-Disposition'] = 'attachment; filename="zipcode_2digit.csv"'
writer = csv.writer(response)

writer.writerow(['zip', 'location', 'destination', 'weight', 'volume', 'latitude', 'longitude', 'lineage'])
# all_objs = ShipmentMasterLatLon.objects.filter(overlap=0, dest_lon__isnull=False, origin_lon__isnull=False)
for each in [1, 2, 3, 3]: 
	# iata = each.origin_coord_name
	# name = 'Origin-' + each.origin_std_city + '-' + each.origin_std_state 
	# state = each.origin_std_state
	# country = 'USA'
	# latitude = each.origin_lat
	# longitude = each.origin_lon  
	# lineage = 1
	writer.writerow("hi!!")
return response	
