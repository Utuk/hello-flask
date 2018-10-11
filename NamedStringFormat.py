markup = """
<!DOCTYPE html>
<html>
    <head>
        <title>{tittle}</title>
    </head>
    <body>
        <h1>{heading}</h1>
    </body>
</html>
"""

markup = markup.format(tittle='My Page Title', heading='Page Heading')
print(markup)
#using named placed holders versus indexed place holders