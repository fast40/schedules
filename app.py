from flask import Flask, request, render_template
from utils import get_timestamps, get_classes_info

days = {
	'monday': 'Mon',
	'tuesday': 'Tue',
	'wednesday': 'Wed',
	'thursday': 'Thu',
	'friday': 'Fri',
	# 'saturday': 'Sat',
	# 'sunday': 'Sun'
}

app = Flask(__name__)


@app.route('/')
def index():
	selected_day = request.args.get('selected_day') or 'monday'

	timestamps = get_timestamps()	
	classes_info = get_classes_info(selected_day)

	return render_template('index.html', days=days, selected_day=selected_day, timestamps=timestamps, classes_info=classes_info)


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=3000)
