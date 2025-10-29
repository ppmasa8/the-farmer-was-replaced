clear()
		
def swap_cactus_x():
	for col in range(get_world_size()):
		flg = False
		for row in range(get_world_size()):
			if row != get_world_size() - 1  and measure() > measure(East):
				swap(East)
				flg = True
			move(East)
		if not flg:
			break

def swap_cactus_y():
	for row in range(get_world_size()):
		flg = False
		for col in range(get_world_size()):
			if col != get_world_size() - 1 and measure() > measure(North):
				swap(North)
				flg = True
			move(North)
		if not flg:
			break
		

while True:
	for _ in range(get_world_size()):
		for _ in range(get_world_size()):
			if get_ground_type() != Grounds.Soil:
				till()
			if get_entity_type() != Entities.Cactus:
				plant(Entities.Cactus)
			use_item(Items.Water)
			move(North)
		move(East)
	
	for _ in range(get_world_size()):
		swap_cactus_x()
		move(North)
		
	for _ in range(get_world_size()):
		swap_cactus_y()
		move(East)
		
	harvest()
		
	
	
		
		
	
