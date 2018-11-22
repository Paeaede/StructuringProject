from markdown import markdown # now package depends on markdown package -> install_requires in setup.py


def joke():
    return markdown(u'Wenn ist das Nunst\u00fcck git und Slotermeyer?'
                    u'Ja! ... **Beiherhund** das Oder die Flipperwaldt '
                    u'gersput.')