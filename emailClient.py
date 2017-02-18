import sys
from socket import *
from PyQt4 import QtCore, QtGui, uic

qtCreatorFile = "emailGUI.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

msg = '\r\n I Love computer networks!'
endmshg= "\r\n.\r\n"
mailserver = 'www.000webhost.com'
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
if recvhelo[:3] != '250':
	print '250 reply not received from server.'

#Set up Some Security
clientSocket.send("AUTH PLAIN password\r\n")
recv2 = clientSocket.recv(1024)
print recv2
if recv2[:3] != '250':
	print '250 reply not received from server.'


#Send MAIL FROM command and print server response.
clientSocket.send("MAIL From: austincoat@gmail.com\r\n")
recv2 = clientSocket.recv(1024)
if recv2[:3] != '250':
	print '250 reply not received from server.'

#Send RCPT TO command and print server response.
print "Sending RCPT TO Command"
clientSocket.send("RCPT TO: alcoates@stetson.edu\r\n")
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
clientSocket.send("SUBJECT: SMTP Mail Client Test\nSMTP Mail Client Test\n.\n\r\n")
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
