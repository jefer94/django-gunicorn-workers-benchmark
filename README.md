# About

Just some benchmarks tests for Gunicorn workers, see `Procfile` for details.

Based on https://gist.github.com/andreif/6088558

# Computer

Intel(R) Core(TM) i5-4460  CPU @ 3.20GHz

8GB

# Workers

## runserver (via manage.py just because of reasons, 50MB)

    $ ./wrk -t20 -c40000 -d30s http://127.0.0.1:8000/
    Running 30s test @ http://localhost:8000/
      20 threads and 40000 connections
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency   832.93ms  625.19ms   2.00s    59.43%
        Req/Sec    93.49     89.39   650.00     85.21%
      39449 requests in 30.09s, 16.33MB read
      Socket errors: connect 11770, read 0, write 0, timeout 28007
    Requests/sec:   1311.14
    Transfer/sec:    555.74KB

    $ ab -n 1000 -c 400 http://localhost:8000/
    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        0    0   0.3      0       2
    Processing:     3   10   1.8     10      23
    Waiting:        1    8   1.5      7      20
    Total:          3   10   1.9     10      23


## sync (80MB)

    $ ./wrk -t20 -c40000 -d30s http://127.0.0.1:8000/
    Running 30s test @ http://localhost:8000/
      20 threads and 40000 connections
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency   562.02ms  319.58ms   1.98s    66.84%
        Req/Sec   156.84    146.40   712.00     73.94%
      30728 requests in 30.09s, 12.66MB read
      Socket errors: connect 34770, read 0, write 0, timeout 2089
    Requests/sec:   1021.03
    Transfer/sec:    430.75KB

    $ ab -n 1000 -c 400 http://localhost:8000/
    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        1  119  80.0    114     326
    Processing:     1  198 106.2    185     367
    Waiting:        1  143  80.2    183     277
    Total:        138  318  63.4    326     377


## gevent (110MB)

    $ ./wrk -t20 -c40000 -d30s http://127.0.0.1:8000/
    Running 30s test @ http://localhost:8000/
      20 threads and 40000 connections
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency     7.63ms   92.40ms   1.98s    99.05%
        Req/Sec     1.09k     1.21k    3.25k    74.31%
      55222 requests in 30.10s, 23.01MB read
      Socket errors: connect 32720, read 5922, write 0, timeout 3032
    Requests/sec:   1834.90
    Transfer/sec:    783.07KB

    $ ab -n 1000 -c 400 http://localhost:8000/
    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        1  129  94.4    105     361
    Processing:     1  251 110.5    284     439
    Waiting:        1  168  95.2    169     338
    Total:         19  380 146.3    365     695


## eventlet (150MB)

    $ ./wrk -t20 -c40000 -d30s http://127.0.0.1:8000/
    Running 30s test @ http://localhost:8000/
      20 threads and 40000 connections
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency    35.75ms  221.46ms   2.00s    97.20%
        Req/Sec   250.51    369.27     3.29k    88.90%
      55235 requests in 30.09s, 23.02MB read
      Socket errors: connect 32720, read 6250, write 0, timeout 2884
    Requests/sec:   1835.67
    Transfer/sec:    783.39KB

    $ ab -n 1000 -c 400 http://localhost:8000/
    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        1  127  90.7    119     363
    Processing:     1  218 111.0    198     391
    Waiting:        1  160  81.1    195     293
    Total:         10  345 109.8    363     722


## tornado (445MB - 650MB)

    $ ./wrk -t20 -c40000 -d30s http://127.0.0.1:8000/
    Running 30s test @ http://localhost:8000/
      20 threads and 40000 connections
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency     1.42s    47.14ms   1.51s    77.91%
        Req/Sec   191.94    662.66     6.96k    96.07%
      33568 requests in 30.10s, 12.39MB read
      Socket errors: connect 11770, read 339, write 0, timeout 33405
    Requests/sec:   1115.27
    Transfer/sec:    421.49KB

    $ ab -n 1000 -c 400 http://localhost:8000/
    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        0    1   1.1      0       3
    Processing:     4  152  24.1    165     192
    Waiting:        1  152  24.1    165     192
    Total:          4  153  24.3    166     195


  ## gthread (160MB)

    $ ./wrk -t20 -c40000 -d30s http://127.0.0.1:8000/
    Running 30s test @ http://localhost:8000/ (broke)
      20 threads and 40000 connections
      Thread Stats   Avg      Stdev     Max   +/- Stdev
        Latency     0.00us    0.00us   0.00us    -nan%
        Req/Sec     0.00      0.00     0.00      -nan%
      0 requests in 30.09s, 0.00B read
      Socket errors: connect 11770, read 0, write 0, timeout 0
    Requests/sec:      0.00
    Transfer/sec:       0.00B

    $ ab -n 1000 -c 400 http://localhost:8000/
    Connection Times (ms)
                  min  mean[+/-sd] median   max
    Connect:        0    1   1.5      0       4
    Processing:    19  211  62.3    221     311
    Waiting:       14  211  62.3    221     311
    Total:         19  212  61.6    222     313

