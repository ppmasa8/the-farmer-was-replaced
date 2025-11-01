clear()

def harvest_column():
	for _ in range(get_world_size()):
		plant(Entities.Bush)
		if get_water() < 0.5:
			use_item(Items.Water)
		if can_harvest():
			harvest()
		move(North)

while True:
	if spawn_drone(harvest_column):
		move(East)
