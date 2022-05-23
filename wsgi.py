#!/var/www/html/inwhome/.venv/bin/python3
# -*- coding: utf-8 -*-

import logging
import sys

logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/var/www/html/inwhome')
sys.path.insert(1, '/var/www/html/inwhome/.venv/lib/python3.8/site-packages')

from inwhome import app as application