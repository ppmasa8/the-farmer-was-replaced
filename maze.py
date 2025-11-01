clear()
maze_size = 16
N = 100  # N回宝箱を再配置する

# 初回のセットアップ
plant(Entities.Bush)
substance = maze_size * 2**(num_unlocked(Unlocks.Mazes) - 1)
use_item(Items.Weird_Substance, substance)

directions = [East, South, West, North]  # 時計回りの方角

chk_list = []  # ある場所を確認したかチェックするリスト
distance_list = []  # 宝箱までの距離をチェックするリスト
for _ in range(maze_size):
	tmp_list1 = []
	tmp_list2 = []
	for _ in range(maze_size):
		tmp_list1.append(False)
		tmp_list2.append(-1)
	chk_list.append(tmp_list1)
	distance_list.append(tmp_list2)


# 方角を壁の方向を示す数値に変換する関数(移動距離半分)
def direc2vec_half(x, y, direction):
	if direction==East:
		return x+0.5, y
	elif direction==South:
		return x, y-0.5
	elif direction==West:
		return x-0.5, y
	elif direction==North:
		return x, y+0.5
	
# 方角を壁の方向を示す数値に変換する関数
def direc2vec(x, y, direction):
	if direction==East:
		return x+1, y
	elif direction==South:
		return x, y-1
	elif direction==West:
		return x-1, y
	elif direction==North:
		return x, y+1

# 初回の迷路解析
can_move_simu = {}
index = 0
cnt = 0
while True:
	# もしまだ確認していない場所なら
	x, y = get_pos_x(), get_pos_y()
	if not(chk_list[x][y]):
		for direction in directions:
			can_move_simu[direc2vec_half(x, y, direction)] = can_move(direction)
		chk_list[x][y] = True
		cnt += 1
	#　すべての場所を調べたら終了
	if cnt == maze_size * maze_size:
		break
	# 右壁に沿って進む
	next_index = (index + 1) % 4
	if can_move(directions[next_index]):
		index = next_index
	elif not(can_move(directions[index])):
		index = (index - 1) % 4
	move(directions[index])

for n in range(N):
	# 初期化
	for x in range(maze_size):
		for y in range(maze_size):
			chk_list[x][y] = False
			distance_list[x][y] = maze_size*maze_size*maze_size
	# 宝箱の位置の距離を0にする
	x_treasure, y_treasure = measure()
	distance_list[x_treasure][y_treasure] = 0
	# 宝箱までの道のりを価値で示す
	if get_entity_type() != Entities.Treasure:
		x_now, y_now = get_pos_x(), get_pos_y()
		queue = [[x_treasure, y_treasure, None]]  # 次に調べる場所のqueue(x, y, どの方向に進んできたか)
		complete_flg = False  # 宝箱までの道のりが完成したフラグ
		while True:
			next_queue = []
			for x, y, came_from in queue:
				for k in range(4):
					# 移動してきた方向はスキップする
					if directions[(k+2)%4] == came_from:
						continue
					# もし移動可能で未更新の場所があれば
					direction = directions[k]
					next_x, next_y = direc2vec(x, y, direction)
					if can_move_simu[direc2vec_half(x, y, direction)]:
						if not(chk_list[next_x][next_y]):
							next_queue.append([next_x, next_y, direction])
							distance_list[next_x][next_y] = distance_list[x][y] + 1
							chk_list[next_x][next_y] = True
							# もし現在位置までの道のりが完成すれば
							if (x_now==next_x) and (y_now==next_y):
								complete_flg = True
			queue = next_queue
			if complete_flg:
				break
			
	# 迷路を解く			
	while True:
		x, y = get_pos_x(), get_pos_y()
		# 価値が1高い方に進んでいく
		for direction in directions:
			next_x, next_y = direc2vec(x, y, direction)
			# もし移動可能で価値が1高いなら
			if can_move_simu[direc2vec_half(x, y, direction)]:
				if (distance_list[next_x][next_y]+1==distance_list[x][y]):
					# 進める方向を更新しておく
					for direction_ in directions:
						can_move_simu[direc2vec_half(x, y, direction_)] = can_move(direction_)
					move(direction)
					break
		# 宝箱があれば
		if get_entity_type() == Entities.Treasure:
			x, y = get_pos_x(), get_pos_y()
			for direction in directions:
				can_move_simu[direc2vec_half(x, y, direction)] = can_move(direction)
			break
	# 再配置
	if n == N - 1:
		harvest()
	else:
		use_item(Items.Weird_Substance, substance)
		print(n, '/', N)
		
