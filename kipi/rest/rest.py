

from flask import Blueprint, request

import pika

bp = Blueprint('kipi', __name__, url_prefix='/kipi')


@bp.route('/kill', methods=('GET',))
def kill():
    if request.method == 'GET':
        
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='kipi')

        channel.basic_publish(exchange='', routing_key='kipi', body='kill')

        return 'all good!', 201

    return 'bad request!', 400


@bp.route('/start', methods=('GET',))
def start():
    if request.method == 'GET':
        
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='kipi')

        channel.basic_publish(exchange='', routing_key='kipi', body='start')

        return 'all good!', 201

    return 'bad request!', 400


@bp.route('/restart', methods=('GET',))
def restart():
    if request.method == 'GET':
        
        connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        channel = connection.channel()

        channel.queue_declare(queue='kipi')

        channel.basic_publish(exchange='', routing_key='kipi', body='restart')

        return 'all good!', 201

    return 'bad request!', 400
