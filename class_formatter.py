string = '08/26/2023-12/15/2023 Lecture Monday 01:15PM - 04:25PM, Physics, Room 108 08/26/2023-12/15/2023 Lecture Wednesday 01:15PM - 02:05PM, Physics, Room 108 08/26/2023-12/15/2023 Extensive Lab Wednesday 02:15PM - 04:20PM, Physics, Room 108'

print(string)

days = [
	'monday',
	'tuesday',
	'wednesday',
	'thursday',
	'friday',
	'saturday',
	'sunday'
]

def analyze(string):
	string = string.lower()
	string = string.replace('extensive lab', 'extensive_lab')
	words = string.split(' ')

	obligations = []

	for i in range(len(words)):
		if words[i] in days:
			obligations.append({
				'type': words[i-1],
				'day': words[i],
				'start': words[i+1],
				'end': words[i+3].removesuffix(',')
			})
	
	for obligation in obligations:
		print(obligation)

	return obligations

analyze(string)
