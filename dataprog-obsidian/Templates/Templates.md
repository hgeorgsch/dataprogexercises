

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

Element styiling with class `smallertext` reduces the font size.

## Existing templates

This templates work, but are fairly crude.  Each box has more
or less fixed width, and I have not managed to get the contents
to scale well.  We should explore the use of CSS flexbox, below.

+ `tpl-titleslide.md` : Titleslide with author 
    + Used in other projects - for the modules we prefer titlepage from Akrinn
+ `tpl-flex.md` : scale images to use available space
    + This can probably replace quote and quote-header
    + Used much in Slumptalsgenerator
    + Uses [CSS flexbox](https://css-tricks.com/snippets/css/a-guide-to-flexbox/).
    + Can also be used as titlepage with image (Using `h1`)
+ `tpl-diagram.md` : White background for TiKz figures 
    + Except for the white background, this works like tpl-flex
+ `tpl-quote-header.md` : Image or quote with header and byline 
    + Can also be used as titlepage with image (Using `h1`)
    + Used.  
    + **Deprecated** in favour of tpl-flex.
+ `tpl-quote.md` : Image or quote with byline 
    + **Deprecated** in favour of tpl-flex.
+ `tpl-smalltext.md` : Reduced text size and wide code boxes
    + **Debug** `code` boxes do not scale well
+ `tpl-three.md` : Three images side by side with byline 
    + Used once, OK
+ `tpl-twocolumn.md` : Two image side by side with byline 
    + Mainly works
+ `tpl-fitdiagram2.md` ???
    + Used only by Jonas. 
    + Early attempt using flexbox.  Does it work?
