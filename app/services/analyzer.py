"""
Prosty silnik reguł – pierwszy etap MVP.
"""

from typing import List, Dict

SUSPICIOUS_KEYWORDS = [
    "pilne", "natychmiast", "zawieszone", "zablokowane",
    "weryfikacja", "ostatnia szansa", "konto zostanie usunięte"
]

SUSPICIOUS_DOMAIN_PATTERNS = [
    "allegro-", "inpost-", "mbank-", "ing-", "poczta-"
]

def analyze(email: Dict) -> Dict:
    score = 0
    reasons = []

    text = f"{email.get('subject', '')} {email.get('body', '')}".lower()

    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in text:
            score += 2
            reasons.append(f"Słowo wywierające presję: {keyword}")

    sender = email.get("sender", "").lower()
    for pattern in SUSPICIOUS_DOMAIN_PATTERNS:
        if pattern in sender and not sender.endswith((".pl", ".com.pl")):
            score += 3
            reasons.append("Podejrzany nadawca (możliwe podszywanie się)")

    for link in email.get("links", []):
        for pattern in SUSPICIOUS_DOMAIN_PATTERNS:
            if pattern in link.lower():
                score += 3
                reasons.append(f"Podejrzany link: {link}")

    if score >= 5:
        level = "wysokie"
        recommendation = "Wysokie ryzyko. Nie klikaj w linki i usuń wiadomość."
    elif score >= 3:
        level = "średnie"
        recommendation = "Wiadomość podejrzana. Zweryfikuj nadawcę innym kanałem."
    else:
        level = "brak"
        recommendation = "Brak wyraźnych sygnałów zagrożenia."

    return {
        "risk_score": score,
        "level": level,
        "reasons": reasons,
        "recommendation": recommendation,
        "is_threat": score >= 3
    }
