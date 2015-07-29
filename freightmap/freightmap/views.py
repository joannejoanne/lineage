from django.shortcuts import render_to_response 
from map.models import ShipmentMasterLatLon, Warehouses
from elasticsearch import Elasticsearch
import csv
import os, sys
from django.http import HttpResponse
from geopy.geocoders import Nominatim
from django.db.models import Sum
import ast
import json 


es = Elasticsearch('http://ec2-52-24-92-192.us-west-2.compute.amazonaws.com')



# def zipcode_2digit(request):
# 	response = HttpResponse(content_type='text/csv')
# 	response['Content-Disposition'] = 'attachment; filename="zipcode_2digit.csv"'
# 	writer = csv.writer(response)

# 	writer.writerow(['zip', 'location', 'destination', 'weight', 'volume', 'latitude', 'longitude', 'lineage'])
# 	all_objs = ShipmentMasterLatLon.objects.filter(overlap=0, dest_lon__isnull=False, origin_lon__isnull=False)
# 	for each in all_objs: 
# 		iata = each.origin_coord_name
# 		name = 'Origin-' + each.origin_std_city + '-' + each.origin_std_state 
# 		state = each.origin_std_state
# 		country = 'USA'
# 		latitude = each.origin_lat
# 		longitude = each.origin_lon  
# 		lineage = 1
# 		writer.writerow([iata, name, state, country, latitude, longitude, lineage])
# 	return response	



def sample(request): 
	zipcode = {"93": {"weight": 352, "volume": 12}, "35": {"weight": 112, "volume": 93}}
	return render_to_response('sample.html', {"zipcode": zipcode})
	


def home(request):
	# all_objs = ShipmentMasterLatLon.objects.filter(overlap=0, dest_lon__isnull=False, origin_lon__isnull=False)

	return render_to_response('home.html', {})

def newhome(request):
	# all_objs = ShipmentMasterLatLon.objects.filter(overlap=0, dest_lon__isnull=False, origin_lon__isnull=False)
	
	file = os.path.join(os.path.dirname(os.path.dirname(__file__)),'freightmap/zipcodelist.csv')
	reader = csv.DictReader(open(file))
	zipcodelist = {}
	for row in reader:
		eachloc = {} 
		eachloc["origin"] = row['origin']
		totalcube = ast.literal_eval(row['totalcube'])
		weight = ast.literal_eval(row['weight'])
		eachloc["weight"] = weight['weight__sum']
		eachloc['totalcube'] = totalcube['totalcube__sum']
 		zipcodelist[row['zipcoderegion']] = eachloc 

 	all_origins = ShipmentMasterLatLon.objects.filter(overlap=0, dest_lon__isnull=False, origin_lon__isnull=False).values('origin_std_city' ).distinct()
 	origin_cities = [] 
 	for each in all_origins: 
 		origin_std_city = each['origin_std_city']
 		origin_cities.append(origin_std_city) 

 	all_dest = ShipmentMasterLatLon.objects.filter(overlap=0, dest_lon__isnull=False, origin_lon__isnull=False).values('dest_std_city' ).distinct()
 	destination_cities = [] 
 	for each in all_dest: 
 		dest_std_city = each['dest_std_city']
 		destination_cities.append(dest_std_city) 

 	customer = []
 	all_customers = ShipmentMasterLatLon.objects.filter(overlap=0, dest_lon__isnull=False, origin_lon__isnull=False).values('custname' ).distinct()
 	for each in all_customers: 
 		cust_name = each['custname']
 		customer.append(cust_name) 

 	customer_directory = {}
 	# for each in customer: 
 	# 	instance = ShipmentMasterLatLon.objects.filter(custname = each)
 	# 	customer_directory[each] = instance




 	
 # 	reader = csv.reader(open('zipcodelist.csv', 'r'))
	# zipcodelist = {}
	# for row in reader: 
	# 	zipcodekey, weight, totalcube = row
	# 	eachloc = {}
	# 	eachloc["weight"] = weight
	# 	eachloc["totalcube"] = totalcube 
	# 	zipcodelist[zipcodekey] = eachloc  



	return render_to_response('ELASTIC_SEARCH.html', {'zipcodelist': json.dumps(zipcodelist), 'customer_directory': customer_directory, 'customer': customer, 'destination': destination_cities, 'origin': origin_cities})       
	# return render_to_response('home-zipcode.html', {'zipcodelist': json.dumps(zipcodelist), 'destination': destination_cities, 'origin': origin_cities})
	# return render_to_response('home-NEWEST.html', {'zipcodelist': json.dumps(zipcodelist)})

def home_expanded(request):
	# all_objs = ShipmentMasterLatLon.objects.filter(overlap=0, dest_lon__isnull=False, origin_lon__isnull=False)

	return render_to_response('home-expanded.html', {})


def warehouses(request):
	# all_objs = ShipmentMasterLatLon.objects.filter(overlap=0, dest_lon__isnull=False, origin_lon__isnull=False)
	all_objs = Warehouses.objects.all()
	return render_to_response('warehouses.html', {'data': all_objs})


def warehousemap(request):
	all_objs = Warehouses.objects.all()
# 	geolocator = Nominatim()	
# def adam: 
# 	for each in all_objs: 
# 		location = geolocator.geocode(each.zip)		
# 		latitude = location.latitude
# 		longitude = location.longitude 
# 		print "{'name':" + each.whname + ", 'radius': 14, 'fillKey': 'RUS', latitude': " \
# 			+ str(latitude) + ", 'longitude': " + str(longitude) + ", 'state': " + str(each.state) + \
# 			", 'country': " + str(each.country_code) + ", 'phone': " + str(each.phone) + ", 'id': " + each.whid \
# 			+  ", 'city': " + str(each.city) + ", 'zip': " + each.zip + "}"
#	data = [{'phone': 'None', 'radius': 14, 'id': 'mi_0701', 'city': 'Dodge City', 'name': 'Dodge City', 'zip': '67801', 'country': 'USA', 'longitude': '16.6532530308', 'state': 'None', 'latitude': '49.3629443217', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_0901', 'city': 'Batavia', 'name': 'Batavia', 'zip': '60510', 'country': 'USA', 'longitude': '2.23018736238', 'state': 'None', 'latitude': '49.4533260549', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_1001', 'city': 'South Omaha', 'name': 'South Omaha', 'zip': '68107', 'country': 'USA', 'longitude': '-95.9388199', 'state': 'None', 'latitude': '41.2213239', 'fillKey': 'RUS'}, {'phone': '(804) 236-0690', 'radius': 14, 'id': 'hj_11000', 'city': 'Sandston', 'name': 'Lineage - RCS Airport', 'zip': '23150', 'country': '', 'longitude': '2.01680643224', 'state': 'VA', 'latitude': '46.0845541508', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_1101', 'city': 'Lincoln', 'name': 'Lincoln', 'zip': '68521', 'country': 'USA', 'longitude': '29.039095', 'state': 'None', 'latitude': '46.392005', 'fillKey': 'RUS'}, {'phone': '(804) 232-1266', 'radius': 14, 'id': 'hj_12000', 'city': 'Richmond', 'name': 'Lineage - RCS Southern', 'zip': '23224', 'country': '', 'longitude': '28.2726604', 'state': 'VA', 'latitude': '49.24546925', 'fillKey': 'RUS'}, {'phone': '(804)748-6424', 'radius': 14, 'id': 'hj_14000', 'city': 'Chester', 'name': 'Lineage - RCS Chester', 'zip': '23836', 'country': '', 'longitude': '9.36555514074', 'state': 'VA', 'latitude': '46.0747579955', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_1401', 'city': 'Grand Island', 'name': 'Grand Island', 'zip': '68803', 'country': 'USA', 'longitude': '-98.406564235', 'state': 'None', 'latitude': '40.9397939594', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_1501', 'city': 'Des Moines', 'name': 'Des Moines', 'zip': '50313', 'country': 'USA', 'longitude': '15.692455529', 'state': 'None', 'latitude': '50.2854990718', 'fillKey': 'RUS'}, {'phone': '(478) 997-8888', 'radius': 14, 'id': 'hj_16000', 'city': 'Unadilla', 'name': 'Lineage - FRS Unadilla', 'zip': '31091', 'country': '', 'longitude': '9.74019247968', 'state': 'GA', 'latitude': '51.9824645486', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_1601', 'city': 'Iowa City', 'name': 'Iowa City', 'zip': '52240', 'country': 'USA', 'longitude': '5.50142431164', 'state': 'None', 'latitude': '48.1001758717', 'fillKey': 'RUS'}, {'phone': '(912) 480-9420', 'radius': 14, 'id': 'hj_19000', 'city': 'Rincon', 'name': 'Lineage - FRS Savannah', 'zip': '31326', 'country': '', 'longitude': '27.23202', 'state': 'GA', 'latitude': '49.498555', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_1901', 'city': 'Denison', 'name': 'Denison', 'zip': '51442', 'country': 'USA', 'longitude': '-95.3569707323', 'state': 'None', 'latitude': '42.0260851629', 'fillKey': 'RUS'}, {'phone': '(804)748-0129', 'radius': 14, 'id': 'hj_24000', 'city': 'Chester', 'name': 'Lineage - RCS Supply Chain', 'zip': '23836', 'country': '', 'longitude': '9.36555514074', 'state': 'VA', 'latitude': '46.0747579955', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_2601', 'city': 'El Paso', 'name': 'El Paso', 'zip': '79924', 'country': 'USA', 'longitude': '-106.4089589', 'state': 'None', 'latitude': '31.899384', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_2701', 'city': 'McAllen', 'name': 'McAllen', 'zip': '78503', 'country': 'USA', 'longitude': '-98.2415039', 'state': 'None', 'latitude': '26.188752', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_2801', 'city': 'Greeley', 'name': 'Greeley', 'zip': '80631', 'country': 'USA', 'longitude': '24.9615643', 'state': 'None', 'latitude': '50.0084095', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_3001', 'city': 'West Omaha', 'name': 'West Omaha', 'zip': '68137', 'country': 'USA', 'longitude': '-96.1228355748', 'state': 'None', 'latitude': '41.2059348191', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_3201', 'city': 'Attalla', 'name': 'Attalla', 'zip': '35954', 'country': 'USA', 'longitude': '-86.0915154801', 'state': 'None', 'latitude': '34.0407529795', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_3301', 'city': 'Jackson', 'name': 'Jackson', 'zip': '39218', 'country': 'USA', 'longitude': '11.7457231', 'state': 'None', 'latitude': '52.0105799', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_3501', 'city': 'Kansas City', 'name': 'Kansas City', 'zip': '66111', 'country': 'USA', 'longitude': '7.0008104', 'state': 'None', 'latitude': '49.2357817', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_3601', 'city': 'Friona', 'name': 'Friona', 'zip': '79035', 'country': 'USA', 'longitude': '24.0652406809', 'state': 'None', 'latitude': '49.8148986429', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_3701', 'city': 'Mira Loma', 'name': 'Mira Loma', 'zip': '91752', 'country': 'USA', 'longitude': '-117.541527603', 'state': 'None', 'latitude': '33.9813722428', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_3901', 'city': 'Allentown', 'name': 'Allentown', 'zip': '18106', 'country': 'USA', 'longitude': '21.9175328215', 'state': 'None', 'latitude': '43.3099005421', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_4001', 'city': 'Atlanta', 'name': 'Atlanta', 'zip': '30253', 'country': 'USA', 'longitude': '-84.1745905568', 'state': 'None', 'latitude': '33.4579500397', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_4201', 'city': 'Fort Worth', 'name': 'Fort Worth', 'zip': '76106', 'country': 'USA', 'longitude': '-97.3504745671', 'state': 'None', 'latitude': '32.7982583597', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_4301', 'city': 'Geneva', 'name': 'Geneva', 'zip': '60134', 'country': 'USA', 'longitude': '2.2027769245', 'state': 'None', 'latitude': '49.3740824823', 'fillKey': 'RUS'}, {'phone': '(256) 301-0028', 'radius': 14, 'id': 'hj_45000', 'city': 'Decatur', 'name': 'Lineage - RCS Decatur', 'zip': '35601', 'country': 'USA', 'longitude': '12.6520927539', 'state': 'AL', 'latitude': '50.1750736403', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_4501', 'city': 'Louisville', 'name': 'Louisville', 'zip': '40258', 'country': 'USA', 'longitude': '12.0319255', 'state': 'None', 'latitude': '57.7513732', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_4901', 'city': 'Statesville', 'name': 'Statesville', 'zip': '28625', 'country': 'USA', 'longitude': '32.4658428', 'state': 'None', 'latitude': '47.8104441', 'fillKey': 'RUS'}, {'phone': '(910) 862-7494', 'radius': 14, 'id': 'hj_51000', 'city': 'Tar Heel', 'name': 'Lineage - RCS Tar Heel', 'zip': '28392', 'country': '', 'longitude': '-78.8024248945', 'state': 'NC', 'latitude': '34.7317305061', 'fillKey': 'RUS'}, {'phone': '(757) 357-0434', 'radius': 14, 'id': 'hj_52000', 'city': 'Smithfield', 'name': 'Lineage - RCS Smithfield', 'zip': '23430', 'country': '', 'longitude': '1.59039614521', 'state': 'VA', 'latitude': '45.9864158265', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_5201', 'city': 'Manteca', 'name': 'Manteca', 'zip': '95336', 'country': 'USA', 'longitude': '11.3504862423', 'state': 'None', 'latitude': '50.0949572937', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_5301', 'city': 'Mt Pleasant', 'name': 'Mt Pleasant', 'zip': '52641', 'country': 'USA', 'longitude': '-91.5707760548', 'state': 'None', 'latitude': '40.9661503466', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_5401', 'city': 'Tremonton', 'name': 'Tremonton', 'zip': '84337', 'country': 'USA', 'longitude': '12.8332778656', 'state': 'None', 'latitude': '48.4963772755', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_5501', 'city': 'Sunnyvale', 'name': 'Sunnyvale', 'zip': '75182', 'country': 'USA', 'longitude': '-96.5734635726', 'state': 'None', 'latitude': '32.7992718166', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_5701', 'city': 'Centralia', 'name': 'Centralia', 'zip': '98531', 'country': 'USA', 'longitude': '34.3532489285', 'state': 'None', 'latitude': '44.7045033119', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_6001', 'city': 'Springfield', 'name': 'Springfield', 'zip': '45502', 'country': 'USA', 'longitude': '-83.8302564251', 'state': 'None', 'latitude': '39.9324868828', 'fillKey': 'RUS'}, {'phone': '(757) 451-3211', 'radius': 14, 'id': 'hj_61000', 'city': 'Norfolk', 'name': 'Lineage - RCS Norfolk', 'zip': '23505-1019', 'country': 'USA', 'longitude': '-77.4667', 'state': 'VA', 'latitude': '37.5333', 'fillKey': 'RUS'}, {'phone': '', 'radius': 14, 'id': 'hj_81000', 'city': 'Richmond', 'name': 'Lineage - RCS Chesapeake/Repair', 'zip': '23224', 'country': '', 'longitude': '28.2726604', 'state': 'VA', 'latitude': '49.24546925', 'fillKey': 'RUS'}, {'phone': '(805) 483-2265', 'radius': 14, 'id': 'in_ox_wmwhse1', 'city': 'Oxnard', 'name': 'Lineage - TF Oxnard', 'zip': '93030', 'country': '', 'longitude': '-119.176182421', 'state': 'CA', 'latitude': '34.2101941711', 'fillKey': 'RUS'}, {'phone': '(831) 761-8415', 'radius': 14, 'id': 'in_wat_wmwhse2', 'city': 'Watsonville', 'name': 'Lineage - TF Watsonville', 'zip': '95076', 'country': '', 'longitude': '-121.8107953', 'state': 'CA', 'latitude': '36.8617787', 'fillKey': 'RUS'}, {'phone': '', 'radius': 14, 'id': 'in_sm_wmwhse3', 'city': 'Santa Maria', 'name': 'Lineage - TF Santa Maria', 'zip': '93458', 'country': '', 'longitude': '-120.4333', 'state': 'CA', 'latitude': '34.9514', 'fillKey': 'RUS'}]
	data = [{'phone': 'None', 'radius': 14, 'id': 'mi_0701', 'city': 'Dodge City', 'name': 'Dodge City', 'zip': '67801', 'country': 'USA', 'longitude': '-100.020499', 'state': 'None', 'latitude': '37.7540865', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_0901', 'city': 'Batavia', 'name': 'Batavia', 'zip': '60510', 'country': 'USA', 'longitude': '-88.3074845178', 'state': 'None', 'latitude': '41.8464770966', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_1001', 'city': 'South Omaha', 'name': 'South Omaha', 'zip': '68107', 'country': 'USA', 'longitude': '-95.9388199', 'state': 'None', 'latitude': '41.2213239', 'fillKey': 'RUS'}, {'phone': '(804) 236-0690', 'radius': 14, 'id': 'hj_11000', 'city': 'Sandston', 'name': 'Lineage - RCS Airport', 'zip': '23150', 'country': '', 'longitude': '-77.2680783388', 'state': 'VA', 'latitude': '37.513199106', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_1101', 'city': 'Lincoln', 'name': 'Lincoln', 'zip': '68521', 'country': 'USA', 'longitude': '-96.7102205076', 'state': 'None', 'latitude': '40.8597286531', 'fillKey': 'RUS'}, {'phone': '(804) 232-1266', 'radius': 14, 'id': 'hj_12000', 'city': 'Richmond', 'name': 'Lineage - RCS Southern', 'zip': '23224', 'country': '', 'longitude': '-77.4196229', 'state': 'VA', 'latitude': '37.5194348', 'fillKey': 'RUS'}, {'phone': '(804)748-6424', 'radius': 14, 'id': 'hj_14000', 'city': 'Chester', 'name': 'Lineage - RCS Chester', 'zip': '23836', 'country': '', 'longitude': '-77.3454757964', 'state': 'VA', 'latitude': '37.3431385394', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_1401', 'city': 'Grand Island', 'name': 'Grand Island', 'zip': '68803', 'country': 'USA', 'longitude': '-98.406564235', 'state': 'None', 'latitude': '40.9397939594', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_1501', 'city': 'Des Moines', 'name': 'Des Moines', 'zip': '50313', 'country': 'USA', 'longitude': '-93.6182573091', 'state': 'None', 'latitude': '41.6432055529', 'fillKey': 'RUS'}, {'phone': '(478) 997-8888', 'radius': 14, 'id': 'hj_16000', 'city': 'Unadilla', 'name': 'Lineage - FRS Unadilla', 'zip': '31091', 'country': '', 'longitude': '-83.7129369413', 'state': 'GA', 'latitude': '32.2429981306', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_1601', 'city': 'Iowa City', 'name': 'Iowa City', 'zip': '52240', 'country': 'USA', 'longitude': '-91.5234917529', 'state': 'None', 'latitude': '41.6557030784', 'fillKey': 'RUS'}, {'phone': '(912) 480-9420', 'radius': 14, 'id': 'hj_19000', 'city': 'Rincon', 'name': 'Lineage - FRS Savannah', 'zip': '31326', 'country': '', 'longitude': '-81.2297936579', 'state': 'GA', 'latitude': '32.2989018117', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_1901', 'city': 'Denison', 'name': 'Denison', 'zip': '51442', 'country': 'USA', 'longitude': '-95.3569707323', 'state': 'None', 'latitude': '42.0260851629', 'fillKey': 'RUS'}, {'phone': '(804)748-0129', 'radius': 14, 'id': 'hj_24000', 'city': 'Chester', 'name': 'Lineage - RCS Supply Chain', 'zip': '23836', 'country': '', 'longitude': '-77.3454757964', 'state': 'VA', 'latitude': '37.3431385394', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_2601', 'city': 'El Paso', 'name': 'El Paso', 'zip': '79924', 'country': 'USA', 'longitude': '-106.415333758', 'state': 'None', 'latitude': '31.9013759186', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_2701', 'city': 'McAllen', 'name': 'McAllen', 'zip': '78503', 'country': 'USA', 'longitude': '-98.2466602902', 'state': 'None', 'latitude': '26.1764103949', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_2801', 'city': 'Greeley', 'name': 'Greeley', 'zip': '80631', 'country': 'USA', 'longitude': '-104.692822631', 'state': 'None', 'latitude': '40.4202528407', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_3001', 'city': 'West Omaha', 'name': 'West Omaha', 'zip': '68137', 'country': 'USA', 'longitude': '-96.1228355748', 'state': 'None', 'latitude': '41.2059348191', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_3201', 'city': 'Attalla', 'name': 'Attalla', 'zip': '35954', 'country': 'USA', 'longitude': '-86.0915154801', 'state': 'None', 'latitude': '34.0407529795', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_3301', 'city': 'Jackson', 'name': 'Jackson', 'zip': '39218', 'country': 'USA', 'longitude': '-90.1518922619', 'state': 'None', 'latitude': '32.2167500089', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_3501', 'city': 'Kansas City', 'name': 'Kansas City', 'zip': '66111', 'country': 'USA', 'longitude': '-94.7774710198', 'state': 'None', 'latitude': '39.0835156975', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_3601', 'city': 'Friona', 'name': 'Friona', 'zip': '79035', 'country': 'USA', 'longitude': '-102.732348715', 'state': 'None', 'latitude': '34.6487889087', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_3701', 'city': 'Mira Loma', 'name': 'Mira Loma', 'zip': '91752', 'country': 'USA', 'longitude': '-117.541527603', 'state': 'None', 'latitude': '33.9813722428', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_3901', 'city': 'Allentown', 'name': 'Allentown', 'zip': '18106', 'country': 'USA', 'longitude': '-75.5839155042', 'state': 'None', 'latitude': '40.5702152611', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_4001', 'city': 'Atlanta', 'name': 'Atlanta', 'zip': '30253', 'country': 'USA', 'longitude': '-84.1745905568', 'state': 'None', 'latitude': '33.4579500397', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_4201', 'city': 'Fort Worth', 'name': 'Fort Worth', 'zip': '76106', 'country': 'USA', 'longitude': '-97.3131839', 'state': 'None', 'latitude': '32.822457', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_4301', 'city': 'Geneva', 'name': 'Geneva', 'zip': '60134', 'country': 'USA', 'longitude': '-88.3162560025', 'state': 'None', 'latitude': '41.8856070165', 'fillKey': 'RUS'}, {'phone': '(256) 301-0028', 'radius': 14, 'id': 'hj_45000', 'city': 'Decatur', 'name': 'Lineage - RCS Decatur', 'zip': '35601', 'country': 'USA', 'longitude': '-86.9871647541', 'state': 'AL', 'latitude': '34.5904345271', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_4501', 'city': 'Louisville', 'name': 'Louisville', 'zip': '40258', 'country': 'USA', 'longitude': '-85.8638254247', 'state': 'None', 'latitude': '38.1434353206', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_4901', 'city': 'Statesville', 'name': 'Statesville', 'zip': '28625', 'country': 'USA', 'longitude': '-80.8760189', 'state': 'None', 'latitude': '35.808404', 'fillKey': 'RUS'}, {'phone': '(910) 862-7494', 'radius': 14, 'id': 'hj_51000', 'city': 'Tar Heel', 'name': 'Lineage - RCS Tar Heel', 'zip': '28392', 'country': '', 'longitude': '-78.8035697227', 'state': 'NC', 'latitude': '34.7374606625', 'fillKey': 'RUS'}, {'phone': '(757) 357-0434', 'radius': 14, 'id': 'hj_52000', 'city': 'Smithfield', 'name': 'Lineage - RCS Smithfield', 'zip': '23430', 'country': '', 'longitude': '-76.6469367575', 'state': 'VA', 'latitude': '36.9856515674', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_5201', 'city': 'Manteca', 'name': 'Manteca', 'zip': '95336', 'country': 'USA', 'longitude': '-121.207267498', 'state': 'None', 'latitude': '37.8205683705', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_5301', 'city': 'Mt Pleasant', 'name': 'Mt Pleasant', 'zip': '52641', 'country': 'USA', 'longitude': '-91.5707760548', 'state': 'None', 'latitude': '40.9661503466', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_5401', 'city': 'Tremonton', 'name': 'Tremonton', 'zip': '84337', 'country': 'USA', 'longitude': '-112.191337846', 'state': 'None', 'latitude': '41.703261654', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_5501', 'city': 'Sunnyvale', 'name': 'Sunnyvale', 'zip': '75182', 'country': 'USA', 'longitude': '-96.5599816', 'state': 'None', 'latitude': '32.8285422', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_5701', 'city': 'Centralia', 'name': 'Centralia', 'zip': '98531', 'country': 'USA', 'longitude': '-122.9561766', 'state': 'None', 'latitude': '46.7086457', 'fillKey': 'RUS'}, {'phone': 'None', 'radius': 14, 'id': 'mi_6001', 'city': 'Springfield', 'name': 'Springfield', 'zip': '45502', 'country': 'USA', 'longitude': '-83.8220783414', 'state': 'None', 'latitude': '39.9338893329', 'fillKey': 'RUS'}, {'phone': '(757) 451-3211', 'radius': 14, 'id': 'hj_61000', 'city': 'Norfolk', 'name': 'Lineage - RCS Norfolk', 'zip': '23505-1019', 'country': 'USA', 'longitude': '-76.286386952', 'state': 'VA', 'latitude': '36.9143688577', 'fillKey': 'RUS'}, {'phone': '', 'radius': 14, 'id': 'hj_81000', 'city': 'Richmond', 'name': 'Lineage - RCS Chesapeake/Repair', 'zip': '23224', 'country': '', 'longitude': '-77.4196229', 'state': 'VA', 'latitude': '37.5194348', 'fillKey': 'RUS'}, {'phone': '(805) 483-2265', 'radius': 14, 'id': 'in_ox_wmwhse1', 'city': 'Oxnard', 'name': 'Lineage - TF Oxnard', 'zip': '93030', 'country': '', 'longitude': '-119.176182421', 'state': 'CA', 'latitude': '34.2101941711', 'fillKey': 'RUS'}, {'phone': '(831) 761-8415', 'radius': 14, 'id': 'in_wat_wmwhse2', 'city': 'Watsonville', 'name': 'Lineage - TF Watsonville', 'zip': '95076', 'country': '', 'longitude': '-121.8107953', 'state': 'CA', 'latitude': '36.8617787', 'fillKey': 'RUS'}, {'phone': '', 'radius': 14, 'id': 'in_sm_wmwhse3', 'city': 'Santa Maria', 'name': 'Lineage - TF Santa Maria', 'zip': '93458', 'country': '', 'longitude': '-120.4376463', 'state': 'CA', 'latitude': '34.9531514', 'fillKey': 'RUS'}]	# data = [{
	#    	"name": 'Joe 4',
	#     "radius": 14,
	#     "latitude": 33.68,
	#     "longitude": -117.79,
	#     "fillKey": 'RUS'
	#   }]


	return render_to_response('warehousemap.html', {'data': data})




def warehouse_init(request): 
	all_objs = Warehouses.objects.all()
	geolocator = Nominatim()	
	adam = [] 
	for each in all_objs: 
		location = geolocator.geocode(each.zip + ", United States")		
		latitude = location.latitude
		longitude = location.longitude
		data = {'name': str(each.whname), 'radius': 14, 'fillKey': 'RUS', 'latitude':  \
			str(latitude), 'longitude': str(longitude), 'state': str(each.state), \
			'country': str(each.country_code), 'phone': str(each.phone), 'id': str(each.whid), \
			'city': str(each.city), 'zip': str(each.zip) }
		adam.append(data)

	return render_to_response('warehouse_init.html', {'data': adam})


def dashboard(request):

	return render_to_response('dashboard.html', {})

def destination(request, code):
	code = code.replace("_"," ").replace("-", ", ")
	dest_city = code.split(", ")[0]
	dest_state = code.split(", ")[1]
	all_objs = ShipmentMasterLatLon.objects.filter(dest_std_city = dest_city, dest_std_state = dest_state) 


	return render_to_response('destination.html', {'title': code, 'all': all_objs})



def origin(request, code):
	code = code.replace("_"," ").replace("-", ", ")
	origin_city = code.split(", ")[0]
	origin_state = code.split(", ")[1]
	all_objs = ShipmentMasterLatLon.objects.filter(origin_std_city = origin_city, origin_std_state = origin_state) 

	return render_to_response('origin.html', {'title': code, 'all': all_objs})


def render(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="realorigin.csv"'
	writer = csv.writer(response)
	writer.writerow(['iata', 'name', 'state', 'country', 'latitude', 'longitude', 'lineage', 'zipregion', 'aggweight', 'aggvolume'])
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

def paths(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="realpaths.csv"'
	writer = csv.writer(response)
	writer.writerow(['origin', 'destination', 'count'])
	all_objs = ShipmentMasterLatLon.objects.filter(overlap=0, dest_lon__isnull=False, origin_lon__isnull=False, origin_coord_name__isnull = False, dest_coord_name__isnull = False)
	for each in all_objs: 
		origin = each.dest_coord_name
		destination = each.origin_coord_name
		count = (each.weight)/20000+.01 
		writer.writerow([origin, destination, count])
	return response	



def get_destinations(request):
	response = HttpResponse(content_type='text/csv')
	response['Content-Disposition'] = 'attachment; filename="realdestination.csv"'
	writer = csv.writer(response)
	writer.writerow(['iata', 'name', 'state', 'country', 'latitude', 'longitude', 'lineage'])
	all_objs = ShipmentMasterLatLon.objects.filter(overlap=0, dest_lon__isnull=False, origin_lon__isnull=False)
	for each in all_objs: 
		iata = each.dest_coord_name
		name = 'Destination-' + each.dest_std_city + '-' + each.dest_std_state 
		state = each.dest_std_state
		country = 'USA'
		latitude = each.dest_lat
		longitude = each.dest_lon  
		lineage = 0
		writer.writerow([iata, name, state, country, latitude, longitude, lineage])
	return response	


