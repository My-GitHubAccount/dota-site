from django.db import models
from django.utils import timezone
# Create your models here.
class Game(models.Model) :
	date_played = models.DateField()
	game = models.TextField()

	radient = models.TextField()
	dire = models.TextField()
	first_pick = models.TextField()
	team_victory = models.TextField()
	
	SHADOW_FIEND = "SF"
	LESHRAC = "LESH"
	PHANTOM_ASSASIN = "PA"
	ALCHEMIST = "ALCH"
	ABBADON = "ABBADON"
	ANCIENT_APPARITION = "AA"
	ANTI_MAGE = "AM"
	AXE = "AXE"
	BANE = "BANE"
	
	heros = (
		(ABBADON, "Abbadon"),
		(ANCIENT_APPARITION, "Ancient Apparition"),
		(ANTI_MAGE, "Anti-Mage"),
		(AXE, "Axe"),
		(BANE, "Bane"),
		(LESHRAC, "Leshrac"),
		(PHANTOM_ASSASIN, "Phantom Assasin"),
		(SHADOW_FIEND, "Shadow Fiend"),
	)
	
	""""heros = (
		'Batrider',
		'Beastmaster',
		'Bloodseeker',
		'Bounty Hunter',
		'Brewmaster',
		'Bristleback',
		'Broodmother',
		'Centaur Warrunner',
		'Chaos Knight',
		'Chen',
		'Clinkz',
		'Clockwerk',
		'Crystal Maiden',
		'Dark Seer',
		'Dazzle',
		'Death Prophet',
		'Disruptor',
		'Doom',
		'Dragon Knight',
		'Drow Ranger',
		'Earth Spirit',
		'Earthshaker',
		'Elder Titan',
		'Ember Spirit',
		'Enchantress',
		'Enigma',
		'Faceless Void',
		'Gyrocopter',
		'Huskar',
		'Invoker',
		'Io',
		'Jakiro',
		'Juggernaut',
		'Keeper of the Light',
		'Kunkka',
		'Legion Commander',
		'Leshrac',
		'Lich',
		'Lifestealer'
		'Lina',
		'Lion',
		'Lone Druid',
		'Luna',
		'Lycanthrope',
		'Magnus',
		'Medusa',
		'Meepo',
		'Mirana',
		'Morphling',
		'Naga Siren',
		'Nature\'s Prophet',
		'Necrolyte',
		'Night Stalker',
		'Nyx Assassin',
		'Ogre Magi',
		'Omniknight',
		'Outworld Devourer',
		'Phantom Assassin',
		'Phantom Lancer',
		'Phoenix',
		'Puck',
		'Pudge',
		'Pugna',	
		'Queen of Pain',
		'Razor',
		'Riki',
		'Rubick',
		'Sand King',
		'Shadow Demon',
		'Shadow Fiend',
		'Shadow Shaman',
		'Silencer',
		'Skywrath Mage',
		'Slardar',
		'Slark',
		'Sniper',
		'Spectre',
		'Spirit Breaker',
		'Storm Spirit',
		'Sven',
		'Templar Assassin',
		'Terrorblade',
		'Tidehunter',
		'Timbersaw',
		'Tinker',
		'Tiny',
		'Treant Protector',
		'Troll Warlord',
		'Tusk',
		'Undying',
		'Ursa',
		'Vengeful Spirit',
		'Venomancer',
		'Viper',
		'Visage',
		'Warlock',
		'Weaver',
		'Windranger',
		'Witch Doctor',
		'Wraith King',
		'Zeus')"""
	
	dire_hero_1 = models.TextField(choices=heros)
	dire_hero_2 = models.TextField(choices=heros)
	dire_hero_3 = models.TextField(choices=heros)
	dire_hero_4 = models.TextField(choices=heros)
	dire_hero_5 = models.TextField(choices=heros)
	
	radient_hero_1 = models.TextField(choices=heros)
	radient_hero_2 = models.TextField(choices=heros)
	radient_hero_3 = models.TextField(choices=heros)
	radient_hero_4 = models.TextField(choices=heros)
	radient_hero_5 = models.TextField(choices=heros)
	
	def __str__(str) :
		string = str(self.date_played) + " : " + str(self.radient) + " vs " + str(self.dire)