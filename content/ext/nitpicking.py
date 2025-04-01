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

    def run(self) -> tuple[list[nodes.Node], list[nodes.system_message]]:
        node = nodes.raw(
            "", f'<span style="color: red;"> {self.text} </span>', format="html"
        )
        return [node], []


class NitpickDirective(SphinxDirective):
    """
    A directive to create red text in an annotated lesson
    to mark as something that you (really) want to say.

    (multi-line version of nitpicking role)
    """

    has_content = True

    def run(self) -> list[nodes.Node]:
        text = "\n".join(self.content)
        paragraph_node = nodes.raw(
            "", f'<span style="color: red;"> {text} </span>', format="html"
        )
        return [paragraph_node]


def setup(app: Sphinx) -> ExtensionMetadata:
    app.add_role("nitpick", NitpickRole())
    app.add_directive("nitpick", NitpickDirective)

    return {
        "version": "0.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
