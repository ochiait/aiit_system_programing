import sys
from array import array
from benchmarker import Benchmarker
from collections import deque

n = int(sys.argv[1]) if len(sys.argv) > 1 else 1000000

"""
## benchmarker:         release 4.0.1 (for python)
## python version:      3.6.4
## python compiler:     GCC 4.2.1 Compatible Clang 4.0.1
## python platform:     Darwin-17.4.0-x86_64-i386-64bit
## python executable:   /anaconda3/bin/python
## cpu model:           Intel(R) Core(TM) i5-5257U CPU @ 2.70GHz

## 100件の場合
## parameters:          loop=100, cycle=1, extra=0
##                        real    (total    = user    + sys)
list                    0.0000    0.0000    0.0000    0.0000
array                   0.0001    0.0000    0.0000    0.0000
deque                   0.0000    0.0000    0.0000    0.0000

## Ranking                real
list                    0.0000  (100.0) ********************
deque                   0.0000  ( 89.8) ******************
array                   0.0001  ( 30.9) ******

## Matrix                 real    [01]    [02]    [03]
[01] list               0.0000   100.0   111.4   323.4
[02] deque              0.0000    89.8   100.0   290.2
[03] array              0.0001    30.9    34.5   100.0
-------------------------------------------------------------
## 10,000件の場合
## parameters:          loop=10000, cycle=1, extra=0
##                        real    (total    = user    + sys)
list                    0.0191    0.0200    0.0200    0.0000
array                   0.0082    0.0100    0.0100    0.0000
deque                   0.0016    0.0000    0.0000    0.0000

## Ranking                real
deque                   0.0016  (100.0) ********************
array                   0.0082  ( 18.9) ****
list                    0.0191  (  8.1) **

## Matrix                 real    [01]    [02]    [03]
[01] deque              0.0016   100.0   528.0  1228.4
[02] array              0.0082    18.9   100.0   232.7
[03] list               0.0191     8.1    43.0   100.0
-------------------------------------------------------------
## 100,000件の場合
## parameters:          loop=100000, cycle=1, extra=0
##                        real    (total    = user    + sys)
list                    1.8456    1.8400    1.8300    0.0100
array                   0.8379    0.8300    0.8300    0.0000
deque                   0.0107    0.0100    0.0100    0.0000

## Ranking                real
deque                   0.0107  (100.0) ********************
array                   0.8379  (  1.3)
list                    1.8456  (  0.6)

## Matrix                 real    [01]    [02]    [03]
[01] deque              0.0107   100.0  7848.7 17287.7
[02] array              0.8379     1.3   100.0   220.3
[03] list               1.8456     0.6    45.4   100.0
-------------------------------------------------------------
## 1,000,000件の場合
## parameters:          loop=1000000, cycle=1, extra=0
##                        real    (total    = user    + sys)
list                  352.2179  350.8600  349.4900    1.3700
array                 127.6248  127.2700  126.9000    0.3700
deque                   0.1173    0.1200    0.1100    0.0100

## Ranking                real
deque                   0.1173  (100.0) ********************
array                 127.6248  (  0.1)
list                  352.2179  (  0.0)

## Matrix                 real    [01]    [02]    [03]
[01] deque              0.1173   100.0 108794.7 300250.8
[02] array            127.6248     0.1   100.0   276.0
[03] list             352.2179     0.0    36.2   100.0
"""
with Benchmarker(n, width=20) as bench:
    nay = [i for i in range(n)]
    iay = array('I', [i for i in range(n)])
    day = deque(nay)

    @bench("list")
    def _(bm):
        for i in bm:
            nay.pop(0)

    @bench("array")
    def _(bm):
        for i in bm:
            iay.pop(0)

    @bench("deque")
    def _(bm):
        for i in bm:
            day.popleft()
