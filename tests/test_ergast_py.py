""" Tests for Ergast Py """

from ergast_py import __version__


class TestErgastPy():
    """
    Tests for the Ergast-py package
    """

    def test_version(self):
        """ Assert the version of the system """
        assert __version__ == '0.6.0'

    def test_ergast(self):
        """ Basic test to check Ergast functions """
        pass
