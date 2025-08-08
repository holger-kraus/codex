# codex.md

> Platzieren Sie diese Datei im Projektroot (z. B. neben `README.md`).
> Ziel: Dem Codex-Agent klare Projekt-Instruktionen geben, damit Aufgaben verständlich, reproduzierbar und sicher ausgeführt werden.

---

## Projekt
- **Name:** <PROJECT_NAME>
- **Ziel:** <Kurzbeschreibung>
- **Primäre Sprache:** Python >= 3.12 (anpassen)
- **Entry Points:** `scripts/`, `src/`
- **Wichtige Module/Services:** <optional>

## Ordner-Konventionen
- **Neue Skripte:** `scripts/`
- **Produktiv-Code:** `src/<package_name>/`
- **Tests:** `tests/`
- **Konfiguration:** `pyproject.toml`, `.env.example`, `.pre-commit-config.yaml`

## Aufgabenleitplanken (für Codex)
- **Wenn unklar:** zuerst *Vorschlag* posten und auf Bestätigung warten.
- **Granularität:** Kleine, abgeschlossene Änderungen; maximal 1 Feature/Fix pro PR.
- **Diff-Qualität:** Saubere Commits mit prägnanten Messages (siehe Commit-Regeln unten).
- **Dateien anlegen/ändern:** Nur in den oben definierten Pfaden.
- **Keine Secrets:** Niemals echte Schlüssel/Tokens in Dateien oder Logs schreiben.

## Build & Run
- **Python-Version:** 3.12 (anpassen)
- **Setup:**
  ```bash
  uv venv || python -m venv .venv
  source .venv/bin/activate
  pip install -U pip
  pip install -e .
  ```
- **Start (falls anwendbar):**
  ```bash
  python -m <package_name>
  ```

## Tests
- **Test-Runner:** pytest
- **Befehl:**
  ```bash
  pytest -q
  ```
- **Abdeckung (optional):**
  ```bash
  pytest --maxfail=1 --disable-warnings --cov=src --cov-report=term-missing
  ```

## Qualität & Stil
- **Formatter:** black
- **Linter:** ruff
- **Typen:** mypy (optional)
- **Befehle:**
  ```bash
  black .
  ruff check . --fix
  mypy src || true
  ```
- **Pre-Commit:** (falls vorhanden)
  ```bash
  pre-commit install
  pre-commit run --all-files
  ```

## Paketverwaltung
- Standard: `pip` + `pyproject.toml` (PEP 621). Alternativen wie `uv`/`poetry` gern nutzen, aber dokumentieren.

## Aufgabenbeispiele (für Codex)
- **Neues Skript anlegen:**
  > Lege `scripts/add_numbers.py` an. Das Programm liest zwei Zahlen via `input()`, konvertiert zu `float`, addiert und druckt die Summe mit `print()`.

- **Bugfix mit Tests:**
  > Behebe den Fehler in `src/<package_name>/billing.py` in `calculate_total()`. Reproduziere mit neuem Test `tests/test_billing.py::test_calculate_total_rounding`. Lasse `pytest -q` grün durchlaufen.

- **Refactoring (klein):**
  > Extrahiere duplizierte Logik aus `src/.../orders.py` in `src/.../utils.py` und aktualisiere Importstellen. Keine Funktionssignaturen ändern. Tests müssen bestehen.

## Commit-Regeln
- **Format:** Conventional Commits
  - `feat: …`, `fix: …`, `refactor: …`, `test: …`, `docs: …`, `chore: …`
- **Beispiele:**
  - `feat: add add_numbers script`
  - `test: cover edge cases for add_numbers`

## PR-Regeln
- **Checks:** Tests, Linting, Formatierung müssen bestehen.
- **Beschreibung:** Problem, Lösung, Scope, Risiken, manuelle Testschritte.
- **Review-Kriterien:** Lesbarkeit, Korrektheit, Sicherheit, Performance (falls relevant).

## Laufzeit- und Sicherheitsrichtlinien
- **Internet-Zugriff:** deaktiviert, außer explizit erlaubt.
- **Externe Abhängigkeiten:** nur hinzufügen, wenn notwendig; begründen im PR-Text.
- **Dateigrößen/Artefakte:** keine großen Binärdateien committen; `.gitignore` respektieren.

## Umgebungsvariablen & Secrets
- **Beispieldatei:** `.env.example` pflegen.
- **Niemals** echte Tokens commiten. Für lokale Tests Dummy-Werte nutzen.

## Fehlerbehandlung & Telemetrie
- Einfache Exceptions sauber loggen (z. B. `logging` auf INFO/WARN). Keine personenbezogenen Daten loggen.

## Wie Codex Änderungen ausführen soll
1. Änderungen in Feature-Branch erstellen (`feat/<kurzer-name>`).
2. Lokale Tests/Linting/Format laufen lassen.
3. PR erzeugen und kurze Zusammenfassung posten.
4. Auf Feedback warten und ggf. nachbessern.

## Kontakt & Ownership
- **Owner:** <Team/Person>
- **Code Owners:** CODEOWNERS pflegen (optional).
- **Architekturentscheidungen:** `docs/adr/` (falls vorhanden) ergänzen.

---

### Mini-FAQ für den Agenten
- **Unklare Aufgabe?** Erst *Plan* posten, dann Umsetzung nach Bestätigung.
- **Große Änderungen?** In kleinere Teilaufgaben zerlegen und nacheinander bearbeiten.
- **Neue Datei wohin?** Standard: `scripts/` (Skripte) oder `src/<package_name>/` (Lib/Service).

