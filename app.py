import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import json
import serial
import string
import sys
import time

# Match credentials with JSON file from Firebase database
cred = credentials.Certificate("/home/pi/tool_tracking-1/capstone-spring-2022-firebase-adminsdk-34g5n-a596aac5a0.json")

# Initialize SDK with Firebase database
firebase_admin.initialize_app(cred, {
    'databaseURL':'https://capstone-spring-2022-default-rtdb.firebaseio.com'   
})

# Establish reference to Firebase database
ref = db.reference('')

# Open serial port
ser = serial.Serial('/dev/ttyACM0',115200)

while True:
    # Determine hard-coded tool labeling based upon serial data
    serial_data = ser.readline()[:-2]
    if str(serial_data) == "b'E2801160600002136008F2C8'":
        serial_data = "tool_a1"
    elif str(serial_data) == "b'E2801160600002136008C0B8'":
        serial_data = "tool_b1"
    elif str(serial_data) == "b'E2801160600002136008F2A8'":
        serial_data = "tool_c1"

    # Declare variables for timing and tool dictionary
    curr_time = time.time()
    print("current time: ")
    print(curr_time)
    #week = datetime.timedelta(days = 7)
    tool_dict = ref.get()
    print("tool_dict: ")
    print(tool_dict)

    # Enumerate dictionary to access tools
    for tool, index in enumerate(tool_dict):
        #if not isinstance(tool, dict):
        #    continue
        #print(serial_data, tool, tool_dict[index], tool_dict[index].get('status'), tool_dict[index].get('time'))
        # Limit number of times the RFID tag is read
        if float(tool_dict[index].get('time')) + 5 < time.time() and serial_data == index:
            print(serial_data)
            # If tool is scanned while "Available" then update as "unavailable"
            if tool_dict[index].get('status') == 'Available':
                ref.update({index:{'status': 'Unavailable', 'time':str(curr_time)}})
            # If tool is scanned while "Unavailable" and 7 days passed then update as "missing"
            #if tool_dict[index].get('status') == 'Unavailable' and tool_dict[index].get('time') >= str(curr_time - week):
            #    ref.update({index:{'status': 'missing'}})
            # If tool is scanned while "Unavailable" then update as "Available"
            elif tool_dict[index].get('status') == 'Unavailable':
                ref.update({index:{'status':'Available', 'time': str(curr_time)}})
