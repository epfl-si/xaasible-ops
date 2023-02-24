"""Parsing Python is hard, let's have Jinja filters instead."""

class FilterModule(object):
    def filters(self):
        return {
            'dictify': self.dictify
        }

    def dictify(self, l, by_key):
        return dict((item[by_key], item) for item in l)
