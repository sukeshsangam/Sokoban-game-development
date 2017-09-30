import sys
import numpy as np
from collections import deque
import timeit
robot=[]
walls=[]
storage=[]
box=[]
directions={}
directions['N']=[0,-1]
directions['E']=[1,0]
directions['W']=[-1,0]
directions['S']=[0,1]

start_time=0
# reading the file
def print_char(filename):
	f = open(filename, 'r')
	i=0
	j=0
	while True:
		char=f.read(1)
		temp=[]
		if char: 
			temp.append(i)
			temp.append(j)
			if char == "O":
				walls.append(temp)
			if char == "R":
				robot.append(temp)
			if char == "S":
				storage.append(temp)
			if char == "B":
				box.append(temp)
			if char == ".":
				box.append(temp)
				storage.append(temp)
			if char == "$":
				robot.append(temp)
				storage.append(temp)
			if char == "\n":
				i=0
				j=j+1
			else:
				i=i+1
		else:
			break

if len(sys.argv)<2:
	print("please provide textfile name as system argument \n python bfs.py <filename>")
	exit(0)

print_char(sys.argv[1])
visited=[]
queue=deque()

if len(robot) == 0 or len(box) == 0 or len(storage) == 0 or len(walls) == 0:
	print("please provide the textfile in write format Walls :O \n storage : S \n box : B \n robot : R \n box on storage : . \n robot on storage : $  \n should include walls,storage,box,robot")
	exit(0)

# function for movement of a box
def move(point,dir,path,temp_box_list):
	box_list=[]
	box_list=temp_box_list[:]
	temp_append=[]
	cur_path=[]
	cur_path=path[:]
	cur_path.append(dir)
	if point not in walls:
		if point in box_list:
			ind=box_list.index(point)
			temp_box=[x + y for x, y in zip(point, directions[dir])]
			if temp_box not in box_list and temp_box not in walls:
				box_list[ind]=[x + y for x, y in zip(point, directions[dir])]
				temp_append.append(point)
				for i in box_list:
					temp_append.append(i)
				if temp_append not in visited:
					counter=0
					popped_robot=temp_append[0]
					for k in visited:
						k_temp_visited=k[:]
						
						k_robot=k_temp_visited.pop(0)
						temporary=[]
						if k_robot==popped_robot:
							count_list=0
							temporary=temp_append[1:]
							for m in k_temp_visited:
								if m in temporary:
									count_list=count_list+1
							if count_list==len(temporary):
								counter=counter+1
					if counter==0:
						temp_append.append(cur_path)
						queue.appendleft(temp_append)
				if set(map(tuple,box_list))==set(map(tuple,storage)):
					stop = timeit.default_timer()
					total_time=stop-start_time
					print("solution found")
					print(cur_path)
					print("total time taken: ")
					print(total_time)
					print("total steps take :")
					print(len(cur_path))
					exit()
		else:
			temp_append.append(point)
			for i in box_list:
				temp_append.append(i)
			if temp_append not in visited:
				counter=0
				popped_robot=temp_append[0]
				for k in visited:
					k_temp_visited=k[:]
					count_list=0
					k_robot=k_temp_visited.pop(0)
					temporary=[]
					if k_robot==popped_robot:
						temporary=temp_append[1:]
						for m in k_temp_visited:
							if m in temporary:
								count_list=count_list+1
						if count_list==len(temporary):
							counter=counter+1
				if counter==0:	
					temp_append.append(cur_path)
					queue.appendleft(temp_append)
			if set(map(tuple,box_list))==set(map(tuple,storage)):
				stop = timeit.default_timer()
				total_time=stop-start_time
				print("solution found")
				print(cur_path)
				print("total time taken")
				print(total_time)
				print("total steps take :")
				print(len(cur_path))
				exit()
#directions
dir_N='N'
dir_S='S'
dir_E='E'
dir_W='W'

#dfs function
def dfs():
	start_time = timeit.default_timer()
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
		move(S,dir_S,temp_path,temp_box_list)
		move(E,dir_E,temp_path,temp_box_list)
		move(W,dir_W,temp_path,temp_box_list)
		count=count+1
		if not queue:
			print("solution not found")
			exit()
dfs()


