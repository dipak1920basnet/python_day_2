# stores information on state
steps_today = 1000
calories_burned = 100
workout_minutes = 200

# Transition phase: 
# update  the state
activity_score = steps_today/1000 + workout_minutes*2
print(activity_score)


if activity_score > 1000:
    print("Excellent score")
elif activity_score > 500:
    print("Moderate Activity")
else:
    print("Low activity")

