import pickle

# saves player file, nothing returned
def player_save(player, path_start = 'files/bin/'):
    path = path_start + player.name
    with open(path, 'wb') as file:
        pickle.dump(player, file)