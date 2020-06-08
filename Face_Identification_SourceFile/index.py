import os
import pymysql
import numpy as np
import cv2
from PIL import Image
conn=pymysql.connect(host="localhost",user="root",passwd="",db="face_identification")
myCursor=conn.cursor()
def fetch(id):
    sql="SELECT * FROM user_data WHERE iD='"+str(id)+"'"
    result=myCursor.execute(sql)
    rows=myCursor.fetchall()
    for i in rows:
        profile=i
    return profile
def insert(mail_id,Name):
    sql="SELECT * FROM user_data WHERE id='"+str(mail_id)+"'"
    result=myCursor.execute(sql)
    count=len(myCursor.fetchall())
    conn.commit()
    if count==0:
        sqla="INSERT INTO user_data (Name,Email_Address) VALUES('"+str(Name)+"','"+str(mail_id)+"')"
        resulta=myCursor.execute(sqla)
        conn.commit()
        if resulta:
            sqla="SELECT * FROM user_data WHERE Email_Address='"+str(mail_id)+"'"
            resulta=myCursor.execute(sqla)
            rows=myCursor.fetchall()
            print("Wait For 2 minute")
            for row in rows:
                return row[0]
    else:
        print("Account Exist")
        return 0
    conn.commit()
    conn.close()
def login():
    print("Welcome..!!!")
    faceDetect = cv2.CascadeClassifier('data/haarcascade_frontalface_alt2.xml')
    cam = cv2.VideoCapture(0)
    rec=cv2.createLBPHFaceRecognizer();
    rec.load("trainingData.yml")
    font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,1,1,0,1)
    id=0
    while(True):
        ret, img = cam.read()
        if ret is True:
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces=faceDetect.detectMultiScale(gray,1.3,5);
            conf=0
            for(x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
                id,conf=rec.predict(gray[y:y+h,x:x+w])
            if conf < 80 and id:
                profile=fetch(id)
                cv2.cv.PutText(cv2.cv.fromarray(img),"Id",(0,20),font,(0,0,255));
                cv2.cv.PutText(cv2.cv.fromarray(img),": "+str(profile[0]),(70,20),font,(0,0,255));
                cv2.cv.PutText(cv2.cv.fromarray(img),"Name",(0,50),font,(0,0,255));
                cv2.cv.PutText(cv2.cv.fromarray(img),": "+str(profile[1]),(70,50),font,(0,0,255));
                cv2.cv.PutText(cv2.cv.fromarray(img),"Email",(0,80),font,(0,0,255));
                cv2.cv.PutText(cv2.cv.fromarray(img),": "+str(profile[2]),(70,80),font,(0,0,255));
            cv2.imshow('Login Window',img);
            if (cv2.waitKey(1))==ord('q'):
                cam.release()
                cv2.destroyAllWindows()
def registration():
    faceDetect = cv2.CascadeClassifier('data/haarcascade_frontalface_alt2.xml')
    cam = cv2.VideoCapture(0)
    name=raw_input('Enter Your Name')
    mail_id=raw_input('Enter Your Email-address')
    id=insert(mail_id,name)
    if id>0:
        sampleNum=0
        while(True):
            ret, img = cam.read()
            if ret is True:
                gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces=faceDetect.detectMultiScale(gray,1.3,5);
                for(x,y,w,h) in faces:
                    sampleNum+=1;
                    cv2.imwrite("dataSet/User."+str(id)+"."+str(sampleNum)+".jpg",gray[y:y+h,x:x+w])
                    cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)
                    cv2.waitKey(100);
                cv2.imshow('Registration Window',img);
                cv2.waitKey(1);
                if(sampleNum>20):
                    break
        recognizer=cv2.createLBPHFaceRecognizer();
        path='dataset'
        def getImagesWithId(path):
            imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
            faces=[]
            Ids=[]
            for imagePath in imagePaths:
                faceImg=Image.open(imagePath).convert('L');
                faceNp=np.array(faceImg,'uint8')
                Id=int(os.path.split(imagePath)[-1].split(".")[1])
                faces.append(faceNp)
                Ids.append(Id)
                cv2.waitKey(10)
            return np.array(Ids),faces
        Ids,faces=getImagesWithId(path);
        recognizer.train(faces,Ids)
        recognizer.save('trainingData.yml')
        faceDetect = cv2.CascadeClassifier('data/haarcascade_frontalface_alt2.xml')
        print("New Record inserted")
        cam.release()
        cv2.destroyAllWindows()
faceDetect = cv2.CascadeClassifier('data/haarcascade_frontalface_alt2.xml')
cam = cv2.VideoCapture(0)
rec=cv2.createLBPHFaceRecognizer();
rec.load("trainingData.yml")
font=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,1,1,0,1)
font2=cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL,1,1,0,1)
while(True):
    ret, img = cam.read()
    flag=0
    if ret is True:
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces=faceDetect.detectMultiScale(gray,1.3,5);
        for(x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            id,conf=rec.predict(gray[y:y+h,x:x+w])
            if conf < 50 and id and conf >0:
                if (x,y,w,h):
                    login()
                elif (cv2.waitKey(1))==ord('q'):
                    cam.release()
                    cv2.destroyAllWindows()
                else:
                    cv2.rectangle(img,(100,200),(550,320),(255,0,0),-1)
                    cv2.cv.PutText(cv2.cv.fromarray(img),"Are you sure",(235,220),font,(0,0,255));
                    cv2.cv.PutText(cv2.cv.fromarray(img),"You want to registration?",(165,250),font,(0,0,255));
                    cv2.rectangle(img,(170,270),(300,315),(255,255,0),-1)
                    cv2.cv.PutText(cv2.cv.fromarray(img),"Yes",(215,288),font2,(0,0,255));
                    cv2.cv.PutText(cv2.cv.fromarray(img),"(Press y)",(177,309),font2,(0,0,255));
                    cv2.rectangle(img,(345,270),(475,315),(255,255,0),-1)
                    cv2.cv.PutText(cv2.cv.fromarray(img),"No",(390,288),font2,(0,0,255));
                    cv2.cv.PutText(cv2.cv.fromarray(img),"(Press n)",(352,309),font2,(0,0,255));
                    flag=1
            else:
                cv2.rectangle(img,(100,200),(550,320),(255,0,0),-1)
                cv2.cv.PutText(cv2.cv.fromarray(img),"Are you sure",(235,220),font,(0,0,255));
                cv2.cv.PutText(cv2.cv.fromarray(img),"You want to registration?",(165,250),font,(0,0,255));
                cv2.rectangle(img,(170,270),(300,315),(255,255,0),-1)
                cv2.cv.PutText(cv2.cv.fromarray(img),"Yes",(215,288),font2,(0,0,255));
                cv2.cv.PutText(cv2.cv.fromarray(img),"(Press y)",(177,309),font2,(0,0,255));
                cv2.rectangle(img,(345,270),(475,315),(255,255,0),-1)
                cv2.cv.PutText(cv2.cv.fromarray(img),"No",(390,288),font2,(0,0,255));
                cv2.cv.PutText(cv2.cv.fromarray(img),"(Press n)",(352,309),font2,(0,0,255));
                flag=1
    else:
        continue
    cv2.imshow('Face Detection Window',img);
    if flag==1:
        if (cv2.waitKey(1))==ord('n'):
            cam.release()
            cv2.destroyAllWindows()
        elif (cv2.waitKey(1))==ord('y'):
            registration()
    if (cv2.waitKey(1))==ord('q'):
        cam.release()
        cv2.destroyAllWindows()
