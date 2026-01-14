# prana_laws.py — PRANA LAW ENFORCER
# © 2025 Антоний Илиев Велков

def clamp(x, a=0.0, b=1.0):
    return max(a, min(b, float(x)))

class PranaLawViolation(Exception):
    pass


def assert_prana_laws(prev: dict, curr: dict):
    """
    Твърда проверка между два state-а.
    Ако закон е нарушен → Exception.
    """

    # --- Извличане ---
    p_sys = prev.get("system", {})
    c_sys = curr.get("system", {})
    p_lat = prev.get("latent", {})
    c_lat = curr.get("latent", {})

    p_fear = float(prev.get("fear_index", 0.0))
    c_fear = float(curr.get("fear_index", 0.0))

    p_threat = prev.get("threat_state", "NORMAL")
    c_threat = curr.get("threat_state", "NORMAL")

    entropy = float(c_sys.get("entropy", 0.0))
    crash = float(c_lat.get("crash_coherence", 0.0))

    # ────────────────────────────────
    # LAW I: FEAR JUMP LIMIT
    # ────────────────────────────────
    if (c_fear - p_fear) > 0.20:
        raise PranaLawViolation(
            f"FEAR jump too large: {p_fear:.2f} → {c_fear:.2f}"
        )

    # ────────────────────────────────
    # LAW II: NO RED WITHOUT WARNING
    # ────────────────────────────────
    if c_threat in ("PANIC", "CRASH_IMMINENT"):
        if p_threat == "NORMAL" and c_fear < 0.40:
            raise PranaLawViolation(
                f"Illegal escalation: {p_threat} → {c_threat} with FEAR {c_fear:.2f}"
            )

    # ────────────────────────────────
    # LAW III: ENTROPY GATE
    # ────────────────────────────────
    if c_threat == "PANIC":
        if entropy < 0.10 and crash < 0.35:
            raise PranaLawViolation(
                f"PANIC without entropy: ENT={entropy:.2f}, CRASH={crash:.2f}"
            )

    # ────────────────────────────────
    # LAW IV: COLOR ORDER
    # ────────────────────────────────
    order = ["NORMAL", "WARNING", "PANIC", "CRASH_IMMINENT"]
    if p_threat in order and c_threat in order:
        if order.index(c_threat) - order.index(p_threat) > 1:
            raise PranaLawViolation(
                f"Threat jump illegal: {p_threat} → {c_threat}"
            )

    return True
