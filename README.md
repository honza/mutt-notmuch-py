mutt-notmuch-py
===============

[![PyPI version](https://badge.fury.io/py/mutt-notmuch.svg)](https://badge.fury.io/py/mutt-notmuch)

This is a python version of the original mutt-notmuch script.

It will interactively ask you for a search query and then symlink the matching
messages to `$HOME/.cache/mutt_results`.

Add this to your muttrc.

```
macro index / "<enter-command>unset wait_key<enter><shell-escape>mutt-notmuch-py<enter><change-folder-readonly>~/.cache/mutt_results<enter>" \
            "search mail (using notmuch)"
```

This script overrides the `$HOME/.cache/mutt_results` each time you run a
query.

Install this by adding this file somewhere on your `PATH`.

Only tested on OSX Lion, OSX El Capitan.

Options
-------

```
-g        Use gmail specific info (All Mail search)
-G        Do not use gmail specific info
-p [path] Limit search results to files with path in the path name
```

License
-------

BSD, short and sweet
