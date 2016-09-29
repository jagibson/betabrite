#!/usr/bin/env python

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
import sys
import logging
import time
import json
import getopt

class shadowCallbackContainer:
	def __init__(self, deviceShadowInstance):
		self.deviceShadowInstance = deviceShadowInstance

	# Custom Shadow callback
	def customShadowCallback_Delta(self, payload, responseStatus, token):
		# payload is a JSON string ready to be parsed using json.loads(...)
		# in both Py2.x and Py3.x
		print("Received a delta message:")
		payloadDict = json.loads(payload)
		deltaMessage = json.dumps(payloadDict["state"])
		print(deltaMessage)
		print("Request to update the reported state...")
		newPayload = '{"state":{"reported":' + deltaMessage + '}}'
		self.deviceShadowInstance.shadowUpdate(newPayload, None, 5)
		print("Sent.")



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
myShadowClient = AWSIoTMQTTShadowClient("basicShadowDeltaListener")
myShadowClient.configureEndpoint("a34ps3jqnolue.iot.us-west-2.amazonaws.com", 8883)
myShadowClient.configureCredentials("/home/montjoy/git/betabrite/certs/AWS_IoT_root_CA.pem", "/home/montjoy/git/betabrite/certs/73cb53c6db-private.pem.key", "/home/montjoy/git/betabrite/certs/73cb53c6db-certificate.pem.crt")
myShadowClient.configureAutoReconnectBackoffTime(1, 32, 20)
myShadowClient.configureConnectDisconnectTimeout(10)  # 10 sec
myShadowClient.configureMQTTOperationTimeout(5)

myShadowClient.connect()

myDeviceShadow = myShadowClient.createShadowHandlerWithName("Input_command", True)
shadowCallbackContainer_Bot = shadowCallbackContainer(myDeviceShadow)

myDeviceShadow.shadowRegisterDeltaCallback(shadowCallbackContainer_Bot.customShadowCallback_Delta)

# Loop forever
while True:
    pass

