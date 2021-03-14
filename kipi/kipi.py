
import subprocess
import argparse
import time
from multiprocessing import Process

import pika

import rest
from mine import MinecraftServer

def queue_callback(ch, method, properties, body):
    if body == 'start':
        MinecraftServer.start_server()
    elif body == 'kill':
        MinecraftServer.kill_server()
    elif body == 'restart':
        MinecraftServer.restart_server()

def main():

    MinecraftServer.start_server()

    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue='kipi')

    channel.basic_consume(queue='kipi', auto_ack=True, on_message_callback=queue_callback)

    subprocess.run(args=["gunicorn", "-w", 1, "kipi.rest:create_app"])

    while True:
        time.sleep(1)

if __name__ == "__main__":
    main()
