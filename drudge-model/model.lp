\ Model Drudge Model
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  30 x1_-_Drudge + 20 x2_-_Donkey
Subject To
 Load: 100 x1_-_Drudge + 50 x2_-_Donkey = 1000
 Food: 3 x1_-_Drudge + 2 x2_-_Donkey <= 35
 Water: 100 x1_-_Drudge + 30 x2_-_Donkey <= 900
 Not_negativity_Drudge: x1_-_Drudge >= 0
 Not_negativity_Donkey: x2_-_Donkey >= 0
Bounds
Generals
 x1_-_Drudge x2_-_Donkey
End
