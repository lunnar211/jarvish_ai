import socket

def is_connected():
    """Check if the system is connected to the internet."""
    try:
        # Check connectivity by connecting to Google's DNS server
        socket.create_connection(("8.8.8.8", 53), 2)
        return True
    except OSError:
        return False
