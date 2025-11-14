# tests/conftest.py
import os
import sys

# add project root (which contains `src/`) to the front of sys.path
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
