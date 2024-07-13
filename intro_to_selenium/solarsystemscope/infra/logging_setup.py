import logging

class LoggingSetup:
    # This class manages a logging file that catches and records
    # important scenarios during tests running.

    logging.basicConfig(filename="../solar_logfile.log",
                level=logging.INFO, format='%(levelname)s:%(message)s:%(asctime)s',
                force=True)