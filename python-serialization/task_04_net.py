#!/usr/bin/env python3
"""
this module demonstrates a basic client-server architecture using
sockets and JSON serialization.
"""
import socket
import json


def start_server():
    """
    starts a TCP server that listens on port 8080.
    it receives data, deserializes it from JSON, and prints it.
    """
    # 1st create the socket (AF_INET = IPv4, SOCK_STREAM = TCP)
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2nd bind to localhost:8080
    # We use 'localhost' so it's only accessible from this machine.
    server_socket.bind(('localhost', 8080))

    # 3rd listen for incoming connections
    server_socket.listen(1)
    # print("Server is listening on port 8080...")

    # 4th accept a connection (this blocks until a client connects)
    connection, address = server_socket.accept()

    try:
        # 5th receive data (buffer size 1024 bytes)
        received_data = connection.recv(1024)

        # 6th deserialize: Bytes -> String -> Dictionary
        if received_data:
            json_string = received_data.decode('utf-8')
            my_dict = json.loads(json_string)
            print("Received Dictionary from Client:")
            print(my_dict)

    except json.JSONDecodeError:
        # handle cases where data isn't valid JSON
        pass
    finally:
        # 7th always close the connection
        connection.close()
        server_socket.close()


def send_data(data):
    """
    acts as a client to send a dictionary to the server.

    args:
        data (dict): the dictionary to serialize and send.
    """
    # create the client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # connect to the server
        client_socket.connect(('localhost', 8080))

        # serialize: Dictionary -> JSON String -> Bytes
        json_string = json.dumps(data)
        bytes_data = json_string.encode('utf-8')

        # send the data
        client_socket.sendall(bytes_data)

    except ConnectionRefusedError:
        # print("Connection failed. Is the server running?")
        pass
    finally:
        # close the connection
        client_socket.close()
