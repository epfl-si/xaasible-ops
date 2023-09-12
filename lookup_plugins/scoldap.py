# Look up things in EPFL's scoldap

from ldap3 import Server, Connection, SUBTREE

from ansible.plugins.lookup import LookupBase
from ansible.errors import AnsibleError

class LookupModule(LookupBase):
    def run(self, terms, by, get, variables=None):
        search_filter = "(%s=%s)" % (by, terms[0])

        ldap = Connection(
            Server("ldaps://scoldap.epfl.ch:636"), auto_bind=True)
        ldap.search(search_filter=search_filter,
                    search_base="o=epfl,c=ch",
                    search_scope=SUBTREE,
                    attributes=[get])

        if len(ldap.entries) == 1:
            return [ldap.entries[0][get].value]
        else:
            raise AnsibleError("%d entries found for %s, expected 1" %
                               (len(ldap.entries), search_filter))
