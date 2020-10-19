from app import create_app
from app import register_socket
import logging

app = create_app()
# logging
gunicorn_logger = logging.getLogger("gunicorn.error")
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)

socket_io = register_socket(app)


if __name__ == "__main__":
    socket_io.run(app)
