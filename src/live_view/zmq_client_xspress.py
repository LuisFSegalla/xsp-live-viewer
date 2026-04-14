"""Module for testing live view."""
import json

import zmq


def live_viewer(stype, host):
    """Simple test function for live view."""
    print(f"Args: {stype} {host}")
    if stype == 'SUB' or stype == 'PUB':
        stype = zmq.SUB
    elif stype == 'PULL' or stype == 'PUSH':
        stype = zmq.PULL
    else:
        stype = zmq.SUB
        print(f"Unsupported socket type {stype}, use SUB")
        raise (TypeError)

    context = zmq.Context()
    sock = context.socket(zmq.SUB)
    sock.setsockopt_string(zmq.SUBSCRIBE, "")
    sock.setsockopt(zmq.SNDHWM, 5)
    sock.connect(host)

    poller = zmq.Poller()
    poller.register(sock, zmq.POLLIN)
    print("after register")
    while True:
        message = sock.recv_multipart()
        header = json.loads(message[0].decode('utf-8'))
        print(f"{header}")
