import pandas
NUM_STATES = 50

states_df = pandas.read_csv("50_states.csv")

states_list = states_df.state.tolist()
mydict = {
    'st-name': states_list,
    'taken': [0] * NUM_STATES
}

taken_df = pandas.DataFrame(mydict)

print(taken_df.loc(5))