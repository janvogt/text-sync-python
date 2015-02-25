#!usr/bin/env python3

"""TextSync is a library for cooperative text editing.

Python implemententaion of the TextSync protocol"""

__author__ = "Jan Vogt"
__copyright__ = "Copyright 2015, Jan Vogt"
__email__ = "jan.vogt@me.com"
__license__ = "GPLv3"

class TextSync:
    def __init__(self, editorOrder, text):
        """TextSync keeps track of the history of some text."""
        self.__editorOrder = editorOrder

    def addChange(self, change):
        """Register the given change atop on the current version.
        That is, the version after all changes recieved by changes are applied."""
        pass

    def changes(self):
        """changes is a generator function which can be iterated for changes."""
        pass

    def toSend(self):
        """toSend is a generator function which can be iterated for messages
        to be pushed."""

    def applyMessage(self, message):
        """applyMessage applies and stores a recieved message to the text."""
        pass


class Change:
    def __init__(self, change, editorOrder, basedOn):
        pass
