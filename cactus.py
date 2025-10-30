clear()

s = get_world_size()
		
def swap_cactus_x():
	for col in range(s):
		f = False
		for row in range(s):
			if row != s - 1  and measure() > measure(East):
				swap(East)
				f = True
			move(East)
		if not f:
			break

def swap_cactus_y():
	for row in range(s):
		f = False
		for col in range(s):
			if col != s - 1 and measure() > measure(North):
				swap(North)
				f = True
			move(North)
		if not f:
			break
		

while True:
	for _ in range(s):
		for _ in range(s):
			if get_ground_type() != Grounds.Soil:
				till()
			if get_entity_type() != Entities.Cactus:
				plant(Entities.Cactus)
			use_item(Items.Water)
			move(North)
		move(East)
	
	for _ in range(s):
		swap_cactus_x()
		move(North)
		
	for _ in range(s):
		swap_cactus_y()
		move(East)
		
	harvest()
		
	
	
		
		
	
