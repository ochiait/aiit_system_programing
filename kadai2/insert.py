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
array                   0.0000    0.0000    0.0000    0.0000
deque                   0.0000    0.0000    0.0000    0.0000

## Ranking                real
deque                   0.0000  (100.0) ********************
array                   0.0000  ( 62.2) ************
list                    0.0000  ( 56.0) ***********

## Matrix                 real    [01]    [02]    [03]
[01] deque              0.0000   100.0   160.7   178.6
[02] array              0.0000    62.2   100.0   111.2
[03] list               0.0000    56.0    90.0   100.0
-------------------------------------------------------------
## 10,000件の場合
## parameters:          loop=10000, cycle=1, extra=0
##                        real    (total    = user    + sys)
list                    0.0268    0.0300    0.0300    0.0000
array                   0.0084    0.0100    0.0100    0.0000
deque                   0.0016    0.0000    0.0000    0.0000

## Ranking                real
deque                   0.0016  (100.0) ********************
array                   0.0084  ( 18.5) ****
list                    0.0268  (  5.8) *

## Matrix                 real    [01]    [02]    [03]
[01] deque              0.0016   100.0   540.3  1716.2
[02] array              0.0084    18.5   100.0   317.7
[03] list               0.0268     5.8    31.5   100.0
-------------------------------------------------------------
## 100,000件の場合
## parameters:          loop=100000, cycle=1, extra=0
##                        real    (total    = user    + sys)
list                    3.0664    3.0000    2.9900    0.0100
array                   0.8482    0.8500    0.8400    0.0100
deque                   0.0115    0.0100    0.0100    0.0000

## Ranking                real
deque                   0.0115  (100.0) ********************
array                   0.8482  (  1.4)
list                    3.0664  (  0.4)

## Matrix                 real    [01]    [02]    [03]
[01] deque              0.0115   100.0  7346.0 26556.6
[02] array              0.8482     1.4   100.0   361.5
[03] list               3.0664     0.4    27.7   100.0
-------------------------------------------------------------
## 1,000,000件の場合
## parameters:          loop=1000000, cycle=1, extra=0
##                        real    (total    = user    + sys)
list                  458.5608  456.9800  455.3100    1.6700
array                 127.7096  126.5400  126.1400    0.4000
deque                   0.1231    0.1300    0.1100    0.0200

## Ranking                real
deque                   0.1231  (100.0) ********************
array                 127.7096  (  0.1)
list                  458.5608  (  0.0)

## Matrix                 real    [01]    [02]    [03]
[01] deque              0.1231   100.0 103747.2 372520.1
[02] array            127.7096     0.1   100.0   359.1
[03] list             458.5608     0.0    27.9   100.0
"""
with Benchmarker(n, width=20) as bench:
    nay = []
    iay = array('I', [])
    day = deque()

    @bench("list")
    def _(bm):
        for i in bm:
            nay.insert(0, i)

    @bench("array")
    def _(bm):
        for i in bm:
            iay.insert(0, i)

    @bench("deque")
    def _(bm):
        for i in bm:
            day.appendleft(i)
