import json


def add_player(players):
    new_player = input("Enter new player name:  ").strip()
    if new_player == "":
        print("Not legal name")
    elif new_player not in players:
        players[new_player] = {"wins": 0, "losses": 0}
    else:
        print("Player already added")


def show_players(players):
    if players:
        for k, v in players.items():
            print(f"player {k} have {v['wins']} wins and {v['losses']} losses")
    else:
        print("No Players yet")


def record_match(players):
    wins_player = input("Enter wins player name:  ").strip()
    losser_player = input("Enter losser player name:  ").strip()
    if validate_plaers(wins_player, losser_player, players):
        players[wins_player]["wins"] += 1
        players[losser_player]["losses"] += 1
        print("match record")


def validate_plaers(winner: str, losser: str, players: dict) -> bool:
    if winner == "" or losser == "":
        print("Plaer name is enpty")
        return False
    elif winner == losser:
        print("Plaers have same name")
        return False
    elif winner not in players or losser not in players:
        print("plaers is not registred")
        return False
    return True


def main():
    players = {}
    while True:
        print("""1. Add player
2. Show players
3. Record match 
4. Exit""")
        choice = input("Enter what u need  ")
        if choice == "1":
            add_player(players)
        elif choice == "2":
            show_players(players)
        elif choice == "3":
            record_match(players)
        elif choice == "4":
            break
        else:
            print("Invalid option")


main()
