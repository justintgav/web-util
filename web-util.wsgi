#!/usr/bin/python3
import sys
import logging
logging.basicConfig(stream=sys.stderr)
#logging.basicConfig(filename='/opt/web-util/debug.log',level=logging.DEBUG)
sys.path.insert(0,"/opt/web-util/")

from app import app as application
