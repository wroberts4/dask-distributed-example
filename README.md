# dask-distributed-example

Instead of using multiprocessing, use distributed dask! It's much more
cloud friendly and can scale like normal dask.

Currently, there is not way to set the port that the cluster runs on. This
is a bug, so you will need to change `PORT` for whatever port the cluster.py
command prints for `tcp`. You can then go to localhost and a dashboard will appear.
When you run test.py, you will see dask stats in the plots.

```
docker build -t dask-distributed .
docker run --rm -it --network host dask-distributed python /cluster.py
docker run --rm -it --network host -e PORT=58415 dask-distributed python /test.py
```
