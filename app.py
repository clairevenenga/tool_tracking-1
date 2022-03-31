import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import sys

cred = credentials.Certificate("/home/pi/tool_tracking-1/capstone-spring-2022-firebase-adminsdk-34g5n-2a374ce7f2.json")
firebase_admin.initialize_app(cred, {
    'databaseURL':'https://capstone-spring-2022-default-rtdb.firebaseio.com'   
})

ref = db.reference('')
ref.update({'tool_a1':sys.argv[1]})