:mod:`project_3` --- Informetrische Untersuchung mit Mendeley und Matplotlib
============================================================================
.. module:: project_3
   :synopsis: Ein Modul für den Mendeley API-Zugriff

Einleitung
----------

Mit dem vorliegenden Programm werden Publikationen informetrisch untersucht. Als Basis für den Datensatz dient das Literaturverwaltungsprogramm Mendeley. Mendeley beinhaltet nicht nur eine Desktopversion zum Verwalten von Referenzen und PDF-Dateien, sondern auch ein soziales Online-Netzwerk für den Austausch und Kollaborationen zwischen Forschern. Das Programm greift auf die Publikationsdaten über die Mendeley-API zu, wertet sie aus und visualisiert sie mit Hilfe von Matplotlib.


Funktionsumfang
---------------

Folgende Daten von den Mendeley-Servern gesammelt und visualisiert:

* Verteilung der Publikationen auf die letzten 10 Jahre
* Top 20 Tags in der Kategorie „Computer and Information Science“
* Top 10 Publikationen aus der „Nature“
* Special: Publikationen von Prof. Wolfang G. Stock

    * Publikationsanzahl pro Jahr
    * Co-Autoren Ranking

* Häufigkeit des Tags „ontology“ in allen Kategorien im Jahr 2011

Benutzung
---------

Wird das Programm direkt ausgeführt werden zunächst alle Daten über die Mendeley-API gesammelt. Dabei wird davon ausgegangen, dass sich eine Datei *config.json* im gleichen Verzeichnis befindet, in der 
Dafür kann "bsp config.json" verwendet werden und muss entsprechend umbenannt werden.
Auswertung und Interpretation
-----------------------------


Blablub informetrie



Funktionen
----------

.. function:: save_as_pickle(p_object, filename)

    Speichert einen beliebigen Datentyp *p_object* als eine Pickle-Datei mit dem Dateinamen *filename*.py. *filename* sollte als String übergeben werden.


.. function:: open_from_pickle(filename)

    Öffnet eine zuvor mit :func:`.save_as_pickle` erstellte Pickle-Datei, bzw. eine beliebe Pickle-Datei, die genau einen (verschachtelten) Datentyp enthält. Der Name der Datei wird durch *filename* bestimmt.

.. function:: draw_barchart(names, values, ylabel, title)

    Zeichnet ein Balkendiagramm für einen bestimmten Datensatz (definiert über die Parameter).
    Eine Liste von Strings als Parameter *names* bestimmt die Labels der x-Achse, *values* eine Anzahl von Daten in Form einer Liste. Die Beschriftung der y-Achse wird durch einen String *ylabel* bestimmt. Das Parameter *title* gibt den Titel des Diagramms in Form eines Strings an.

.. function:: draw_piechart(names, values)

    Zeichnet ein Kreisdiagramm für einen bestimmten Datensatz (definiert über die Parameter). Eine Liste von Strings als Parameter *names*, bestimmt die Labels jedes Teilstücks des Kreisdiagramms, *values* ist eine Liste von Daten in Form von Integern.

.. function:: draw_timeline(names, values, ylabel, title)

    Zeichnet eine Timeline für einen bestimmten Datensatz (definiert über die Parameter).
    Eine Liste von Strings als Parameter *names* bestimmt die Labels der x-Achse, *values* eine Anzahl von Daten in Form einer Liste. Die Beschriftung der y-Achse wird durch einen String *ylabel* bestimmt. Das Parameter *title* gibt den Titel des Diagramms in Form eines Strings an.

Referenzen
----------

Folgende Module fanden neben der Python Standard Library Verwendung:

* mendeley-oapi-example-master `https://github.com/Mendeley/mendeley-oapi-example: <https://github.com/Mendeley/mendeley-oapi-example/>`_
* Matplotlib: `http://matplotlib.org <http://matplotlib.org/>`_

Alle Daten wurden mithilfe von Mendeley gesammelt:

* Mendeley: `http://mendeley.com <http://mendeley.com/>`_
* Mendeley-API: `http://dev.mendeley.com <http://dev.mendeley.com/>`_
