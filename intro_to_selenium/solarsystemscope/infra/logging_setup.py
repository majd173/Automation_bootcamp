import logging

class LoggingSetup:
    logging.basicConfig(filename="../solar_logfile.log",
                        level=logging.INFO, format='%(levelname)s:%(message)s:%(asctime)s',
                        force=True)