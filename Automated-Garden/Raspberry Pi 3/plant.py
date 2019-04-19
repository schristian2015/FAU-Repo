#!/usr/bin/python

import datetime
import time
import temperature as temperature
import gpio_test as output
import weight as weight

class Plant:
  
  def __init__(self, day_temp, night_temp, water_times):
    self.day_temp = day_temp
    self.night_temp = night_temp
    self.water_times = water_times
    self.light = 1
    self.ac = 0
    self.water = 1
    self.weight = weight.weight()
    
    self.minute = datetime.datetime.now().minute
    self.counter = datetime.datetime.now().hour
    self.temp = temperature.temp(1, 10, 3.3)
    
    #Error checking to confirm plant isn't over watered
    if (self.water_times > 18):
      print "Error too many watering times"
      self.water_times = 18
    
    self.water_shift = 18 / self.water_times
    
    output.light(self.light)
    output.water(self.water)
    output.ac(self.ac)

  #Confirms light is only on after 6 am or any variable that can be added to the class
  def light_switch(self):
    now = datetime.datetime.now()
    light_Start = now.replace(hour = 6, minute = 0, second = 0, microsecond = 0)
    if (now < light_Start):
      self.light = 0
    else:
      self.light = 1
    output.light(self.light)
  
  #Water will turn on when light is on, once water time is over will check for next watering time
  def water_switch(self):
    now = datetime.datetime.now()
    water_start = now.replace(hour = self.counter, minute = self.minute, second = 0, microsecond = 0)
    
    #Error checking if start time has overlap of minutes to next hour
    if (self.minute + 5 >= 60):
	if (self.counter + 1 > 23):
		water_end = now.replace(hour = 0, minute = self.minute + -55, second = 0, microsecond = 0)
	else:
      		water_end = now.replace(hour = self.counter + 1, minute = self.minute + -55, second = 0, microsecond = 0)
    else:
      water_end = now.replace(hour = self.counter, minute = self.minute + 5, second = 0, microsecond = 0)
      
    
    #Stops datetime hour from going above 23.
    hour_overlap_prevention = self.counter + self.water_shift
    if (hour_overlap_prevention  > 23):
      
      hour_overlap_prevention = hour_overlap_prevention - 23

    #Turns water on for set time.
    if ((water_start < now and water_end > now) and self.light == 1):
      self.water = 1

    #Keeps water off until next watering cycle
    elif ((water_end < now) and water_start.replace(hour = hour_overlap_prevention, minute = self.minute, second = 0, microsecond = 0) > now):
      self.water = 0
    
    #updates the counter to prepare for next watering cycle
    elif (self.light == 1):
      self.counter+=self.water_shift
      if (self.counter >= 24):
        self.counter = 6
    
    else:
      self.water = 0
    
    output.water(self.water)
  #def check_temp(self):
  
  
  
  def ac_switch(self):

    self.temp = temperature.temp(1, 10, 3.3)

    #temp is above day_temp
    if (self.light == 1 and (self.temp > self.day_temp + 2)):
      self.ac = 1
    
    elif (self.light == 1 and self.temp < self.day_temp - 2):
      self.ac = 2
    
    elif (self.light == 0 and self.temp > self.night_temp + 2):
      self.ac = 1
    
    elif (self.light == 0 and self.temp < self.night_temp - 2):
      self.ac = 2
    
    else:
      self.ac = 0
      
    output.ac(self.ac)

  def light_status(self):
    return self.light
    
  def water_status(self):
    return self.water
  
  def ac_status(self):
    return self.ac

  def temp_status(self):
    return format(self.temp, '.2f')

