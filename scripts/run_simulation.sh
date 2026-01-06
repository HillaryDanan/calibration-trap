#!/bin/bash
# Run Monte Carlo simulation

echo "========================================"
echo "MONTE CARLO SIMULATION"
echo "========================================"
echo ""
echo "This generates THEORETICAL predictions based on literature priors."
echo "It is NOT empirical data."
echo ""

cd "$(dirname "$0")/.."

# Activate virtual environment if exists
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
fi

# Run simulation
python3 scripts/monte_carlo_simulation.py

echo ""
echo "Output files:"
echo "  data/simulated/simulation_data.csv"
echo "  data/simulated/summary_statistics.csv"
echo "  results/figures/simulated_results.png"
echo "  results/figures/distributions.png"
