import pickle

with open('sue.pkl', 'rb') as sue_file:
    sue = pickle.load(sue_file)

sue['pay'] *= 1.10

with open('sue.pkl', 'wb') as sue_file:
    pickle.dump(sue, sue_file)
