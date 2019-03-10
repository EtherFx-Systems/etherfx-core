import pika, sys, os, logging, json
import dill as pickle

logging.basicConfig()

IP_ADDRESS = "35.188.49.28"


class RabbitMQInterface:
    def __init__(self):
        self.payload = None

    def create_connection(self, host):
        connection = pika.BlockingConnection(pika.ConnectionParameters(host))
        return connection

    def publishToQueue(self):
        connection = self.create_connection(IP_ADDRESS)
        channel = connection.channel()

        channel.queue_declare(queue="demo_publishing_queue")

        channel.basic_publish(
            exchange="", routing_key="demo_publishing_queue", body=self.payload
        )
        print(" Sent Message from Orchestrator")
        connection.close()

    def publish_taskMetadata_to_queue_from_orchestrator(self, TaskMetaData):
        print("========")
        print(TaskMetaData)
        print(type(TaskMetaData))
        print("========")
        self.payload = pickle.dumps(TaskMetaData)
        self.publishToQueue()

    def subscribe_from_queue(self):
        connection = self.create_connection(IP_ADDRESS)
        channel = connection.channel()
        channel.queue_declare(queue="demo_publishing_queue")

        channel.exchange_declare(
            exchange="demo_exchange",
            exchange_type="direct",
            passive=False,
            durable=True,
            auto_delete=False,
        )

        channel.basic_consume(self.callback, queue="demo_publishing_queue", no_ack=True)

        channel.start_consuming()

    def callback(self, ch, method, properties, body):
        task_meta = json.loads(body)
        task_id = task_meta["task_id"]
        return task_id
