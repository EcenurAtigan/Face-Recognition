# Face-Recognition

I made a face recognition system that will only allow the entry and exit of the known people and limit the rest for my graduation project.

All technologies and programming languages that I use in my project are OpenCV, Python, Dlib library, Face recognition libraries, Linux operating system, Virtualbox, Nvidia Jetson Nano. And several electronic circuit components such as; led, breadboard, relay, battery and resistor.

<h2> How Does It Work </h2>

-	First of all, the photos of the people to be recognized will be uploaded, then the face encoding and name database will be created within the code.

-	Later, when the camera at the door detect the faces, it will compare the face encoding in the frame that receives, with the face encoding in the database.

-	If there is a match, a name defined for that person will be written from the name database by placing a box around the persons face and the door will be open for a certain period of time.

-	However, if no match is found, the persons face will be framed again and this time "UNKNOWN PERSON" writing will appear. There will be no movement at the door.

-	If there is more than one person at the door and one or more of them is registered, the door will open after the person whose face matches first. No time will be spent making other matches to avoid time issues.
