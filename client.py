#!/usr/bin/env python3
import click

from push_example.utils import create_channel, Timer


received_count = 0


@click.command()
@click.option("--payload-count", type=int, default=50)
@click.option("--host", type=str, default="localhost")
def main_cli(payload_count, host):
    main(payload_count, host)


class Consumer(object):
    def __init__(self, payload_count):
        self.received_count = 0
        self.payload_count = payload_count

    def consume_msg(self, ch, method, properties, body):
        ch.basic_ack(delivery_tag=method.delivery_tag)
        self.received_count += 1

        if self.received_count == self.payload_count:
            ch.stop_consuming()


def main(payload_count, host):
    channel = create_channel(host=host)
    consumer = Consumer(payload_count=payload_count)

    print("Waiting for {} messages...".format(payload_count))
    channel.basic_consume(consumer.consume_msg, queue="test_queue", no_ack=False)
    with Timer() as t:
        channel.start_consuming()

    print("Took {:.6f} seconds to receive.".format(t.interval))



if __name__ == "__main__":
    main_cli()
