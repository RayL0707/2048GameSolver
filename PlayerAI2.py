from random import randint
from BaseAI import BaseAI
import time,math
class PlayerAI(BaseAI):
    def getMove(self, grid):
        # moves = grid.getAvailableMoves()
        # return moves[randint(0, len(moves) - 1)] if moves else None
        start_time = time.clock()
        depth = 0
        dd = self.solver(grid,True,-float('inf'),float('inf'), start_time, depth)
        # while time.clock() - start_time < 0.13:
        # 	dd = self.solver(grid,True,-float('inf'),float('inf'), start_time, depth)
        # 	if dd == None:
        # 		break
        # 	depth += 1
        return dd[0][2]

	

	def getvct(self,k):
		if k == 1:
			return (0,1)
		elif k == 2:
			return (1,0)
		pass

    

    def valfun(self, grid):
    	Ecells = grid.getAvailableCells()
    	Ecellslength = math.log(len(Ecells)) if len(Ecells)!=0 else -float('inf')#how to handle
    	sms = self.getsmooth(grid)
    	mono = self.monoto(grid)
    	cluster = self.cluster(grid)
    	
    	#-----set weight ------
    	smoothWeight = 1.2
    	emptyWeight = 5.0
    	maxWeight = 1.0
    	monoWeight = 1.2
    	clusterWeight = 0.6
    	#----------------------

    	vals = Ecellslength * emptyWeight\
    		 + grid.getMaxTile() * maxWeight\
    		 + sms * smoothWeight\
    		 + mono * monoWeight\
    		 + cluster * clusterWeight

    	return vals
    	pass
    def getsmooth(self,grid):
    	smoothness = 0;
    	for i in range(grid.size):
    		for j in range(grid.size):
    			#if grid.getCellValue([i,j])!= None and grid.getCellValue([i,j])!= 0:
    			if grid.getCellValue([i,j])!= 0:
    				vl = math.log(float(grid.getCellValue([i,j]))) / math.log(2)
    				for k in range(1,3):
						#vct = self.getvct(k)
						if k == 1:
							vct = (0,-1)
						elif k == 2:
							vct = (-1,0)
						# elif k == 3:
						# 	vct = (0,1)

						_, target = self.farthest(grid,[i,j],vct)
						if grid.getCellValue(target)!= None and grid.getCellValue(target)!= 0:
							#print type(grid.getCellValue(target))
							diff = math.log(float(grid.getCellValue(target))) / math.log(2)
							smoothness -= abs(vl - diff)
    	return smoothness
    	pass

    def monoto(self,grid):
    	gridcopy = grid.clone()
    	# visited =[]
    	# queue = []
    	# Mvalue = increase = 0
    	# Mcell = [0,0]
    	totals =[0 for i in range(4)]

    	x = y = 0
    	# ----------up/down----------
    	while x < 4:
    		cur = 0
    		nex = cur + 1

	    	while nex < 4:
	    		#print nex,'x'
	    		while nex < 4 and gridcopy.getCellValue((x,nex)) ==0:
	    			nex += 1
	    		if nex >= 4:
	    			nex -=1
	    		cvalue = math.log(gridcopy.getCellValue((x,cur))) / math.log(2) if gridcopy.getCellValue((x,cur)) != 0 else 0
	    		nvalue = math.log(gridcopy.getCellValue((x,nex))) / math.log(2) if gridcopy.getCellValue((x,nex)) != 0 else 0

	    		if cvalue > nvalue:
	    			totals[0] += nvalue -cvalue
	    		elif nvalue > cvalue:
	    			totals[1] += cvalue - nvalue
	    		cur = nex
	    		nex += 1
	    	x += 1
		#print "xx",y
	    #------------left/rignt---------
		while y < 4:
			#print 'y',y
			cur = 0
			nex = cur + 1
			#print 'nex',nex < 4
			while nex < 4:

				#print "hi"
				while nex < 4 and gridcopy.getCellValue((nex, y)) ==0:
					nex += 1
				if nex >= 4:
					nex -=1
				cvalue = math.log(gridcopy.getCellValue((cur, y))) / math.log(2) if gridcopy.getCellValue((cur, y)) != 0 else 0
				nvalue = math.log(gridcopy.getCellValue((nex, y))) / math.log(2) if gridcopy.getCellValue((nex, y)) != 0 else 0

				if cvalue > nvalue:
					totals[2] += nvalue -cvalue
				elif nvalue > cvalue:
					totals[3] += cvalue - nvalue
				cur = nex
				nex += 1
			y += 1
		#print "yy"
		return max(totals[0],totals[1]) + max(totals[2], totals[3])

		pass
	  
    def farthest(self,grid,cell,dirc):
		gridcopy = grid.clone()
		prv = cell
		cell = (cell[0] + dirc[0],cell[1] + dirc[1])
		while not gridcopy.crossBound(cell) and gridcopy.getCellValue(cell)!=0:
			prv = cell
			cell = (cell[0] + dirc[0],cell[1] + dirc[1])
		return [prv, cell]

		pass
    def cluster(self, grid):
		clusterscore = 0
		for i in range(grid.size):
			for j in range(grid.size):
				if grid.map[i][j]==0:
				 	continue
				nN = 0
				sumn = 0
				neighbors = [-1,0,1]
				for k in neighbors:
					x = i+k
					if x<0 or x>=grid.size:
						continue
					for l in neighbors:
						y = j+l
						if y<0 or y>= grid.size:
							continue
						if grid.map[x][y]>0:
							nN = nN+1
							sumn = sumn+abs(math.log(grid.map[x][y],2)-math.log(grid.map[i][j],2))
				clusterscore = clusterscore+sumn/nN
		return clusterscore

    def solver(self,grid,turn,alpha,beta,start_time,depth):
		valgrid = self.valfun(grid)
		moves = grid.getAvailableMoves()
		if (time.clock() - start_time) > 0.18 or not moves or depth > 20:
			return [None, valgrid]

		if turn == True:
			Maxs = [None, alpha]
			Best_Moves = []
			for step in moves:
				subgrid = grid.clone()
				subgrid.move(step)
				Best_Moves.append([self.valfun(subgrid), subgrid,step])

			Best_Moves =sorted(Best_Moves, key = lambda x : x[0],reverse=True)

			for decision in Best_Moves:
				move,vals = self.solver(decision[1], False, alpha, beta, start_time, depth +1)
				if vals > Maxs[1]:
					Maxs = [decision, vals]
				if Maxs[1] >= beta:
					break
				if Maxs[1] > alpha:
					alpha = Maxs[1]
			return Maxs
		elif turn == False:
			Mins = [None, beta]
			Worst_Moves = []
			# ----------beta 0.2------------
			cells = grid.getAvailableCells()
			scores = [2,4]
			mgrid = grid.clone()
			for score in scores:
				for epty in cells:
					subgrid = mgrid.clone()
					subgrid.setCellValue(epty, score)
					#mgrid.setCellValue(epty, score)
					tmpval = self.valfun(subgrid)
					#mgrid.setCellValue(epty, 0)
					if not Worst_Moves or len(Worst_Moves) < 2:
						Worst_Moves.append([tmpval, subgrid])
					elif tmpval < Worst_Moves[0][0]:
						Worst_Moves =[[tmpval, subgrid]]


			#Worst_Moves =sorted(Worst_Moves, key = lambda x : x[0])
			# if not Worst_Moves:
			# 	for step in moves:
			# 		subgrid = mgrid.clone()
			# 		subgrid.move(step)
			# 		Worst_Moves.append([self.valfun(subgrid), subgrid])

			# 	Worst_Moves =sorted(Worst_Moves, key = lambda x : x[0])

			# 	for decision in Worst_Moves:
			# 		move,vals = self.solver(decision[1], True, alpha, beta, start_time, depth+1)
			# 		if vals > Mins[1]:
			# 			Maxs = [decision, vals]
			# 		if Mins[1] <= alpha:
			# 			break
			# 		if Mins[1] < beta:
			# 			beta = Mins[1]
			# 	return Mins
			#------possible prun--------
			if not Worst_Moves:
				return Mins
			# move,vals = self.solver(Worst_Moves[0][1], True, alpha, beta, start_time, depth+1)
			# if vals > Mins[1]:
			# 	Maxs = [decision, vals]
			# if Mins[1] <= alpha:
			# 	return Mins
			# if Mins[1] < beta:
			# 	beta = Mins[1]
			# return Mins
			#print len(Worst_Moves)
			for decision in Worst_Moves:
				#newbata = self.valfun(decision[1])
				movee,vals = self.solver(decision[1], True, alpha, beta, start_time, depth + 1)
				if vals > Mins[1]:
					Mins = [decision, vals]
				if Mins[1] <= alpha:
					return Mins
				if Mins[1] < beta:
					beta = Mins[1]
				return Mins


			# for step in moves:
			# 	subgrid = grid.clone()
			# 	subgrid.move(step)
			# 	Worst_Moves.append([self.valfun(subgrid), subgrid])

			# Worst_Moves =sorted(Worst_Moves, key = lambda x : x[0])

			# possible prun
			# move,vals = self.solver(Worst_Moves[0][1], False, alpha, beta, start_time, depth+1)
			# if vals > Mins[1]:
			# 	Maxs = [decision, vals]
			# if Mins[1] <= alpha:
			# 	return Mins
			# if Mins[1] < beta:
			# 	beta = Mins[1]

			#--------beta 0.1---------
			# for step in moves:
			# 	subgrid = mgrid.clone()
			# 	subgrid.move(step)
			# 	Worst_Moves.append([self.valfun(subgrid), subgrid])

			# Worst_Moves =sorted(Worst_Moves, key = lambda x : x[0])

			# for decision in Worst_Moves:
			# 	move,vals = self.solver(decision[1], False, alpha, beta, start_time, depth+1)
			# 	if vals > Mins[1]:
			# 		Maxs = [decision, vals]
			# 	if Mins[1] <= alpha:
			# 		break
			# 	if Mins[1] < beta:
			# 		beta = Mins[1]
			# return Mins