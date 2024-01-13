import logging


def initialize():
    logger = logging.getLogger()
    logger.setLevel(0)
    formatter = logging.Formatter(u'# %(levelname)-8s [%(asctime)s] %(filename)-20s [LINE:%(lineno)s]   %(message)s')

    handler_info = logging.FileHandler("logs\\info.log", encoding="utf-8")
    handler_info.setFormatter(formatter)
    handler_info.setLevel(logging.INFO)

    handler_debug = logging.FileHandler("logs\\debug.log", encoding="utf-8")
    handler_debug.setFormatter(formatter)
    handler_debug.setLevel(logging.DEBUG)

    logger.handlers = [handler_info, handler_debug]
