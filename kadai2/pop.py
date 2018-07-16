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
list                    0.0000  (100.0) ********************
array                   0.0000  ( 75.0) ***************
deque                   0.0000  ( 69.5) **************

## Matrix                 real    [01]    [02]    [03]
[01] list               0.0000   100.0   133.3   143.9
[02] array              0.0000    75.0   100.0   107.9
[03] deque              0.0000    69.5    92.7   100.0
-------------------------------------------------------------
## 10,000件の場合
## parameters:          loop=10000, cycle=1, extra=0
##                        real    (total    = user    + sys)
list                    0.0015    0.0000    0.0000    0.0000
array                   0.0016    0.0000    0.0000    0.0000
deque                   0.0011    0.0000    0.0000    0.0000

## Ranking                real
deque                   0.0011  (100.0) ********************
list                    0.0015  ( 74.1) ***************
array                   0.0016  ( 70.5) **************

## Matrix                 real    [01]    [02]    [03]
[01] deque              0.0011   100.0   135.0   141.9
[02] list               0.0015    74.1   100.0   105.1
[03] array              0.0016    70.5    95.1   100.0
-------------------------------------------------------------
## 100,000件の場合
## parameters:          loop=100000, cycle=1, extra=0
##                        real    (total    = user    + sys)
list                    0.0135    0.0100    0.0100    0.0000
array                   0.0141    0.0200    0.0200    0.0000
deque                   0.0113    0.0100    0.0100    0.0000

## Ranking                real
deque                   0.0113  (100.0) ********************
list                    0.0135  ( 83.8) *****************
array                   0.0141  ( 80.2) ****************

## Matrix                 real    [01]    [02]    [03]
[01] deque              0.0113   100.0   119.3   124.7
[02] list               0.0135    83.8   100.0   104.5
[03] array              0.0141    80.2    95.7   100.0
-------------------------------------------------------------
## 1,000,000件の場合
## parameters:          loop=1000000, cycle=1, extra=0
##                        real    (total    = user    + sys)
list                    0.1296    0.1300    0.1200    0.0100
array                   0.1463    0.1500    0.1500    0.0000
deque                   0.1080    0.1100    0.1000    0.0100

## Ranking                real
deque                   0.1080  (100.0) ********************
list                    0.1296  ( 83.4) *****************
array                   0.1463  ( 73.8) ***************

## Matrix                 real    [01]    [02]    [03]
[01] deque              0.1080   100.0   119.9   135.4
[02] list               0.1296    83.4   100.0   112.9
[03] array              0.1463    73.8    88.6   100.0
"""
with Benchmarker(n, width=20) as bench:
    nay = [i for i in range(n)]
    iay = array('I', [i for i in range(n)])
    day = deque(nay)

    @bench("list")
    def _(bm):
        for i in bm:
            nay.pop()

    @bench("array")
    def _(bm):
        for i in bm:
            iay.pop()

    @bench("deque")
    def _(bm):
        for i in bm:
            day.pop()
