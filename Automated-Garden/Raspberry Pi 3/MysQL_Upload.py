#!/usr/bin/python

import MySQLdb
import plant as plant

MySQL_Host = "localhost"
MySQL_User = "--Username--"
MySQL_Pass = "--password--"
MySQL_DB = "Plant_DB"


def insert_DB(light_status, water_status, ac_status, temp_status, water_level_status, weight_status, time_stamp):

	db = MySQLdb.connect(host = MySQL_Host, user = MySQL_User, passwd = MySQL_Pass, db = MySQL_DB)

	cur = db.cursor()

	cur.execute("Create table if not exists Plant_DB(light_status varchar(1), water_status varchar(1), ac_status varchar(1), temp_status varchar(3), water_level_status varchar(4), weight_status varchar(10),time_stamp varchar(26), PRIMARY KEY (time_stamp))")


	add_entry = ("Insert into %s (light_status, water_status, ac_status, temp_status, water_level_status, weight_status, time_stamp) values(%s, %s, %s, %s, %s, %s, %s)")
	entry_data = (light_status, water_status, ac_status, temp_status, water_level_status, weight_status, time_stamp)

	cur.execute(add_entry, entry_data)
	db.close()
