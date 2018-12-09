#!/usr/bin/env python3
import random

import click

from push_example.utils import Timer, create_channel


@click.command()
@click.option("--payload-size", type=int, default=2048)
@click.option("--payload-count", type=int, default=50)
def main_cli(payload_size, payload_count):
    main(payload_size, payload_count)


def main(payload_size, payload_count):
    channel = create_channel()

    payload = b"".join([
        bytes([random.randint(0, 255)]) for _ in range(0, payload_size)
    ])

    with Timer() as t:
        for _ in range(0, payload_count):
            channel.basic_publish(
                exchange="", routing_key="test_queue",
                body=payload)

    print(
        "Sent {payload_count} messages with size of {payload_size} bytes.\n"
        "Took {interval:.6f} seconds to send.".format(
            payload_count=payload_count, payload_size=payload_size,
            interval=t.interval
        )
    )


if __name__ == "__main__":
    main_cli()
