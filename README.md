# About

Just some benchmarks tests for Gunicorn workers, see `Procfile` for details

# Computer

Intel(R) Core(TM) i5-2500 CPU @ 3.30GHz

16GB

# Workers

## runserver (via manage.py just because of reasons)




## sync

    $ ./wrk -t12 -c400 -d30s http://127.0.0.1:8000/
    Running 30s test @ http://127.0.0.1:8000/
      12 threads and 400 connections
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency     3.98s     2.99s   13.08s    62.87%
        Req/Sec    53.83     80.50   271.00     75.23%
      10456 requests in 30.01s, 3.72MB read
      Socket errors: connect 0, read 230, write 0, timeout 3903
    Requests/sec:    348.38
    Transfer/sec:    126.91KB

    $ ab -n 1000 -c 4 http://localhost:8000/
    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        0    0   0.0      0       1
    Processing:     3    4   1.0      4      16
    Waiting:        3    4   1.0      4      16
    Total:          3    4   1.0      4      16



## gevent

    $ ./wrk -t12 -c400 -d30s http://127.0.0.1:8000/
    Running 30s test @ http://127.0.0.1:8000/
      12 threads and 400 connections
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency    24.77s    11.00s   29.72s    83.53%
        Req/Sec   485.35    482.74     1.11k    18.71%
      27152 requests in 30.01s, 9.79MB read
      Socket errors: connect 0, read 0, write 0, timeout 5791
    Requests/sec:    904.64
    Transfer/sec:    333.95KB

    $ ab -n 1000 -c 4 http://localhost:8000/
    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        0    0   0.0      0       0
    Processing:     5    5   1.2      5      20
    Waiting:        4    5   1.2      5      20
    Total:          5    5   1.2      5      20



## eventlet




## tornado

    $ ./wrk -t12 -c400 -d30s http://127.0.0.1:8000/
    Running 30s test @ http://127.0.0.1:8000/
      12 threads and 400 connections
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency   444.39ms   57.81ms 503.32ms   92.68%
        Req/Sec    75.93     38.73   224.00     83.99%
      26318 requests in 30.01s, 7.60MB read
      Socket errors: connect 0, read 0, write 0, timeout 131
    Requests/sec:    877.09
    Transfer/sec:    259.53KB

    $ ab -n 1000 -c 4 http://localhost:8000/
    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        0    0   0.0      0       0
    Processing:     1    5   1.9      4      19
    Waiting:        1    5   1.9      4      19
    Total:          2    5   1.9      4      19

