import sys

# This seems to be a reasonable way to avoid printing warnings.
for line in sys.stdin:
    if " " not in line:
        print line.rstrip()
