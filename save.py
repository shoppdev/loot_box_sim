import pickle

# this will work need to pass in the player object, not the name


path_start = 'files/bin/'

# saves player file, nothing returned
def player_save(player, path_start = 'files/bin'):
    path = path_start + player
    with open(path, 'wb') as file:
        pickle.dump(player, file)