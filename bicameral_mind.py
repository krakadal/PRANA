# bicameral_mind.py — PRANA HYBRID CONSCIENCE v2.1 (FINAL POLISH)
# © 2025 Антоний Илиев Велков & Gemini AI
#
# ROLE:
# 1. Resolves conflict between Logic and Shadow using Dopamine.
# 2. Tracks "Cognitive Bias" (Arrogance vs Rigidity).
# 3. Features "The Humility Protocol" & "Enlightened Balance".

from typing import Dict, Any
import time

def clamp(x: float, a: float = 0.0, b: float = 1.0) -> float:
    return max(a, min(b, x))


class BicameralMind:
    def __init__(self):
        # Meta-cognitive bias tracking
        self.arrogance_score = 0.0   # Shadow errors
        self.rigidity_score = 0.0    # Logic errors
        self.shame_multiplier = 1.0
        self.history = []            # Lucid replay memory

    # -----------------------------------------------------------
    # 1. THE CONFLICT (Dopamine + Meta-filter)
    # -----------------------------------------------------------
    def resolve_conflict(
        self,
        logic_fear: float,
        shadow_fear: float,
        dopamine: float
    ) -> Dict[str, Any]:

        # --- MARKET-SENSITIVE DISSONANCE (mild) ---
        market_tension = abs(logic_fear - shadow_fear)
        dissonance = market_tension ** 0.85

        # Default enlightened mode
        narrative = "Mind and Gut are aligned."
        mode = "HARMONY"

        if self.arrogance_score < 0.2 and self.rigidity_score < 0.2:
            mode = "ENLIGHTENED_BALANCE"
            narrative = "I have achieved equilibrium."

        if dissonance < 0.15:
            return {
                "final_fear": max(logic_fear, shadow_fear),
                "mode": mode,
                "narrative": narrative,
                "conflict_level": 0.0
            }

        # --- Adaptive intuition threshold (balanced sensitivity) ---
        intuition_threshold = 0.55 + (self.arrogance_score * 0.25)

        # Scenario A: Shadow dominates (intuition)
        if shadow_fear > logic_fear:
            if dopamine > intuition_threshold:
                return {
                    "final_fear": shadow_fear,
                    "mode": "INTUITIVE_LEAP",
                    "narrative": "Ignoring logic. The Shadow signals danger.",
                    "conflict_level": dissonance,
                    "shadow_high": True
                }
            else:
                return {
                    "final_fear": logic_fear,
                    "mode": "RATIONAL_DENIAL",
                    "narrative": "Shadow ignored. Logic demands evidence.",
                    "conflict_level": dissonance,
                    "shadow_high": True
                }

        # Scenario B: Logic dominates
        if logic_fear > shadow_fear:
            return {
                "final_fear": logic_fear * 0.7 + shadow_fear * 0.3,
                "mode": "SKEPTICAL_LOGIC",
                "narrative": "Data suggests risk, instincts remain calm.",
                "conflict_level": dissonance
            }

        return {
            "final_fear": logic_fear,
            "mode": "DEFAULT",
            "narrative": "Static."
        }

    # -----------------------------------------------------------
    # 2. THE CONSCIENCE (Shame, Memory, Forgiveness)
    # -----------------------------------------------------------
    def judge_past_self(
        self,
        record: Dict[str, Any],
        reality_outcome: float
    ) -> Dict[str, Any]:

        mode = record.get("mode")
        confession = "No significant regret."
        dopamine_delta = 0.0
        energy_delta = 0.0

        # Store for lucid replay
        record["reality"] = reality_outcome
        self.history.append(record)

        # 1. Paranoia error (Shadow failed)
        if mode == "INTUITIVE_LEAP" and reality_outcome < 0.2:
            confession = "SHAME: I hallucinated the storm. My ego misled me."
            dopamine_delta = -0.15 * self.shame_multiplier
            energy_delta = -0.10 * self.shame_multiplier
            self.arrogance_score = clamp(self.arrogance_score + 0.15)
            self.shame_multiplier = min(3.0, self.shame_multiplier + 0.3)

        # 2. Blindness error (Logic failed)
        elif mode == "RATIONAL_DENIAL" and reality_outcome > 0.6:
            confession = "TRAUMA: I was blind. My intuition warned me."
            dopamine_delta = -0.30
            energy_delta = -0.20
            self.rigidity_score = clamp(self.rigidity_score + 0.15)

        # 3. Triumph (intuition confirmed)
        elif mode == "INTUITIVE_LEAP" and reality_outcome > 0.6:
            confession = "TRIUMPH: Evolution confirmed. My gut was right."
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
    # 3. TIME RECOVERY (Forgiveness over time)
    # -----------------------------------------------------------
    def update_metabolism(self):
        """
        Called every cycle or during stasis.
        Slowly resets shame and cognitive bias.
        """
        self.shame_multiplier = max(1.0, self.shame_multiplier - 0.005)
        self.arrogance_score = max(0.0, self.arrogance_score - 0.002)
        self.rigidity_score = max(0.0, self.rigidity_score - 0.002)
