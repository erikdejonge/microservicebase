#!/usr/local/opt/python3/bin/python3.4

# -*- coding: utf-8 -*-
import re
import sys

from api_hour.application import run

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw|\.exe)?$', '', sys.argv[0])
    print(sys.argv[0])
    sys.exit(run())
