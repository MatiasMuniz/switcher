<p align="center">
  <img src="./switcher.png" alt="switcher" />
</p>

# Switcher
Switcher is a project developed in Python that implements a server and clients that communicate with each other via sockets. Clients can send messages to other clients connected through the server, and the server is responsible for redirecting these messages to the correct recipient. Additionally, Switcher allows sending messages to all connected clients simultaneously.

## Features

- **Multiple Connections**: Support for multiple clients connected at the same time.
- **Message Redirection**: The server redirects messages to the correct client.
- **Messages to All Clients**: Ability to send messages to all connected clients.
- **Multithreading**: Uses multithreading to handle multiple client connections efficiently.

## Requirements

- Python 3.x

## Installation

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/MatiasMuniz/switcher.git
    ```

2. Navigate to the project directory:
    ```bash
    cd switcher
    ```

3. (Optional) Create and activate a virtual environment:
    ```bash
    python -m venv switcher_env
    source switcher_env/bin/activate  # On Linux/Mac
    switcher_env\Scripts\activate  # On Windows
    ```

## Usage

### Starting the Server

Run the server using the following command:
```bash
python server.py
```

### Starting the Client

Run one or more clients using the following command:

```bash
python client.py
```

### Message Format
Messages should be in the following format:

```bash
IP:DEST@PORT:CONTENT
```

**IP**: IP of the sender.
**DEST@PORT**: IP address and port of the recipient. Use all@all to send the message to all clients.
**CONTENT**: Content of the message.

## Licence
```
   GNU GENERAL PUBLIC LICENSE
    Version 3, 29 June 2007
```