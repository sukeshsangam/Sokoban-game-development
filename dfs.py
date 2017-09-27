import sys
import numpy as np
from collections import deque
robot=[]
walls=[]
storage=[]
box=[]
directions={}
directions['N']=[0,-1]
directions['E']=[1,0]
directions['W']=[-1,0]
directions['S']=[0,1]
def print_char(filename):
	f = open(filename, 'r')
	i=0
	j=0
	x_array=[]
	y_array=[]
	while True:
		char=f.read(1)
		temp=[]
		if char: 
			temp.append(i)
			temp.append(j)
			if char == "O":
				walls.append(temp)
				x_array.append(i)
				y_array.append(j)
			if char == "R":
				robot.append(temp)
				x_array.append(i)
				y_array.append(j)
			if char == "S":
				storage.append(temp)
				x_array.append(i)
				y_array.append(j)
			if char == "B":
				box.append(temp)
				x_array.append(i)
				y_array.append(j)
			if char == "\n":
				i=0
				j=j+1
			else:
				i=i+1
		else:
			break	
	#print(box)
	#print(robot)
	#print(walls)
	#print(storage)
	#exit()
	i=max(x_array)
	j=max(y_array)
	board=np.chararray([i+1,j+1])
	board[:]=' '
	return board
print_char(sys.argv[1])
visited=[]
queue=deque()

def move(point,dir,path,temp_box_list):
	#print("path inside starting method")
	#print(path)
	#print(queue)
	#print(temp_box_list)
	box_list=[]
	box_list=temp_box_list[:]
	#exit()
	temp_append=[]
	cur_path=[]
	cur_path=path[:]
	cur_path.append(dir)
	#print(point)
	#print(walls)
	#print(visited)
	#exit()
	if point not in walls:
		#print("hello i am here")
		#exit()
		if point in box_list:
			ind=box_list.index(point)
			temp_box=[x + y for x, y in zip(point, directions[dir])]
			if temp_box not in box_list and temp_box not in walls:
				box_list[ind]=[x + y for x, y in zip(point, directions[dir])]
				temp_append.append(point)
				for i in box_list:
					temp_append.append(i)
				#print(temp_append)
				if temp_append not in visited:
					counter=0
					popped_robot=temp_append[0]
					for k in visited:
						k_temp_visited=k[:]
						
						k_robot=k_temp_visited.pop(0)
						temporary=[]
						#print(k_temp_visited)
						#print()
						if k_robot==popped_robot:
							#print("hello")
							count_list=0
							temporary=temp_append[1:]
							#print(temporary)
							for m in k_temp_visited:
								if m in temporary:
									count_list=count_list+1
							if count_list==len(temporary):
								counter=counter+1
					if counter==0:
					#print("hello")
						temp_append.append(cur_path)
							#print(temp_append)
						queue.appendleft(temp_append)
					#break
				if set(map(tuple,box_list))==set(map(tuple,storage)):
					print("solution found")
					print(cur_path)
					exit()
		else:
			temp_append.append(point)
			for i in box_list:
				temp_append.append(i)
			if temp_append not in visited:
				counter=0
				popped_robot=temp_append[0]
				#print(popped_robot)
				for k in visited:
					k_temp_visited=k[:]
					#print(k_temp_visited)
					count_list=0
					k_robot=k_temp_visited.pop(0)
					#print(k_robot)
					temporary=[]
					if k_robot==popped_robot:
						#print("hello")
						temporary=temp_append[1:]
						for m in k_temp_visited:
							if m in temporary:
								count_list=count_list+1
						if count_list==len(temporary):
							counter=counter+1
				if counter==0:	
						#print("hello")
					temp_append.append(cur_path)
					queue.appendleft(temp_append)
						#print(queue)
			if set(map(tuple,box_list))==set(map(tuple,storage)):
				print("solution found")
				print(cur_path)
				exit()
		#exit()
	#print("queue inside ending method")
	#print(path)
	#print(queue)
	#print(cur_path)
dir_N='N'
dir_S='S'
dir_E='E'
dir_W='W'
def bfs():
	temp_queue=[]
	initial=robot[0]
	temp_queue.append(initial)
	for i in box:
		temp_queue.append(i)
	path=[]
	temp_queue.append(path)
	queue.append(temp_queue)
	count=0
	while queue:
		temp_box_list=[]
		visited_adding=[]
		robot_position_list=queue.popleft()
		robot_position=robot_position_list[0]
		visited_adding=robot_position_list[:-1]
		if visited_adding not in visited:
			visited.append(visited_adding)
		temp_path=robot_position_list[-1][:]
		temp_box_list=robot_position_list[1:-1]
		N=[x + y for x, y in zip(robot_position, directions['N'])]
		S=[x + y for x, y in zip(robot_position, directions['S'])]
		E=[x + y for x, y in zip(robot_position, directions['E'])]
		W=[x + y for x, y in zip(robot_position, directions['W'])]
		move(N,dir_N,temp_path,temp_box_list)
		#print("hello S")
		move(S,dir_S,temp_path,temp_box_list)
		#print("hello E")
		move(E,dir_E,temp_path,temp_box_list)
		#print("hello W")
		move(W,dir_W,temp_path,temp_box_list)
		count=count+1
		
		#print(count)
		#print(visited)
		
		#print(queue)
		#exit()
		
		#if count == 4:
		#	exit()
		
		if not queue:
			print("solution not found")
			exit()
bfs()


