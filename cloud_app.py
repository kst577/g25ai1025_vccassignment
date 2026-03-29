from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Replace with your actual Student ID for the final submission
    return "<h1>HI I AM SAITEJA G25AI1025</h1><p>Cloud Instance Scaled Successfully!</p>"

if __name__ == "__main__":
    # Port 80 is the standard web port allowed by your GCP Firewall
    app.run(host='0.0.0.0', port=80)
