from channels.generic.websocket import WebsocketConsumer

import json
import string
import datetime as dt
from time import sleep
from random import randint
from datetime import datetime
import mysql.connector as mysql

from .read_json import ManageJson
from .Broker_Connect import Client
from .Broker_GetIoTData import Message
from .Process_IoTData import (
    Get_Mqtt_Data, config, dictfetchall,
    MQTT_DATA
)


client_instance = Client()  # Instantiate mqtt client
data_reader = ManageJson()

def default(obj): return obj.isoformat() if isinstance(obj, datetime) else obj


def Read_Gateway_Data(raw_data):
    mqtt_data = raw_data.decode('utf-8').replace("'", '"')
    mqtt_data = json.loads(mqtt_data)

    Get_Mqtt_Data(mqtt_data)
    # old_data = data_reader.load_json()
    # print(mqtt_data)

    # data_reader.save_json(mqtt_data)
    # return mqtt_data


def Message(client=None, obj=None, msg=None):
    Read_Gateway_Data(msg.payload)


client_instance.client_.on_message = Message


class WsConsumer(WebsocketConsumer):
    def connect(self):
        # global MQTT_DATA
        self.accept()

        Connector = mysql.connect(**config)
        Cursor = Connector.cursor()

        query = '''SELECT * FROM TBL_Mqtt
                    WHERE TIMEDIFF(CURRENT_TIMESTAMP(), Timestamp) < TIME('00:00:03') AND
                          TIMEDIFF(CURRENT_TIMESTAMP(), Timestamp) > TIME('00:00:01') LIMIT 1'''
        Cursor.execute(query)
        results = dictfetchall(Cursor)
        results = json.dumps(results, default=default)
        # results = MQTT_DATA
        print(results)

        self.send(json.dumps(({
            'data': results
        })))
