from ergast_py import __version__


class TestErgastPy():
    """
    Tests for the Ergast-py package
    """

    def test_version(self):
        assert __version__ == '0.1.0'
