import sys

from loguru import logger
from .log_levels import LogLevel


def init_logger(log_level: LogLevel) -> None:
    logger.remove()
    logger.add(
        sys.stderr,
        level=log_level.upper(),
        backtrace=True,
        diagnose=True,
        catch=True,
        format="<green>{time:YYYY-MM-DD at HH:mm:ss}</green> | <level>{level}</level> | <white>{file}:{function}:{"
        "line}</white> | "
        "<level>{message}</level>",
        colorize=True,
    )
    logger.level("TRACE", color="<white>")
    logger.level("DEBUG", color="<cyan>")
    logger.level("INFO", color="<cyan>")
    logger.level("SUCCESS", color="<green>")
    logger.level("WARNING", color="<yellow>")
    logger.level("ERROR", color="<light-red>")
    logger.level("CRITICAL", color="<red>")
