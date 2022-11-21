import logging
from pathlib import Path

from omegaconf import DictConfig

from .core.io.reader import read_hydra
from .infra.trace import configure_logging
from .version import __version__

root_logger = logging.getLogger("root")


def setup() -> DictConfig:
    """
    Default setup configuration upon module load
    :return:
    """
    # load experiment structure
    conf_folder: str = Path("config")
    # gather experiment structure
    exp_conf: DictConfig = read_hydra(conf_folder.joinpath("experiment.yaml"))
    exp_log_dir: str = exp_conf.experiment.reporting.logs
    # configure logging
    log_conf_path: str = Path(conf_folder).joinpath("logging.yaml")
    configure_logging(file_path=log_conf_path, prefix=exp_log_dir)
    # log information
    root_logger.info(f"{__name__} => Root Logger and Experiment Structure Enabled")
    return exp_conf


exp_conf = setup()
