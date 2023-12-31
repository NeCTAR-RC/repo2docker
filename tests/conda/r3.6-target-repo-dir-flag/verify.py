#!/usr/bin/env python
import os
import sys
from glob import glob

# conda should still be in /srv/conda
# and Python should still be in $NB_PYTHON_PREFIX
assert sys.executable == os.path.join(
    os.environ["NB_PYTHON_PREFIX"], "bin", "python"
), sys.executable
assert sys.executable.startswith("/srv/conda/"), sys.executable

# Repo should be in /srv/repo
assert os.path.exists("/srv/repo/verify.py")
assert os.path.abspath(__file__) == "/srv/repo/verify.py"

# Repo should be writable
assert os.access("/srv/repo", os.W_OK)

# All files in repo dir should be readable and writeable
for path in glob("/src/repo/**/*", recursive=True):
    assert os.access(path, os.R_OK)
    assert os.access(path, os.W_OK)

# Should be able to make a new file
with open("/srv/repo/writeable", "w") as fp:
    fp.write("writeable")
