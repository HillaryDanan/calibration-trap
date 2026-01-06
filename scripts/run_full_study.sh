#!/bin/bash
# Run full study (n=50 per condition)

echo "========================================"
echo "PROTOCOL A: FULL STUDY (n=50)"
echo "========================================"
echo ""
echo "This will run 50 trials per condition per model."
echo "Estimated cost: \$5-15"
echo "Estimated time: ~10 minutes"
echo ""

cd "$(dirname "$0")/.."

# Activate virtual environment if exists
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
fi

# Run full study
python3 src/run_experiment.py --n 50 "$@"

echo ""
echo "========================================"
echo "NEXT STEPS"
echo "========================================"
echo "1. Run embedding analysis:"
echo "   python3 src/analysis/embeddings.py"
echo ""
echo "2. Run keyword analysis (secondary):"
echo "   python3 src/analysis/keywords.py"
