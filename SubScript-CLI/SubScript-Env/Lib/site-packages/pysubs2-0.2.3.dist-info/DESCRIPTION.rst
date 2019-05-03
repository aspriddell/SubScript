\
pysubs2 is a Python library for editing subtitle files.
It’s based on *SubStation Alpha*, the native format of
`Aegisub <http://www.aegisub.org/>`_; it also supports *SubRip*,
*MicroDVD* and *MPL2* formats. There is a small CLI tool for batch conversion
and retiming.

::

    import pysubs2
    subs = pysubs2.load("my_subtitles.ass", encoding="utf-8")
    subs.shift(s=2.5)
    for line in subs:
        line.text = "{\\be1}" + line.text
    subs.save("my_subtitles_edited.ass")



