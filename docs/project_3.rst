:mod:`project_3` --- Ein Modul für den Mendeley API-Zugriff
===================================================================
.. module:: project_3
   :synopsis: Ein Modul für den Mendeley API-Zugriff

Einleitung
----------

TODO Einleitung


Anleitung
---------
TODO Anleitung

Referenzen
----------

- Beispielmodul
- Mendeley-API
Funktionen
----------

.. function:: save_as_pickle(p_object, filename)

    Speichert einen beliebigen Datentyp *p_object* als eine Pickle-Datei mit dem Dateinamen *filename*.py.


.. function:: open_from_pickle(filename)

    Öffnet eine zuvor mit :func:`.save_as_pickle` erstellte Pickle-Datei, bzw. eine beliebe Pickle-Datei, die genau einen (verschachtelten) Datentyp enthält. Der Name der Datei wird durch *filename* bestimmt.