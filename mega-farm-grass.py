clear()

def harvest_column():
	for _ in range(get_world_size()):
		harvest()
		move(North)

while True:
	if spawn_drone(harvest_column):
		move(East)
