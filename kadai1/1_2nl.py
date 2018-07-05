import sys

arg = len(sys.argv)
if arg == 1:
    f = sys.stdin
elif arg == 2:
    try:
        f = open(sys.argv[1], "rU")
    except IOError:
        sys.exit("nl: %s: ファイルが開けません" % (sys.argv[1]))
else:
    sys.exit("usage: nl [file]")

i = 1
for s in f:
    s = s.rstrip()
    if s:
        print("{:6d}\t{}".format(i, s))
        i += 1

f.close()
