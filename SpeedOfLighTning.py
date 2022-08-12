from flask import Flask, render_template, request
from walk_time_differences import walk_time_differences
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/select_line')
def select_line():
    t_line_value = walk_time_differences[request.args.get("list_of_lines")]
    print(type(json.dumps(t_line_value)))
    return json.dumps(t_line_value, ensure_ascii=True)

app.run()