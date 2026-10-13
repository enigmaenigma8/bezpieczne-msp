"""
Prosty test silnika analizy.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.services.analyzer import analyze


def test_phishing():
    email = {
        "sender": "support@allegro-secure.com",
        "subject": "Twoje konto zostało zawieszone",
        "body": "Kliknij natychmiast, aby odblokować konto.",
        "links": ["https://allegro-secure.com/verify"]
    }
    result = analyze(email)
    assert result["is_threat"] is True
    print("Test phishingu: OK")


def test_clean():
    email = {
        "sender": "kontakt@firma.pl",
        "subject": "Potwierdzenie zamówienia",
        "body": "Dziękujemy za zakupy.",
        "links": []
    }
    result = analyze(email)
    assert result["is_threat"] is False
    print("Test bezpiecznej wiadomości: OK")


if __name__ == "__main__":
    test_phishing()
    test_clean()
    print("Wszystkie testy przeszły.")
