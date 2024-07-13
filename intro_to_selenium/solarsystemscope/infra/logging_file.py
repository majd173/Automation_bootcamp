import logging.config
class Logging:

    # Create and configure logger
    logging.basicConfig(
        filename="C:/Users/Admin/Desktop/Automation_bootcamp/intro_to_selenium/solarsystemscope/solar_logfile.log",
        format='%(asctime)s: %(levelname)s: %(message)s', filemode='w')

    # Creating an object
    logger = logging.getLogger(__name__)

    # Setting the threshold of logger to DEBUG
    logger.setLevel(logging.DEBUG)

    logger.debug('THIS IS A DEBUG MESSAGE: ')
    logger.info('THIS IS AN INFO MESSAGE: ')
    logger.warning('THIS IS A WARNING MESSAGE: ')
    logger.error('THIS IS AN ERROR MESSAGE: ')
    logger.critical('THIS IS A CRITICAL MESSAGE: ')

#--------------------------------------------------------------------------------------------------------------------
