from flask import Flask, jsonify, render_template
import markdown


app = Flask(__name__)


def render_markdown_file(file_path):
    '''Opens a markdown file and returns the contents rendered as html.
       Returns None if the file does not exist.'''
    try:
        file_contents = open(file_path, 'r').read()
    except IOError:
        return 'File "%s" does not exist.' % file_path
    content = markdown.markdown(file_contents)
    return content


@app.route('/')
def index():
    return ':)'


@app.route('/<path:file_path>')
def document(file_path):
    markup = render_markdown_file(file_path)
    return render_template('document.html', markup=markup)


if __name__ == '__main__':

    app.debug = True
    app.run()
