from flask import Flask, request, send_file, jsonify
from flask_cors import CORS
from enhancer import enhance_image
from io import BytesIO

app = Flask(__name__)
CORS(app)

@app.route("/upload", methods=["POST"])
def upload_image():
    try:
        file = request.files.get("image")
        if not file:
            return jsonify({"error": "No file uploaded"}), 400

        input_bytes = file.read()
        output_bytes_io, mimetype = enhance_image(input_bytes)

        return send_file(output_bytes_io, mimetype=mimetype)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)