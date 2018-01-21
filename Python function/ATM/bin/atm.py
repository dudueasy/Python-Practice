# -*- coding: utf-8 -*-
#__author__: 'Apolo Du'

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from core import main

sys.path.insert(0, BASE_DIR)


if __name__ == '__main__':
    main.run()

