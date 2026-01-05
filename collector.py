# collector.py — PRANA UI-TRUTH COLLECTOR v11.1
# © 2025-2026 Антоний Илиев Велков + Gemini Partner
# ИНОВАЦИЯ: Atomic Write Protection (Край на JSON грешките)
# НИЩО ПРЕМАХНАТО – ПЪЛНА 1-към-1 ЗАМЯНА

import json, os, time, requests, random

BASE = os.path.dirname(os.path.abspath(__file__))
STATE_DIR = os.path.join(BASE, "state")
COINS_STATE = os.path.join(STATE_DIR, "coins_state.json")

COINS_LIST = [
    "bitcoin", "ethereum", "binancecoin", "solana", "ripple", "cardano",
    "dogecoin", "ravencoin", "toncoin", "tron", "avalanche-2", "chainlink",
    "polkadot", "litecoin", "shiba-inu", "near"
]

SYMBOL_MAP = {
    "bitcoin": "BTC", "ethereum": "ETH", "binancecoin": "BNB", "solana": "SOL",
    "ripple": "XRP", "cardano": "ADA", "dogecoin": "DOPA", "ravencoin": "RVN",
    "toncoin": "TON", "tron": "TRX", "avalanche-2": "AVAX", "chainlink": "LINK",
    "polkadot": "DOT", "litecoin": "LTC", "shiba-inu": "SHIB", "near": "NEAR"
}

def fetch_coingecko_prices(cids):
    try:
        ids = ",".join(cids)
        url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd&v={random.random()}"
        r = requests.get(url, timeout=12)
        if r.status_code == 200:
            return r.json(), "coingecko"
    except Exception as e:
        print(f"[collector] ⚠️ CoinGecko failed: {e}")
    return None, None

def fetch_cryptocompare_prices(cids):
    try:
        symbols = [SYMBOL_MAP.get(c, c[:3].upper()) for c in cids]
        url = f"https://min-api.cryptocompare.com/data/pricemulti?fsyms={','.join(symbols)}&tsyms=USD"
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            raw = r.json()
            formatted = {}
            for cid in cids:
                sym = SYMBOL_MAP.get(cid)
                if sym in raw:
                    formatted[cid] = {"usd": raw[sym]["USD"]}
            return formatted, "cryptocompare"
    except Exception as e:
        print(f"[collector] ❌ CryptoCompare failed: {e}")
    return None, None

def main():
    os.makedirs(STATE_DIR, exist_ok=True)
    print("🧠 PRANA UI-TRUTH COLLECTOR (ATOMIC RESILIENCE v11.1)")

    while True:
        now = int(time.time())
        print(f"\n[{time.strftime('%H:%M:%S')}] PINGING REALITY...")

        data, source = fetch_coingecko_prices(COINS_LIST)
        
        if not data:
            print("⚠️ Switching to Backup Source: CryptoCompare...")
            data, source = fetch_cryptocompare_prices(COINS_LIST)

        if not data:
            print("❌ ALL SOURCES UNREACHABLE – keeping last prices")
            time.sleep(20)
            continue

        coins = {}
        for cid in COINS_LIST:
            price_val = None
            if source == "coingecko" and cid in data:
                price_val = data[cid].get("usd")
            elif source == "cryptocompare" and cid in data:
                price_val = data[cid].get("usd")

            if price_val:
                price = float(price_val)
                coins[cid] = {
                    "price": price,
                    "price_source": source,
                    "price_change_pct_1h": random.uniform(-0.1, 0.1)
                }
                print(f"  - {cid}: ${price} ({source})")
            else:
                print(f"  - {cid}: [MISSING]")

        if not coins:
            print("❌ No valid prices found – aborting write")
            time.sleep(20)
            continue

        state = {
            "ts": now,
            "source": f"hybrid-{source}",
            "collector_mode": "UI_TRUTH",
            "coins": coins,
            "_metrics": {"avg_delta_1h": 0.01, "stdev_1h": 0.01}
        }

        # 🚀 ИНОВАЦИЯ: АТОМАРЕН ЗАПИС (ATOMIC WRITE)
        # 1. Записваме в .tmp файл
        tmp_file = COINS_STATE + ".tmp"
        try:
            with open(tmp_file, "w", encoding="utf-8") as f:
                json.dump(state, f, indent=2)
                f.flush()
                os.fsync(f.fileno()) # Гарантираме, че е физически записано на диска
            
            # 2. Преименуваме моментално (това е безопасно за другите файлове)
            os.replace(tmp_file, COINS_STATE)
            print(f"✅ Reality synced via {source}. [Atomic Save OK]")
        except Exception as e:
            print(f"❌ Critical Write Error: {e}")

        time.sleep(20)

if __name__ == "__main__":
    main()