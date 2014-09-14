#! /usr/bin/python2.7
# -*- coding: utf-8 -*-


import meinheld
from flask import Flask, render_template, redirect, url_for

from settings import DICS, SERVER_SETTINGS


app = Flask(__name__)
app.debug = SERVER_SETTINGS['debug']
app.LOCALES = ['en', 'ko']


@app.route('/')
def home():
    return redirect('ko')

@app.route('/ko/')
def ko():
    return redirect(url_for('ko_dic', dic='mechanics'))

@app.route('/ko/<dic>')
def ko_dic(dic):
    return render_template('ko.html', dics=DICS, dic=dic)

def cmd_args():
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('-l', dest='locale',
            choices=app.LOCALES + ['auto'],
            default='auto')
    args = parser.parse_args()
    return args


def main():
    args = cmd_args()
    if args.locale and args.locale != 'auto':
        app.babel.locale_selector_func = lambda: args.locale
    if SERVER_SETTINGS['type']=='flask':
        app.run(SERVER_SETTINGS['host'], SERVER_SETTINGS['port'])
    elif SERVER_SETTINGS['type']=='meinheld':
        print 'On http://%s:%s/' % (SERVER_SETTINGS['host'], SERVER_SETTINGS['port'])
        meinheld.listen((SERVER_SETTINGS['host'], SERVER_SETTINGS['port']))
        meinheld.run(app)


if __name__ == '__main__':
    main()
