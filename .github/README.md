# The black-holes.org public site

This repo contains the [Jekyll](https://jekyllrb.com/) code responsible for creating the public
portion of the black-holes.org site.  Basically, this means that we can write pages for the site as
standard markdown, and it will be rendered for us to a nice, fancy website.  Currently, github
automatically does this rendering for us because it detects jekyll files in the `gh-pages` branch,
though it would also be possible to render manually via github actions if we need to use features
github doesn't enable by default.

See the rendered site [here](https://sxs-collaboration.github.io/www_black-holes_org).


## Quickstart for updaters: building locally with Jekyll

If you want to test the site locally before submitting a PR, you need
to have Jekyll and all the dependencies installed.

1. Install ruby through your system's package manager
2. Optionally install rbenv so you can have more fine-grained control
   to use a specific version of ruby in just this repo
3. Do `gem install bundler` to install the ruby "gem" named bundler
4. Do `bundle install` to install the gems for jekyll and all other
   dependancies
5. Do `git submodule init` followed by `git submodule update` to make
   sure you have the files in `_sass/bulma`
6. You should now be able to build locally.  To serve the site in real
   time, do `bundle exec jekyll serve`.  To build the deployment into
   the `_site` subdirectory, do `bundle exec jekyll build`.

## Your details in /about-sxs/people

Please feel free to add yourself to the SXS members page! This page is
generated from all files in the directory `_people/`. To start, create
a file e.g. `_people/My_Name.markdown`, with contents:

```markdown
---
name: Given Middle Surname
lastname: Surname
group: (faculty|academic_staff|postdocs|graduate_students|alumni)
position: My position title
address: My address
institution: My institution
email: My email
website: https://just/a/plain/url
phone: My phone number
advisor: My advisor
specialties: My specialties
---

#### Biography

When I was young, I looked up at the stars...

```

The `lastname` field is for sorting purposes, while the `name` field
is how your name will be displayed.

If you want to include a photo, it *must* be in
`/images/people/My_Name.jpg`, and this must be the exact same
`My_Name` as the markdown file above.

It is important for the `group:` field to take on *exactly* one of the
values in the list `faculty, academic_staff, postdocs,
graduate_students, alumni`. If not, you won't appear in the list.

It's also possible to have multiple affiliations. In this case, put
your info associated to each affiliation under the `affiliations:`
group as follows:

```yml
affiliations:
    - position: Position 1 title
      address: My address 1
      institution: My institution 1
      email: My email 1
      website: My web site 1
      phone: My phone 1
    - position: Position 2 title
      address: My address 2
      institution: My institution 2
      email: My email 2
      website: My web site 2
      phone: My phone 2
    ...
```

Each affiliation can have any subset of the fields `position`,
`address`, `institution`, `email`, `website`, and `phone`.  If a field
is omitted, it will be suppressed in the output.

## Writing your own posts

One of the goals of making this website more usable is to encourage SXS members to write entries
about their research for the site.  The two most recent entries show up on the homepage under
"Recent Research", along with brief synopses and links to the full description.

To write your own entry, just create a Pull Request on this repo, with a file as described below.
This file should be [github-flavored markdown](https://github.github.com/gfm/) (basically [standard
markdown](https://www.markdownguide.org/) with a few extensions), but you need to remember a few
points to get it published:

1. You *must* put the file in the `_posts` directory

2. You *must* name the file starting with the date as `YYYY-MM-DD-awesome_file_name.md` (where you
   get to pick the awesome name, but the date should be its actual value)

3. You *must* start the file with your title — something like this:
    ```
    # The title of my awesome research
    ```
    Again, you get to pick the title, but nothing other than whitespace should appear in the file
    before this line (unless you're getting fancy with adding YAML front matter...).  Try to keep
    the title quite short so that it fits in its place on the homepage, and maybe not so technical
    so that the public have a chance of understanding it.

4. The first paragraph will be used on the homepage to advertise this post, so think of this part as
   your [elevator pitch](https://en.wikipedia.org/wiki/Elevator_pitch).  Try to limit the jargon in
   this part, since it's the part that most non-scientists will see.  Try to keep it brief, but also
   include a little motivation and the most important conclusions.

5. The rest of the post can be as long as you like — though remember that this isn't the paper.
   Long technical details should go in a paper; this is for communicating your results to people who
   are mostly science literate, but not as technically knowledgeable as you.

6. If you need to include figures, you'll want to use PNG; PDFs do not embed well, and JPGs get
   fuzzy too easily.  The files should be placed in `images/posts/YYYY-MM-DD-other-file-name.png`,
   and you can add them to your page with code like
   ```
   Here's the picture: ![Description of image]({{ site.baseurl }}/images/posts/YYYY-MM-DD-other-file-name.png)
   ```
   If you want to adjust attributes of the image like width and height, you can use [span inline
   attribute lists](https://kramdown.gettalong.org/syntax.html#span-ials): *immediately* after the
   image code above (with no whitespace in between), add something like this:
   ```
   {:height="313px" width="600px"}
   ```

7. Remember to link to the *free* (presumably arXiv) version of your paper.

## Links in jekyll

The [Jekyll docs on
linking](https://jekyllrb.com/docs/liquid/tags/#links). When making
internal links to pages, use the `{% link ... %}` tag, as follows:

```
[text of link]({{ site.baseurl }}{% link real/path/to/file.md %})
```

where `real/path/to/file.md` is the path in the filesystem, based at
the root of this repo.  At build time, Jekyll will check that this
path actually exists, and substitute its permalink (so we can later
change the url without rewriting all links to that page).

## Including math

We use the [MathJax](https://www.mathjax.org/) javascript library to
render LaTeX math in the user's browser on the fly.  Just like regular
LaTeX, math can be either inline, like $E=mc^2$, or "display" mode,
like

$$
E=mc^2.
$$

We are using the [default MathJax options for
delimiters](https://docs.mathjax.org/en/latest/input/tex/delimiters.html).
For inline math, MathJax expects `\( latex code \)`, or `$$ latex code $$`. For
display math, MathJax expects

```
\[
latex code.
\]
```

However, note that [kramdown (the markdown variant used here) has its
own set of backslash
escapes](https://kramdown.gettalong.org/syntax.html#automatic-and-manual-escaping). Therefore,
if you want to use `\( latex \)` or `\[ latex \]` in markdown-parsed
blocks, you must escape the backslashes.  Using `$$ latex $$` does not
require escaping the delimiters.

Note that [kramdown recognizes certain blocks as HTML and
does not parse
them](https://kramdown.gettalong.org/syntax.html#html-blocks), meaning
that within HTML blocks you don't need to escape backslashes.  This
is most useful for long displaymath equations.  The simplest solution
is to just wrap them in a `<div> ... </div>` pair, e.g.

```
<div>\[
display mode latex.
\]</div>
```

MathJax will also automatically render blocks in
`\begin{env}...\end{env}` without delimiters, so if you use the align
environment, you can actually get away with

```
<div>\begin{align}
aligned equation latex.
\end{align}</div>
```

## Embedding Youtube videos

[This very clever tip](http://www.beingy.net/blog/embed-youtube-video-in-jekyll/) allows us to
simply use code in our pages like this:
```
{% include youtube-embed.html id="Zt8Z_uzG71o" %}
```
Basically, all the hassle of writing the HTML for embedding youtube videos has been offloaded to the
single file `_includes/youtube-embed.html`, and we just specify the ID of the video as a parameter
on the page we're writing.


## To Do

- [x] Add page collecting all research posts
- [x] Add "Explore" and quote to homepage
- [x] Move `assets` to root; we don't have many JS or CSS things anyway, and the extra characters are
      annoying
- [x] Breadcrumbs and/or sub-navigation in sidebar for main pages
- [x] Add Prev/Next buttons in the main pages
- [x] Randomly select a sidebar quote for pages that don't have one specified
- [x] Create menu automatically from ~~pages~~ `_data/menu.yml`
- [ ] Fix menu on mobile devices
- [ ] Fix navigation coins on homepage, so that they're in rows of 4, 2, or 1
- [ ] Add navigation coins in the sidebar for articles
- [ ] "Featured Video" in sidebar?
- [ ] Streamline CSS, so that only the necessary elements get served: one for homepage, another for
      everything else; maybe get rid of Bulma?
- [x] Styling on the about-sxs/people page is very broken
- [x] Style audio so that it's visible
- [ ] Switch to the SVG logo, using
      [Ubuntu](https://fonts.google.com/specimen/Ubuntu?preview.text=IMULATING%20ETREME%20PACETIMES&preview.text_type=custom&query=ubuntu)
      for the title and
      [Yellowtail](https://fonts.google.com/specimen/Yellowtail?category=Handwriting&preview.text=Black%20holes,%20neutron%20stars,%20and%20beyond%E2%80%A6&preview.text_type=custom&slant=8&subset=latin)
      or similar for the extras
- [ ] Automate glossary links?  (This would presumably require some non-standard plugin, and thus
      more CI work)
- [ ] Add `index.md` files in every relevant directory
- [ ] Add redirects for old ugly pages with
      [jekyll-redirect-from](https://github.com/jekyll/jekyll-redirect-from), which is allowed on github
- [ ] Update old `.markdown` files to actually use markdown and have correct front matter
- [ ] Make the FAQ something like [the old one](https://www.black-holes.org/explore/faq)
- [ ] Correct Next/Prev buttons to use `_data/menu.yml`
- [ ] Convert old Flash animations to use CSS or JavaScript


## Fonts used on the SXS website

For some icons (e.g. the email envelope on the people page, speaker
icon for sounds), we use [Font Awesome
6.6.0](https://fontawesome.com/).  For the arXiv icon, we use
[Academicons](https://jpswalsh.github.io/academicons/).

[The following is from the style guide written by our original web developer, Yvonne Tang.]
 
We made use of high quality free webfonts available through the [Google Font API]("https://www.google.com/fonts"). This allows everyone to be able to experience the website in the font we specified, even though the font might not be installed on the person's own computer/device.

[Open Sans]("https://www.google.com/fonts/specimen/Open+Sans") - The font we use for body text, eg, this current line you are reading. This is also the font we use for Heading 3 and Heading 5.

[Oswald]("https://www.google.com/fonts/specimen/Oswald") - This font we use for Heading 2 (eg, the title of this article), top level navigation of the Main Menu, titles of the modules on the sidebar and footer.

**Georgia** - This is not a Google Font, but a common serif font that is installed on most computers. This font is used for Heading 4, as well as blockquotes ("Inspiration" on the sidebar, and some quotes on the Science pages).
