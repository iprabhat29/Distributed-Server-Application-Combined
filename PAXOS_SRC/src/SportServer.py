#!/usr/bin/python
# -*- coding: utf-8 -*-
# ===============================================================================
## Contributors:
#    Prabhat Bhatt
#    Apoorva Saxena
# ===============================================================================

import time
import threading
import socket
from thread import *
from Queue import Queue

# from cache_tst import hash_dic

from xml.sax import default_parser_list
ThreadLock = threading.Lock()
cv = threading.Condition()
import re
import requests
from api import api as api_back
import hash

# from api2 import api as api_f2
# from api1 import api as api_f1

from restart.serving import Service
from random import *
import random
from api import var
import datetime
FEP1_timeDiff = 0
FEP2_timeDiff = 0

# print "API ID--->",bid
# This function creates REST API server for each client which connects

service = Service(api_back)

# service1 = Service(api_f1)
# service2 = Service(api_f2)

fep1TimeDiff = 0
fep2TimeDiff = 0


 # ===============================================================================
 # IMPORTANT !!
 # FEP1 HAS A LOCAL CLOCK WHICH STARTS FROM 1.0000 AND INCREASE AS 1.0001,
 # 1.0002,1.0003...
 # SIMILARLY FEP2 HAS A LOCAL CLOCK WHICH STARTS AT 2.0000 AND FOLLOWS AS 2.0001,
 # 2.0002,...
 # ALOGORITM OF LOGICAL CLOCK SAYS THAT WHEN A MSG IS SENT FROM A SENDER IT
 # SENDS IT LOCAL CLOCK AND THE RECEIVER TICKS ITS CLOCK AND TAKE MAX OF WHAT
 # SENDER SENDS AND ITS OWN CLOCK.
 # FOR EXAMPLE SENDERLC(1.0003)--->RECEIVERLC(2.0004)
 # -------> RECEIVERLC = MAX(1.0003,2.0004) + 0.0001
 # ===============================================================================

def addSecs(tm, secs):
    fulldate = datetime.datetime(
        100,
        1,
        1,
        tm.hour,
        tm.minute,
        tm.second,
        )
    fulldate = fulldate + datetime.timedelta(seconds=secs)
    return fulldate.time()


# ===============================================================================
# THIS MODULE IS RUNNING OUR REST API SERVICE
# ===============================================================================

# ===============================================================================
# URL_CONVERT
# ===============================================================================

def url_convert(data):
    print 'DATA--->', data
    if 'Rome' in data:
        data_str = '/getMedalTally/Rome'
    elif 'Gual' in data:
        data_str = '/getMedalTally/Gual'
    elif 'Stone Curling' in data:
        data_str = '/getScore/Stone Curling'
    elif 'Stone Throwing' in data:
        data_str = '/getScore/Stone Throwing'
    print 'DAT_STR--->', data_str
    return data_str


# ===============================================================================
# Ends here
# ===============================================================================

def startserver(num):

    # print "RUNNIN SERVER REST--->"

    service.run(port=5000)

    return


# def startserver1(num):
#    # print "RUNNIN SERVER REST--->"
#
#    service1.run(port=9090)
#    return

# def startserver2(num):
#    # print "RUNNIN SERVER REST--->"
#
#    service2.run(port=9091)
#    return

# ===============================================================================
# CODE ENDS HERE
# ===============================================================================


# ===============================================================================
# THIS IS MODULES RUN WHENEVER A SOMEONE TRIES TO CONNECT WITH FEP2. WE HAVE 2
# ON FEP MODUEL IN OUR IMPLEMENTATIO.
# ===============================================================================

def onConnectFEP1(conn1,conn2,conn3,conn4):
    global busyFlagF2
    global localCLKFEP2
    print '----FEP1 CONNECTED FEP1 FEP2 FEP3 SOCKET-->'
    return


# ===============================================================================
# CODE ENDS HERE
# ===============================================================================


def onConnectFEP2(conn1,conn2,conn3,conn4):
    global busyFlagF2
    global localCLKFEP2
    print '----FEP2 CONNECTED FEP1 FEP3 FEP4 SOCKET-->'
    return


# ===============================================================================
# CODE ENDS HERE
# ===============================================================================


def onConnectFEP3(conn1,conn2,conn3,conn4):
    global busyFlagF2
    global localCLKFEP2
    print '----FEP3 CONNECTED FEP1 FEP2 FEP4 SOCKET-->'
    return


# ===============================================================================
# CODE ENDS HERE
# ===============================================================================


def onConnectFEP4(conn1,conn2,conn3,conn4):
    global busyFlagF2
    global localCLKFEP2
    print '----FEP4 CONNECTED FEP1 FEP2 FEP3 SOCKET-->'
    return


# ===============================================================================
# CODE ENDS HERE
# ===============================================================================















# # ===============================================================================
# # THIS THREAD IS MONITORING RAFFLE_WINNER LIST . IT RANDOMLY PICKS A WINNER AMONGST
# # THE CLIENTS WHO WERE ENTERED INTO THE CONTEST.THESE CIENTS WERE
# # 100TH , 200TH ...1000TH CLIENT.
# # ===============================================================================
# 
# def Winner(num):
#     print 'Starting raffle winner'
#     count = 0
#     while True:
#         cv.acquire()
#         if len(RaffleWinner) == 10 and count == 0:
#             x = randint(0, 9)
#             print 'And the WINNER is--------->', RaffleWinner[x]
#             count = 1
#             cv.notify_all()
#         else:
# 
#             cv.wait()
#         cv.release()
# 
# 
# # ===============================================================================
# # CODE ENDS HERE
# # ===============================================================================

# # ===============================================================================
# # THIS THREAD IS JUST MONITORING raf_LIST WHICH IS THE LIST WHICH CONTAINS THE
# # CLIENTS REQUEST.
# # ===============================================================================
# 
# def RaffleLottery(num):
#     print '-----Starting Raffle Lottery-------'
#     count = 0
#     while True:
# 
#     # cv.acquire()
#     # print len(raf_list)
# 
#         if len(raf_list) == 100 and count == 0:
#             print '100th client --------------------------------------------->', \
#                 raf_list[99]
#             RaffleWinner.append(raf_list[99])
#             count = 1
#         elif len(raf_list) == 200 and count == 1:
# 
#       # cv.notify_all()
# 
#             print '200th client --------------------------------------------->', \
#                 raf_list[199]
#             RaffleWinner.append(raf_list[199])
#             count = 2
#         elif len(raf_list) == 300 and count == 2:
# 
#       # cv.notify_all()
# 
#             print '300th client --------------------------------------------->', \
#                 raf_list[299]
#             RaffleWinner.append(raf_list[299])
#             count = 3
#         elif len(raf_list) == 400 and count == 3:
# 
#       # cv.notify_all()
# 
#             print '400th client --------------------------------------------->', \
#                 raf_list[399]
#             RaffleWinner.append(raf_list[399])
#             count = 4
#         elif len(raf_list) == 500 and count == 4:
# 
#       # cv.notify_all()
# 
#             print '500th client --------------------------------------------->', \
#                 raf_list[499]
#             RaffleWinner.append(raf_list[499])
#             count = 5
#         elif len(raf_list) == 600 and count == 5:
# 
#       # cv.notify_all()
# 
#             print '600th client --------------------------------------------->', \
#                 raf_list[599]
#             RaffleWinner.append(raf_list[599])
#             count = 6
#         elif len(raf_list) == 700 and count == 6:
# 
#       # cv.notify_all()
# 
#             print '700th client --------------------------------------------->', \
#                 raf_list[699]
#             RaffleWinner.append(raf_list[699])
#             count = 7
#         elif len(raf_list) == 800 and count == 7:
# 
#       # cv.notify_all()
# 
#             print '800th client --------------------------------------------->', \
#                 raf_list[499]
#             RaffleWinner.append(raf_list[799])
#             count = 8
#         elif len(raf_list) == 900 and count == 8:
# 
#       # cv.notify_all()
# 
#             print '900th client --------------------------------------------->', \
#                 raf_list[499]
#             RaffleWinner.append(raf_list[899])
#             count = 9
#         elif len(raf_list) == 1000 and count == 9:
# 
#       # cv.notify_all()
# 
#             print '1000th client --------------------------------------------->', \
#                 raf_list[499]
#             RaffleWinner.append(raf_list[999])
#             count = 10
# 
# 
#       # cv.notify_all()
#     # else:
#       # cv.wait()
#     # cv.release()
# 
# # ===============================================================================
# # CODE ENDS HERE
# # ===============================================================================

# ===============================================================================
# THIS THREAD TAKES REQUEST FROM FEPS AND FORWARD THEM TO OUR BACKEND SERVER.
# THE FINAL RESULT IS RETURNED FROM HERE TO FEP.
# ===============================================================================

def EndServer(data):

  # return data + " will be sent"

    data_temp = re.sub('[^A-Za-z0-9]+', '', data)
    if 'incrementMedalTally' in data_temp:
        url = 'http://127.0.0.1:5000' + str(data)

    # print "Sending Reuest ",url

        data1 = requests.put(url).json()
    elif 'getMedalTally' in data_temp:
        url = 'http://127.0.0.1:5000' + str(data)

    # print "Sending Request ",url

        data1 = requests.get(url).json()
    elif 'pushUpdate' in data_temp:
        url = 'http://127.0.0.1:5000' + str(data)

    # print "Sending Request ",url

        data1 = requests.put(url)
    elif 'setScore' in data_temp:
        url = 'http://127.0.0.1:5000' + str(data)

    # print "Sending request ",url

        data1 = requests.put(url).json()
    elif 'registerClient' in data_temp:

    # print "Set Score",data1

        url = 'http://127.0.0.1:5000' + str(data)

    # print "Sending Request ",url

        data1 = requests.put(url)
    elif 'getScore' in data_temp:
        url = 'http://127.0.0.1:5000' + str(data)

    # print "Sending Request ",url

        data1 = requests.get(url).json()
    return data1


# ===============================================================================
# CODE ENDS HERE
# ===============================================================================

class FEP1():
    
    n_h=0
    v_a=''
    n_a=0
    V = ''
    v_a_array = []
    temp1 = 0
    temp11 = 0
    temp2 = 0
    temp22 = 0
    temp3 = 0
    temp33 = 0
    flag = ""
    n = ""
    start = ""
    Client=""
    def FEP1_result(self):
        while True:
            if FEP1Queue.qsize() != 0:
                client = FEP1Queue.get()
                data = FEP1Queue.get()
                FEP1.Client = data
                print 'f1:data',data
                print 'f1:client',client
                result = EndServer(str(client))
                FEP1.n=result
                FEP1.Client = data
                FEP1.flag = 1
                break
            else:
                continue
        return
    
    def FEP1(self,num):
        global busyFlagF1
        global mode
        poll = 0
        global localCLKFEP1
        print 'Starting FEP1'
        #start_new_thread(self.FEP1_socket, (1, ))
        FEP1.FEP1_result(self)
        r_list = []
        time.sleep(2)
        HOST = "localhost" 
        #start_new_thread(self.FEP1_result, (1,))
        while True:
            #print "FEP1.flag==",FEP1.flag,FEP1.n
            FEP1.FEP1_result(self)
            if FEP1.flag == 1:
                print "****************F1:STARTING PAXOS*******************"
                while True:
                    f1_majority = 0
                    my_n=FEP1.n_h+1
                    FEP1.n_h = my_n
                    time.sleep(3)
                    print 'FEP1 connecting with FEP2 SOCKET'
                    PORT = 9093
                    s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s1.connect((HOST, PORT))
                    print "F1:Connected"
                    s1.send("FEP1:<prepare,"+str(my_n)+">")
                    data1=s1.recv(1024)
                    if data1:
                        print "DATA RCVD FROM FEP2   ",data1
                        if 'prepare-ok' in data1:
                            #print data1
                            msg1 = data1
                            arr1=msg1.replace('<',' ').replace(':',' ').replace(',',' ').replace('>','').split()
                            f1_majority = f1_majority + 1
                            print "Rcvd From FEP2-->",arr1
                            temp1 = str(arr1[3:])
                            temp11 = arr1[2]
                            print "temp1==",temp1
                        
                    
                
                    time.sleep(3)
                    print 'FEP1 connecting with FEP3 SOCKET'
                    PORT = 9094
                    s2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s2.connect((HOST, PORT))
                    s2.send("FEP1:<prepare,"+str(my_n)+">")
                    data2=s2.recv(1024)
                    if data2:
                        if 'prepare-ok' in data2:
                            #print data2
                            msg2 = data2
                            arr2=msg2.replace('<',' ').replace(':',' ').replace(',',' ').replace('>','').split()
                            f1_majority = f1_majority + 1
                            print "Rcvd From FEP3-->",arr2
                            temp2 = arr2[3]
                            temp22 = arr2[2]
                    
                    
                    time.sleep(5)
                    print 'FEP1 connecting with FEP4 SOCKET'
                    PORT = 9095
                    s3 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s3.connect((HOST, PORT))
                    s3.send("FEP1:<prepare,"+str(my_n)+">")
                    data3=s3.recv(1024)
                    if data3:
                        if 'prepare-ok' in data3:
                            msg3 = data3
                            arr3=msg3.replace('<',' ').replace(':',' ').replace(',',' ').replace('>','').split()
                            f1_majority = f1_majority + 1
                            print "Rcvd From FEP4-->",arr3
                            temp3 = arr3[3]
                            temp33 = arr3[2]
                             
                    
                    if f1_majority > 2:
                        print "Fep1 got majority",f1_majority,temp11,temp22,temp33
                        print "Val",temp1,temp2,temp3
                        if int(temp11) >= int(temp22) and int(temp11) >= int(temp33):
                            print "FEP2 WINS"
                            if 'NULL' in temp1:
                                V=0
                            else:
                                V = temp1
                                
                        elif int(temp22) >= int(temp11) and int(temp22) >= int(temp33):
                            print "FEP3 WINS"
                            if 'NULL' in temp2:
                                V=0
                            else:
                                V = temp2
                        else:
                            print "FEP4 WINS"
                            if 'NULL' in temp3:
                                V = 0
                            else:
                                V = temp3
                        print "V=====",V
                    else:
                        print "Start Over"
                        s1.close()
                        s2.close()
                        s3.close()
                        time.sleep(5)
                        FEP1.start = 0
                        F1_majority = 0
                        continue
                        
                    f1_majority = 0
                    
                    s1.send("FEP1:<accept,"+str(my_n)+","+str(V)+">")
                    time.sleep(2)
                    data1 = s1.recv(1024)
                    if data1:
                        print "FEP1 Phase 2 from FEP2-->",data1
                        if 'accept' in data1:
                            f1_majority = f1_majority + 1
                    
                    s2.send("FEP1:<accept,"+str(my_n)+","+str(V)+">")
                    time.sleep(2)
                    data2 = s2.recv(1024)
                    if data2:
                        print "FEP1 Phase 2 from FEP3-->",data2
                        if 'accept' in data2:
                            f1_majority = f1_majority + 1
                    
                    s3.send("FEP1:<accept,"+str(my_n)+","+str(V)+">")
                    time.sleep(2)
                    data3 = s3.recv(1024)
                    if data3:
                        print "FEP1 Phase 2 from FEP4-->",data3
                        if 'accept' in data3:
                            f1_majority = f1_majority + 1
                            
                    if f1_majority > 2:
                        print "Phase 2 majority found sending data to all"
                        s1.send("FEP1:<decide,"+str(V)+">")
                        time.sleep(2)
                        s2.send("FEP1:<decide,"+str(V)+">")
                        time.sleep(2)
                        s3.send("FEP1:<decide,"+str(V)+">")
                        print "Fep1 start == 1"
                        FEP1.start = 1
                        FEP1.flag = 0
                        f1Client = FEP1.Client
                        f1Client.send(str(FEP1.n))
                        time.sleep(3)
                        break
                    else:
                        print "Phase 2 majority not found"
                        s1.close()
                        s2.close()
                        s3.close()
                        FEP1.start = 0
                        time.sleep(5)
                        continue
            else:
                #print "F1:Not Yet..."
                continue
    
    # ===============================================================================
    # CODE ENDS HERE
    # ===============================================================================
    # ===============================================================================
    # THIS IS OUR SOCKET FOR FEP1 WHICH STARTES AS SOON AS FEP IS INITIATED.
    # ===============================================================================
    
    def FEP1_socket(self,num1):
        print '--------Starting FEP1 Socket'
        HOST = ''  # Symbolic name meaning the local host
        PORT = 9092  # Arbitrary non-privileged port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((HOST, PORT))
        s.listen(1)
        print '--------FEP1 SOCKET LISTNING ON PORT 9092'
    
      # conn, addr = s.accept()
      # print "Connected to FEP1 by", addr
        while True:
            (conn1, addr1) = s.accept()
            print 'Connected to FEP1 by', addr1
            data=conn1.recv(1024)
            if data:
                print data
        
    #     (conn2, addr2) = s.accept()
    #     print 'Connected to FEP1 by', addr2
    #     
    #     (conn3, addr3) = s.accept()
    #     print 'Connected to FEP1 by', addr3
    
      # print conn.recv(1024)
    
    
        #t = threading.Thread(target=onConnectFEP1, args=(conn1,conn2,conn3, ))
        #t.start()
    
    
      # print conn.recv(1024)
    # ===============================================================================
    # CODE ENDS HERE
    # ===============================================================================


class FEP2():
    
    n_h=0
    v_a='NULL'
    n_a=0
    flag = 0
    Client = ""
    # ===============================================================================
    # THIS IS ONE OF OUR REPLICATED SERVER CALLED FEP2. THIS FEP IS LISTNING TO THE
    # DISPATCHER TO INSERT LOAD IN ITS QUEUE.
    # ===============================================================================
    def FEP2_result(self):
            while True:
                if FEP2Queue.qsize() != 0:
                    client = FEP2Queue.get()
                    data = FEP2Queue.get()
                    FEP2.Client = data
                    print 'f2:data',data
                    print 'f2:client',client
                    result = EndServer(str(client))
                    FEP2.v_a=result
                    FEP2.Client = data
                    FEP2.flag = 1
                    break
                else:
                    continue
            return
    
    
    def FEP2(self,num):
        global busyFlagF2
        global FEP2_pro_flag
        r_list = []
        global mod
        poll = 0
        global localCLKFEP2
        print 'Starting FEP2'
        start_new_thread(self.FEP2_socket, (1, ))
        time.sleep(2)
        HOST = ''  # The remote host
    
    def FEP2_socket(self,num1):
        print '---------Starting FEP2 Socket'
        HOST = ''  # Symbolic name meaning the local host
        PORT = 9093  # Arbitrary non-privileged port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
     # s.setblocking(0)
     # fcntl.fcntl(s, fcntl.F_SETFL, os.O_NONBLOCK)
    
        s.bind((HOST, PORT))
        s.listen(1)
        print '------FEP2 SOCKET LISTNING ON PORT 9093'
        FEP2.FEP2_result(self)
    
     # conn, addr = s.accept()
     # print 'Connected to FEP2 by', addr
        #start_new_thread(self.FEP2_result, (1, ))
        while True:
            FEP2.FEP2_result(self)
            if FEP2.flag == 1:
                (conn1, addr1) = s.accept()
                print 'Connected to FEP2 by', addr1
                data=conn1.recv(1024)
                if data:
                    print data
                    if 'prepare' in data:
                        msg=data
                        arr=msg.replace('<',' ').replace(':',' ').replace(',',' ').replace('>','').split()
                        print arr
                        if int(arr[2])>FEP2.n_h:
                            FEP2.n_h=int(arr[2])
                            FEP2.start = 1
                            time.sleep(1)
                            msg='FEP2<prepare-ok,'+str(FEP2.n_a)+','+str(FEP2.v_a)+'>'
                            conn1.send(msg)
                        else:
                            msg='FEP2<prepare-reject>'
                            conn1.send(msg)
                data = conn1.recv(1024)
                if data:
                    print "FEP2-->",data
                    msg = data
                    arr=msg.replace('<',' ').replace(':',' ').replace(',',' ').replace('>','').split()
                    print "arr FEP2-->",arr
                    if int(arr[2])>=FEP2.n_h:
                        FEP2.n_h=int(arr[2])
                        FEP2.n_a=int(arr[2])
                        FEP2.v_a=str(arr[3])
                        print "Sending data from FEP2 to FEP1"
                        conn1.send('FEP2<accept-ok>')
                    else:
                        conn1.send("<accept-reject>")  
                        
                data = conn1.recv(1024)
                if data:
                    print "F2:Final data RECVD from F1 after PAXOS",data   
                    FEP2.flag = 0         

class FEP3():
    
    n_h=0
    v_a='NULL'
    n_a=0
    flag = 0
    Client = ""
    # ===============================================================================
    # THIS IS ONE OF OUR REPLICATED SERVER CALLED FEP2. THIS FEP IS LISTNING TO THE
    # DISPATCHER TO INSERT LOAD IN ITS QUEUE.
    # ===============================================================================
    
    def FEP3(self,num):
        global busyFlagF2
        global FEP3_pro_flag
        r_list = []
        global mod
        poll = 0
    
    
    
        global localCLKFEP2
        print 'Starting FEP3'
        start_new_thread(self.FEP3_socket, (1, ))

    def FEP3_result(self):
            while True:
                if FEP3Queue.qsize() != 0:
                    client = FEP3Queue.get()
                    data = FEP3Queue.get()
                    FEP3.Client = data
                    print 'f3:data',data
                    print 'f3:client',client
                    result = EndServer(str(client))
                    FEP3.v_a=result
                    FEP3.Client = data
                    FEP3.flag = 1
                    break
                else:
                    continue
            return

    def FEP3_socket(self,num1):
        print '---------Starting FEP3 Socket'
        HOST = ''  # Symbolic name meaning the local host
        PORT = 9094  # Arbitrary non-privileged port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.bind((HOST, PORT))
        s.listen(1)
        print '------FEP3 SOCKET LISTNING ON PORT 9094'
        FEP3.FEP3_result(self)
        while True:
            FEP3.FEP3_result(self)
            if FEP3.flag == 1:
                (conn1, addr1) = s.accept()
                print 'Connected to FEP3 by', addr1
                data=conn1.recv(1024)
                if data:
                    print data
                    if 'prepare' in data:
                        msg=data
                        arr=msg.replace('<',' ').replace(':',' ').replace(',',' ').replace('>','').split()
                        print arr
                        if int(arr[2])>FEP3.n_h:
                            FEP3.n_h=int(arr[2])
                            FEP3.start = 1
                            time.sleep(1)
                            msg='FEP3<prepare-ok,'+str(FEP2.n_a)+','+str(FEP2.v_a)+'>'
                            conn1.send(msg)
                        else:
                            msg='FEP3<prepare-reject>'
                            conn1.send(msg)
                data = conn1.recv(1024)
                if data:
                    print "FEP3-->",data
                    msg = data
                    arr=msg.replace('<',' ').replace(':',' ').replace(',',' ').replace('>','').split()
                    print "arr FEP3-->",arr
                    if int(arr[2])>=FEP3.n_h:
                        FEP3.n_h=int(arr[2])
                        FEP3.n_a=int(arr[2])
                        FEP3.v_a=str(arr[3])
                        print "Sending data from FEP3 to FEP1"
                        conn1.send('FEP3<accept-ok>')
                    else:
                        conn1.send("<accept-reject>")  
                        
                data = conn1.recv(1024)
                if data:
                    print "F3:Final data RECVD from F1 after PAXOS",data   
                    FEP3.flag = 0
class FEP4(): 

    n_h=0
    v_a=0
    n_a=0
    
    # ===============================================================================
    # THIS IS ONE OF OUR REPLICATED SERVER CALLED FEP2. THIS FEP IS LISTNING TO THE
    # DISPATCHER TO INSERT LOAD IN ITS QUEUE.
    # ===============================================================================
    
    def FEP4(self,num):
        global busyFlagF2
        global FEP4_pro_flag
        r_list = []
        global mod
        poll = 0
        global localCLKFEP2
        print 'Starting FEP4'
        start_new_thread(self.FEP4_socket, (1, ))
    
        while True:
            cv.acquire()
            if FEP4Queue.qsize() != 0:
                client = FEP4Queue.get()
                data = FEP4Queue.get()
                print 'f4:data',data
                print 'f4:client',client
                result = EndServer(str(client))
                print 'f4:result',result
                if FEP4_pro_flag == 1:
                    data.send(str(result))
                    
    
                cv.notify_all()
            else:
    
                cv.wait()
    
            cv.release()
    
    
    def FEP4_socket(self,num1):
        print '---------Starting FEP3 Socket'
        HOST = ''  # Symbolic name meaning the local host
        PORT = 9095  # Arbitrary non-privileged port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
     # s.setblocking(0)
     # fcntl.fcntl(s, fcntl.F_SETFL, os.O_NONBLOCK)
    
        s.bind((HOST, PORT))
        s.listen(1)
        print '------FEP4 SOCKET LISTNING ON PORT 9094'
    
     # conn, addr = s.accept()
     # print 'Connected to FEP2 by', addr
        while True:
            (conn1, addr1) = s.accept()
            print 'Connected to FEP4 by', addr1
            data=conn1.recv(1024)
            if data:
                print data
                if 'prepare' in data:
                    msg=data
                    arr=msg.replace('<',' ').replace(':',' ').replace(',',' ').replace('>','').split()
                    print arr
                    if int(arr[2])>FEP4.n_h:
                        FEP4.n_h=int(arr[2])
                        conn1.send('FEP4<prepare-ok,'+str(FEP4.n_a)+','+str(FEP4.v_a)+'>')
                    else:
                        msg='FEP4<prepare-reject>'
                        conn1.send(msg)                    
            data = conn1.recv(1024)
            if data:
                print "FEP4-->",data
                msg = data
                arr=msg.replace('<',' ').replace(':',' ').replace(',',' ').replace('>','').split()
                print "F4 arr-->",arr
                if int(arr[2])>=FEP4.n_h:
                    FEP4.n_h=int(arr[2])
                    FEP4.n_a=int(arr[2])
                    FEP4.v_a=str(arr[3])
                    print "Sending data from FEP4 to FEP1"
                    conn1.send('FEP4<accept-ok>')
            else:
                conn1.send("<accept-reject>")                   
            data = conn1.recv(1024)
            if data:
                print "******LEARNER F4:Final data RECVD from F1 after PAXOS",data   
    #     (conn2, addr2) = s.accept()
    #     print 'Connected to FEP4 by', addr2
    #     
    #     (conn3, addr3) = s.accept()
    #     print 'Connected to FEP4 by', addr3
    
     # print conn1.recv(1024)
    
        #t = threading.Thread(target=onConnectFEP4, args=(conn1,conn2,conn3, ))
        #t.start()
    
    
    # ===============================================================================
    # CODE ENDS HERE
    # ===============================================================================




# ===============================================================================
# THIS THREAD IS CALLED FOR EACH CLIENT WHICH CONNECTS TO OUR SERVER.IT TAKES A
# CLIENT AND LOAD THE CLIENT ONTO CLIENT LOAD QUEUE.
# ===============================================================================
# Client Thread Which adds request to Queue

def ClientThread(c):

  # print "CLIENT THREAD Started"

    cv.acquire()
    ClientLoad.put(c)
    cv.notify_all()
    cv.release()


# ===============================================================================
# CODE ENDS HERE
# ===============================================================================

# ===============================================================================
# THIS IS OUR WORK DISPENSER , WHOSE MAIN TASK IS TO SEND REQUEST TO EITHER FEP1
# OR FEP2.THIS IS SENDING THE CLIENT NOT ITS REQUEST.WE HAVE DESIGNED THIS SUCH
# THAT THE FIRST REQUEST FROM ANY CLIENT GOES TO FEP1 AND SECOND GOES TO FEP2.
# ===============================================================================

def WorkDispatcher(num):
    i = 0
    global FEP1_pro_flag
    global FEP2_pro_flag
    global FEP3_pro_flag
    global FEP4_pro_flag
    while True:
        cv.acquire()
        if ClientLoad.qsize() > 0:
            
            FEP1_pro_flag = 1
            
            client = ClientLoad.get()
            
            data=client.recv(1024)
            
            if data:
                FEP1Queue.put(data)
                FEP1Queue.put(client)
                 
                FEP2Queue.put(data)
                FEP2Queue.put(client)
               
                FEP3Queue.put(data)
                FEP3Queue.put(client)
                
                
                #FEP4Queue.put(data)
                #FEP4Queue.put(client)
            
                      
            
            cv.notify_all()
        else:

    # cv.wait()

            cv.wait()

        cv.release()


# ===============================================================================
# CODE ENDS HERE
# ===============================================================================

# ===============================================================================
# THE FOLLOWING VARIABLES ARE GLOBAL VARIABLES.
# FEP1Queue: CONTAINS CLIENT INFO WHICH IS BEEN GIVEN TO FEP1 TO PROCESS ITS REQUEST
# FEP1Queue: CONTAINS CLIENT INFO WHICH IS BEEN GIVEN TO  FEP2 TO PROCESS ITS REQUEST
# ClientQueu: CONTAINS INFO ABOUT THE CLIENT
# RAF_LIST: CONTAINS ORDERED LIST OF CLIENTS STARTING FROM 0 TO N.
# RAFFLEWINNER: STORES 1OOTH , 200TH ... 1000TH CLIENT INFO.
# ===============================================================================

ThreadList = []

WorkQueue = Queue()  # THis Queue Stores all request from client. Top 2 request will be sent to FEP queues to process

FEP1Queue = Queue()  # This Queue stores request sent to FEP1 to handle

FEP2Queue = Queue()  # This queue stores requests sent to FEP2 to handle

FEP3Queue = Queue()

FEP4Queue = Queue()

ClientQueue = Queue()  # This Queue contains client info

ClientFEP1Queue = Queue()  # client info which are assigned to FEP1

ClientFEP2Queue = Queue()  # client info which are assigned to FEP2

ClientLoad = Queue()

RaffleList = []

RaffleWinner = []

busyFlagF1 = 0

busyFlagF2 = 0

localCLKFEP1 = 1.0000

localCLKFEP2 = 2.0000

counter = 0

raf_dict = dict()

raf_list = []

cache_dic = {}

cache_dicf2 = {}

cache_dicf2  = {}

cache_dicf3 = {}

cache_dicf4 = {}

FEP1_pro_flag = 0

FEP2_pro_flag = 0

FEP3_pro_flag = 0

FEP4_pro_flag = 0



mode = 1


#######

# ===============================================================================
# CODE ENDS HERE
# ===============================================================================

# ===============================================================================
# THIS IS OUR MAIN CODE WHICH OPENS THE SOCKET, ALLOW SNCHRONIZATION
# ===============================================================================

def Main():
    host = ''
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))

    # print("socket binded to post", port)

    s.listen(5)

    # print("socket is listening")
    # a forever loop until client wants to exit

    ThreadNumber = 1
    while True:

        # establish connection with client

        (c, addr) = s.accept()

        # print('Connected to :', addr[0], ':', addr[1])
        # Start a new thread for socket communication
        # print "Creating Client Threads Client",ThreadNumber
        # print " C " , c

        t = threading.Thread(target=ClientThread, args=(c, ))
        ThreadList.append(t)
        t.start()
        ThreadNumber = ThreadNumber + 1


    # s.close()
# ===============================================================================
# CODE ENDS HERE
# ===============================================================================

# ===============================================================================
# ALL THE THREAD WHICH WILL START
# ===============================================================================

if __name__ == '__main__':
    start_new_thread(WorkDispatcher, (1, ))
    start_new_thread(startserver, (1, ))

  # castVoteFEP1()
  # start_new_thread(castVoteFEP1, (1,))
 # start_new_thread(startserver2, (1,))
    object1=FEP1()
    object2=FEP2()
    object3=FEP3()
    object4=FEP4()

#     start_new_thread(Winner, (1, ))
#     start_new_thread(RaffleLottery, (1, ))
    start_new_thread(object1.FEP1, (1, ))
    start_new_thread(object2.FEP2, (1, ))
    start_new_thread(object3.FEP3, (1, ))
    start_new_thread(object4.FEP4, (1, ))
    Main()

# =============================================================================
# PROGRAM ENDS HERE
# =============================================================================


            
