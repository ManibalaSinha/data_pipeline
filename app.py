#Flask API to trigger pipeline
from flask import Flask, jsonify
from pipeline import run_pipeline
import threading

app = Flask(__name__)
@app.route("/run_pipeline", methods=["POST"])
def trigger_pipeline():
   thread = threading.Thread(target=run_pipeline)
   thread.start()
   return jsonify({"status":"Pipeline triggered"}), 202
if __name__ == "__main__":
   app.run(debug=True, port=5000)