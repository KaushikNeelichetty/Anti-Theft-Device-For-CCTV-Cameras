######################
#######IMPORTS########
######################
import RPi.GPIO as GPIO         ## Import GPIO Library
import time                     ## Import 'time' library (for 'sleep')
import smtplib
import urllib
flag1=0
flag2=0
######################
###SET UP GPIO PINS###
######################
outPin = 7                      ## LED connected to pin 7
inCamera1 = 11
inCamera2 = 12                      ## Switch connected to pin 13
GPIO.setmode(GPIO.BOARD)        ## Use BOARD pin numbering
GPIO.setup(outPin, GPIO.OUT)    ## Set pin 7 to OUTPUT
GPIO.setup(inCamera1, GPIO.IN)      ## Set pin 13 to INPUT for camera 1
GPIO.setup(inCamera2, GPIO.IN)      ## Set pin 14 to INPUT for camera 2
GPIO.output(outPin,False) 
######################
#CODE TO SEND MAIL####
######################
def sendMail(x):
	smtpUser='from@domain.com'
	smtpPass='password'
	toAdd='to@domain.com'
	fromAdd=smtpUser
	subject='CAMERA THEFT'
	if(x==1):
		header='To: ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: ' +subject
		body='Camera CCTV#001 Stolen !! Click here to reset the portal for this camera http://itoa.esy.es/esptalk.php?safe=1&&camera=1'
	elif(x==2):
		header='To: ' + toAdd + '\n' + 'From: ' + fromAdd + '\n' + 'Subject: ' +subject
		body='Camera CCTV#002 Stolen !! Click here to reset the portal for this camera http://itoa.esy.es/esptalk.php?safe=1&&camera=2'
	s=smtplib.SMTP('smtp.gmail.com',587)
	s.ehlo()
	s.starttls()
	s.ehlo()
	s.login(smtpUser,smtpPass)
	s.sendmail(fromAdd,toAdd, header + '\n\n' +body)
	s.quit()
	print 'Mail Sent'
	return
#######################
#CODE TO NOTIFY PORTAL#
#######################
def notifyPortal(x):
	if(x==1):	
		url = "http://itoa.esy.es/esptalk.php?safe=0&&camera=1"
		response = urllib.urlopen(url).read()
		print response
	elif(x==2):
		url = "http://itoa.esy.es/esptalk.php?safe=0&&camera=2"
		response = urllib.urlopen(url).read()
		print response
	return
#######################
#RUNS FOREVER##########
#######################	
while True:                     ## Do this forever
	time.sleep(1)	
	value = GPIO.input(inCamera1)   ## Read input from switch
	if value==1:	## If switch is released
		if flag1==0:
			print 'CAMERA 1 THEFT!!!'
			sendMail(1)
			notifyPortal(1)
			flag1=1
	value = GPIO.input(inCamera2)   ## Read input from switch
	if value==1:	## If switch is released
		if flag2==0:
			print 'CAMERA 2 THEFT!!!'
			sendMail(2)
			notifyPortal(2)
			flag2=1
GPIO.cleanup() 