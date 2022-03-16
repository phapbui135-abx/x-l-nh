import cv2
import numpy as np
import sqlite3
import pyodbc
import os


def read(conn, id):
    print("Read")
    cursor = conn.cursor()
    cursor.execute("Select * from person where ID = " +str(id))
    for row in cursor:
        print(f'row = {row}')
    print()

def create(conn,id, name):
    print("Create")
    a = input("Nhập ID: ")
    b = input("Nhập tên: ")
    cursor = conn.cursor()
    cursor.execute("insert into person(ID,name) values(?,?);",(id,name))
    conn.commit()
    read(conn, id)

def update(conn, id , name):
    print("Update")
    cursor = conn.cursor()
    cursor.execute('update person set name = ? where id = ?;',(id,name))
    conn.commit()
    read(conn, id)

def delete(conn, id):
    print("Delete")
    cursor = conn.cursor()
    cursor.execute('delete from person where id = ?;',(id))
    conn.commit()
    read(conn, id)
def insertOrUpdate(id, name):
    conn = pyodbc.connect(
        "Driver={SQL Server Native Client 11.0};"
        "Server=PHAP\SQLEXPRESS;"
        "Database=people;"
        "Trusted_Connection=yes;"   
    )
    query = "select * from person where id = " + str(id)
    cursor = conn.execute(query)

    isRecordExit = 0
    for row in cursor:
        isRecordExit = 1
    if(isRecordExit == 0):
        create(conn,id, name)
    else:
        update(conn, id, name)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cap = cv2.VideoCapture(0)

id = input("Enter your ID: ")
name = input("Enter your name: ")

insertOrUpdate(id, name)

sampleNum = 0
while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.3,5)
    for(x, y, w, h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        if not os.path.exists('dataSet'):
            os.mkdir('dataSet')
        sampleNum += 1
        cv2.imwrite('dataSet/User.'+str(id)+'.'+str(sampleNum)+'.jpg',gray[y:y+h , x:x+w])
        print(sampleNum)
    cv2.imshow('frame',frame)
    cv2.waitKey(10)

    if sampleNum > 100 :
        break
cap.realease()
cv2.destroyAllWindows()