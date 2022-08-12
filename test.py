import multiprocessing
from dask import array as da
import dask.bag as db
from dask.distributed import Client
import dask
import glob
import time
import os


def sleep_one(x, y):
    print(x, y)
    time.sleep(1)
    return x, y


def sleep_two(x, y):
    print(x, y)
    time.sleep(2)
    return x, y


if __name__ == '__main__':
    client = Client(os.environ["SOCKET"])
    num_workers = len(client.scheduler_info()['workers'])
    xs = range(2 * num_workers)
    ys = range(2 * num_workers)

    start = time.time()
    with multiprocessing.Pool(num_workers) as p:
        output1 = p.starmap(sleep_one, zip(xs, ys))
        output2 = p.starmap(sleep_two, zip(xs, ys))
    print((output1, output2))
    print('multiprocessing:', time.time() - start)

    start = time.time()
    npartitions = 2 * num_workers
    dask_xs = db.from_sequence(xs, npartitions=npartitions)
    dask_ys = db.from_sequence(ys, npartitions=npartitions)
    output1 = dask.bag.map(sleep_one, dask_xs, dask_ys)
    output2 = dask.bag.map(sleep_two, dask_xs, dask_ys)
    print(da.compute(output1, output2))
    print('dask:', time.time() - start)
