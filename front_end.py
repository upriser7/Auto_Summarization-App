#This module is for the main front-end of the summarizer program, using Flask

from summarize import *
from flask import *
from werkzeug import secure_filename
from processdoc import Textblob_with_file_name
from spellcheck_and_translate import *

ALLOWED_EXTENTIONS = ['docx']

def check_ext(file_name):
    '''Checks if the type of file is supported'''
    return '.' in file_name and file_name.split('.')[1] in ALLOWED_EXTENTIONS

app = Flask(__name__)

@app.route('/')
def upload_file():
    return render_template('upload.html')

@app.route('/upload', methods = ["GET", "POST"])
def save_and_process_file():
    if request.method == 'POST':
        f = request.files['file']
        if check_ext(f.filename):
            f.save(secure_filename(f.filename))
            if len(request.form.getlist('edit')) == 0:
                return redirect(url_for('summary', filename = f.filename))
            else:
                return redirect(url_for('summary_with_edit', filename = f.filename, edits = request.form.getlist('edit'), language = request.form.get('language')))
        else:
            abort(415) ###unsupported media type error message

@app.route('/summarize/<filename>')
def summary(filename):
    return render_template('summary.html', text = ''.join(create_summary(Textblob_with_file_name(filename), length_of_summary = None)))



@app.route('/summarize/<filename>/<edits>/<language>')
def summary_with_edit(filename, edits, language):
    if 'spellcheck' in edits and 'translate' in edits:
        return render_template('summary.html', text = translate(spellcheck(''.join(create_summary(Textblob_with_file_name(filename), length_of_summary = None))), language))
    elif 'spellcheck' in edits:
        return render_template('summary.html', text = spellcheck(''.join(create_summary(Textblob_with_file_name(filename), length_of_summary = None))))
    elif 'translate' in edits:
        return render_template('summary.html', text = translate(''.join(create_summary(Textblob_with_file_name(filename), length_of_summary = None)), language))



if __name__ == "__main__":
    app.run(debug = True)
