import logging
import re
import sys


class AccessLogFormatter(logging.Formatter):
    def format(self, record):
        # Example: "127.0.0.1:49342 - "GET / HTTP/1.1" 200 OK"
        message = record.getMessage()
        parts = message.split(" - ", 1)
        if len(parts) == 2:
            client_addr, rest = parts
            match = re.search(r'"(.*?)"(.*)', rest)
            if match:
                request_info, status = match.groups()
                status = status.strip()
                return f"{record.levelname} 1 ({status}) {client_addr} - {request_info}"
        return message


class AppLogFormatter(logging.Formatter):
    def format(self, record):
        return f"{record.levelname} 2 [{record.name}] {record.getMessage()}"


class ErrorLogFormatter(logging.Formatter):
    def format(self, record):
        return f"{record.levelname} 3  {record.getMessage()}"


def configure_logging():
    """Configure logging for the application."""
    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    # Remove any existing handlers
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    # Create console handler with app formatter for stdout
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(AppLogFormatter())
    root_logger.addHandler(stdout_handler)

    # Configure Uvicorn access logger
    access_logger = logging.getLogger("uvicorn.access")
    access_logger.handlers = []  # Remove default handlers
    access_handler = logging.StreamHandler(sys.stdout)
    access_handler.setFormatter(AccessLogFormatter())
    access_logger.addHandler(access_handler)
    access_logger.propagate = False  # Prevent propagation to root logger

    # Configure Uvicorn error logger
    error_logger = logging.getLogger("uvicorn.error")
    error_logger.handlers = []  # Remove default handlers
    error_handler = logging.StreamHandler(sys.stdout)
    error_handler.setFormatter(ErrorLogFormatter())
    error_logger.addHandler(error_handler)
    error_logger.propagate = False  # Prevent propagation to root logger
