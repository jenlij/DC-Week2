pets = [
  ('milla', 12),
  ('oakley', 7),
  ('snoop', 45)
]

def pet_age_sorter_decending(item1, item2):
  age1 = item1[1]
  age2 = item2[1]
  return age2 - age1

def pet_age_sorter_ascending(item1, item2):
  age1 = item1[1]
  age2 = item2[1]
  return age1 - age2


print sorted(pets, cmp=pet_age_sorter_decending)