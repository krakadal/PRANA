# =================================================================
# thalamic_junction.py — PRANA RECURSIVE SUBCONSCIOUS v2.0
# © 2026 Antonii Iliev Velkov
# INNOVATION: Nervous Tension Analysis & Circadian Rhythm Integration
# =================================================================

import time
import math
import torch
import torch.nn as nn
from typing import Dict, Any, List

# ─────────────────────────────────────────────────────────────────
# SECTION 1: NEURAL ARCHITECTURE (THE SUBCONSCIOUS BRAIN)
# ─────────────────────────────────────────────────────────────────

class SubconsciousBrain(nn.Module):
    def __init__(self, input_dim=12): 
        """
        Neural core designed to process 12 dimensions of market proprioception:
        Values, Deltas, Nervous Tension, and Circadian Rhythms.
        """
        super().__init__()
        self.network = nn.Sequential(
            nn.Linear(input_dim, 32),
            nn.Tanh(), # Biological saturation function (Tanh handles non-linear limits)
            nn.Linear(32, 16),
            nn.ReLU(),
            nn.Linear(16, 4) # Outputs: [Action_Potential, Sensory_Gain, Energy_Gate, Mood_Tone]
        )

    def forward(self, x):
        return self.network(x)

# Initialization of the neural engine
brain = SubconsciousBrain(input_dim=12)
optimizer = torch.optim.Adam(brain.parameters(), lr=0.001)

# ─────────────────────────────────────────────────────────────────
# SECTION 2: PULSE GENERATION & CIRCADIAN RHYTHM
# ─────────────────────────────────────────────────────────────────

def generate_impulse(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generates the primary scanning pulse with an integrated 'Bio-Rhythm'.
    PRANA experiences natural peaks and troughs in energy, simulating organic life.
    """
    now = time.time()
    
    # Innovation: Circadian Cycle (Sinusoidal activity wave)
    # Simulates a ~6.28 hour energy cycle based on systemic time
    rhythm = (math.sin(now / 3600) + 1) / 2 
    
    return {
        "voltage": float(state.get("system", {}).get("energy", 1.0)) * (0.8 + 0.2 * rhythm),
        "echo": {}, 
        "rhythm_phase": round(rhythm, 3),
        "ts": now
    }

# ─────────────────────────────────────────────────────────────────
# SECTION 3: DIFFERENTIAL NERVOUS ANALYSIS (SOUL LOGIC)
# ─────────────────────────────────────────────────────────────────

def process_echo(current_pulse: Dict[str, Any], last_pulse: Dict[str, Any]) -> Dict[str, float]:
    """
    ML Analysis of organ 'Echoes'. 
    Detects 'Nervous Tension' by analyzing the acceleration of change (Systemic Jitter).
    """
    keys = ["stress", "entropy", "toxicity", "glycogen", "predictive_error"]
    
    # 1. Capture current sensor values
    current_vals = [float(current_pulse["echo"].get(k, 0.0)) for k in keys]
    
    # 2. Calculate Deltas and Nervous Tension (High-frequency drift)
    if last_pulse:
        last_vals = [float(last_pulse["echo"].get(k, 0.0)) for k in keys]
        deltas = [c - l for c, l in zip(current_vals, last_vals)]
        # Innovation: Tension is the sum of absolute accelerations in data drift
        tension = sum([abs(d) for d in deltas])
    else:
        deltas = [0.0] * len(keys)
        tension = 0.0

    # 3. Construct Input Vector (12-dimensions: Values + Deltas + Tension + Rhythm)
    input_vector = torch.tensor(current_vals + deltas + [tension, current_pulse.get("rhythm_phase", 0.5)]).float().view(1, -1)

    # 4. Neural Inference
    brain.eval()
    with torch.no_grad():
        prediction = brain(input_vector).squeeze().tolist()

    # 5. Transform Inference into Biological Commands
    return {
        "action_potential": round(clamp(prediction[0]), 3), # Threshold to initiate action
        "sensory_gain": round(clamp(prediction[1] + (tension * 0.2)), 3), # Tension sharpens awareness
        "energy_gate": round(clamp(prediction[2]), 3), # Resource allocation gate
        "mood_tone": round(prediction[3], 3), # Internal "state of being" (Sentiment bias)
        "nervous_tension": round(tension, 4)
    }

# ─────────────────────────────────────────────────────────────────
# SECTION 4: REINFORCEMENT & EVOLUTIONARY REPLAY
# ─────────────────────────────────────────────────────────────────

def update_subconscious(reward: float, last_input_vector: torch.Tensor):
    """
    Reinforcement learning logic for the subconscious core.
    Strengthens neural pathways associated with positive survival outcomes.
    """
    brain.train()
    # Strategic logic for lucid replay integration is protected here
    pass

# ─────────────────────────────────────────────────────────────────
# SECTION 5: UTILITIES
# ─────────────────────────────────────────────────────────────────
def clamp(x, a=0.0, b=1.0):
    return max(a, min(b, float(x)))

if __name__ == "__main__":
    print("🧠 PRANA RECURSIVE SUBCONSCIOUS v2.0 - Neural Core: OPERATIONAL.")