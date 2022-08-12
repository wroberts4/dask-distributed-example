import multiprocessing
from dask import array as da
import dask.bag as db
from dask.distributed import Client
import dask
import glob
import time
import os


def test_func(x):
    print(x)
    time.sleep(1)
    return x

if __name__ == '__main__':
    client = Client(os.environ["SOCKET"])
    num_workers = len(client.scheduler_info()['workers'])
    input = range(4 * num_workers)

    start = time.time()
    with multiprocessing.Pool(num_workers) as p:
        output = p.map(test_func, input)
    print(output)
    print('multiprocessing:', time.time() - start)

    start = time.time()
    dask_input = db.from_sequence(input, npartitions=2 * num_workers)
    output = dask_input.map(test_func)
    print(da.compute(output))
    print('dask:', time.time() - start)
