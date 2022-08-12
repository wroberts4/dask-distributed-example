FROM condaforge/mambaforge:4.12.0-0
RUN mamba install -y --strict-channel-priority -c conda-forge python=3.10 dask
COPY cluster.py /cluster.py
COPY test.py /test.py
