import json
import logging
import shutil
from pathlib import Path
from typing import List

import pandas as pd

logger = logging.getLogger(__name__)


def copy_to_dest(src_dir: str, dst_dir):
    """
    Copy Source to Destination
    :param src_dir: path to source directory
    :param dst_dir: path to destination directory
    """
    shutil.copy(src_dir, dst_dir)


def write_json(file_path: str, data: dict, indent: int = 4, encoding="utf-8") -> None:
    """
    Writes dictionary to JSON file
    :param file_path: file path towards content to write
    :param data: data dictionary content to write
    :param indent: formatting indentation, defaults to 4
    :param encoding: encoding representation of file, defaults to utf-8
    :return: None
    """
    # create parent directory if necessary
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    try:
        # writes content to file
        with open(file_path, "w", encoding=encoding) as f:
            json.dump(data, f, indent=indent)

    except Exception as e:
        logger.exception(f"Exception Occured Writing File: {file_path}:{e}")


def write_records_json(file_path: str, records: List[dict], indent: int = 4, encoding="utf-8") -> None:
    """
    Writes list of dictionaries to JSON file
    :param file_path: file path towards content to write
    :param records: list of data dictionaries of content to write
    :param indent: formatting indentation, defaults to 4
    :param encoding: encoding representation of file, defaults to utf-8
    :return: None
    """
    # create parent directory if necessary
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    try:
        # writes content to file
        with open(file_path, "w", encoding=encoding) as f:
            f.write(json.dumps(records, indent=indent))

    except Exception as e:
        logger.exception(f"Exception Occured Writing File: {file_path}:{e}")


def write_csv(df: pd.DataFrame, file_path: str, with_index: bool = False) -> None:
    """
    Writes DataFrame to a given filepath/filename
    :param df: pandas dataframe to write
    :param file_path: file path towards content to write
    :param with_index: boolean indicator if to write index to file, defaults to False
    :return: None
    """
    # create parent directory if necessary
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    try:
        # writes content to file
        df.to_csv(file_path, index=with_index)

    except Exception as e:
        logger.exception(f"Exception Occured Writing File: {file_path}:{e}")
