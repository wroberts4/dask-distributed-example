from dask.distributed import LocalCluster
import time
import os


def create_cluster():
    cluster = LocalCluster(n_workers=10, threads_per_worker=1, dashboard_address=80)
    print(cluster.dashboard_link)
    print(cluster.scheduler_address)


if __name__ == "__main__":
    create_cluster()
    while True:
        time.sleep(10)

