buyer1 = Buyer.objects.create(name='Troll1568', balance=100.00, age=25)
buyer2 = Buyer.objects.create(name='RickUbivator', balance=50.00, age=17)
buyer3 = Buyer.objects.create(name='Zip_kyn', balance=150.00, age=30)

game1 = Game.objects.create(title='Elden Ring', cost=60.00, size=45.5, description='Action RPG', age_limited=True)
game2 = Game.objects.create(title='Minecraft', cost=20.00, size=1.5, description='Sandbox game', age_limited=False)
game3 = Game.objects.create(title='Cyberpunk 2077', cost=70.00, size=70.0, description='Sci-fi RPG', age_limited=True)

game1.buyer.set([buyer1])
game2.buyer.set([buyer1, buyer2])
game3.buyer.set([buyer1, buyer3])
