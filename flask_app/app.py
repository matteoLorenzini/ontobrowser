from flask import Flask, render_template, request
import rdflib

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        graph = rdflib.Graph()
        graph.parse(file, format='application/rdf+xml')
        return render_template('visualize.html', data=graph.serialize(format='turtle').decode('utf-8'))

if __name__ == '__main__':
    app.run(debug=True)