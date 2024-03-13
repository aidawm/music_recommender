import pika, sys, os
import json 
import music_recognizer

class AMQP: 
    def __init__(self) -> None:
        data_address = "configs.json"
        f = open(data_address)
        self.configs = json.load(f)
        self.configs = self.configs["rabbitmq"]

        self.connect_to_rabbitmq()



    def connect_to_rabbitmq(self):
        self.connection = pika.BlockingConnection(pika.URLParameters(self.configs["server_url"]))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue=self.configs["queue_name"])

    def publish_message(self, id):
        self.channel.basic_publish(exchange='',
                      routing_key=self.configs["queue_name"],
                      body=str(id))
        print(f" [x] Sent 'id = {id}'")


    def recieve_message(self):
        def callback(ch, method, properties, body):
            music_recognizer.notify(body)


        self.channel.basic_consume(queue=self.configs["queue_name"], on_message_callback=callback, auto_ack=True)

        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()