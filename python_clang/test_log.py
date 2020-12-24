import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')
logger = logging.getLogger("API-debug")

if "__main__" == __name__:
    logger.debug("shiads")
