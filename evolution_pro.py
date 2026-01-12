# shadow_core.py — PRANA SHADOW v2.5 (Monte Carlo Behavioral Pulse)
# © 2026 Антоний Илиев Велков
# ИНОВАЦИЯ: Monte Carlo Behavioral Simulation (MCBS) - симулация на тълпата в 100 свята

import math
import random
import statistics
from typing import Dict

def clamp(x: float, a: float = 0.0, b: float = 1.0) -> float:
    return max(a, min(b, x))

def shadow_step(state: Dict) -> Dict:
    """
    Shadow v2.5: Разиграва 100 Монте Карло симулации, за да предвиди 
    кога отричането на тълпата ще се превърне в масова паника.
    """
    system = state.get("system", {}) or {}
    stress = float(system.get("stress", 0.0))
    entropy = float(system.get("entropy", 0.0))
    velocity = float(system.get("stress_velocity", 0.0))
    energy = float(system.get("energy", 1.0))

    # --- ИНОВАЦИЯ: MONTE CARLO BEHAVIORAL SIMULATION (MCBS) ---
    num_simulations = 100
    shadow_outcomes = []
    
    for _ in range(num_simulations):
        # Всеки "индивид" в тълпата има различен праг на болка (Pain Threshold)
        # Симулираме разсейване на прага на паника между 0.45 и 0.65
        pain_threshold = random.uniform(0.45, 0.65)
        
        # Симулираме "Закъснение на реакцията" (Reaction Lag)
        lag_factor = random.uniform(0.8, 1.4)
        
        # Логика за отричане (Denial) в този специфичен свят
        sim_denial = clamp((pain_threshold - stress) * 1.5) if stress < pain_threshold else 0.0
        
        # Логика за паника (Panic) в този специфичен свят
        sim_panic = 0.0
        if stress > pain_threshold:
            # Колкото по-ниска е енергията на PRANA, толкова по-бързо се чупи тълпата
            sim_panic = (stress - pain_threshold) * 2.0 * lag_factor * (1.1 - energy)
            
        shadow_outcomes.append(clamp(sim_panic - sim_denial))

    # Статистически анализ на 100-те симулации
    mean_shadow = statistics.mean(shadow_outcomes)
    std_dev = statistics.stdev(shadow_outcomes)
    
    # "Hysteria Risk" - какъв процент от тълпата вече е в паника
    panic_percentage = len([x for x in shadow_outcomes if x > 0.5]) / num_simulations

    # --- Crowds Echo Logic ---
    # Добавяме и FOMO елемент от базовия модел
    fomo = clamp(velocity * 2.5) if velocity > 0 and stress < 0.3 else 0.0
    
    final_shadow_fear = clamp(mean_shadow + fomo)

    # Определяне на интерпретацията чрез квантовите резултати
    if panic_percentage > 0.7:
        interpretation = "TOTAL COLLAPSE (CROWD HYSTERIA)"
    elif panic_percentage > 0.3:
        interpretation = "FRACTURED SENTIMENT"
    elif fomo > 0.4:
        interpretation = "IRRATIONAL EXUBERANCE (FOMO)"
    elif mean_shadow < 0 and stress < 0.3:
        interpretation = "MASS DENIAL"
    else:
        interpretation = "NEUTRAL DRIFT"

    return {
        "shadow_fear": round(final_shadow_fear, 3),
        "mean_panic": round(mean_shadow, 3),
        "panic_probability": round(panic_percentage * 100, 1), # В проценти за UI
        "uncertainty_index": round(std_dev, 4), # Колко е разединена тълпата
        "denial_strength": round(clamp(abs(min(shadow_outcomes))), 3) if min(shadow_outcomes) < 0 else 0,
        "interpretation": interpretation
    }