#!/usr/bin/env python
"""
mutt-notmuch-py

This is a Gmail-only version of the original mutt-notmuch script.

It will interactively ask you for a search query and then symlink the matching
messages to $HOME/.cache/mutt_results.

Add this to your muttrc.

macro index / "<enter-command>unset wait_key<enter><shell-escape>mutt-notmuch-py<enter><change-folder-readonly>~/.cache/mutt_results<enter>" \
          "search mail (using notmuch)"

This script overrides the $HOME/.cache/mutt_results each time you run a query.

Install this by adding this file somewhere on your PATH.

Only tested on OSX Lion.

(c) 2012 - Honza Pokorny
Licensed under BSD
"""
import hashlib, sys
from commands import getoutput
from mailbox import Maildir
from optparse import OptionParser


def digest(filename):
    with open(filename) as f:
        return hashlib.sha1(f.read()).hexdigest()


def pick_all_mail(messages):
    for m in messages:
        if 'All Mail' in m:
            return m


def empty_dir(directory):
    box = Maildir(directory)
    box.clear()


def command(cmd):
    return getoutput(cmd)


def main(dest_box):
    query = raw_input('Query: ')

    command('mkdir -p %s' % dest_box)
    command('mkdir -p %s/cur' % dest_box)
    command('mkdir -p %s/new' % dest_box)

    empty_dir(dest_box)

    files = command('notmuch search --output=files %s' % query).split('\n')
    files = filter(None, files)

    data = {}
    messages = []

    for f in files:
        sha = digest(f)
        if sha not in data.keys():
            data[sha] = [f]
        else:
            data[sha].append(f)

    for sha in data.keys():
        if is_gmail and len(data[sha]) > 1:
            messages.append(pick_all_mail(data[sha]))
        else:
            messages.append(data[sha][0])

    for m in messages:
        command('ln -s "%s" %s/cur/' % (m, dest_box))


if __name__ == '__main__':
    global is_gmail

    p = OptionParser("usage: %prog [OPTIONS] [RESULTDIR]")
    p.add_option('-g', '--gmail', dest='gmail',
                 action='store_true', default=True,
                 help='gmail-specific behavior')
    p.add_option('-G', '--not-gmail', dest='gmail',
                 action='store_false',
                 help='gmail-specific behavior')
    (options, args) = p.parse_args()

    is_gmail = options.gmail

    if args:
        dest = args[0]
    else:
        dest = '~/.cache/mutt_results'

    main(dest.rstrip('/'))
