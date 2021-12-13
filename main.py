"""1. Feladat
Készíts egy programot, amely a felhasználótól bekér egy egész számot, majd megvizsgálja, hogy a megadott szám
- pozitív páros vagy
- negatív páratlan.
Az eredményről tájékoztatja a felhasználót.
"""
x = int(input(" kérek egy egész számot:"))
if x > 0:
  print("Ez egy pozitív szám")
elif x < 0:
  print("Ez egy negatív szám")
