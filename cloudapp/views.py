from django.shortcuts import render

import json
from .read_json import ManageJson
import mysql.connector as mysql

config = {
    'host': 'bgplatformdb1.mysql.database.azure.com',
    'user': 'bg37hayysoftadmin',
    'password': 'DoNotHack2021',
    'database': 'bluguarddb',
    # 'client_flags': [mysql.ClientFlag.SSL],
    # 'ssl_ca': 'C',
    'port': '3306'
}


def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def index(request):
  Connector = mysql.connect(**config)
  Cursor = Connector.cursor()

  query = 'SELECT * FROM TBL_Mqtt'
  Cursor.execute(query)
  results = dictfetchall(Cursor)

  return render(request,
                'index.html',
                {'text': 'Hayysoft Systems Pte',
                 'mqtt_data2': results})
