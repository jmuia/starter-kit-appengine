#!/usr/bin/env python

import os
import sys

os.environ['SERVER_SOFTWARE'] = 'Development'


from distutils.spawn import find_executable
from os.path import realpath, dirname

SDK_GUESSES = ['/usr/local/google_appengine', '/Program Files (x86)/Google/google_appengine']
path = find_executable('dev_appserver.py')
if path:
    SDK_GUESSES.append(dirname(realpath(path)))

sdk_path = next((guess for guess in SDK_GUESSES if os.path.isdir(guess)), None)
if sdk_path is None:
    raise Exception("""
I couldn't find your app engine SDK. Please figure out where it is, and add
it to SDK_GUESSES in test/__init__.py for posterity :)
""")

sys.path.insert(0, sdk_path)
import dev_appserver
dev_appserver.fix_sys_path()
