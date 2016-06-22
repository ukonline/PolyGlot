#!/usr/bin/env python3
# Author: Sébastien Combéfis
# Version: June 22, 2016

import cherrypy

class PolyGlot:
    def index(self):
        return 'PolyGlot'
    index.exposed = True

if __name__ == '__main__':
    cherrypy.quickstart(PolyGlot())