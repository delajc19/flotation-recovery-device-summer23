#Joseph de la Viesca
#Luthy Lab Summer 23
#Tetherless Flotation Recovery Device
#Underwater Receiver for Magnet Trigger
#---------------------------------------------------------------
#This program is an indefinitely looping script meant to constantly check
#for messages received from the top-side transmitter. When a message containing
#the "fire" command is received, the RPi will trigger the magnet to fire for the
#specified length of time in the range [0, 30](s)

from wlmodem import WlModem
#import pyserial
import RPi.GPIO as GPIO
import time
import sys

magPin = 16; #magnet pin

modem = WlModem("/dev/ttyS0") #m64 modem configuration

def setup(): #put your setup code here, to run once:
    #GPIO setup
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(magPin, GPIO.OUT) #set pin 23 as an output
    GPIO.output(magPin, GPIO.LOW)
    #GPIO.setup(13,GPIO.OUT)
    
    #Modem setup
    if not modem.connect(): #Check modem connection
        print("Failed connecting to modem")
        sys.ext(1)
        GPIO.cleanup() #GPIO cleanup necessary for EVERY EXIT CASE
    success = modem.cmd_configure("b",4)
    if success: #check role congiguration
        print("role configuration success")
    if modem.cmd_get_diagnostic().get("link_up"): #check for link
        print("Link is up")
    success = modem.cmd_queue_packet(b"HelloTop")
    if success: #check for message sent
        print("packet queue success")
    
    
def loop(): #put your main code here, to run repeatedly:
    while True:
        msg = "" #initialize message variable
        fireTime = 0 #initialize fire time variable
        pkt = modem.get_data_packet(timeout = 0) #make packet request
        if pkt: #check for packets received
            print("Got data", pkt)        
            msg = str(pkt).split('\'')[1] #cast data packet to string and use tokenizer to isolate messge
        if 'fire,' in msg: #run magnet trigger code if msg contains "fire,"
            fireTime = int(msg.split(',')[1]) #split message with comma delimiter and cast second element to an int to set magnet fire time
            #restrict magnet fire time to [0,30]
            if fireTime > 30:
                fireTime = 30
            if fireTime < 0:
                fireTime = 0
            GPIO.output(magPin,GPIO.HIGH) #trigger magnet
            time.sleep(fireTime) #leave magnet on for time t, where t = fireTime(s)
            GPIO.output(magPin,GPIO.LOW) #turn off magnet
        #time.sleep(2)
        #GPIO.output(magPin, GPIO.LOW)
        #time.sleep(2)

def destroy(): #This function ensures that no GPIO pins remain in use after closing program
    GPIO.output(magPin,GPIO.LOW)
    GPIO.cleanup()
    print("clean up")

if __name__ == '__main__': #main function to run setup and loop functions
    setup()
    try:
        loop()
    except KeyboardInterrupt: #press Ctrl+c to stop the program
        destroy()