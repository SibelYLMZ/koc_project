import pickle 
from flask import Flask, request, jsonify 

app = Flask(__name__)

# Diğer Flask route'larını ve kodlarını burada tanımlayabilirsiniz.

@app.route('/get_classification_report_log', methods=['GET'])
def get_classification_report_log():
    with open('class_report_log.pkl', 'rb') as file:
        class_report_log = pickle.load(file)
    return jsonify(class_report_log)

@app.route('/get_classification_report_xgb', methods=['GET'])
def get_classification_report_xgb():
    with open('class_report_xgb.pkl', 'rb') as file:
        class_report_xgb = pickle.load(file)
    return jsonify(class_report_xgb)

if __name__ == '__main__':
    app.run(debug=True)

# * Detected change in '/Users/sibelyilmaz/Desktop/koc2/app.py', reloading
# * Restarting with stat
# * Debugger is active!
# * Debugger PIN: 488-415-343
#127.0.0.1 - - [13/Oct/2023 09:24:34] "GET / HTTP/1.1" 404 -
#127.0.0.1 - - [13/Oct/2023 09:24:48] "GET / HTTP/1.1" 404 -
#127.0.0.1 - - [13/Oct/2023 09:29:23] "GET /get_classification_report_xgb HTTP/1.1" 200 -
