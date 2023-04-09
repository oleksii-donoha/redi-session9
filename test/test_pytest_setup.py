import pytest

from src.unittest_demo import write_to_file


@pytest.fixture
def test_file():
    with open('test_data/file.txt', 'w') as f:
        yield f


def test_file_not_closed(test_file):
    write_to_file(test_file, "Hello from pytest")
    assert not test_file.closed
