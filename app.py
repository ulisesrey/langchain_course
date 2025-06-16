from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from prompt import ice_break_with

load_dotenv()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process', methods=['POST'])
def process():
    name = request.form.get('name')
    if not name:
        return jsonify({'error': 'Name is required'}), 400

    try:
        summary, photo_url = ice_break_with(name=name)
        return jsonify({
            'summary': summary.to_dict(),
            'photo_url': photo_url
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4800)