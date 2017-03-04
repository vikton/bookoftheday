#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :

"""
Client web per https://www.packtpub.com/packt/offers/free-learning

@author: victor.ferrer.2012@gmail.com
"""

import urllib2
from bs4 import BeautifulSoup
url = "https://www.packtpub.com/packt/offers/free-learning"


class BookOfTheDay(object):
    """Book Class."""

    def main(self):
        u"""Main de la funció."""
        web = self.getWeb(url)
        result = self.Search(web)
        print result.replace('\t', '')

    def getWeb(self, url):
        """Download the url's web."""
        file = urllib2.urlopen(url)
        code = file.read()
        file.close()
        return code

    def Search(self, web):
        """Search for the name of the book."""
        soup = BeautifulSoup(web, 'html.parser')
        el = soup.find_all("div", "dotd-title")
        for element in el:
            title = element.find("h2")
        return title.text


if __name__ == "__main__":
    book = BookOfTheDay()
    book.main()
