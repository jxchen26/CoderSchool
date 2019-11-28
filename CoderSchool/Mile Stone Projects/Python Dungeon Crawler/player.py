from random import randint

hp = randint(1,100)

ME = {
  "name":input("Whats your name"),
  "lvl":1,
  "max_hp":hp,
  "atk":randint(1, 100),
  "def":randint(1, 100),
  "magic":randint(1, 100),
  "hp":hp,
  "bag":[],
  "equip":[],
  "money":100000,
  "exp":0,
  "exp_goal":100,
  "spells":["heal","fireball"],
}
