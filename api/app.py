from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/produccion")
def produccion():
    datos = [
        {"fabrica": "A", "produccion": 120},
        {"fabrica": "B", "produccion": 90},
        {"fabrica": "C", "produccion": 150},
    ]
    return jsonify(datos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
