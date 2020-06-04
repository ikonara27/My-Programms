
import random

Type = "Ragged","Polished","Mysterous","Seductive","Gregarious","Insane","Weeping","Imperious","Placid","Paranoid","Scarred","Amusing","Arcane","Enormus","Tiny","Colorful","Overjoy","Pious","Sinister"
#(random.choice(Type))

NPC = "Sailor","Acolyte","Soldier","Charlatan","Urchin","Criminal","Talking Beast","Entertainer","Apparition","Folk Hero","Authority","Artisan","Peasant","Hermit","Monster","Noble","Blacksmith","Outlander","Friend","Sage"
#(random.choice(NPC))

Verbs = "steal","Find","mend","Destroy","Outwit","Protect","Hide","Understand","Bury","Deafeat","Reach","Sabotage","Counterfelt","Collect","Expose","Reassemble","Enshrine","Pacify","Transport","Free"
#(random.choice(Verbs))

Sort = "Bloodthirsty","Disguised","Undying","Haunted","Enchanted","Clockwork","Uncanny","Lost","Holy","Wicked","Golden","Chosen","Secret","Prophesied","Otherworldly","Broken","Promised","Cursed","Stolen","Blasphemous"
#(random.choice(Sort))

Subject = "Heir","Blade","Monster","Relic","Texts","Tower","Monarch","Letter","Betrothed","Flowers","Beast of the Wild","Treasure","Tree","Bird","Mirror","Tomb","Stranger","Occultist","Child","Warrior"
#(random.choice(Subject))

Deadline = "Famine strikes the region","It wakes again","A terrible flood","The invasion begins","The last day of the trial","An innocent life is lost","The illness spreads","The day of the wedding","The chance for justice is lost","They all die","Twilight, 1d6 sunsets from now","Morning, 1d6 sunrises from now","The ritual is complete","Noon, 1d6 days from now","The coronation is complete","Life becomes an insufferable hellscape","The spell wears off","Everyone is transformed","The spell’s effects become permanent","The land falls into darkness"
#(random.choice(Deadline))

Reward = "A heartfelt thanks","1d4+1 barrels of ale","1d3+1 bottles of fine wine","2d100 pieces of silver","A First-Born Child","A Life-Debt","A Divine Blessing","1d100 Gold","1 Magic Scroll","Information you need","1d3 Magic Items of Some Interest","1 Magic Weapon","A Map of a Grand Treasure","1d3 Magic Scrolls","Rename the location after you","Double your money","1 Finely Cooked Meal for Everyone","1d4 Days Worth of Food","An exotic pet","6d100 Copper"
#(random.choice(Reward))

print("A(n)",(random.choice(Type)),(random.choice(NPC)),"approaches the party and asks that they",(random.choice(Verbs)),"the",(random.choice(Sort)),(random.choice(Subject)),"before",(random.choice(Deadline)),".", "In return they promise to grant",(random.choice(Reward)),"as payment.")
