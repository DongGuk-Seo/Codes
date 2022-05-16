# 문제
# Canada Cosmos Control has received a report of another incident. They believe that an alien has illegally entered our space. A person who witnessed the appearance of the alien has come forward to describe the alien’s appearance. It is your role within the CCC to determine which alien has arrived. There are only 3 alien species that we are aware of, described below:

# TroyMartian, who has at least 3 antenna and at most 4 eyes;
# VladSaturnian, who has at most 6 antenna and at least 2 eyes;
# GraemeMercurian, who has at most 2 antenna and at most 3 eyes.
# 입력
# The first line contain the number of antenna that the witness claimed to have seen on the alien. The second line contain the number of eyes seen on the alien.

# 출력
# The output will be the list of aliens who match the possible description given by the witness. If no aliens match the description, there is no output.

a = int(input())
b = int(input())
if a >= 3 and b <= 4:
    print('TroyMartian')
if a <= 6 and b>= 2:
    print('VladSaturnian')
if a <= 2 and b<= 3:
    print('GraemeMercurian')