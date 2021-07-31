
def addname(name: str, team=[]):
    if not team:
        team = []
    team.append(name)
    return team

a = 'aaa'

res1 = addname(a)
res2 = addname('bbb', res1)
res3 = addname('ccc', res2)
