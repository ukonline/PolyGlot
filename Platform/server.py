#!/usr/bin/env python3
# Author: Sébastien Combéfis
# Version: June 21, 2016

from flask import Flask

app = Flask('PolyGlot')

@app.route('/')
def main():
    return 'PolyGlot'

if __name__ == '__main__':
    app.run()