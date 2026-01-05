# =================================================================
# prana_core.py — PRANA RELATIVISTIC CORE v12.9 (FINAL MONOLITH)
# © 2026 Антоний Илиев Велков
# INTEGRATION: Neural Tensor + Aggressive On-chain Cardiogram
# =================================================================

import statistics
import random
import math
import time
from collections import deque
from typing import Dict, Any, Optional

# --- Neural Bus Integration ---
try:
    from neural_bus import emit as bus_emit
    HAS_BUS_EMIT = True
except Exception:
    HAS_BUS_EMIT = False
    bus_emit = None

# ─────────────────────────────────────────────────────────────────
# SECTION 1: CORE UTILS & MATH
# ─────────────────────────────────────────────────────────────────

def clamp(x: float, a: float = 0.0, b: float = 1.0) -> float:
    return max(a, min(b, x))

def _safe_float(x, default: float = 0.0) -> float:
    try:
        return float(x)
    except:
        return default

def _pick_change(c: Dict[str, Any]) -> Optional[float]:
    for k in ("price_change_pct_1h", "price_change_pct_24h", "price_change_pct_7d"):
        v = c.get(k)
        if v is not None:
            try:
                return float(v)
            except:
                continue
    return None

def _extract_changes(tick: Dict[str, Any]) -> list:
    changes = []
    coins = tick.get("coins") or {}
    for c in coins.values():
        ch = _pick_change(c)
        if ch is not None:
            changes.append(max(-80.0, min(80.0, float(ch))))
    return changes

def _baseline_buf(prev_state: Dict[str, Any], cfg: Dict[str, Any]) -> deque:
    mem = (prev_state or {}).get("_memory") or {}
    buf_list = mem.get("changes_mean_buf") or []
    win = int(cfg.get("baseline_window", 60))
    return deque(buf_list, maxlen=max(10, min(5000, win)))

# ─────────────────────────────────────────────────────────────────
# SECTION 2: SENSORY & NEUROBIOLOGY (The Cardiogram)
# ─────────────────────────────────────────────────────────────────

def real_ingestors(current_prices: Dict, prev_prices: Dict) -> Dict[str, float]:
    """ИНОВАЦИЯ: Агресивна кардиограма с усилвател за микро-делти."""
    diffs = []
    for k in current_prices:
        if k in prev_prices and isinstance(current_prices[k], (int, float)):
            delta = abs(current_prices[k] - prev_prices[k]) / (prev_prices[k] + 1e-9)
            # УСИЛВАТЕЛ: Правим ядрото чувствително към малки трептения
            boosted_delta = delta * 15.0 if delta > 0.0005 else delta
            diffs.append(boosted_delta)
    
    market_stress = statistics.mean(diffs) * 300 if diffs else 0.05
    return {
        "onchain": clamp(market_stress * 2.5, 0.05, 0.95),
        "liquidations": clamp(market_stress * 6.0, 0.05, 0.95),
        "chaos_attractor": clamp(market_stress * 1.2, 0.0, 0.6)
    }

def neuro_evolution(prev_neuro: Dict, surprise: float, velocity: float, fatigue: float, entropy: float) -> Dict[str, float]:
    dop_base = prev_neuro.get("dopamine", 0.5)
    ser_base = prev_neuro.get("serotonin", 0.5)
    
    dopamine = clamp(dop_base + (surprise * 0.12) - (fatigue * 0.05))
    serotonin = clamp(ser_base + (0.02 if abs(velocity) < 0.05 else -0.04))
    adrenaline = clamp(abs(velocity) * 4.5 + entropy * 0.4)
    
    return {"dopamine": dopamine, "serotonin": serotonin, "adrenaline": adrenaline}

def vascular_step(stress: float, entropy: float) -> Dict[str, float]:
    rbc = clamp(1.0 - stress * 0.3)
    wbc = clamp(entropy * 0.4)
    inflammation = clamp(wbc * 0.5 + stress * 0.2)
    return {"rbc": rbc, "wbc": wbc, "inflammation": inflammation}

# ─────────────────────────────────────────────────────────────────
# SECTION 3: SHADOW & QUANTUM LAYERS
# ─────────────────────────────────────────────────────────────────

def shadow_core(stress: float, velocity: float, fragility: float) -> Dict[str, Any]:
    outcomes = [clamp(stress + velocity * random.uniform(-1, 2) + random.uniform(-0.1, 0.1) * fragility) for _ in range(12)]
    panic_prob = sum(1 for o in outcomes if o > 0.72) / 12
    interpretation = "COLLAPSE" if panic_prob > 0.5 else "STABLE_SHIFT" if panic_prob > 0.2 else "NEUTRAL"
    return {
        "worlds": outcomes,
        "shadow_fear": clamp(stress * 0.85 + panic_prob * 0.4), 
        "interpretation": interpretation,
        "panic_prob": panic_prob
    }

def temporal_consensus(prev_prices: Dict, current_prices: Dict) -> Dict[str, Any]:
    changes = [abs(current_prices.get(k, 0) - prev_prices.get(k, 1e-6)) / (prev_prices.get(k, 1e-6) + 1e-9) 
               for k in current_prices if k in prev_prices]
    minority_hits = sum(1 for c in changes if c > 0.05)
    return {"status": "TRUTH_MIGRATION" if minority_hits > 2 else "CONSENSUS_STABLE", "minority_hits": minority_hits}

# ─────────────────────────────────────────────────────────────────
# SECTION 4: NARRATIVE & MODULATIONS
# ─────────────────────────────────────────────────────────────────

def generate_conscience(state: dict) -> str:
    override = state.get("narrative_override")
    if override == "CATHARSIS COMPLETE": return "Purging the trauma..."
    if override == "STASIS_RECHARGING" or state.get("system", {}).get("in_stasis"): return "Entering the void to recharge."
    
    neuro = state.get("neurochemistry", {})
    dopamine = float(neuro.get("dopamine", 0.5))
    fear = float(state.get("fear_index", 0.0))

    if fear > 0.75: return "Systemic shock approaching. Monte Carlo paths are collapsing."
    if dopamine > 0.8: return "Neural harmony achieved."
    return "Observing the flow. All systems operational."

def internal_thought(system: Dict[str, Any], latent: Dict[str, Any], cfg: Dict[str, Any]):
    stress = _safe_float(system.get("stress", 0.0))
    ent = _safe_float(system.get("entropy", 0.0))
    tension = clamp(0.4 * stress + 0.3 * ent + 0.3 * latent.get("asa_amp", 1.0)/5.0)
    clarity = clamp(1.0 - tension)
    thought = "STASIS_RECHARGING" if system.get("in_stasis") else ("HIGH_TENSION" if tension > 0.7 else "OBSERVING")
    return {"tension": round(tension, 3), "clarity": round(clarity, 3), "thought": thought}, {}

def apply_scar_damping(system: Dict[str, Any], scars: list) -> Dict[str, Any]:
    if not scars: return system
    active = [s for s in scars if s.get("state") == "active"]
    integrated = [s for s in scars if s.get("state") == "integrated"]
    entropy_damp = 1.0 - min(0.25, 0.05 * len(active))
    energy_boost = min(0.15, 0.03 * len(integrated))
    system["entropy"] = clamp(system.get("entropy", 0.0) * entropy_damp)
    system["energy"] = clamp(system.get("energy", 1.0) + energy_boost)
    return system

def apply_ghost_pre_echo(system: Dict[str, Any], prev_state: Dict[str, Any]) -> Dict[str, Any]:
    q_fear = prev_state.get("shadow", {})
    worlds = q_fear.get("worlds", [])
    if worlds and len([w for w in worlds if w > 0.70]) >= 2:
        system["entropy"] = clamp(system.get("entropy", 0.0) * 1.25)
        system["_ghost_active"] = True
    else:
        system["_ghost_active"] = False
    return system

# ─────────────────────────────────────────────────────────────────
# SECTION 5: THE CORE ENGINE (PRANA STEP)
# ─────────────────────────────────────────────────────────────────

memory_history = deque(maxlen=30) 

def prana_step(tick: Dict[str, Any], prev_state: Optional[Dict[str, Any]], cfg: Optional[Dict[str, Any]] = None, genome=None) -> Dict[str, Any]:
    cfg = cfg or {}
    prev_state = prev_state or {}
    prev_sys = prev_state.get("system") or {}

    # 1. ПАМЕТ И ДЕФИНИЦИИ (NameError Prevention)
    prev_neuro = prev_state.get("neurochemistry", {"dopamine": 0.5, "serotonin": 0.5, "adrenaline": 0.1})
    prev_prices = prev_state.get("prices", {})
    prev_stress = _safe_float(prev_sys.get("stress", 0.15))
    prev_entropy = _safe_float(prev_sys.get("entropy", 0.10))
    prev_energy = _safe_float(prev_sys.get("energy", 1.0))
    prev_velocity = _safe_float(prev_sys.get("stress_velocity", 0.0))
    prev_fatigue = _safe_float(prev_sys.get("fatigue", 0.0))
    prev_shadow_fear = _safe_float(prev_state.get("shadow", {}).get("shadow_fear", 0.1))

    # 2. СЕНЗОРИ И ЦЕНИ (Current Market Access)
    current_prices = {k: v.get("price") for k, v in (tick.get("coins") or {}).items()}
    ingestors = real_ingestors(current_prices, prev_prices)
    buf = _baseline_buf(prev_state, cfg)
    changes = _extract_changes(tick)
    
    mean_ch = statistics.mean(changes) if changes else 0.0
    stdev_ch = statistics.pstdev(changes) if len(changes) > 1 else 0.0
    buf.append(float(mean_ch))
    baseline = statistics.mean(buf) if len(buf) >= 5 else float(mean_ch)

    # 3. ЕНТРОПИЯ
    vol_signal = clamp(stdev_ch / 2.0)
    entropy = clamp(prev_entropy * 0.88 + vol_signal * 0.40) if prev_entropy >= 0.03 else max(0.0, prev_entropy * 0.70 + random.uniform(0.0, 0.001))
    neg_pressure = sum(1 for c in changes if c < 0) / max(1, len(changes))
    entropy = clamp((entropy + neg_pressure * 0.15) * 0.80)

    # 4. СТРЕС И ПАРАМЕТРИ (FIXED SYNTAX)
    worse = max(0.0, float(baseline) - float(mean_ch))
    pain_gate = _safe_float(cfg.get("pain_gate", 0.22))
    pain = clamp((worse - pain_gate) / _safe_float(cfg.get("pain_scale", 4.5))) if worse > pain_gate else 0.0
    
    fragility = clamp((0.22 - entropy) * 4.5) if mean_ch > -0.05 and entropy < 0.22 else 0.0
    surprise = clamp((baseline - mean_ch) / (abs(baseline) + pain_gate + 1e-6))
    asa_amp = 1.0 + 2.8 * fragility * surprise
    
    # Дефинираме pain_eff и coherence за да няма NameError
    pain_eff = pain * asa_amp
    coherence = sum(1 for c in changes if c < -2.0) / max(1, len(changes))

    # Stress Target интегриран с Кардиограмата
    stress_target = clamp(
        0.4 * pain_eff + 
        0.2 * entropy + 
        0.2 * ingestors["onchain"] + 
        0.2 * ingestors["liquidations"]
    )
    
    alpha = 1.0 if (coherence * 1.6) > 0.35 else (_safe_float(cfg.get("rise", 0.12)) if stress_target > prev_stress else _safe_float(cfg.get("fall", 0.20)))
    stress = clamp(prev_stress * (1.0 - alpha) + stress_target * alpha)
    velocity = 0.6 * prev_velocity + 0.4 * (stress - prev_stress)
    fatigue = clamp(prev_fatigue + (0.018 if stress > 0.7 else -0.045))

    # 5. СЛОЕВЕ НА ОБРАБОТКА (Neural Tensor)
    neuro = neuro_evolution(prev_neuro, surprise, velocity, fatigue, entropy)
    shadow = shadow_core(stress, velocity, fragility)
    shadow["shadow_fear"] = 0.06 * stress + 0.94 * prev_shadow_fear
    vascular = vascular_step(stress, entropy)
    
    # 6. ЕНЕРГИЯ И СТАСИС
    energy = clamp(prev_energy - (stress * 0.02) + (0.002 if stress < 0.2 else 0.0))
    in_stasis = energy < 0.15

    system = {
        "stress": round(stress, 3),
        "entropy": round(entropy, 3),
        "stress_velocity": round(velocity, 3),
        "energy": round(energy, 3),
        "fatigue": round(fatigue, 3),
        "in_stasis": in_stasis,
        "pain": round(pain, 3),
        "fragility": round(fragility, 3),
    }

    # 7. МОДУЛАЦИИ
    system = apply_scar_damping(system, prev_state.get("_scars", []))
    system = apply_ghost_pre_echo(system, prev_state)

    # 8. СГЛОБЯВАНЕ (Output structure)
    out = {
        "ts": int(tick.get("ts", time.time())),
        "system": system,
        "neurochemistry": neuro,
        "shadow": shadow,
        "vascular": vascular,
        "temporal": temporal_consensus(prev_prices, current_prices),
        "fear_index": round(0.4 * ((stress + shadow["shadow_fear"])/2) + 0.4 * stress + 0.2 * entropy, 3),
        "latent": {"asa_amp": round(asa_amp, 3), "crash_coherence": round(coherence, 3)},
        "prices": current_prices,
        "_memory": {"changes_mean_buf": list(buf)},
        "_scars": prev_state.get("_scars", [])
    }

    if bool(cfg.get("enable_internal_thought", True)):
        pkt, _ = internal_thought(system, out["latent"], cfg)
        out["thought"] = pkt

    return out

# ─────────────────────────────────────────────────────────────────
# SECTION 6: SELF-TEST BLOCK
# ─────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print("🚀 PRANA CORE v12.9 - FULL BOOT SEQUENCE")
    mock_tick = {
        "ts": int(time.time()),
        "coins": {
            "bitcoin": {"price": 42000, "price_change_pct_24h": 1.2},
            "ethereum": {"price": 2200, "price_change_pct_24h": -2.5}
        }
    }
    state = {
        "system": {"stress": 0.1, "entropy": 0.1, "energy": 1.0},
        "neurochemistry": {"dopamine": 0.5, "serotonin": 0.5, "adrenaline": 0.1},
        "prices": {"bitcoin": 41500, "ethereum": 2250},
        "shadow": {"worlds": [0.1]*12, "shadow_fear": 0.1}
    }
    for i in range(3):
        state = prana_step(mock_tick, state)
        print(f"Step {i+1} | Fear: {state['fear_index']} | Thought: {state.get('thought', {}).get('thought')}")
    print("✅ SELF-TEST COMPLETE. CORE IS STEADY.")