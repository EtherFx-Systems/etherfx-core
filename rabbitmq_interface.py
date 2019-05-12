import pika, sys, os, logging, json
import json
#import dill as pickle

logging.basicConfig()

IP_ADDRESS = "35.202.107.208"


class RabbitMQInterface:
    def create_connection(self, host):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        return connection

    def publishToQueue(self, payload):
        connection = self.create_connection(IP_ADDRESS)
        channel = connection.channel()
        channel.queue_declare(queue="demo_publishing_queue")
        channel.basic_publish(
            exchange="", routing_key="demo_publishing_queue", body=payload
        )
        print("Sent Message from Orchestrator")
        connection.close()

    def publish_taskMetadata_to_queue_from_orchestrator(self, TaskMetaData):
        print("========")
        print(TaskMetaData)
        print(type(TaskMetaData))
        print("========")
        payload = json.dumps(TaskMetaData)
        self.publishToQueue(payload)

    def subscribe_to_queue(self, callback_method=None):
        connection = self.create_connection(IP_ADDRESS)
        channel = connection.channel()
        channel.queue_declare(queue="demo_publishing_queue")

        # channel.exchange_declare(
        #     exchange="demo_exchange",
        #     exchange_type="direct",
        #     passive=False,
        #     durable=True,
        #     auto_delete=False,
        # )

        if callback_method is None:
            callback_method = self.callback

        channel.basic_consume(callback_method, queue="demo_publishing_queue")
        channel.start_consuming()

    def callback(self, ch, method, properties, body):
        task_meta = json.loads(body)
        task_id = task_meta["task_id"]
        return task_id
