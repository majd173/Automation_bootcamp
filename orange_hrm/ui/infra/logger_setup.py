import logging


class LoggingSetup():
    # This class manages a logging file that catches and records
    # important scenarios during tests running.
    logging.basicConfig(filename=r"C:\Users\Admin\Desktop\Automation_bootcamp\orange_hrm\orange_hrm.log",
                        level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s:',
                        force=True)


