import sys
import os
from functions import *
from crc import crcheck
import folium
import webbrowser

if len(sys.argv) != 2:
    print("Usage: python drawDefault.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

fhandle = open(filename)

map_center = [0, 0]  # Начальные координаты центра карты
my_map = folium.Map(location=map_center, zoom_start=2)  # Зум по умолчанию

latitude_val = 0
longitude_val = 0

while True:
    
    line1 = fhandle.readline().strip()
    line2 = fhandle.readline().strip()
    
    line1 = line1.replace(';', '').replace('*', '')
    line2 = line2.replace(';', '').replace('*', '')
    
    if not line2: break  # EOF

    frame_1 = hexToDec(line1[8:22])[21]
    frame_2 = hexToDec(line2[8:22])[21]
    frame_1_1 = hexToDec(line1[8:22])
    frame_2_2 = hexToDec(line2[8:22])

    bin_alt = frame_2_2[8:20]
    
    if(frame_1 != frame_2):
        if(frame_2 == "1"):
            bin_lat_odd = frame_2_2[22:39]
            bin_lat_even = frame_1_1[22:39]
            bin_long_even = frame_1_1[39:]
            bin_long_odd = frame_2_2[39:]
            try:
                crcheck(line1)
            except Exception as e:
                continue;
            try:
                crcheck(line2)
            except Exception as e:
                continue;
                
            latitude_val = latitude(bin_lat_even, bin_lat_odd, 1, 0)
            longitude_val = longitude(bin_lat_even, bin_lat_odd, bin_long_even, bin_long_odd, 1, 0, latitude_val)

            if(latitude_val < 49.29899 or latitude_val > 54.29899):
                continue;
            if(longitude_val < 14.24712 or longitude_val > 23.89251):
                continue;
            
            print("ICAO", line1[2:7])
            print("latitude:", latitude(bin_lat_even, bin_lat_odd, 0, 1))
            print("longitude:", longitude(bin_lat_even, bin_lat_odd, bin_long_even, bin_long_odd, 0, 1, latitude(bin_lat_even, bin_lat_odd, 0, 1)))
            print("Altitude:",altitude(bin_alt),"ft OR", (altitude(bin_alt)*0.3048),"m")

            
            marker_text = f"ICAO: {line1[2:7]}, Altitude: {altitude(bin_alt)} ft"
            folium.Marker(location=[latitude_val, longitude_val], popup=marker_text).add_to(my_map)
            
            
        elif(frame_2 == "0"):
            bin_lat_odd = frame_1_1[22:39]
            bin_lat_even = frame_2_2[22:39]
            bin_long_even = frame_2_2[39:]
            bin_long_odd = frame_1_1[39:]

            try:
                crcheck(line1)
            except Exception as e:
                continue;
            try:
                crcheck(line2)
            except Exception as e:
                continue;
                
            latitude_val = latitude(bin_lat_even, bin_lat_odd, 1, 0)
            longitude_val = longitude(bin_lat_even, bin_lat_odd, bin_long_even, bin_long_odd, 1, 0, latitude_val)

            if(latitude_val < 49.29899 or latitude_val > 54.29899):
                continue;
            if(longitude_val < 14.24712 or longitude_val > 23.89251):
                continue;
            
            print("ICAO", line1[2:7])
            print("latitude:", latitude(bin_lat_even, bin_lat_odd, 1, 0))
            print("longitude:", longitude(bin_lat_even, bin_lat_odd, bin_long_even, bin_long_odd, 1, 0, latitude(bin_lat_even, bin_lat_odd, 1, 0)))
            print("Altitude:",altitude(bin_alt),"ft OR", (altitude(bin_alt)*0.3048),"m")

            
            marker_text = f"ICAO: {line1[2:7]}, Altitude: {altitude(bin_alt)} ft"
            folium.Marker(location=[latitude_val, longitude_val], popup=marker_text).add_to(my_map)


        print()
fhandle.close()
my_map.save("map.html")

script_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_directory, 'map.html')

webbrowser.open('file://' + file_path, new=2)
