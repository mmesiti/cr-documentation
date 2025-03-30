# Following the instructions here:
# https://www.sphinx-doc.org/en/master/development/tutorials/extending_syntax.html
# Also asked Claude for help about in-line html escaping.

from __future__ import annotations

from docutils import nodes

from sphinx.application import Sphinx
from sphinx.util.docutils import SphinxDirective, SphinxRole
from sphinx.util.typing import ExtensionMetadata

class NitpickRole(SphinxRole):
    """
    A role to create red text in an annotated lesson 
    to mark as something that you (really) want to say.
    """

    def run(self)-> tuple[list[nodes.Node], list[nodes.system_message]]:
        node = nodes.raw('', f'<span style="color: red;"> {self.text} </span>', format = 'html')
        return [node] , []


def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_role('nitpick', NitpickRole())

    return { 
        'version' :'0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
        }
