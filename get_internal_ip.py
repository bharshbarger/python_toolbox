import socket

def get_internal_address(self):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 53))
    except Exception as e:
        print(e)
    return s.getsockname()[0]
