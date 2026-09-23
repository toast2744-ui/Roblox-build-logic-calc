from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# 1. GET Request (For checking if your server is alive)
@app.route('/status', methods=['GET'])
def get_status():
    return "Flask server is online!", 200

# 2. POST Request (Captures your calculator's answer from Build Logic!)
@app.route('/send_data', methods=['POST'])
def receive_data():
    # Reads the raw binary string text sent by the HTTP Transmitter block
    calculator_data = request.data.decode('utf-8')
    
    print(f"[Build Logic Calculator Data Received]: {calculator_data}")
    
    # Return a message back to the game
    return f"Success! Received: {calculator_data}", 200

if __name__ == "__main__":
    # Ties to the port Render dynamically provides
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

