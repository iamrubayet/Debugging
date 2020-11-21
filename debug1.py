def remove_html_markup(s):
    tag = False
    out = ""

    for c in s:
        if c == '<':  #start markup
            tag = True
        elif c == '>': #end markup
            tag = False
        elif not tag:
            out = out + c

    return out


print (remove_html_markup("<b>foo<b>"))
