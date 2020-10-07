<h1 align="center"> <b>FaceIdentification_With_Database</b> </h1>  

Hello,</br>Face identification algorithms focus on the identifiction of frontal human faces. It is analogous to image detection in which the image of a person is matched bit by bit. Image matches with the image stores in database. Any facial feature changes in the database will invalidate the matching process. It's mostly used for the security.

<h3 align="center"> <b>Which technology is used …???</b> </h3>  

-	Python

<h3 align="center"> <b>What is requirement …???</b> </h3>    

-	<b>Software Requirement</b>  
            i] Python v2.7 IDLE  
           ii] Text Editor or Python IDE [eg Eg Notepad++,Anaconda]  
-	<b>Package Requirement</b>  
		        i] OpenCv 	[For Image Processing]  
           ii] Pymysql 	[For Database]  
          iii] Numpy  
           iv] Pillow

<h3 align="center"> <b>How to Install the Software …???</b> </h3>  

-	<b>Python 2.7:-</b>  
	32-bit:  
	https://www.python.org/ftp/python/2.7/python-2.7.msi  
	64-bit:  
	https://www.python.org/ftp/python/2.7/python-2.7.amd64.msi  
-	<b>Package Installation</b>  
		```Open Command Prompt Window [go Start menu > search cmd > open]```</br>
    ```>>cd C:\Python27\Scripts\pip install opencv-python```</br>
    ```>>cd C:\Python27\Scripts\pip install pymysql```</br>
    ```>>cd C:\Python27\Scripts\pip install numpy```</br>
    ```>>cd C:\Python27\Scripts\pip install pillow```</br>

<h3 align="center"> <b>How to import the Database …???</b> </h3></br>

- <b>Start the XAMPP Server</b>  
-	Open Browser/<b>Search :-localhost/phpmyadmin</b>/Create New Database/Database name :- face_identification  
<b>Note:-</b> If you are renaming the databse,please rename the database to Face_Identification_SourceFile/index.py file otherwise there will be an error.
```
conn=pymysql.connect(host="localhost",user="root",passwd="",db="face_identification") /* db="Database Name"*/
```
- Import Sql Table file  
<b>Path:-</b>Database/Database.sql

<h3 align="center"> <b>How to run the Project …???</b> </h3>  

-	<b>Path</b>  
			Face_Identification_SourceFile/index.py.

-	<b>Note:-</b>  
			XAMPP Server must be start</br>
       i] Press 'q' for Quit.</br>
			ii] Press 'y' for Yes.</br>
     iii] Press 'n' for No. </br>
                                                    
<h3 align="center"> <b>SnapShot of the pages…!!!</b> </h3>  

![picture alt](/SnapShot/First_Time_User.png "First_Time_User")
![picture alt](/SnapShot/Secound_Time_User.png "Secound_Time_User")

<h3 align="center"> <b>Copyright & Powered By</b> </h3>
<p align="right"><b>Smit Shah</br>smitshah22050602@gmail.com</br>8849364239</br></b></p>

<h3 align="center"> <b>Thank You..!!! :)</b> </h3>
