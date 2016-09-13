#!/usr/bin/env python

from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import sys
import logging
import time
import getopt

# Configure logging
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



# For certificate based connection
myMQTTClient = AWSIoTMQTTClient("iottscript")
# For Websocket connection
# myMQTTClient = AWSIoTMQTTClient("myClientID", useWebsocket=True)
# Configurations
# For TLS mutual authentication
myMQTTClient.configureEndpoint("a34ps3jqnolue.iot.us-west-2.amazonaws.com", 8883)
# For Websocket
# myShadowClient.configureEndpoint("YOUR.ENDPOINT", 443)
myMQTTClient.configureCredentials("/home/montjoy/git/betabrite/certs/AWS_IoT_root_CA.pem", "/home/montjoy/git/betabrite/certs/73cb53c6db-private.pem.key", "/home/montjoy/git/betabrite/certs/73cb53c6db-certificate.pem.crt")
# For Websocket, we only need to configure the root CA
# myMQTTClient.configureCredentials("YOUR/ROOT/CA/PATH")
myMQTTClient.configureOfflinePublishQueueing(-1)  # Infinite offline Publish queueing
myMQTTClient.configureDrainingFrequency(2)  # Draining: 2 Hz
myMQTTClient.configureConnectDisconnectTimeout(30)  # 10 sec
myMQTTClient.configureMQTTOperationTimeout(20)  # 5 sec


myMQTTClient.connect()
myMQTTClient.publish("$aws/things/Input_command/shadow/update", "stuff", 0)
#myMQTTClient.subscribe("$aws/things/Input_command/shadow/update", 1, customCallback)
#myMQTTClient.unsubscribe("$aws/things/Input_command/shadow/update")
myMQTTClient.disconnect()


# You're not connected to the Device Gateway
#Go to the "Device Gateway connection" tab

#Type in your desired Client ID or generate one using the "Generate client ID" button

#Once the connection to the Device Gateway succeeds, Subscribe or Publish to topics using the "Subscribe to topic" and "Publish to topic" tabs

#If the connection to the Device Gateway fails, ensure that your Client ID is less than 128 bytes and encoded in UTF-8

# client ID 187f1
# subscription topic "stuff"
# max message capture 100
