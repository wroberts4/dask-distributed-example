# dask-distributed-example

Instead of using multiprocessing, use distributed dask! It's much more
cloud friendly and can scale like normal dask.

You will need to change `SOCKET` for whatever ip the cluster.py
command prints for `tcp`. You can then go to localhost and a dashboard will appear.
When you run test.py, you will see dask stats in the plots.

```
$ docker build -t dask-distributed .
$ docker run --rm -it -p 80:80 -p 1234:1234 dask-distributed python /cluster.py
DASHBOARD: http://172.17.0.3:80/status
SOCKET: tcp://172.17.0.3:1234
$ docker run --rm -it -e SOCKET=tcp://172.17.0.3:1234 dask-distributed python /test.py
```
