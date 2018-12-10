# RabbitMQ Work Queue

A simple RabbitMQ based work queue using a push architecture.

# Description

The work queue uses the RabbitMQ message broker to transmit messages from the server to the client. Each message is ACK'd by the client before being removed from the message broker.

The following is done for each message:

1. Server broadcasts a message to `test_queue` queue
2. Client listens to the `test_queue` and receives a message.
3. Client acknowledges the message, removing the message from the queue 

To benchmark the performance of the message broker, the server broadcasts a set amount of equal-sized messages which are processed by the client.

The `benchmark.py` script starts the sender (`server.py`) and receiver (`client.py`) scripts in parallel and prints the time taken once both
scripts have finished sending and receiving the messages.

# Installation

How to install (assuming Virtualenv for Python 3 is installed and RabbitMQ is running)

    $ virtualenv -p python3 venv
    $ source venv/bin/activate
    $ pip install -r requirements.txt
    
Run a benchmark and print the time to send and receive the messages

    $ # Send 5,000 messages, each with a size of 500 kB and measure the time it takes to send and receive the messages
    $ python benchmark.py --payload-size=500000 --payload-count=5000
    
Run client and server individually

    $ python server.py --payload-size=500000 --payload-count=5000
    $ # In another terminal
    $ python client.py --payload-count=5000
