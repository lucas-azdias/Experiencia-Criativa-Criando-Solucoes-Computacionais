from flask_mqtt import Mqtt


mqtt_client = Mqtt()
topics_subscribed = [
    "soil-humidity-system/data"
]
