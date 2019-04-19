import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

CLK = 18
MISO = 23
MOSI = 24
CS = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)


#average is the number of polling times to approximate temp.
def temp (number_Temp_Sensors, average, voltage):
	total = 0

	#Calculating mV read from ADC
	#for i in range(average):
	#	values = []
	#	for k in range(number_Temp_Sensors):
	#		values.append(mcp.read_adc(k))
	#	time.sleep(.1)
	#	total += sum(values)
	total = mcp.read_adc(0)
	#total = total / 10
	total_Milli_Volts  = total * (voltage * 1000.0 / 1024.0)


	#Converting from mV to Celsius to Farenheit
	celsius = (total_Milli_Volts - 500) / 10
	farenheit = (celsius) * 1.8 + 32


	#Hardcode an offset for tmp sensor calibration
	return farenheit
