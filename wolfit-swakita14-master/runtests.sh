#!/bin/bash
export WOLFIT_SETTINGS=$(pwd)/test.settings
export FLASK_ENV=test
export FLASK_DEBUG=0
pytest tests/unit -x $@
