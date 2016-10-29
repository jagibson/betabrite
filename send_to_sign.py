#!/usr/bin/env python

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTShadowClient
import sys
import logging
import time
import json
import getopt
import alphasign
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config.ini')

iot_endpoint = config.get('general', 'iot_endpoint')
iot_port = config.getint('general', 'iot_port')
iot_device_name = config.get('general', 'iot_device_name')
credentials_ca = config.get('general', 'credentials_ca')
credentials_private_key= config.get('general', 'credentials_private_key')
credentials_cert = config.get('general', 'credentials_cert')
sign_device = config.get('general', 'sign_device')


def publish_to_sign(myJSONPayload):
	print myJSONPayload
	iot_message = json.loads(myJSONPayload)
	msg = iot_message['state']['message']
	color = getattr(alphasign.colors, iot_message['state']['color'])
	mode = getattr(alphasign.modes, iot_message['state']['mode'])
	font = getattr(alphasign.charsets, iot_message['state']['font'])

	sign = alphasign.Serial(device=sign_device)
	sign.connect()

	text = alphasign.Text("%s%s%s" % (color, font, msg), label="A", mode=mode)

	sign.write(text)
	sign.disconnect()



class shadowCallbackContainer:
	def __init__(self, deviceShadowInstance):
		self.deviceShadowInstance = deviceShadowInstance

	# Custom Shadow callback
	def customShadowCallback_Delta(self, payload, responseStatus, token):
		# payload is a JSON string ready to be parsed using json.loads(...)
		# in both Py2.x and Py3.x
		print("Received a delta message:")
		payloadDict = json.loads(payload)
		publish_to_sign(payload)
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
myShadowClient.configureEndpoint(iot_endpoint, iot_port)
myShadowClient.configureCredentials(credentials_ca, credentials_private_key, credentials_cert)
myShadowClient.configureAutoReconnectBackoffTime(1, 32, 20)
myShadowClient.configureConnectDisconnectTimeout(10)  # 10 sec
myShadowClient.configureMQTTOperationTimeout(5)

myShadowClient.connect()

myDeviceShadow = myShadowClient.createShadowHandlerWithName(iot_device_name, True)
shadowCallbackContainer_Bot = shadowCallbackContainer(myDeviceShadow)

myDeviceShadow.shadowRegisterDeltaCallback(shadowCallbackContainer_Bot.customShadowCallback_Delta)

# Loop forever
while True:
    pass