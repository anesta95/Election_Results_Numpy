import numpy as np
import matplotlib.pyplot as plt
import os
os.chdir('C:/Users/Adrian/Documents/Data Journalism/Datacamp Lesson'
         'Datafiles/')

survey_responses_open = open('electionresults.txt')
survey_responses = survey_responses_open.read()
total_ceballos = 33.0
print(total_ceballos)
survey_length = float(len(survey_responses))
percentage_ceballos = total_ceballos / survey_length
print(percentage_ceballos)

possible_surveys = np.random.binomial(survey_length, .54, size=10000)\
    / survey_length

plt.hist(possible_surveys, range=(0, 1), bins=20)
plt.show()
possible_surveys_length = float(len(possible_surveys))

incorrect_predictions = len(possible_surveys[possible_surveys < .5])

ceballos_loss_surveys = incorrect_predictions / possible_surveys_length

print(ceballos_loss_surveys)

large_survey_length = float(7000)

large_survey = np.random.binomial(large_survey_length, .54, size=10000)\
    / large_survey_length
incorrect_predictions_two = len(large_survey[large_survey < 0.5])
ceballos_loss_new = incorrect_predictions_two / large_survey_length

print(ceballos_loss_new)
