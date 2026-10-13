"""
Proste demo silnika analizy Bezpieczne MSP.
"""

from app.services.analyzer import analyze


def run_demo():
    print("=== Bezpieczne MSP – Demo ===\n")

    # Przykład 1: Phishing
    phishing = {
        "sender": "support@allegro-secure-login.com",
        "subject": "Twoje konto zostało zawieszone",
        "body": "Kliknij natychmiast w link, aby odblokować konto. Ostatnia szansa.",
        "links": ["https://allegro-secure-login.com/verify"]
    }

    result = analyze(phishing)
    print("1. Wiadomość phishingowa:")
    print(f"   Poziom ryzyka: {result['level']}")
    print(f"   Rekomendacja: {result['recommendation']}")
    print(f"   Powody: {result['reasons']}\n")

    # Przykład 2: Bezpieczna wiadomość
    clean = {
        "sender": "sklep@twojafirma.pl",
        "subject": "Potwierdzenie zamówienia nr 12345",
        "body": "Dziękujemy za zakupy. Twoje zamówienie zostało przyjęte do realizacji.",
        "links": []
    }

    result = analyze(clean)
    print("2. Bezpieczna wiadomość:")
    print(f"   Poziom ryzyka: {result['level']}")
    print(f"   Rekomendacja: {result['recommendation']}\n")


if __name__ == "__main__":
    run_demo()
