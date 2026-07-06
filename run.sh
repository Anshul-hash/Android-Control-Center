#!/bin/bash

set -e

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"

cd "$PROJECT_DIR"

source venv/bin/activate

export PYTHONPATH=src

exec python main.py