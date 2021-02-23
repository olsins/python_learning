

def play():
    inventory = ['Dagger', 'Gold(5)', 'Crusty Bread',
                 'Vanilla(10)', 'Chocolate(0)']
    print("Escape from Nillas Castle")
    while True:
        action_input = get_player_command()
        if action_input in ['n', 'N']:
            print("Go North")
        elif action_input in ['s', 'S']:
            print("Go South")
        elif action_input in ['e', 'E']:
            print("Go East")
        elif action_input in ['w', 'W']:
            print("Go West")
        elif action_input == 'i' or action_input == 'I':
            print("Inventory: ")
            for item in inventory:
                print('* ' + str(item))
        else:
            print("Invalid Action")


def get_player_command():
    return input('Action: ')


play()
