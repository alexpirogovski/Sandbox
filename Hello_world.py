#!/usr/bin/env python
import logging

logger = logging.getLogger("Schultz")
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

# print "Hello, world!"

# Some comment


def my_function(message):
    logger.info(message)

my_function("Hello, world!")



