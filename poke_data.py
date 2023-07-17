# MOVES
TACKLE = 40
SCRATCH = 40
LEECH_SEED = 15
VINE_WHIP = 45
RAZOR_LEAF = 55
SEED_BOMB = 80
TAKE_DOWN = 90
DOUBLE_EDGE = 120
SOLAR_BEAM = 120
EMBER = 40
SMOKESCREEN = 15
DRAGON_BREATH = 60
FIRE_FANG = 65
SLASH = 70
FLAMETHROWER = 90
INFERNO = 100
FLARE_BLITZ = 130
WATER_GUN = 40
RAPID_SPIN = 50
BITE = 60
WATER_PULSE = 60
AQUA_TAIL = 90
HYDRO_PUMP = 110
SKULL_BASH = 130
BUG_BITE = 60
CONFUSION = 50
PSYBEAM = 65
AIR_SLASH = 75
POISON_STING = 15
ASSURANCE = 60
POISON_JAB = 80
GUST = 40
QUICK_ATTACK = 40
TWISTER = 40
WING_ATTACK = 60
AERIAL_ACE = 60
HURRICANE = 110
CRUNCH = 80
SUCKER_PUNCH = 70
PECK = 35
FURY_ATTACK = 15
DRILL_PECK = 80
ACID = 40
THUNDER_FANG = 65
ACID_SPRAY = 40
SLUDGE_BOMB = 90
BELCH = 120
NUZZLE = 20
THUNDER_SHOCK = 40
ELECTRO_BALL = 40
DISCHARGE = 80
SPARK = 65
SWIFT = 60
IRON_TAIL = 100

# POKÉMON(S)
def Bulbasaur():
	hp = 200
	speed = 85
	moveset = [TACKLE, LEECH_SEED, VINE_WHIP, RAZOR_LEAF]
	type = ['grass', 'poison']
def Ivysaur():
	hp = 230
	speed = 112
	moveset = [VINE_WHIP, RAZOR_LEAF, SEED_BOMB, TAKE_DOWN]
	type = ['grass', 'poison']
def Venusaur():
	hp = 270
	speed = 148
	moveset = [SEED_BOMB, TAKE_DOWN, DOUBLE_EDGE, SOLAR_BEAM]
	type = ['grass', 'poison']

def Charmander():
	hp = 188
	speed = 121
	moveset = [SCRATCH, EMBER, SMOKESCREEN, DRAGON_BREATH]
	type = ['fire']
def Charmeleon():
	hp = 226
	speed = 148
	moveset = [EMBER, DRAGON_BREATH, FIRE_FANG, SLASH]
	type = ['fire']
def Charizard():
	hp = 266
	speed = 184
	moveset = [SLASH, FLAMETHROWER, INFERNO, FLARE_BLITZ]
	type = ['fire', 'flying']

def Squirtle():
	hp = 198
	speed = 81
	moveset = [TACKLE, WATER_GUN, RAPID_SPIN, BITE]
	type = ['water']
def Wartortle():
	hp = 228
	speed = 108
	moveset = [WATER_GUN, BITE, WATER_PULSE, AQUA_TAIL]
	type = ['water']
def Blastoise():
	hp = 268
	speed = 144
	moveset = [WATER_PULSE, AQUA_TAIL, HYDRO_PUMP, SKULL_BASH]
	type = ['water']

def Caterpie():
	hp = 200
	speed = 85
	moveset = [TACKLE, BUG_BITE]
	type = ['bug']
def Metapod():
	hp = 210
	speed = 58
	HARDEN = hp + 30
	moveset = [HARDEN]
	type = ['bug']
def Butterfree():
	hp = 230
	speed = 130
	moveset = [BUG_BITE, CONFUSION, PSYBEAM, AIR_SLASH]
	type = ['bug']	

def Weedle():
	hp = 190
	speed = 94
	moveset = [POISON_STING, BUG_BITE]
	type = ['bug', 'poison']
def Kakuna():
	hp = 210
	speed = 67
	HARDEN = hp + 30
	moveset = [HARDEN]
	type = ['bug', 'poison']
def Beedrill():
	hp = 240
	speed = 139
	moveset = [POISON_STING, FURY_CUTTER, ASSURANCE, POISON_JAB]
	type = ['bug', 'poison']	

def Pidgey():
	hp = 190
	speed = 105
	moveset = [TACKLE, GUST, QUICK_ATTACK]
	type = ['normal', 'flying']
def Pidgeotto():
	hp = 236
	speed = 132
	moveset = [TACKLE, GUST, QUICK_ATTACK, TWISTER]
	type = ['normal', 'flying']
def Pidgeot():
	hp = 276
	speed = 186
	moveset = [WING_ATTACK, AERIAL_ACE, AIR_SLASH, HURRICANE]
	type = ['normal', 'flying']

def Rattata():
	hp = 170
	speed = 134
	moveset = [TACKLE, QUICK_ATTACK, BITE]
	type = ['normal']
def Raticate():
	hp = 220
	speed = 179
	moveset = [TAKE_DOWN, ASSURANCE, CRUNCH, SUCKER_PUNCH]
	type = ['normal']

def Spearow():
	hp = 190
	speed = 130
	moveset = [PECK, ASSURANCE, FURY_ATTACK]
	type = ['normal', 'flying']
def Fearow():
	hp = 240
	speed = 184
	moveset = [AERIAL_ACE, WING_ATTACK, TAKE_DOWN, DRILL_PECK]
	type = ['normal', 'flying']

def Ekans():
	hp = 180
	speed = 103
	moveset = [WRAP, POISON_STING, BITE, ACID]
	type = ['poison']
def Arbok():
	hp = 230
	speed = 148
	moveset = [THUNDER_FANG, ACID_SPRAY, SLUDGE_BOMB, BELCH]
	type = ['poison']

def Pikachu():
	hp = 180
	speed = 166
	moveset = [NUZZLE, QUICK_ATTACK, THUNDER_SHOCK, ELECTRO_BALL]
	type = ['electric']
def Raichu():
	hp = 230
	speed = 202
	moveset = [DISCHARGE, SPARK, SWIFT, IRON_TAIL]
	type = ['electric']

# KANTO REGION (source: https://docs.google.com/document/d/1fH_n_BPbIk1bZCrK1hLAJrYPH2d5RTy9IgdR5Ck_lNw/edit#bookmark=id.anuwftomx89m)
pokelist = [Bulbasaur, Ivysaur, Venusaur, Charmander, Charmeleon, Charizard, Squirtle, Wartortle, Blastoise, Caterpie, Metapod, Butterfree, Weedle, Kakuna, Beedrill, Pidgey, Pidgeotto, Pidgeot, Rattata, Raticate, Spearow, Fearow, Ekans, Arbok, Pikachu, Raichu, Sandshrew, Sandslash, Nidoran, Nidorina, Nidoqueen, Nidorino, Nidoking, Clefairy, Clefable, Vulpix, Ninetales, Jigglypuff, Wigglytuff, Zubat, Golbat, Oddish, Gloom, Vileplume, Paras, Parasect, Venonat, Venomoth, Diglett, Dugtrio, Meowth, Persian, Psyduck, Golduck, Mankey, Primeape, Growlithe, Arcanine, Poliwag, Poliwhirl, Poliwrath, Abra, Kadabra, Alakazam, Machop, Machoke, Machamp, Bellsprout, Weepinbell, Victreebel, Tentacool, Tentacruel, Geodude, Graveler, Golem, Ponyta, Rapidash, Slowpoke, Slowbro, Magnemite, Magneton, Farfetchd, Doduo, Dodrio, Seel, Dewgong, Grimer, Muk, Shellder, Cloyster, Gastly, Haunter, Gengar, Onix, Drowzee, Hypno, Krabby, Kingler, Voltorb, Electrode, Exeggcute, Exeggutor, Cubone, Marowak, Hitmonlee, Hitmonchan, Lickitung, Koffing, Weezing, Rhyhorn, Rhydon, Chansey, Tangela, Kangaskhan, Horsea, Seadra, Goldeen, Seaking, Staryu, Starmie, Mr.Mime, Scyther, Jynx, Electabuzz, Magmar, Pinsir, Tauros, Magikarp, Gyarados, Lapras, Ditto, Eevee, Vaporeon, Jolteon, Flareon, Porygon, Omanyte, Omastar, Kabuto, Kabutops, Aerodactyl, Snorlax, Articuno, Zapdos, Moltres, Dratini, Dragonair, Dragonite, Mewtwo, Mew]
