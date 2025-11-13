import logging


def setup_logging(level=logging.INFO):
    fmt = "%(asctime)s %(levelname)s %(name)s: %(message)s"
    logging.basicConfig(format=fmt, level=level)
    return logging.getLogger()
