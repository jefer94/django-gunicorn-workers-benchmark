# About

Just some benchmarks tests for Gunicorn workers, see `Procfile` for details.

Based on https://gist.github.com/andreif/6088558

# Computer

Intel(R) Core(TM) i5-4460  CPU @ 3.20GHz

8GB

# Workers

## runserver (via manage.py just because of reasons)

    $ ./wrk -t12 -c400 -d30s http://127.0.0.1:8000/
    Running 30s test @ http://127.0.0.1:8000/
      12 threads and 400 connections
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency     0.00us    0.00us   0.00us    -nan%
        Req/Sec     0.00      0.00     0.00      -nan%
      0 requests in 30.02s, 3.94MB read
      Socket errors: connect 0, read 12982, write 0, timeout 3997
    Requests/sec:      0.00
    Transfer/sec:    134.33KB

    $ ab -n 1000 -c 4 http://localhost:8000/
    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        0    0   0.0      0       0
    Processing:     2   10   2.9      9      25
    Waiting:        2    9   2.7      8      23
    Total:          2   10   2.9     10      25


## sync

    $ ./wrk -t12 -c400 -d30s http://127.0.0.1:8000/
    Running 30s test @ http://127.0.0.1:8000/
      12 threads and 400 connections
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency     5.46s     8.36s   26.30s    87.42%
        Req/Sec    79.14    101.27   298.00     69.16%
      17322 requests in 30.01s, 6.16MB read
      Socket errors: connect 0, read 184, write 0, timeout 3593
    Requests/sec:    577.24
    Transfer/sec:    210.27KB

    $ ab -n 1000 -c 4 http://localhost:8000/
    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        0    0   0.0      0       0
    Processing:     1    4   1.0      4      18
    Waiting:        1    4   1.0      4      18
    Total:          1    4   1.1      4      18


## gevent

    $ ./wrk -t12 -c400 -d30s http://127.0.0.1:8000/
    Running 30s test @ http://127.0.0.1:8000/
      12 threads and 400 connections
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency    24.60s    10.63s   29.20s    84.26%
        Req/Sec   535.94    528.13     1.33k    20.69%
      29415 requests in 30.07s, 10.60MB read
      Socket errors: connect 0, read 62, write 0, timeout 5515
      Non-2xx or 3xx responses: 1
    Requests/sec:    978.37
    Transfer/sec:    361.15KB

    $ ab -n 1000 -c 4 http://localhost:8000/
    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        0    0   0.0      0       0
    Processing:     2    5   1.2      5      18
    Waiting:        1    5   1.2      5      18
    Total:          2    5   1.2      5      18


## eventlet

    $ ./wrk -t12 -c400 -d30s http://127.0.0.1:8000/
    Running 30s test @ http://127.0.0.1:8000/
      12 threads and 400 connections
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency    22.18s    11.17s   29.12s    79.80%
        Req/Sec   483.90    473.59     1.33k    26.67%
      25098 requests in 30.01s, 9.05MB read
      Socket errors: connect 0, read 324, write 0, timeout 5557
    Requests/sec:    836.31
    Transfer/sec:    308.72KB

    $ ab -n 1000 -c 4 http://localhost:8000/
    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        0    0   0.0      0       0
    Processing:     4    5   1.1      5      17
    Waiting:        4    5   1.1      5      17
    Total:          4    5   1.1      5      17


## tornado

    $ ./wrk -t12 -c400 -d30s http://127.0.0.1:8000/
    Running 30s test @ http://127.0.0.1:8000/
      12 threads and 400 connections
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency   505.63ms  126.52ms 711.74ms   69.13%
        Req/Sec    71.24     43.08   238.00     52.78%
      25157 requests in 30.01s, 7.27MB read
      Socket errors: connect 0, read 0, write 0, timeout 98
    Requests/sec:    838.41
    Transfer/sec:    248.09KB


    $ ab -n 1000 -c 4 http://localhost:8000/
    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        0    0   0.0      0       0
    Processing:     1    4   1.8      4      23
    Waiting:        1    4   1.8      4      23
    Total:          1    4   1.8      4      23
