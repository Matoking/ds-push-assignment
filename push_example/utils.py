import time

import pika


def create_channel(host):
    """
    Create a channel connection
    """
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=host)
    )
    channel = connection.channel()
    channel.queue_declare(queue="test_queue")

    return channel


class Timer:
    """
    https://preshing.com/20110924/timing-your-code-using-pythons-with-statement/
    """
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.interval = self.end - self.start
