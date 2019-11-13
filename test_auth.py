#!python3

import pytest
from shutil import copyfile
from libs.base_class import BaseClass


@pytest.fixture(autouse=True)
def setup_and_teardown():
    yield
    copyfile(BaseClass.logfile, "logs/latest.log")


class Test(BaseClass):
    def test(self):
        self.log_this("test")