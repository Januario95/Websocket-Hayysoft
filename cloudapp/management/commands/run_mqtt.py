from django.core.management.base import (
    BaseCommand, CommandError
)
import os

from ...consumer import client_instance, Message

def X(s): return os.system(s)


client_instance.client_.on_message = Message


class Command(BaseCommand):
    help = 'Get cloud mqtt'

    def handle(self, *args, **kwargs):
        try:
            client_instance.Start_connection()
        except:
            raise Command('Something wrong with cloud mqtt')
