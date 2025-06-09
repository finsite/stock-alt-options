"""Repo-specific configuration for stock-alt-options."""

from app.config_shared import *


def get_poller_name() -> str:
    return get_config_value("POLLER_NAME", "stock_alt_options")


def get_rabbitmq_queue() -> str:
    return get_config_value("RABBITMQ_QUEUE", "stock_alt_options_queue")


def get_dlq_name() -> str:
    return get_config_value("DLQ_NAME", "stock_alt_options_dlq")


# Optional: Add limits if the processor requires it later
def get_options_contract_limit() -> int:
    return int(get_config_value("OPTIONS_CONTRACT_LIMIT", "100"))
