from flask import Flask, request, jsonify
from flask_cors import CORS
from duplicate import find_duplicates, find_any_duplicates, process_directory_similarity
import os

app = Flask(__name__)
CORS(app)

@app.route('/find-pdf-duplicates', methods=['POST'])
def find_pdf_duplicates_route():
    data = request.get_json()
    directory = data.get('directory')
    if not os.path.isdir(directory):
        return jsonify({'message': 'Invalid directory path'}), 400

    try:
        duplicates = find_duplicates(directory, '.pdf')
        return jsonify({'message': 'Duplicate PDF files found', 'duplicates': duplicates}), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

@app.route('/find-docx-duplicates', methods=['POST'])
def find_docx_duplicates_route():
    data = request.get_json()
    directory = data.get('directory')
    if not os.path.isdir(directory):
        return jsonify({'message': 'Invalid directory path'}), 400

    try:
        duplicates = find_duplicates(directory, '.docx')
        return jsonify({'message': 'Duplicate DOCX files found', 'duplicates': duplicates}), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

@app.route('/find-text-duplicates', methods=['POST'])
def find_text_duplicates_route():
    data = request.get_json()
    directory = data.get('directory')
    if not os.path.isdir(directory):
        return jsonify({'message': 'Invalid directory path'}), 400

    try:
        duplicates = find_duplicates(directory, '.txt')
        return jsonify({'message': 'Duplicate TXT files found', 'duplicates': duplicates}), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

@app.route('/find-any-duplicates', methods=['POST'])
def find_any_duplicates_route():
    data = request.get_json()
    directory = data.get('directory')
    if not os.path.isdir(directory):
        return jsonify({'message': 'Invalid directory path'}), 400

    try:
        duplicates = find_any_duplicates(directory)
        return jsonify({'message': 'Duplicate files found', 'duplicates': duplicates}), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500

@app.route('/find-similarity', methods=['POST'])
def find_similarity_route():
    data = request.get_json()
    directory = data.get('directory')
    if not os.path.isdir(directory):
        return jsonify({'message': 'Invalid directory path'}), 400

    try:
        similarities = process_directory_similarity(directory)
        return jsonify({'message': 'Similarity analysis completed', 
                        'similarities': similarities}), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500
    
@app.route('/delete-duplicates', methods=['POST'])
def delete_duplicates_route():
    data = request.get_json()
    duplicates = data.get('duplicates', [])
    try:
        for pair in duplicates:
            os.remove(pair[1])  # Remove the duplicate file
        return jsonify({'message': 'Duplicates deleted successfully'}), 200
    except Exception as e:
        return jsonify({'message': 'An error occurred', 'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
