# Siddhant Dhar - PSID: 1512852
# Zylabs 11.27: Soccer team roster (Dictionaries)

team_dict = {}

player_number = 1

for i in range(1, 6):
    jersey_number = int(input('Enter player {}\'s jersey number:\n'.format(i)))
    rating = int(input('Enter player {}\'s rating:\n'.format(i)))
    print()

    if jersey_number < 0 or jersey_number > 99 or rating < 0 or rating > 9:
        print('invalid entry')
        break
    else:
        team_dict[jersey_number] = rating

print("ROSTER")
for jersey_number, rating in sorted(team_dict.items()):
    print("Jersey number: %d, Rating: %d" % (jersey_number, rating))

option = ''

while option.upper() != 'Q':
    print('\nMENU\n'
          'a - Add player\n'
          'd - Remove player\n'
          'u - Update player rating\n'
          'r - Output players above a rating\n'
          'o - Output roster\n'
          'q - Quit\n')

    option = input('Choose an option:\n')

    if option == 'a':
        jersey_number = int(input('Enter a new player\'s jersey number:\n'.format(player_number)))
        rating = int(input('Enter the players\'s rating:\n'.format(player_number)))
        team_dict[jersey_number] = rating

    elif option == 'd':
        jersey_number = int(input('Enter a jersey number:\n'))
        if jersey_number in team_dict.keys():
            del team_dict[jersey_number]

    elif option == 'u':
        jersey_number = int(input('Enter a jersey number:\n'))
        if jersey_number in team_dict.keys():
            rating = int(input('Enter a new rating for player:\n'))
            team_dict[jersey_number] = rating

    elif option == 'r':
        rating_input = int(input('Enter a rating:\n'))
        print('ABOVE {}'.format(rating_input))
        for jersey_number, rating in sorted(team_dict.items()):
            if rating > rating_input:
                print("Jersey number: %d, Rating: %d" % (jersey_number, rating))

    elif option == 'o':
        print("ROSTER")
        for jersey_number, rating in sorted(team_dict.items()):
            print("Jersey number: %d, Rating: %d" % (jersey_number, rating))