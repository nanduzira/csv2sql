#!d:\workspace\csv2sql\test\env\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'myhello','console_scripts','myhello'
__requires__ = 'myhello'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('myhello', 'console_scripts', 'myhello')()
    )
