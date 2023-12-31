from fastapi import APIRouter, Body
#fastapi_mqtt
from fastapi_mqtt.fastmqtt import FastMQTT
from fastapi_mqtt.config import MQTTConfig

# from fastapi.encoders import jsonable_encoder
import json

mqtt_config = MQTTConfig(host = "192.168.1.2",
    port= 1883,
    keepalive = 1,
    username="TGR_GROUP10",
    password="LV741N")

fast_mqtt = FastMQTT(config=mqtt_config)

router = APIRouter()

fast_mqtt.init_app(router)

from server.database import (
    add_water,
    delete_water,
    retrieve_water,
    retrieve_waters,
    update_water,
)
from server.models.water import (
    ErrorResponseModel,
    ResponseModel,
    WaterSchema,
    UpdateWaterModel,
)

@fast_mqtt.on_connect()
def connect(client, flags, rc, properties):
    fast_mqtt.client.subscribe("CMU_MAVERICK") #subscribing mqtt topic
    print("Connected: ", client, flags, rc, properties)

@fast_mqtt.on_message()
async def message(client, topic, payload: WaterSchema, qos, properties):
    water = json.loads(payload.decode())
    new_water = await add_water(water)
    return ResponseModel(new_water, "Water added successfully.")
    # print("Received message: ",topic, payload.decode(), qos, properties)

# @fast_mqtt.subscribe("CMU_MAVERICK")
# async def message_to_topic(client, topic, payload, qos, properties):
#     print("Received message to TGR_10 topic: ", topic, payload.decode(), qos, properties)

@fast_mqtt.on_disconnect()
def disconnect(client, packet, exc=None):
    print("Disconnected")

@fast_mqtt.on_subscribe()
def subscribe(client, mid, qos, properties):
    print("subscribed", client, mid, qos, properties)

################################################################################################################################

################################################################################################################################

@router.get("/", response_description="test publish to mqtt")
async def publish_hello():
    fast_mqtt.publish("CMU_MAVERICK", {"ID":10, "enable":True}) #publishing mqtt topic
    return {"result": True,"message":"Published" }

########################################################################################################################################

