#!/usr/bin/env python3
import logging

logging.basicConfig(
    format="%(asctime)s [%(levelname)s]: %(message)s", level=logging.ERROR
)
logger = logging.getLogger()


def main():
    logger.error("Hello from ERROR")
    logger.warning("Hello from WARNING")
    logger.info("Hello from INFO")
    logger.debug("Hello from DEBUG")
    # var = 150.1
    # logger.warning("Var is %.3f", var)


if __name__ == "__main__":
    main()
