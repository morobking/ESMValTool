"""Script to download Duveiller2018 from its webpage."""
import logging

from esmvaltool.cmorizers.data.downloaders.wget import WGetDownloader
from esmvaltool.cmorizers.data.utilities import (
    unpack_files_in_folder, read_cmor_config)

logger = logging.getLogger(__name__)


def download_dataset(config, dataset, _, __, overwrite):
    """
    Download dataset.

    Parameters
    ----------
    config : dict
        ESMValTool's user configuration
    dataset : str
        Name of the dataset
    start_date : datetime
        Start of the interval to download
    end_date : datetime
        End of the interval to download
    overwrite : bool
        Overwrite already downloaded files
    """
    downloader = WGetDownloader(
        config=config,
        dataset=dataset,
        overwrite=overwrite,
    )
    downloader.tier = 2
    cmor_config = read_cmor_config(dataset)
    raw_path = (
        "https://opendata.dwd.de/climate_environment/GPCC/"
        "full_data_2018/full_data_monthly_{version}.nc.gz"
    )
    for version in cmor_config['attributes']['version'].values():
        downloader.download_file(
            raw_path.format(version=version),
            wget_options=[]

        )
    unpack_files_in_folder(downloader.local_folder)
