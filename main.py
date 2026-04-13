from framework import TestLoader, TestRunner
from tests import TestLoaderTest

loader = TestLoader()
suite = loader.make_suite(TestLoaderTest)

runner = TestRunner()
runner.run(suite)