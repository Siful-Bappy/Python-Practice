

from time import sleep
import os, sys
import RPi.GPIO as GPIO
import paho.mqtt.client as paho
import urlparse

GPIO.setmode(GPIO.BOARD)
GPIO.setwornings(False)
LED_PIN = 11

GPIO.setup(LED_PIN, GPIO.OUT)

def on_connect(self, mosq, obj, rc):
    self.subscribe("led", 0)
    
def on_message(mosq, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))
    if(msg.payload == "on"): 
        print("Light on")
        GPIO.output(LED_PIN, GPIO.HIGH)
    else:
        print("Light off")
        GPIO.output(LED_PIN, GPIO.LOW)
        
mqttc = paho.client()
mqttc.on_message = on_message
mqttc.on_connet = on_connect 

url_str = os.environ.get("CLOUDMQTT_URL", "TCP://broker.emqx.io:1883")
url = urlparse.urlparse(url_str)
mqttc.connet(url.hostname, url.port)

rc = 0
while True:
    while rc == 0:
        import time
        rc = mqttc.loop()
        time.sleep(1)