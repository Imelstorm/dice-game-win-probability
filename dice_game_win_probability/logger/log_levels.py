from enum import Enum


class LogLevel(str, Enum):
    CRITICAL = "critical"
    FATAL = "fatal"
    ERRORS = "errors"
    WARN = "warn"
    WARNING = "warning"
    INFO = "info"
    DEBUG = "debug"
