import unittest

class TestHero(unittest.TestCase):
    def setUp(self):
        self.hero = Hero("Bob", 1, "Elf")
        self.superhero = SuperHero("SuperBob", 1, "Elf", 1)

    def test_init(self):
        self.assertEqual(self.hero.name, "Bob")
        self.assertEqual(self.hero.level, 1)
        self.assertEqual(self.hero.race, "Elf")
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.superhero.magiclevel, 1)
        self.assertEqual(self.superhero.magic, 100)

    def test_level_up(self):
        self.hero.level_up()
        self.assertEqual(self.hero.level, 2)

    def test_move(self):
        self.hero.move()
        self.assertEqual(self.hero.name, "Bob")

    def test_set_health(self):
        self.hero.set_health(90)
        self.assertEqual(self.hero.health, 90)

    def test_makemagic(self):
        self.superhero.makemagic()
        self.assertEqual(self.superhero.magic, 90)

    def test_eblootorvalo(self):
        self.superhero.eblootorvalo()
        self.assertEqual(self.superhero.health, 95)
