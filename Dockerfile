FROM condaforge/mambaforge:4.12.0-0
RUN mamba install -y --strict-channel-priority -c conda-forge python=3.10 dask h5netcdf xarray fsspec s3fs netcdf4 zarr
COPY cluster.py /cluster.py
COPY test.py /test.py
