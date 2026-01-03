from datetime import datetime, timedelta
from collections import Counter

def build_weekly_profile(memory, days=7):
    cutoff = datetime.utcnow() - timedelta(days=days)
    recent = []

    # -------- Filter Recent Entries Safely --------
    for m in memory:
        try:
            ts = datetime.fromisoformat(m["timestamp"])
        except Exception:
            continue

        if ts >= cutoff:
            recent.append(m)

    if len(recent) < 5:
        return {
            "status": "insufficient_data",
            "message": "Not enough entries to build a reliable profile."
        }

    # -------- Emotional Stats --------
    sentiments = [m["sentiment"]["label"] for m in recent]
    counts = Counter(sentiments)
    total = len(sentiments)

    stability = {
        "positive": counts.get("POSITIVE", 0) / total,
        "negative": counts.get("NEGATIVE", 0) / total
    }

    switches = sum(
        sentiments[i] != sentiments[i - 1]
        for i in range(1, total)
    )

    volatility_ratio = switches / total

    if volatility_ratio < 0.3:
        volatility = "low"
    elif volatility_ratio < 0.6:
        volatility = "moderate"
    else:
        volatility = "high"

    stability["volatility"] = volatility

    # -------- Intents --------
    intents = [m.get("intent", "unknown") for m in recent]
    dominant_intents = [
        k for k, _ in Counter(intents).most_common(2)
    ]

    # -------- Confidence --------
    try:
        days_span = (
            datetime.fromisoformat(recent[-1]["timestamp"]) -
            datetime.fromisoformat(recent[0]["timestamp"])
        ).days + 1
    except Exception:
        days_span = 1

    volume_score = min(1.0, len(recent) / 10)
    span_score = min(1.0, days_span / days)
    diversity_score = len(set(sentiments)) / 2  # POSITIVE / NEGATIVE

    confidence = round(
        0.4 * volume_score +
        0.3 * span_score +
        0.3 * diversity_score,
        2
    )

    return {
        "period": f"last_{days}_days",
        "emotional_stability": stability,
        "dominant_intents": dominant_intents,
        "entry_count": len(recent),
        "confidence": confidence
    }
