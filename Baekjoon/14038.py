# 문제
# Each player in a tournament plays six games. There are no ties. The tournament director places the players in groups based on the results of games as follows:

# if a player wins 5 or 6 games, they are placed in Group 1;
# if a player wins 3 or 4 games, they are placed in Group 2;
# if a player wins 1 or 2 games, they are placed in Group 3;
# if a player does not win any games, they are eliminated from the tournament.
# Write a program to determine which group a player is placed in

# 입력
# The input consists of six lines, each with one of two possible letters: W (to indicate a win) or L (to indicate a loss).

# 출력
# The output will be either 1, 2, 3 (to indicate which Group the player should be placed in) or -1 (to indicate the player has been eliminated).

l = [input() for _ in range(6)]
if l.count('W') == 0:
    print(-1)
else:
    print(4-(l.count('W')+1)//2)