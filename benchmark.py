#!/usr/bin/env python3
import click

from concurrent.futures import ProcessPoolExecutor

from client import main as client_main
from server import main as server_main

from push_example.utils import Timer


@click.command()
@click.option("--payload-size", type=int, default=2048)
@click.option("--payload-count", type=int, default=50)
@click.option("--host", type=str, default="localhost")
def main_cli(payload_size, payload_count, host):
    main(payload_size=payload_size, payload_count=payload_count, host=host)


def main(payload_size, payload_count, host):
    print("Creating server and client...")

    threads = []

    with ProcessPoolExecutor(max_workers=2) as executor:
        with Timer() as t:
            threads += [
                executor.submit(
                    client_main, payload_count=payload_count, host=host),
                executor.submit(
                    server_main,
                    payload_size=payload_size,
                    payload_count=payload_count,
                    host=host)
            ]

            executor.shutdown(wait=True)

        print("Took {:.6f} seconds to complete workflow.".format(t.interval))


if __name__ == "__main__":
    main_cli()
