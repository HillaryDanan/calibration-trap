#!/bin/bash
# Run pilot study (n=10 per condition)

echo "========================================"
echo "PROTOCOL A: PILOT STUDY (n=10)"
echo "========================================"
echo ""
echo "This will run 10 trials per condition per model."
echo "Estimated cost: \$1-3"
echo "Estimated time: ~3 minutes"
echo ""

cd "$(dirname "$0")/.."

# Activate virtual environment if exists
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
fi

# Run pilot
python3 src/run_experiment.py --n 10 "$@"
