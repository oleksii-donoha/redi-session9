from typing import TextIO


def hyperbolic_function(x) -> float:
    """
    Returns the hyperbolic function of x.
    :param x: number
    :return: function value as float
    """
    return 1 / x


def write_to_file(file: TextIO, line: str):
    """
    Writes a line to a file.
    :param file: open file object
    :param line: string to write
    :return: None
    """
    file.write(line)
