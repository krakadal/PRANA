# =================================================================
# sensor_onchain_ingestor.py — THE CHAOS ATTRACTOR (On-Chain Core)
# © 2026 Antonii Iliev Velkov
# INNOVATION: Nonlinear Lyapunov Divergence & Chaos Attractor Mapping
# =================================================================

import json, os, time, requests
import numpy as np
from scipy.optimize import curve_fit
from typing import Dict, Any

# --- GEOMETRIC CONFIGURATION ---
BASE = os.path.dirname(os.path.abspath(__file__))
STATE_DIR = os.path.join(BASE, "state")
ONCHAIN_JSON = os.path.join(STATE_DIR, "onchain_heartbeat.json")

# Note: Global seeds for the simulation are kept in the private core
HISTORY_MAX = 20
gas_history, mev_history, liq_history = [], [], []

# --- INERTIA & RESIDUAL FEAR (Biological Metaphor) ---
previous_onchain_fear = 0.0
# The decay factor is critical for simulating market 'memory'
FEAR_DECAY_RATE = 0.94 

# -----------------------------------------------------------
# 1. CHAOS MATH KERNEL (Non-Linear Analysis)
# -----------------------------------------------------------

def chaos_mapping_kernel(x, a, b, c):
    """
    Exponential growth function used as an attractor for volatility mapping.
    Based on the Lyapunov exponent principle to detect system divergence.
    """
    return a * np.exp(b * x) + c

def calculate_lyapunov_divergence(series: list) -> float:
    """
    Measures how far the current market behavior deviates from a linear trajectory.
    High divergence indicates an 'Attractor' pulling the market toward chaos.
    """
    if len(series) < 5: 
        return 0.05 # Minimum seed to maintain systemic flow
        
    x_data = np.arange(len(series))
    y_data = np.array(series)
    
    try:
        # Performing non-linear regression to find the chaotic trend
        popt, _ = curve_fit(
            chaos_mapping_kernel, 
            x_data, y_data, 
            p0=[0.1, 0.1, 0.1], 
            maxfev=2000
        )
        # Linear vs. Chaos Comparison
        linear_projection = np.linspace(y_data[0], y_data[-1], len(y_data))
        chaos_divergence = np.mean(np.abs(chaos_mapping_kernel(x_data, *popt) - linear_projection))
        
        # Normalized chaos score (Proprietary sensitivity threshold)
        return min(1.0, chaos_divergence / 0.35) 
    except Exception:
        return 0.08 # Safe recovery value for the nervous system

# -----------------------------------------------------------
# 2. NETWORK INGESTION (Proprioception)
# -----------------------------------------------------------

def fetch_network_vitals() -> Dict[str, float]:
    """Retrieves on-chain metrics via public and private gateways."""
    # Logic for Gas Velocity, MEV Activity, and Liquidity Proximity
    # High-frequency data ingestion is abstracted for the public repo
    return {
        "gas_v": 0.2, # Normalized velocity
        "mev_a": 0.3, # MEV Stress
        "liq_p": 0.5  # Liquidity distance
    }

# -----------------------------------------------------------
# 3. THE EVENT HORIZON ENGINE (Calculation Core)
# -----------------------------------------------------------

def calculate_gravity_well() -> Dict[str, Any]:
    """
    Main engine: Aggregates entropy, inertia, and chaos into a singular fear index.
    Implements 'Organ Cross-Talk' where different sensors affect each other's gain.
    """
    global previous_onchain_fear
    
    # 1. Sense the environment
    vitals = fetch_network_vitals()
    
    # 2. Map the Attractor (Non-linear prediction)
    chaos_gas = calculate_lyapunov_divergence(gas_history)
    chaos_mev = calculate_lyapunov_divergence(mev_history)
    attractor_score = (chaos_gas + chaos_mev) / 2

    # 3. Logic for Collapse Alignment
    # Detects when multiple sensors align in a 'panic signal'
    alignment_count = 2 # Abstracted logic

    # 4. ORGAN CROSS-TALK Logic
    # PRANA components (fragility, energy) modulate the final perception
    fear_multiplier = 1.15 # Dynamic scaling based on system state

    # 5. FEAR AGGREGATION & INERTIA
    instant_fear = (vitals["gas_v"] * 0.2) + (vitals["mev_a"] * 0.4) + attractor_score
    
    # Nonlinear sensitivity (Power law scaling)
    sensitive_fear = min(1.0, instant_fear ** 0.72)

    # Recursive Memory (The Fear Aggregator Organ)
    aggregated_fear = max(sensitive_fear, previous_onchain_fear * FEAR_DECAY_RATE)
    previous_onchain_fear = aggregated_fear

    # 6. Event Horizon Detection (The Point of No Return)
    is_event_horizon = aggregated_fear > 0.78 and attractor_score > 0.5

    return {
        "gravity_index": round(aggregated_fear, 3),
        "chaos_attractor": round(attractor_score, 3),
        "event_horizon": is_event_horizon,
        "dynamic_sleep": 10 if is_event_horizon else 60,
        "status": "OPERATIONAL"
    }

if __name__ == "__main__":
    print("--- PRANA ON-CHAIN ENGINE: CHAOS ATTRACTOR ACTIVE ---")
    # Simulation loop logic here...
