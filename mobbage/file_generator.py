import collections
import os



seed = "1092384956781341341234656953214543219"
words = open("lorem.txt", "r").read().replace("\n", '').split()

def fdata():
    a = collections.deque(words)
    b = collections.deque(seed)
    while True:
        yield ' '.join(list(a)[0:1024])
        a.rotate(int(b[0]))
        b.rotate(1)

g = fdata()
size = 12000 # 12kb
fname = "test.out"
fh = open(fname, 'w')
while os.path.getsize(fname) < size:
    fh.write(g.next())