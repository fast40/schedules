from datetime import datetime, timedelta
import json

CLASSES_JSON = 'static/classes.json'

default_start = datetime.strptime('8:00am', '%I:%M%p')
default_end = datetime.strptime('7:00pm', '%I:%M%p')


def parse_time(time, time_format='%I:%M%p'):
	return datetime.strptime(time, time_format)


def format_time(time):
	result = time.strftime('%I:%M')
	result = result.removeprefix('0')

	return result


def get_timestamps(day_start=default_start, day_end=default_end, period=timedelta(minutes=60)):
	current_timestamp = day_start.replace(minute=0, second=0, microsecond=0)
	timestamps = []

	while current_timestamp < day_end:
		timestamps.append(format_time(current_timestamp))
		current_timestamp += period
	
	return timestamps


def get_classes_info(day, day_start=default_start, day_end=default_end):
	with open(CLASSES_JSON, 'r') as file:
		data = json.load(file)

	interval = day_end - day_start

	classes_info = {student_key: [] for student_key in data}

	for student_key in data:
		for class_key in data[student_key]:
			for meeting in data[student_key][class_key]:
				if day in meeting['days']:  # TODO: Make 'monday' not hard-coded
					meeting_start = parse_time(meeting['start'])
					meeting_end = parse_time(meeting['end'])

					top = round(((meeting_start - day_start) / interval) * 100, 3)
					height = round(((meeting_end - meeting_start) / interval) * 100, 3)

					classes_info[student_key].append(f'top: {top}%; height: {height}%;')

	return classes_info
