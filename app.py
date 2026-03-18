from flask import Flask, render_template
import os

base_dir = os.path.abspath(os.path.dirname(__file__))

# If the "templates" directory doesn't exist (like on your GitHub right now), use the base directory
template_dir = os.path.join(base_dir, 'templates')
if not os.path.exists(template_dir):
    template_dir = base_dir

# Same for "static" directory
static_dir = os.path.join(base_dir, 'static')
if not os.path.exists(static_dir):
    static_dir = base_dir

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
