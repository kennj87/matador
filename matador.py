import random

gader = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0,13:0,14:0,15:0,16:0,17:0,18:0,19:0,20:0,21:0,22:0,23:0,24:0,25:0,26:0,27:0,28:0,29:0,30:0,31:0,32:0,33:0,34:0,35:0,36:0,37:0,38:0,39:0,40:0}
def dice(n):
     rolls = []
     for i in range(n):
          two_dice = random.randint(1,6) + random.randint(1,6)
          rolls.append(two_dice)
     return rolls

moves = 100000000
m = 1

def kort_til_næste_rederi(m):
     if m >= 6:
          return 16
     if m >= 16:
          return 26
     if m >= 26:
          return 36
     if m >= 36:
          return 6
#her trækker vi kort

def træk_kort(m):
    træk = random.randint(1,40)
    if træk == 1 or træk == 2:
         return 11
    if træk == 3 or træk == 4:
         kort_til_næste_rederi(m)
    if træk == 5:
         return 40
    if træk == 6:
         return 38
    if træk == 7:
         return 1
    if træk == 8:
         return 25
    else:
         return(m)

for i in range(0,moves):
  roll = dice(1)[0]
  if m + roll >= 40:
       m = m - 40
  m = m + roll
  if m == 11:
       m = 11
  if m == 3 or m == 8 or m == 18 or m == 23 or m == 34 or m == 37:
       m = træk_kort(m)
  if m == 0:
       m = 40
  gader[m] = gader[m] + 1
print(gader)
s = [(k, gader[k]) for k in sorted(gader, key=gader.get, reverse=True)]
for k, v in s:
     print(k,v)
