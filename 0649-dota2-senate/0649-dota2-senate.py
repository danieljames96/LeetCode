class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        
        bans = list(senate)

        counter = 0

        while bans:
            sen = bans.pop(0)
            # print(f'Senate:{sen}')
            if sen == 'D':
                indx = -1 if 'R' not in bans else bans.index('R')
            else:
                indx = -1 if 'D' not in bans else bans.index('D')

            if indx == -1:
                # print(f'Victory')
                return 'Dire' if sen == 'D' else 'Radiant'

            bans.append(sen)
            banned = bans.pop(indx)
            # print(f'Banned: {banned}')