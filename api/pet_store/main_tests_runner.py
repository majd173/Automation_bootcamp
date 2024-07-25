import unittest

if __name__ == '__main__':

    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover(start_dir='tests', pattern='test*.py')


    # Run the tet suite.
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(test_suite)