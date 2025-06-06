import paho.mqtt.client as mqtt

# Broker and topic subscription list
MQTT_HOST = "test.mosquitto.org"
MQTT_TOPIC = [('/merakimv/#', 0)]
MQTT_CLIENTID = "ProgrammabilityClass"

# One-time code execution upon connection
def on_connect(client, userData, flags, reasonCode, properties):
    client.subscribe(MQTT_TOPIC)

# Executed code block per message received
def on_message(client, userData, msg):
    print(msg.payload.decode('utf-8'))

# Initialize MQTT
mqtt_client = mqtt.Client(client_id=MQTT_CLIENTID, callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect(MQTT_HOST, 1883)
mqtt_client.loop_forever()