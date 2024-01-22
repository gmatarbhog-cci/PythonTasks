from yattag import Doc


def generate_content():
    doc, tag, text, line = Doc().ttl()
    table_css = 'border: 1px solid black; border-collapse: collapse'
    with tag('html'):
        with tag('body'):
            with tag('h1', style='text-align:center'):
                text('My HTML page')
            with tag('h4'):
                text('Table')
            with tag('table', style=table_css):
                with tag('tr', style=table_css):
                    with tag('thead'):
                        with tag('tr'):
                            with tag('th'):
                                text('id')
                            with tag('th'):
                                text('value')
                    with tag('tr'):
                        with tag('td'):
                            text('1')
                        with tag('td'):
                            text('Python')
            with tag('h4'):
                text('Bulleted list')
            with tag('ul', id='langs'):
                line('li', 'Java')
                line('li', 'Python')
                line('li', 'Nodejs')
    f = open("html-page.html", "w")
    f.write(doc.getvalue())
    f.close()


generate_content()
