clear()
		
pum_cnt = 0

while True:
	for _ in range(get_world_size()):
		for _ in range(get_world_size()):
			if get_ground_type() != Grounds.Soil:
				till()
			if get_entity_type() == Entities.Dead_Pumpkin:
				pum_cnt = 0
				harvest()
				plant(Entities.Pumpkin)
				use_item(Items.Water)
			elif get_entity_type() == Entities.Pumpkin:
				pum_cnt += 1
				if pum_cnt == 484:
					pum_cnt = 0
					harvest()
			else:
				plant(Entities.Pumpkin)
				use_item(Items.Water)
					
			move(North)
		move(East)
				
