from flask import Flask, render_template, request
from walk_time_differences import walk_time_differences, train_lists, irregular_stop_name_list
import json
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/select_line')
def select_line():
    t_line_value = train_lists[request.args.get("list_of_lines")]
    train_list = t_line_value
    return json.dumps(t_line_value[0:-1], ensure_ascii=True).replace("'", '"')

@app.route('/select_stop')
def select_stop():
    t_stop_value = request.args.get("first_stop_list")
    t_line_value = train_lists[request.args.get("list_of_lines")]
    sub_train_list = t_line_value[t_line_value.index(t_stop_value)+1:]
    return json.dumps(sub_train_list, ensure_ascii=True).replace("'", '"')

@app.route('/get_difference')
def get_difference():
    t_line_value = request.args.get("list_of_lines")
    t_first_stop_value = request.args.get("first_stop_list")
    t_second_stop_value = request.args.get("second_stop_list")

    t_line_value = "walk_time_difference_" + "_".join(t_line_value.split("_")[0:-1])
    t_first_stop_value = t_first_stop_value + "_" + t_line_value[-1]
    t_second_stop_value = t_second_stop_value + "_" + t_line_value[-1]

    walk_time_list = walk_time_differences[t_line_value]
    time_diff = walk_time_list[t_first_stop_value + " " + t_second_stop_value]
    return str(format(abs(time_diff/60), ".0f"))

port = int(os.environ.get('PORT'))


if __name__ == '__main__':
    app.run(port=port)