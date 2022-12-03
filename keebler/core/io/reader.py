import glob
import io
import json
import logging
import os
import zipfile
from pathlib import Path

import hydra
import pandas as pd
import yaml
from omegaconf import DictConfig, OmegaConf

logger = logging.getLogger(__name__)

read_filenames = lambda path: glob.glob(path)  # read_filenames('data/names/*.txt')
read_io = lambda raw_bytes: io.BytesIO(raw_bytes)  # read_io(response.content)
read_home_dir = lambda: os.getenv("HOME")  # expand home directory path
trsfrm_user_home = lambda s: Path(s).expanduser()  # get fully qualifying home path


def read_json(file_path: str, encoding="utf-8") -> dict:
    """
    Reads a JSON File
    :param file_path: file path towards content to read
    :param encoding: encoding representation of file, defaults to utf-8
    :return: dictionary of contents read
    """
    try:
        if Path(file_path).is_file():
            with open(file_path, encoding=encoding) as f:
                data: dict = json.load(f)
            return data
        else:
            logger.error(f"File: {file_path} does not Exist")
    except Exception as e:
        logger.exception(f"Exception Occured Reading File: {file_path}:{e}")


def read_yaml(file_path: str, encoding: str = "utf-8") -> dict:
    """
    Reads a Yaml File
    :param file_path: file path towards content to read
    :param encoding: encoding representation of file, defaults to utf-8
    :return: dictionary of contents read
    """
    try:
        if Path(file_path).is_file():
            with open(file_path, encoding=encoding) as f:
                data: dict = yaml.load(f, Loader=yaml.FullLoader)
                return data
        else:
            logger.error(f"File: {file_path} does not Exist")
    except Exception as e:
        logger.exception(f"Exception Occured Reading File: {file_path}:{e}")


def read_hydra(file_path: str) -> DictConfig:
    """
    Reads a Yaml File
    :param file_path: file path towards content to read
    :return: dictionary configuration
    """
    try:
        if Path(file_path).is_file():
            return OmegaConf.load(file_path)
        else:
            logger.error(f"File: {file_path} does not Exist")
    except Exception as e:
        logger.exception(f"Exception Occured Reading File: {file_path}:{e}")


def read_tabular(file_path: str, **kwargs) -> pd.DataFrame:
    """
    Reads Tabular File Content into a Pandas DataFrame
    :param file_path: file path towards content to read
    :param kwargs: optional keyword arguments
    :return: pandas dataframe
    """
    try:
        if Path(file_path).is_file():
            df = None
            suffix = Path(file_path).suffix
            if ".csv" in suffix:
                # Assume that the user uploaded a CSV file
                df = pd.read_csv(file_path, **kwargs)
            elif ".xls" in suffix or ".xlsx" in suffix:
                # Assume that the user uploaded an excel file
                df = pd.read_excel(file_path, **kwargs)
                return df
        else:
            logger.error(f"File: {file_path} does not Exist")

    except Exception as e:
        logger.exception(f"Exception Occured Reading File: {file_path}:{e}")


def decompress_archive(src_path: str, out_path: str = ".") -> dict:
    """Decompresses a zip archive to a given path

    :param src_path: file path towards content to decompress
    :param out_path: path to decompress to if not current path, defaults to .
    :return: None
    """
    try:
        if Path(src_path).is_file():
            with open(src_path) as ref:
                ref.extractall(out_path)
        else:
            logger.error(f"File: {src_path} does not Exist")
    except Exception as e:
        logger.exception(f"Exception Occured Decompressing File: {src_path}:{e}")
