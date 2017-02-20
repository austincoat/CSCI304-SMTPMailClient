import sys
from socket import *
from Tkinter import *

#!/usr/bin/python
def sendEmail():
    mailserver = T.get("1.0",END)
    receivers = T2.get("1.0",END)
    receivers = receivers.split(",")
    #receive = T2.get("1.0",END)
    cc = T3.get("1.0",END)
    subject = T4.get("1.0",END)
    body = T5.get("1.0",END)
    for i in receivers:
        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.connect((mailserver, 25))
        recvconnect = clientSocket.recv(1024)
        print recvconnect

        if recvconnect[:3] != '220':
            print '220 reply not received from server.'

    #Send HELO command and print server response
        heloCommand = 'HELO Alice \r\n'
        clientSocket.send(heloCommand)
        recv1 = clientSocket.recv(1024)
        print recv1
    # Include This everytime there is no reply
        if recv1[:3] != '250':
            print '250 reply not received from server.'

    #Send MAIL FROM command and print server response.
        clientSocket.send("MAIL From: alcoates@delenn.artifice\r\n")
        recv2 = clientSocket.recv(1024)
        if recv2[:3] != '250':
	           print '250 reply not received from server.'

    #Send RCPT TO command and print server response.
        print "Sending RCPT TO Command"
        clientSocket.send("RCPT TO:" + i +"\r\n")
        recv2 = clientSocket.recv(1024)
        if recv2[:3] != '250':
	           print '250 reply not received from server.'
    #Send DATA command and print server response.
        print "Sending DATA Command"
        clientSocket.send("DATA\r\n")
        recv2 = clientSocket.recv(1024)
        print recv2
        if recv2[:3] != '250':
	           print '250 reply not received from server.'


               #Send Data and print server response.
        print "Sending Data"
        clientSocket.send("SUBJECT:"+subject+ "\n"+ body +"\n.\r\n")
        recv2 = clientSocket.recv(1024)
        print recv2
        if recv2[:3] != '250':
	           print '250 reply not received from server.'

        #Send QUIT command and get server response.
        clientSocket.send("QUIT\r\n")
        recv2 = clientSocket.recv(1024)
        if recv2[:3] != '250':
            print '250 reply not received from server.'

        print "Email Sent!"


top = Tk()
# Code to add widgets will go here...
w = Label(top, text= "Local Server")
w2 = Label(top, text="Recepient")
w3 = Label(top, text="CC")
w4 = Label(top, text="Subject")
w5 = Label(top, text="Body")
T = Text(top, height=2, width=30)
T2 = Text(top,height=3, width=30)
T3 = Text(top,height=2, width=30)
T4 = Text(top,height=2, width=30)
T5 = Text(top,height=2,width=30)
b1= Button(top, text='Send', width=25, command= sendEmail)
b2= Button(top, text='Cancel',width=25, command= top.destroy)
w.pack()
T.pack()
w2.pack()
T2.pack()
w3.pack()
T3.pack()
w4.pack()
T4.pack()
w5.pack()
T5.pack()
b1.pack()
b2.pack()
top.mainloop()
