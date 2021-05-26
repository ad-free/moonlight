# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils.translation import gettext_lazy as _
from django.conf import settings
from django.shortcuts import render
from django.views import View

import paho.mqtt.client as mqtt
import uuid


class Home(View):
    template = 'home/index.html'

    def get(self, request):

        def on_connect(client, userdata, flags, rc):
            print("Subscribed....")
            client.subscribe("test/auth")

        def on_message(client, userdata, msg):
            print("Message:")
            print(f"{msg.topic} - {msg.payload}")

        print("Connecting to MQTT broker")
        client = mqtt.Client(client_id=f"{uuid.uuid4().hex}")
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect("127.0.0.1")
        client.loop_forever()

        return render(request, self.template, context={})
