# Bezpieczne MSP

Automatyczna ochrona poczty elektronicznej dla małych i średnich przedsiębiorstw.

## Opis

Narzędzie analizuje przychodzące wiadomości e-mail pod kątem phishingu, fałszywych faktur i podszywania się pod znane marki (Allegro, InPost, banki, urzędy).  
Generuje alert tylko wtedy, gdy wykryje podwyższone ryzyko, wraz z jasną rekomendacją działania.

Projekt jest skierowany do firm, które nie posiadają dedykowanego zespołu IT.

## Główne założenia

- Jednorazowe podłączenie skrzynki
- Automatyczna analiza w tle
- Minimalne obciążenie użytkownika
- Wsparcie podstawowych obowiązków związanych z bezpieczeństwem informacji

## Status

Wczesna faza rozwoju (MVP).

## Technologie

- Python
- FastAPI
- PostgreSQL
- Celery + Redis
- Docker
