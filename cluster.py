from dask.distributed import LocalCluster
import time
import os
import socket


def create_cluster():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    cluster = LocalCluster(host=ip, n_workers=10, threads_per_worker=1, dashboard_address=80, scheduler_port=1234)
    print('DASHBOARD:', cluster.dashboard_link)
    print('SOCKET:', cluster.scheduler_address)


if __name__ == "__main__":
    create_cluster()
    while True:
        time.sleep(10)

