# import csv
# import json
# import requests
#
# firms_data_url = 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/c6/csv/MODIS_C6_USA_contiguous_and_Hawaii_24h.csv'
# response = requests.get(firms_data_url)
# # text = response.iter_lines()
# with open(response, 'rb') as f:
#     reader = csv.reader(f, delimiter=',')
#     for row in reader:
#         print(row)


import csv
import requests


def get_fire_data():
    V_CSV_URL = 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/viirs/csv/VNP14IMGTDL_NRT_USA_contiguous_and_Hawaii_24h.csv'
    M_CSV_URL = 'https://firms.modaps.eosdis.nasa.gov/data/active_fire/c6/csv/MODIS_C6_USA_contiguous_and_Hawaii_24h.csv'
    list_of_dict = []

    with requests.Session() as s:
        download = s.get(M_CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        # print(my_list[0])
        for row in my_list:
            lat = row[0]
            lng = row[1]
            lat_lng = {'lat':lat, 'lng':lng}
            list_of_dict.append(lat_lng)
        # print(my_list[-1])
    with requests.Session() as s:
        download = s.get(V_CSV_URL)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')
        my_list = list(cr)
        # print(my_list[0])
        for row in my_list[1:]:
            lat = row[0]
            lng = row[1]
            lat_lng = {'lat':lat, 'lng':lng}
            list_of_dict.append(lat_lng)
        # print(my_list[-1])

    return list_of_dict

get_fire_data()
