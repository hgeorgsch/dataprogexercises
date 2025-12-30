

Common CSS styles are loaded using the following metadata on
document level.
```
css: css/templates.css
```

## Formatting conventions

Use `h1` on titleslide.  Use the tpl-titleslide template
only when adding author and other information.

Use `h2` for slide headers throughout.
This is styled with a medium text size and ugly colour.

## Existing templates

This templates work, but are fairly crude.  Each box has more
or less fixed width, and I have not managed to get the contents
to scale well.  We should explore the use of CSS flexbox, below.

+ `tpl-titleslide.md` : Titleslide with author 
    + Used in other projects - for the modules we prefer titlepage from Akrinn
+ `tpl-diagram.md` : White background for TiKz figures 
    + This mainly works.
    + One might prefer automatic scaling of image size to fit the page.
+ `tpl-quote-header.md` : Image or quote with header and byline 
    + Can also be used as titlepage with image (Using `h1`)
    + Used.  
    + Can we merge this with `tpl-smalltext.md`
+ `tpl-quote.md` : Image or quote with byline 
    + This mainly works
    + One might prefer automatic scaling of image size to fit the page.
+ `tpl-smalltext.md` : Reduced text size and wide code boxes
    + **Debug** `code` boxes do not scale well
+ `tpl-three.md` : Three images side by side with byline 
    + Used once, OK
+ `tpl-twocolumn.md` : Two image side by side with byline 
    + Mainly works

## flexbox templates

These templates are early attempts using
[CSS flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/).

+ `tpl-flex.md` scales images to use available space
    + Tested in Test.md - seems to work
    + Should be tested with tables, code and other contents
    + Not yet put to use
+ `tpl-fitdiagram2.md` ???
    + Used only by Jonas. 
+ `tpl-fit-table.md` : Supposed to scale a table to fit the page
    + **Debug** This does not work
    + Not used
