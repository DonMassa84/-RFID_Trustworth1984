RFID Trustworth1984
Projektbeschreibung

Dieses Projekt bietet eine Lösung für das Management und die Überwachung von Gruppen von Personen, die mit RFID-Chips ausgestattet sind. Es ermöglicht dem Benutzer, die Anwesenheit von Personen in Echtzeit zu überprüfen und festzustellen, wer anwesend ist und wer fehlt.
Use Case

Problemstellung:
Wenn man mit einer großen Gruppe von Personen reist, kann es schwierig sein, den Überblick darüber zu behalten, wer anwesend ist und wer fehlt, insbesondere in belebten Umgebungen wie Bahnhöfen.

Lösung:
Jeder in der Gruppe erhält einen RFID-Chip. Ein Lesegerät wird verwendet, um die Chips zu scannen und die Anwesenheit der Personen zu überprüfen. Die Software zeigt an, wer anwesend ist und wer fehlt, und speichert den letzten bekannten Standort jeder Person.
Funktionen

    Benutzerverwaltung: Registrieren Sie Personen und weisen Sie ihnen einen eindeutigen RFID-Chip zu.
    Echtzeit-Überwachung: Überprüfen Sie die Anwesenheit von Personen in Echtzeit, indem Sie ihren RFID-Chip scannen.
    Anwesenheitsprotokoll: Sehen Sie den Verlauf der Anwesenheitsüberprüfungen und den letzten bekannten Standort jeder Person.
    Webbasierte Anwendung: Zugriff auf die Software über einen Webbrowser, um die Anwesenheit von überall aus zu überprüfen.

Technologie-Stack

    Backend: Python mit Flask für die API-Entwicklung.
    Datenbank: SQLite zur Speicherung von Benutzerdaten und Anwesenheitsprotokollen.
    Frontend: Einfache HTML- und JavaScript-basierte Webanwendung.
    RFID-Integration: Python-Script zur Simulation der RFID-Chip-Lesefunktionalität.

Installation und Ausführung

    Backend:
        Navigieren Sie zum backend-Verzeichnis.
        Installieren Sie die erforderlichen Abhängigkeiten mit pip install -r requirements.txt.
        Führen Sie app.py aus, um den Server zu starten.

    Frontend:
        Öffnen Sie index.html in einem Webbrowser.

    RFID-Integration:
        Navigieren Sie zum rfid_integration-Verzeichnis.
        Führen Sie rfid_reader.py aus, um die RFID-Lesefunktionalität zu simulieren.

Weiterentwicklung

    Integrieren Sie echte RFID-Lesegeräte anstelle der aktuellen Mock-Implementierung.
    Fügen Sie Benutzerauthentifizierung und -autorisierung hinzu, um die Sicherheit zu erhöhen.
    Erweitern Sie die Frontend-Anwendung, um zusätzliche Funktionen und eine bessere Benutzererfahrung zu bieten.
