from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    selected_fields = request.form.getlist('values[]')
    print(selected_fields)
    if file and selected_fields:
        file_content = file.read().decode('utf-8')
        # Process the content and selected fields as needed
        # For demonstration purposes, we return a JSON response with the file content and selected fields
        return jsonify({'file_content': file_content, 'selected_fields': selected_fields})


if __name__ == '__main__':
    app.run(debug=True)
