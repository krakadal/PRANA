# =================================================================
# shadow_core.py — PRANA SHADOW v2.5 (Architectural Pulse)
# © 2026 Antonii Iliev Velkov
# INNOVATION: Monte Carlo Behavioral Simulation (MCBS)
# =================================================================

import statistics
import random
from typing import Dict

def clamp(x: float, a: float = 0.0, b: float = 1.0) -> float:
    """Clamps the value between a minimum and maximum range."""
    return max(a, min(b, x))

def shadow_step(state: Dict) -> Dict:
    """
    Shadow v2.5: Executes multi-layer Monte Carlo simulations to predict 
    the transition from market denial to mass hysteria.
    
    NOTE: Specific mathematical weights and simulation coefficients 
    have been abstracted in this public repository for IP protection.
    """
    system = state.get("system", {}) or {}
    stress = float(system.get("stress", 0.0))
    velocity = float(system.get("stress_velocity", 0.0))
    energy = float(system.get("energy", 1.0))

    # --- MONTE CARLO BEHAVIORAL SIMULATION (MCBS) ---
    # Simulating 100 possible market 'realities' based on crowd psychology
    num_simulations = 100
    shadow_outcomes = []
    
    # We simulate crowd behavior through variable reaction thresholds
    for _ in range(num_simulations):
        # Stochastic methods are used to determine psychological resilience.
        # This logic simulates the lag between market shocks and mass panic.
        
        # Placeholder for PRANA's proprietary 'Pain Threshold' logic
        # Real-world parameters are injected during private deployment
        sim_outcome = (stress * random.uniform(0.8, 1.2)) - (energy * 0.5)
        shadow_outcomes.append(clamp(sim_outcome))

    # Statistical analysis of the simulated outcomes
    mean_shadow = statistics.mean(shadow_outcomes)
    std_dev = statistics.stdev(shadow_outcomes)
    
    # Calculating the probability of systemic collapse (Hysteria Risk)
    panic_probability = len([x for x in shadow_outcomes if x > 0.6]) / num_simulations

    # Narrative Interpretation (The Voice of the Shadow)
    if panic_probability > 0.7:
        interpretation = "CRITICAL HYSTERIA DETECTED"
    elif velocity > 0.4:
        interpretation = "FOMO ACCELERATION"
    else:
        interpretation = "STABLE BEHAVIORAL DRIFT"

    return {
        "shadow_fear": round(mean_shadow, 3),
        "panic_probability": round(panic_probability * 100, 1),
        "uncertainty_index": round(std_dev, 4),
        "interpretation": interpretation,
        "status": "MCBS_ENCRYPTED_LOGIC"
    }
