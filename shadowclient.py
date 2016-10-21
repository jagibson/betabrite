#!/usr/bin/env python

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
import sys
import logging
import time
import json
import getopt

# Custom Shadow callback
def customShadowCallback_Update(payload, responseStatus, token):
	# payload is a JSON string ready to be parsed using json.loads(...)
	# in both Py2.x and Py3.x
	#print responseStatus
	if responseStatus == "timeout":
		print("Update request " + token + " time out!")
	if responseStatus == "accepted":
		payloadDict = json.loads(payload)
		print("~~~~~~~~~~~~~~~~~~~~~~~")
		print("Update request with token: " + token + " accepted!")
		#print("property: " + str(payloadDict["state"]["desired"]["property"]))
		print("property: " + str(payloadDict["state"]))
		print("~~~~~~~~~~~~~~~~~~~~~~~\n\n")
	if responseStatus == "rejected":
		print("Update request " + token + " rejected!")

def customShadowCallback_Delete(payload, responseStatus, token):
	if responseStatus == "timeout":
		print("Delete request " + token + " time out!")
	if responseStatus == "accepted":
		print("~~~~~~~~~~~~~~~~~~~~~~~")
		print("Delete request with token: " + token + " accepted!")
		print("~~~~~~~~~~~~~~~~~~~~~~~\n\n")
	if responseStatus == "rejected":
		print("Delete request " + token + " rejected!")

logger = None
if sys.version_info[0] == 3:
	logger = logging.getLogger("core")  # Python 3
else:
	logger = logging.getLogger("AWSIoTPythonSDK.core")  # Python 2
logger.setLevel(logging.DEBUG)
streamHandler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
streamHandler.setFormatter(formatter)
logger.addHandler(streamHandler)

myShadowClient = None
myShadowClient = AWSIoTMQTTShadowClient("basicShadowUpdater")
myShadowClient.configureEndpoint("a34ps3jqnolue.iot.us-west-2.amazonaws.com", 8883)
myShadowClient.configureCredentials("/home/montjoy/git/betabrite/certs/AWS_IoT_root_CA.pem", "/home/montjoy/git/betabrite/certs/73cb53c6db-private.pem.key", "/home/montjoy/git/betabrite/certs/73cb53c6db-certificate.pem.crt")
myShadowClient.configureAutoReconnectBackoffTime(1, 32, 20)
myShadowClient.configureConnectDisconnectTimeout(10)  # 10 sec
myShadowClient.configureMQTTOperationTimeout(5)

myShadowClient.connect()

myDeviceShadow = myShadowClient.createShadowHandlerWithName("Input_command", True)
#myDeviceShadow.shadowDelete(customShadowCallback_Delete, 5)


myJSONPayload = '{ "state": { "desired": { "message": "hello", "color": "BLUE", "font": "FIVE_HIGH_STD", "mode": "HOLD" } } }'
myDeviceShadow.shadowUpdate(myJSONPayload, customShadowCallback_Update, 5)
