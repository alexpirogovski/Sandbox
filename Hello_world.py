#!/usr/bin/env python
import logging
from optparse import OptionParser

logger = logging.getLogger("Schultz")
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logger.info("Hello, world!")
print "Hello, world!"

parser=OptionParser()
parser_parse_args = parser.parse_args()


def read_param(message):
    print message

read_param(parser_parse_args)





