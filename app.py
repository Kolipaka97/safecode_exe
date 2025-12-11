from flask_cors import CORS
from flask import Flask, request, jsonify
import subprocess
import uuid
import os

app = Flask(__name__)
CORS(app)


@app.route("/run", methods=["POST"])
def run_code():
    data = request.get_json(silent=True)

    # ✅ Handle missing or empty code safely
    if not data or "code" not in data or not data["code"].strip():
        return jsonify({
            "output": "No code provided. Please enter some Python code."
        })

    code = data["code"]

    # ✅ Code length protection (5000 characters)
    if len(code) > 100:
        return jsonify({
            "output": "Code too long. Maximum allowed length is 100 characters."
        })

    filename = f"{uuid.uuid4()}.py"

    with open(filename, "w") as f:
        f.write(code)

    try:
        result = subprocess.run(
            [
                "docker", "run",
                "--rm",
                "--read-only",
                "--cpus=1",
                "--memory=128m",
                "--network", "none",
                "-v", f"{os.getcwd()}:/app",
                "python:3.11-slim",
                "python", f"/app/{filename}"
            ],
            capture_output=True,
            text=True,
            timeout=10
        )

        output = result.stdout + result.stderr

    except subprocess.TimeoutExpired:
        output = "Execution timed out after 10 seconds"

    except Exception as e:
        output = str(e)

    finally:
        if os.path.exists(filename):
            os.remove(filename)

    return jsonify({"output": output})


if __name__ == "__main__":
    app.run(debug=True)