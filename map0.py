room = {
    "tavern":   Room("The Laughing Hanged Man",
                    "Great place to find new adventures"),
    'upstairs': Room("The Laughing Hanged Man Upstairs",
                    "Rest ye weary travelor")
}

room['tavern'].n_to = room['upstairs']
room['upstairs'].s_to = room['tavern']