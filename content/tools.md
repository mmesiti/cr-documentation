# Popular tools and solutions

```{questions}
- What tools are out there?
- What are their pros and cons?
```

```{objectives}
- Choose the right tool for the right reason.
```

---

{nitpick}`Can code self-document? Some people say so, but it is hard!`

## In-code documentation

- Comments, function docstrings, ...
- Advantages
  - Good for programmers
  - Version controlled alongside code
  - Can be used to auto-generate documentation for functions/classes
- Disadvantage
  - Probably not enough for users of the code

We will have a closer look at this in the {ref}`in-code-documentation` episode.

---

## README files

- Advantages
  - Versioned (goes with the code development)
  - It is often good enough to have a `README.md` or `README.rst` along with your code/script
- If you use README files, use either
  [RST](https://docutils.sourceforge.net/rst.html) or
  [Markdown](https://commonmark.org/help/)
- A great guide to README files: [MakeaREADME](https://www.makeareadme.com/)

We will have a closer look at this in the {ref}`writing-readme-files` episode.

{nitpick}`Talking about READMEs: they are possibly the most AI-Friendly documentation format (you can just copy&paste the whole README in the context window of the LLM of your choice)`

---

## reStructuredText and Markdown

```markdown
# This is a section in Markdown   This is a section in RST
                                  ========================

## This is a subsection           This is a subsection
                                  --------------------

Nothing special needed for        Nothing special needed for
a normal paragraph.               a normal paragraph.

                                  ::

    This is a code block          This is a code block


**Bold** and *emphasized*.        **Bold** and *emphasized*.

A list:                           A list:
- this is an item                 - this is an item
- another item                    - another item

There is more: images,            There is more: images,
tables, links, ...                tables, links, ...
```

- Two of the most popular lightweight markup languages.
- reStructuredText (RST) has more features than Markdown but the choice is a matter of taste.
- There are (unfortunately) [many flavors of Markdown](https://github.com/jgm/CommonMark/wiki/Markdown-Flavors).
- Motivation to stick to a standard text-based format: **They make it easier to move the documentation to other tools
  which also expect a standard format, as the project/organization grows**.
- We will use [MyST](https://myst-parser.readthedocs.io/en/latest/)
  flavored Markdown in the {ref}`sphinx` episode and the
  {ref}`gh-pages` example.
- Nice resource to learn Markdown: [Learn Markdown in 60 seconds](https://commonmark.org/help/)
- [Pandoc](https://pandoc.org/) can convert between MD and RST (and many other formats).

---

## HTML static site generators

There are many tools that can turn RST or Markdown into beautiful HTML pages:

- [Sphinx](https://www.sphinx-doc.org) **← we will exercise this, this is how this lesson material is built**
  - Generate HTML/PDF/LaTeX from RST and Markdown.
  - Basically all Python projects use Sphinx but **Sphinx is not limited to Python**.
  - [Read the docs](https://readthedocs.org)
    hosts public Sphinx documentation for free!
  - Also hostable anywhere else, like Github pages.
  - API documentation possible.

- [Jekyll](https://jekyllrb.com)
  - Generates HTML from Markdown.
  - GitHub supports this without adding extra build steps.

- [pkgdown](https://pkgdown.r-lib.org/)
  - Popular in the R community

- [MkDocs](https://www.mkdocs.org/)
- [GitBook](https://www.gitbook.com/)
- [Hugo](https://gohugo.io)
- [Hexo](https://hexo.io)
- [Zola](https://www.getzola.org/) **<- this is what we use for our project website and workshop websites**
- There are many more ...

GitHub, GitLab, and Bitbucket make it possible to serve HTML pages:
- [GitHub Pages](https://pages.github.com)
- [Bitbucket Pages](https://pages.bitbucket.io/)
- [GitLab Pages](https://pages.gitlab.io)

---

## Wikis

- Popular solutions (but many others exist):
  - [MediaWiki](https://www.mediawiki.org)
  - [Dokuwiki](https://www.dokuwiki.org)
- Advantage
  - Barrier to write and edit is low
- Disadvantages
  - Typically disconnected from source code repository (**reproducibility**)
  - Difficult to serve multiple versions
  - Difficult to check out a specific old version
  - Typically needs to be hosted and maintained

---

## LaTeX/PDF

- Advantage
  - Popular and familiar in the physics and mathematics community
- Disadvantages
  - PDF format is not ideal for copy-pasting of examples
  - Possible, but not trivial to automate rebuilding documentation after every Git push

---

## Doxygen

- Auto-generates API documentation
- Documented directly in the source code
- Popular in the C++ community
- Has support for C, Fortran, Python, Java, etc.,
  see [Doxygen Github Repo](https://github.com/doxygen/doxygen)
- Many keywords are understood by Doxygen:
  [Doxygen special commands](https://www.doxygen.nl/manual/commands.html)
- Can be used to also generate higher-level ("human") documentation
- Can be deployed to GiHub/GitLab/Bitbucket Pages

{nitpick}`If you prefer the look&feel of Sphinx, you can still use Doxygen as a backend and Sphinx through Breathe.`

---

## Other tools

- Fortran
  - [Fortran Documenter (FORD)](https://github.com/Fortran-FOSS-Programmers/ford)

- Julia
  - [Franklin](https://franklinjl.org/): static site generator
  - [Documenter.jl](https://juliadocs.github.io/Documenter.jl/stable/)

- [Quarto](https://quarto.org/) converts markdown to websites, pdfs, ebooks and many other things

---

```{keypoints}
- Some popular solutions make reproducibility and maintenance of multiple code versions difficult.
```
