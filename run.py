from app import create_app
from app import register_socket

app = create_app()
socket_io = register_socket(app)

if __name__ == "__main__":
    socket_io.run(app)
