import logging
import logging.config

# Create and configure logger
logging.basicConfig(
    filename="C://Users//Admin//Desktop//Automation_bootcamp//intro_to_selenium//solarsystemscope//logfile.log",
    format='%(asctime)s: %(levelname)s: %(message)s', filemode='w')

# Creating an object
logger = logging.getLogger(__name__)

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

logging.debug('THIS IS A DEBUG MESSAGE: ')
logging.info('THIS IS AN INFO MESSAGE: ')
logging.warning('THIS IS A WARNING MESSAGE: ')
logging.error('THIS IS AN ERROR MESSAGE: ')
logging.critical('THIS IS A CRITICAL MESSAGE: ')

#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------
# def loggingDmo():
#     # getLogger() method takes the test case name as input
#     logger = logging.getLogger(__name__)
#
#     # FileHandler() method takes location and path of log file
#     fileHandler = logging.FileHandler('C://Users//Admin//Desktop//Automation_bootcamp//intro_to_selenium//solarsystemscope//logfile.log')
#     # Formatter() method takes care of the log file formatting
#     formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
#     fileHandler.setFormatter(formatter)
#     # addHandler() method takes fileHandler object as parameter
#     logger.addHandler(fileHandler)
#     # setting the logger level
#     logger.setLevel(logging.INFO)
#     logger.debug('THIS IS A DEBUG MESSAGE: ')
#     logger.error('THIS IS AN ERROR MESSAGE: ')
#     logger.warning('THIS IS A WARNING MESSAGE: ')
#     logger.critical('THIS IS A CRITICAL MESSAGE: ')
#     logger.info('THIS IS AN INFO MESSAGE: ')

#-----------------------------------------------------------------------------------------------------------------------

#
# def test_logging(log_path):
#
#
#     logger = logging.getLogger(__name__)
#
#     logger.setLevel(logging.DEBUG)
#
#     handler = logging.FileHandler("C://Users//Admin//Desktop//Automation_bootcamp//intro_to_selenium//solarsystemscope//logfile.log")
#     logger.addHandler(handler)
#
#     logging.getLogger('selenium.webdriver.remote').setLevel(logging.WARN)
#     logging.getLogger('selenium.webdriver.common').setLevel(logging.DEBUG)
#     logging.getLogger('selenium.webdriver.remote').setLevel(logging.INFO)
#     logging.getLogger('selenium.webdriver.common').setLevel(logging.ERROR)
#     logging.getLogger('selenium.webdriver.common').setLevel(logging.CRITICAL)
#
#     logger.debug('THIS IS A DEBUG MESSAGE: ')
#     logger.error('THIS IS AN ERROR MESSAGE: ')
#     logger.warning('THIS IS A WARNING MESSAGE: ')
#     logger.critical('THIS IS A CRITICAL MESSAGE: ')
#     logger.info('THIS IS AN INFO MESSAGE: ')
#
#     with open("C://Users//Admin//Desktop//Automation_bootcamp//intro_to_selenium//solarsystemscope//logfile.log", 'r') as fp:
#         assert len(fp.readlines()) == 3
