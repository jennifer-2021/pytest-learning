# -*- coding: utf-8 -*-
from collections import defaultdict

import pytest

durations = defaultdict(dict)
slow = 3.0

def pytest_addoption(parser):
    parser.addoption(
        "--slow",
        action="store",
        default="N",
        help="'Default 'No' for slow, option: Y or N"
    )


def pytest_configure(config):
    durations.update(
        config.cache.get("cache/case_duration", defaultdict(dict))
    )

def pytest_runtest_logreport(report):
    durations[report.nodeid][report.when] = report.duration

@pytest.mark.tryfirst
def pytest_collection_modifyitems( session, config, items):
    if config.getoption("--slow") == "Y":
        for item in items:
            duration = sum(durations[item.nodeid].values())
            if duration > slow:
                item.add_marker(pytest.mark.slow)

def pytest_sessionfinish(session):
    session.config.cache.set("cache/case_duration", durations)
