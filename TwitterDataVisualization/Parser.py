file_handler = open("ClemVSWake.json")

clemson_qb = ["Deshaun Watson", "Deshaun", "deshaun"]
#fsu_coach = ["Jimbo Fisher", "jimbo", "Jimbo"]
clemson_coach = ['Dabo','Dabo Swinney']
#fsu_qb = ['Deondre Francois', 'Deondre', 'deondre']
Wake_qb = ['Hinton', 'hinton', 'Kendall Hinton']

lines_count = 0
clemson_qb_count = 0
#fsu_qb_count = 0
clemson_coach_count = 0
#fsu_coach_count = 0
Wake_qb_count = 0
for line in file_handler:
	lines_count = lines_count + 1
	if any(x in line for x in clemson_qb):
		clemson_qb_count = clemson_qb_count+1
	'''if any(x in line for x in fsu_qb):
		fsu_qb_count = fsu_qb_count + 1'''
	if any(x in line for x in clemson_coach):
		clemson_coach_count = clemson_coach_count + 1
	'''if any(x in line for x in fsu_coach):
		fsu_coach_count = fsu_coach_count + 1'''
	if any(x in line for x in Wake_qb):
		Wake_qb_count = Wake_qb_count + 1


print ("Total number of lines: ", lines_count)
print ("Deshaun Watson mentions: ", clemson_qb_count)
#print ("Jimbo Fisher mentions: ", fsu_coach_count)
print ("Dabo Swinney mentions: ", clemson_coach_count)
#print ("Deondre Francois mentions: ", fsu_qb_count)
print ("Kendall Hinton mentions: ", Wake_qb_count)