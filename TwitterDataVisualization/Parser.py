#Writes all the live streaming tweets into this JSON file
file_handler = open("ClemVSWake.json")

'''
Below are the Lists of different names a Player/Coach can we addressed in Twitter
'''
#Clemson QB
clemson_qb = ["Deshaun Watson", "Deshaun", "deshaun"]
#Clemson Head Coach
clemson_coach = ['Dabo','Dabo Swinney']
#FSU QB
fsu_qb = ['Deondre Francois', 'Deondre', 'deondre']
#FSU Head Coach
fsu_coach = ["Jimbo Fisher", "jimbo", "Jimbo"]

#Getting the count of Each Player/Coach
tweet_count = 0
clemson_qb_count = 0
fsu_qb_count = 0
clemson_coach_count = 0
fsu_coach_count = 0
for line in file_handler:
	tweet_count = tweet_count + 1
	if any(x in line for x in clemson_qb):
		clemson_qb_count = clemson_qb_count+1
	if any(x in line for x in fsu_qb):
		fsu_qb_count = fsu_qb_count + 1
	if any(x in line for x in clemson_coach):
		clemson_coach_count = clemson_coach_count + 1
	if any(x in line for x in fsu_coach):
		fsu_coach_count = fsu_coach_count + 1
	if any(x in line for x in Wake_qb):
		Wake_qb_count = Wake_qb_count + 1


print ("Total tweet count: ", tweet_count)
print ("Deshaun Watson mentions: ", clemson_qb_count)
print ("Jimbo Fisher mentions: ", fsu_coach_count)
print ("Dabo Swinney mentions: ", clemson_coach_count)
print ("Deondre Francois mentions: ", fsu_qb_count)
