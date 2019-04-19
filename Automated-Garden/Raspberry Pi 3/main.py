
#!/usr/bin/python

import plant
import temperature as temperature
import MySQL_Upload as sql

import time
import datetime

lettuce = plant.Plant(78,68, 18)

f = open("data.txt" , 'a')

try:
	while 1:
	  
	  lettuce.light_switch()
	  lettuce.water_switch()
	  lettuce.ac_switch()
	  
	  print
	  light = lettuce.light_status()
	  print "Light status ",  light
	  # print "Adding light status to txt file. "
	  f.write("%s " %light)
	  print
	  water = lettuce.water_status()
	  print "Water status ", water
	  f.write("%s " %water)
	  print
	  ac = lettuce.ac_status()
	  print "Ac status ", ac
	  f.write("%s " %ac)
	  print
	  temp = lettuce.temp_status()
	  print "Temperature status ", temp
	  f.write("%s " %temp)

	  time_stamp =  datetime.datetime.now()
	  print time_stamp
	  f.write("%s \n" %time_stamp)
	  print
	 # sql.insert_DB(light, water, ac, temp, 1, 10, time_stamp)
  	  time.sleep(5)
  
except KeyboardInterrupt:

	f.close()
	plant.output.clear()
	exit()
