import logging
from pathlib import Path

from omegaconf import DictConfig
from rich.logging import RichHandler

from keebler.core.io.reader import read_hydra

logger = logging.getLogger(f"PROGRAM:{__name__}")
# logger.addHandler(RichHandler(markup=True))

if __name__ == "__main__":
    # load experiment and log structure
    conf_folder: str = Path("config/")
    log_conf_path: str = Path(conf_folder).joinpath("logging.yaml")
    # gather experiment structure
    exp_conf: DictConfig = read_hydra(conf_folder.joinpath("experiment.yaml"))
    exp_log_dir: str = exp_conf.experiment.reporting.logs
    # log information, enable a rich handler instead
    logger.info(f"{__name__} => Logger and Experiment Structure Enabled")
