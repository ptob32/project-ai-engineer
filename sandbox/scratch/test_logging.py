from enterprise_ai_platform.utils.logger import (configure_logging, get_logger, )

configure_logging()

logger = get_logger(__name__)

logger.debug("Debug message")
logger.info("Info message")
logger.warning("Warning message")
logger.error("Error message")