from flask import Flask, render_template, request, jsonify

from Lab8.src.flask.services.FigureService import FigureService

app = Flask(__name__)
service = FigureService()

# figure_colors = {"square": "#808080", "circle": "#808080", "triangle": "#808080"} # code smell

@app.route('/')
def index():
    return render_template('index.html', figure_colors=service.get_colors())

@app.route('/change-color', methods=['POST'])
def change_color():
    data = request.get_json()
    figure_type = data.get('figure_type')
    new_color = data.get('new_color')

    if not figure_type or not new_color:
        return jsonify({"status": "error", "message": "Invalid data"}), 400

    if service.update_figure_color(figure_type, new_color):
        return jsonify({"status": "success", "figure_colors": service.get_colors()})
    return jsonify({"status": "error", "message": "figure type error"}), 400



@app.route('/change-color-all', methods=['POST'])
def change_color_all():
    data = request.get_json()
    new_color = data.get('new_color')

    if not new_color:
        return jsonify({"status": "error", "message": "New color required"}), 400

    service.update_all_colors(new_color)
    return jsonify({"status": "success", "figure_colors": service.get_colors()})


if __name__ == '__main__':
    app.run(debug=True)