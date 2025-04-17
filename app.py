from flask import Flask, request, jsonify
import main  # importing your main.py (you might need to adapt this)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to CPTXT Extract API!"

@app.route('/run', methods=['POST'])
def run_script():
    try:
        # You can call the function you want to run from main.py here
        # Assuming main.py has a function like main.run()
        output = main.main()  # adjust based on your main.py structure
        return jsonify({'status': 'success', 'output': output})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
