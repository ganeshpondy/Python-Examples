from flask import Flask

# create an instance of the Flask app:
app = Flask(__name__)

# Define a route that will return the contents of the HTML file:
@app.route("/")
def home():
    # with open("/mnt/c/GaneshB/DRIVE/DevOps/SandipDas/LAB/Python/Project-Flask-1/index.html", "r") as f:
    with open("index.html", "r") as f:
        return f.read()

# Run the Flask app:
if __name__ == "__main__":
    app.run(debug=True)
