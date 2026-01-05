# sensor_onchain_ingestor.py — THE CHAOS ATTRACTOR + CROSS-TALK EDITION + DYNAMIC SLEEP
# © 2025-2026 Антоний Илиев Велков
# ИНОВАЦИЯ: Nonlinear Lyapunov Divergence, Chaos Attractor Mapping,
# Organ Cross-Talk, Fear Aggregator (INERTIA), Dynamic Sleep

import json, os, time, requests
import numpy as np
from scipy.optimize import curve_fit
from typing import Dict, Any
import random

BASE = os.path.dirname(os.path.abspath(__file__))
STATE_DIR = os.path.join(BASE, "state")
ONCHAIN_JSON = os.path.join(STATE_DIR, "onchain_heartbeat.json")

# --- КОНФИГУРАЦИЯ ---
DUNE_API_KEY = ""
HISTORY_MAX = 20

# История за CHAOS
gas_history = []
mev_history = []
liq_history = []

# PRANA Core Values (глобални базови)
asa_k = 0.7
core_stress = 0.5
fragility = 0.3

# --- FEAR MEMORY (INERTIA ORGAN) ---
previous_onchain_fear = 0.0
FEAR_DECAY = 0.94   # колко бързо "забравя" страха (биологично)
FEAR_FLOOR = 0.02   # минимален residual страх – предотвратява 0.000

# --- ПОМОЩНИ ФУНКЦИИ ---
def fetch_gas_velocity() -> float:
    try:
        r = requests.get("https://ethgasstation.info/api/ethgasAPI.json", timeout=5)
        if r.status_code == 200:
            avg_gas = float(r.json().get("average", 50)) / 10
            return min(1.0, avg_gas / 200)
    except:
        return 0.2
    return 0.2

def fetch_mev_activity() -> float:
    try:
        r = requests.get("https://blocks.flashbots.net/v1/blocks?limit=1", timeout=5)
        if r.status_code == 200:
            blocks = r.json().get("blocks", [])
            if blocks:
                reward = float(blocks[0].get("mev_reward", 0))
                return min(1.0, reward / 1e18)
    except:
        return 0.3
    return 0.3

def fetch_liq_proximity() -> float:
    if not DUNE_API_KEY:
        return 0.5
    url = f"https://api.dune.com/api/v1/query/3773000/results?api_key={DUNE_API_KEY}"
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            rows = r.json().get("result", {}).get("rows", [])
            return min(1.0, len(rows) / 100)
    except:
        return 0.5
    return 0.5

# --- CHAOS MATH ---
def chaos_func(x, a, b, c):
    return a * np.exp(b * x) + c

def nonlinear_chaos_predictor(series: list) -> float:
    if len(series) < 5:
        return 0.05  # <<< НЕ 0.0 → минимален chaos seed
    x_data = np.arange(len(series))
    y_data = np.array(series)
    try:
        popt, _ = curve_fit(
            chaos_func,
            x_data,
            y_data,
            p0=[0.1, 0.1, 0.1],
            maxfev=2000
        )
        linear_pred = np.linspace(y_data[0], y_data[-1], len(y_data))
        chaos_div = np.mean(np.abs(chaos_func(x_data, *popt) - linear_pred))
        return min(1.0, chaos_div / 0.35)
    except:
        return 0.08

def update_history(gas: float, mev: float, liq: float):
    gas_history.append(gas)
    mev_history.append(mev)
    liq_history.append(liq)
    if len(gas_history) > HISTORY_MAX:
        gas_history.pop(0)
        mev_history.pop(0)
        liq_history.pop(0)

# --- CALCULATION CORE ---
def calculate_gravity_well() -> Dict[str, Any]:
    global previous_onchain_fear

    gas_v = fetch_gas_velocity()
    mev_v = fetch_mev_activity()
    liq_p = fetch_liq_proximity()

    update_history(gas_v, mev_v, liq_p)

    # 1. Линейна база
    base_gravity = (gas_v * 0.25) + (mev_v * 0.35) + (liq_p * 0.40)

    # 2. Alignment и Collapse
    alignment_count = ((gas_v > 0.6) + (mev_v > 0.6) + (liq_p > 0.6))
    collapse_multiplier = (
        1.0 + (alignment_count - 1) * 0.35
        if alignment_count >= 2 else 1.0
    )

    # 3. Chaos Attractor Score
    chaos_gas = nonlinear_chaos_predictor(gas_history)
    chaos_mev = nonlinear_chaos_predictor(mev_history)
    chaos_liq = nonlinear_chaos_predictor(liq_history)
    attractor_score = (chaos_gas + chaos_mev + chaos_liq) / 3

    # 4. Финална гравитация
    final_gravity = min(
        1.0,
        (base_gravity * collapse_multiplier) + (attractor_score * 0.25)
    )

    # 5. Event Horizon Detection
    is_event_horizon = final_gravity > 0.78 and attractor_score > 0.5

    # 6. --- ORGAN CROSS-TALK ---
    fear_multiplier = 1.0 + fragility * 0.3
    current_asa = asa_k * (1.0 + attractor_score * 0.4)

    shadow_onchain_fear = final_gravity * fear_multiplier * 0.8
    delayed_onchain_fear = final_gravity * fear_multiplier * 0.5

    # --- FEAR AGGREGATOR (НОВ ОРГАН) ---
    instant_fear = final_gravity * (1.0 + attractor_score)

    raw_fear = (
        instant_fear * 0.5 +
        shadow_onchain_fear * 0.3 +
        delayed_onchain_fear * 0.2
    )

    # Нелинейна чувствителност (усилва малките стойности)
    sensitive_fear = min(1.0, raw_fear ** 0.72)

    # Inertia / Memory
    aggregated_fear = max(
        sensitive_fear,
        previous_onchain_fear * FEAR_DECAY,
        FEAR_FLOOR
    )

    previous_onchain_fear = aggregated_fear

    # Visual heartbeat
    visual_heartbeat = 0.5 * core_stress + 0.5 * final_gravity

    # --- Динамично време за сън ---
    if final_gravity > 0.75:
        sleep_time = 10
    elif final_gravity > 0.6:
        sleep_time = 30
    else:
        sleep_time = 120

    return {
        "gravity_index": round(final_gravity, 3),
        "event_horizon": is_event_horizon,
        "chaos_attractor": round(attractor_score, 3),
        "alignment_force": alignment_count,
        "mev_stress": round(mev_v, 3),
        "gas_velocity": round(gas_v, 3),
        "liq_proximity": round(liq_p, 3),
        "current_asa": round(current_asa, 3),
        "fear_multiplier": round(fear_multiplier, 3),
        "shadow_onchain_fear": round(shadow_onchain_fear, 3),
        "delayed_onchain_fear": round(delayed_onchain_fear, 3),
        "onchain_fear_index": round(aggregated_fear, 3),
        "heartbeat_rate": round(0.3 + (final_gravity * 0.7), 3),
        "visual_heartbeat": round(visual_heartbeat, 3),
        "dynamic_sleep": sleep_time,
        "ts": int(time.time())
    }

# --- MAIN LOOP ---
def main():
    print("--- PRANA ON-CHAIN [CHAOS + FEAR AGGREGATOR + DYNAMIC BREATHING] ---")
    try:
        import scipy, numpy
    except ImportError:
        print("ГРЕШКА: pip install numpy scipy")
        return

    while True:
        try:
            data = calculate_gravity_well()
            os.makedirs(STATE_DIR, exist_ok=True)

            tmp_path = ONCHAIN_JSON + ".tmp"

            def json_serializable(obj):
                if isinstance(obj, (np.bool_, bool)):
                    return bool(obj)
                if isinstance(obj, (np.integer, int)):
                    return int(obj)
                if isinstance(obj, (np.floating, float)):
                    return float(obj)
                return str(obj)

            with open(tmp_path, "w", encoding="utf-8") as f:
                json.dump(
                    data,
                    f,
                    ensure_ascii=False,
                    indent=2,
                    default=json_serializable
                )

            os.replace(tmp_path, ONCHAIN_JSON)

            status = "⚠️ EVENT HORIZON" if data["event_horizon"] else "STABLE"
            print(
                f"[{status}] Gravity: {data['gravity_index']} | "
                f"Fear: {data['onchain_fear_index']} | "
                f"Chaos: {data['chaos_attractor']} | "
                f"Heartbeat: {data['visual_heartbeat']:.2f} | "
                f"Sleep: {data['dynamic_sleep']}s"
            )

        except Exception as e:
            print(f"[ON-CHAIN ERROR]: {e}")

        time.sleep(data["dynamic_sleep"])

if __name__ == "__main__":
    main()
