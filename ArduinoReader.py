
import serial
import db_connector as db

def insert_hr_data(number):
	try:
			# set up the serial line
			# set up serial port
			# set up timeout
		ser = serial.Serial('/dev/ttyS3',9600, timeout = 2)	
			#show the data
			#get data from serial port:
		while True:
			data = (str(ser.readline().decode("utf-8"))).strip()	
			if data:
				print(data)
				#print(len(data))
				db.insert_hr(number,data)			
		     
			
	except Exception as ex:
		print(ex)

# si quieren probar la lectura del puerto serial desactivar la linea 22
if __name__ == "__main__":
	insert_hr_data("6576")
