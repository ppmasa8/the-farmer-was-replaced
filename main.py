clear()

pum_cnt = 0

while True:
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			# pumpkin
			if i < 6 and j < 6:
				if get_ground_type() != Grounds.Soil:
					till()
				if get_entity_type() == Entities.Dead_Pumpkin:
					pum_cnt = 0
					harvest()
					plant(Entities.Pumpkin)
					if get_water() < 0.5:
						use_item(Items.Water)
				elif get_entity_type() == Entities.Pumpkin:
					pum_cnt += 1
					if pum_cnt == 36:
						harvest()
				else:
					plant(Entities.Pumpkin)
					if get_water() < 0.5:
						use_item(Items.Water)
				
			# grass
			elif i % 4 == 0:
				harvest()
				
			# bush and tree
			elif i % 4 == 1:
				if get_entity_type() != Entities.Tree:
					plant(Entities.Tree)
					if get_water() < 0.5:
						use_item(Items.Water)
				else:
					if can_harvest():
						harvest()
						plant(Entities.Tree)
						if get_water() < 0.5:
							use_item(Items.Water)
					
			# sunflower
			elif i % 4 == 2:
				if get_ground_type() != Grounds.Soil:
					till()
				if can_harvest():
					harvest()
				if get_entity_type() != Entities.Sunflower:
					plant(Entities.Sunflower)
					if get_water() < 0.5:
						use_item(Items.Water)
				
			# carrot
			elif i % 4 == 3:
				if get_ground_type() != Grounds.Soil:
					till()
				if can_harvest():
					harvest()
				if get_entity_type() != Entities.Carrot:
					plant(Entities.Carrot)
					if get_water() < 0.5:
						use_item(Items.Water)
			
			move(North)
		move(East)
			
