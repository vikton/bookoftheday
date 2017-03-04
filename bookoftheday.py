#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :

"""
Client web per https://www.packtpub.com/packt/offers/free-learning

@author: victor.ferrer.2012@gmail.com
"""

import urllib2
url = "https://www.packtpub.com/packt/offers/free-learning"


class BookOfTheDay(object):
    """Book Class."""

    def main(self):
        u"""Main de la funció."""
        web = self.getWeb(url)
        print web

    def getWeb(self, url):
        """Download the url's web."""
        file = urllib2.urlopen(url)
        code = file.read()
        file.close()
        return code


if __name__ == "__main__":
    book = BookOfTheDay()
    book.main()
