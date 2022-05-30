import face_recognition
import cv2
import Jetson.GPIO as gpio
import time
import numpy as np

light = 18
HIGH = 1
LOW = 0

gpio.setwarnings (False)
gpio.setmode (gpio.BCM)

gpio.setup(light, gpio.OUT)
gpio.output(light, HIGH)


# Start the camera - 0 for laptop camera
# Write the camera address inside captura.open() for ip camera and leave the first one empty
capture = cv2.VideoCapture()
capture.open('')


# Read the image
example_image = cv2.imread("/home/example/images/ex.png")
rgb_example = cv2.cvtColor(example_image, cv2.COLOR_BGR2RGB)


img_encoding = face_recognition.face_encodings(rgb_example)[0]


# Creating name database
known_encodings = [
	img_encoding
	
	]
	
	
known_names = [
	"NAME SURNAME"
	
	]
		
while True:

	while True:
    		ret, frame = capture.read()
    		
    		if ret:
        	    break
        	    
	# Resize the captured frame
	resized = cv2.resize(frame, (0,0), fx=0.2, fy=0.2)
	rgb_resized = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)

	# Find all faces
	faces = face_recognition.face_locations(rgb_resized)
	
	# Get the face encodins to compare
	encodings = face_recognition.face_encodings(rgb_resized, faces)

	face_names = []
        

	for face_encoding in encodings:
	
		# If there is no matched face, name it "UNKNOWN PERSON"
		match = face_recognition.compare_faces(known_encodings, face_encoding)
		name = "UNKNOWN PERSON"

		# If there more than one person at the door, just use the first match.
		if True in match:
		
	    		first = match.index(True)
	    		name = known_names[first]
	    		gpio.output(light, LOW)
	    		time.sleep(1)
	    		gpio.output(light, HIGH)
	    		time.sleep(1)

		face_names.append(name)


	for location in faces:
	
		top = location[0]
		right = location[1]
		bottom = location[2]
		left = location[3]
		
		# Now resize the frame again to it's original size
		top *= 5
		right *= 5
		bottom *= 5
		left *= 5
		
	
		cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0),2)
		cv2.putText(frame, name,(left, top - 15), cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 255, 0), 2)


	cv2.imshow("Frame", frame)
	
	# Press 'q' if you want to quit
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

gpio.cleanup()
capture.release()
cv2.destroyAllWindows()