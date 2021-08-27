from django import template
from django.utils.safestring import mark_safe

from random import randint
import mysql.connector as mysql


register = template.Library()

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


@register.filter(name='random_number')
def random_number(text):
    Connector = mysql.connect(**config)
    Cursor = Connector.cursor()

    query = 'SELECT Type, Mac FROM TBL_Mqtt'
    Cursor.execute(query)
    results = dictfetchall(Cursor)

    return results
