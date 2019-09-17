import os


def make_a_file(fname, fsize):
  fh = open(fname, 'wb')
  fh.write(os.urandom(fsize))
