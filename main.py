import pytest

from sdk.utils import logger

logger.initialize()
log_format_configuration = (
    "--log-level", "DEBUG",
    "--log-format", "# %(levelname)-8s [%(asctime)s] %(filename)-20s [LINE:%(lineno)s]   %(message)s",
    "--log-date-format", "%Y-%m-%d %H:%M:%S")

pytest.main(["-v", "--browser=edge", *log_format_configuration])
