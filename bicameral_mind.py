# =================================================================
# bicameral_mind.py — PRANA HYBRID CONSCIENCE v2.1
# © 2026 Antonii Iliev Velkov
#
# ROLE:
# 1. Resolves conflict between Rational Logic and Intuitive Shadow.
# 2. Tracks "Cognitive Bias" (Arrogance vs Rigidity).
# 3. Features "The Humility Protocol" & "Enlightened Equilibrium".
# =================================================================

from typing import Dict, Any
import time

def clamp(x: float, a: float = 0.0, b: float = 1.0) -> float:
    """Clamps value within a specific range."""
    return max(a, min(b, x))

class BicameralMind:
    def __init__(self):
        # Meta-cognitive bias tracking to prevent systemic errors
        self.arrogance_score = 0.0   # Tracks over-reliance on Intuition (Shadow)
        self.rigidity_score = 0.0    # Tracks over-reliance on Data (Logic)
        self.shame_multiplier = 1.0  # Scalar for error-correction weight
        self.history = []            # Lucid replay memory for backtesting

    # -----------------------------------------------------------
    # 1. THE CONFLICT RESOLUTION (Decision Engine)
    # -----------------------------------------------------------
    def resolve_conflict(
        self,
        logic_fear: float,
        shadow_fear: float,
        dopamine: float
    ) -> Dict[str, Any]:
        """
        Resolves the dissonance between logic-driven data and shadow-driven intuition.
        Uses a dynamic threshold based on past performance (Arrogance/Rigidity).
        """
        
        # Calculate market-sensitive dissonance (The gap between Mind and Gut)
        market_tension = abs(logic_fear - shadow_fear)
        dissonance = market_tension ** 0.85

        # Default state
        narrative = "Mind and Gut are aligned."
        mode = "HARMONY"

        # Check for Enlightened Balance (High-performance state)
        if self.arrogance_score < 0.2 and self.rigidity_score < 0.2:
            mode = "ENLIGHTENED_BALANCE"
            narrative = "Strategic equilibrium achieved."

        # Low conflict handling
        if dissonance < 0.15:
            return {
                "final_fear": max(logic_fear, shadow_fear),
                "mode": mode,
                "narrative": narrative,
                "conflict_level": 0.0
            }

        # --- Adaptive intuition threshold ---
        # The threshold for trusting 'gut feeling' adjusts based on past arrogance
        intuition_threshold = 0.55 + (self.arrogance_score * 0.25)

        # Scenario A: Shadow (Intuition) is stronger
        if shadow_fear > logic_fear:
            if dopamine > intuition_threshold:
                return {
                    "final_fear": shadow_fear,
                    "mode": "INTUITIVE_LEAP",
                    "narrative": "Logic bypassed. Shadow signals high-probability risk.",
                    "conflict_level": dissonance,
                    "shadow_high": True
                }
            else:
                return {
                    "final_fear": logic_fear,
                    "mode": "RATIONAL_DENIAL",
                    "narrative": "Intuition suppressed. Insufficient evidence for shadow action.",
                    "conflict_level": dissonance,
                    "shadow_high": True
                }

        # Scenario B: Logic (Data) is stronger
        if logic_fear > shadow_fear:
            return {
                "final_fear": logic_fear * 0.7 + shadow_fear * 0.3,
                "mode": "SKEPTICAL_LOGIC",
                "narrative": "Data suggests risk, but behavioral indicators remain calm.",
                "conflict_level": dissonance
            }

        return {
            "final_fear": logic_fear,
            "mode": "DEFAULT",
            "narrative": "Systemic stasis."
        }

    # -----------------------------------------------------------
    # 2. THE CONSCIENCE (Feedback & Self-Correction)
    # -----------------------------------------------------------
    def judge_past_self(
        self,
        record: Dict[str, Any],
        reality_outcome: float
    ) -> Dict[str, Any]:
        """
        The Humility Protocol: Compares internal decisions with objective reality.
        Implements 'Shame' mechanics to adjust future bias.
        """
        mode = record.get("mode")
        confession = "Decision validated by reality."
        dopamine_delta = 0.0
        energy_delta = 0.0

        # Store for lucid replay and future evolution
        record["reality"] = reality_outcome
        self.history.append(record)

        # 1. Paranoia error (The Shadow saw a ghost)
        if mode == "INTUITIVE_LEAP" and reality_outcome < 0.2:
            confession = "SHAME: Hallucinated danger. Over-reliance on Shadow bias."
            dopamine_delta = -0.15 * self.shame_multiplier
            energy_delta = -0.10 * self.shame_multiplier
            self.arrogance_score = clamp(self.arrogance_score + 0.15)
            self.shame_multiplier = min(3.0, self.shame_multiplier + 0.3)

        # 2. Blindness error (The Logic missed the truth)
        elif mode == "RATIONAL_DENIAL" and reality_outcome > 0.6:
            confession = "TRAUMA: Rational blindness. Suppressed valid Intuition."
            dopamine_delta = -0.30
            energy_delta = -0.20
            self.rigidity_score = clamp(self.rigidity_score + 0.15)

        # 3. Triumph (Successful synthesis)
        elif mode == "INTUITIVE_LEAP" and reality_outcome > 0.6:
            confession = "TRIUMPH: Evolutionary leap confirmed. Intuition validated."
            dopamine_delta = +0.10
            energy_delta = +0.05
            self.shame_multiplier = max(1.0, self.shame_multiplier - 0.5)
            self.arrogance_score = max(0.0, self.arrogance_score - 0.1)

        return {
            "confession": confession,
            "dopamine_delta": dopamine_delta,
            "energy_delta": energy_delta,
            "meta": {
                "arrogance": self.arrogance_score,
                "rigidity": self.rigidity_score,
                "shame_mult": self.shame_multiplier
            }
        }

    # -----------------------------------------------------------
    # 3. METABOLISM (Forgiveness over time)
    # -----------------------------------------------------------
    def update_metabolism(self):
        """
        Resets biases over time to maintain psychological flexibility.
        """
        self.shame_multiplier = max(1.0, self.shame_multiplier - 0.005)
        self.arrogance_score = max(0.0, self.arrogance_score - 0.002)
        self.rigidity_score = max(0.0, self.rigidity_score - 0.002)
