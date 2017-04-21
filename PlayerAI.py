from random import randint
from BaseAI import BaseAI
import time,math
class PlayerAI(BaseAI):
    def getMove(self, grid):
        # moves = grid.getAvailableMoves()
        # return moves[randint(0, len(moves) - 1)] if moves else None
        start_time = time.clock()
        #-------DFS--------------
        #depth = 0
        dd = self.solver(grid,True,-float('inf'),float('inf'), start_time, 0, 3)
        #-------IDS--------------
        #dd = self.idsolver(grid,start_time)
        return dd[0][2]

	

	def getvct(self,k):
		if k == 1:
			return (0,1)
		elif k == 2:
			return (1,0)
		pass

    

    def valfun(self, grid):
    	Ecells = grid.getAvailableCells()
    	Ecellslength = math.log(len(Ecells)) if len(Ecells)!=0 else -9000#how to handle
    	sms = self.getsmooth(grid)
    	mono = self.monoto(grid)
    	cluster = self.cluster(grid)
    	#nislands = self.numIslands(grid)
    	
    	#-----set weight ------
    	smoothWeight = 1.2 #1.05
    	#islandWeight = 1.3
    	emptyWeight = 5.1
    	maxWeight = 1.0
    	monoWeight = 1.3 #1.25
    	clusterWeight = 0.6 # 0.3
    	#----------------------

    	vals = Ecellslength * emptyWeight\
    		 + math.log(grid.getMaxTile()) / math.log(2) * maxWeight\
             + mono * monoWeight\
    		 - cluster * clusterWeight\
    		 + sms * smoothWeight
    		 #- nislands * islandWeight

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
							vct = (0,1)
						elif k == 2:
							vct = (1,0)
						# elif k == 3:
						# 	vct = (0,1)

						_, target = self.farthest(grid,[i,j],vct)
						if grid.getCellValue(target)!= None and grid.getCellValue(target)!= 0:
							#print type(grid.getCellValue(target))
							diff = math.log(float(grid.getCellValue(target))) / math.log(2)
							smoothness -= abs(vl - diff)
    	return smoothness
    	pass

    def monoto(self,gridcopy):
    	#gridcopy = grid.clone()
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
		#----------use corner optimize--------
		tst = max(totals[0],totals[1]) + max(totals[2], totals[3])
		corners = [(0,0),(0,3),(3,0),(3,3)]
		maxtile = gridcopy.getMaxTile()
		for corner in corners:
			if gridcopy.map[corner[0]][corner[1]] == maxtile:
				#-------add cons -------
				#tst += 2.0
				#-------add log---------
				tst += math.log(maxtile,2) * 12
		return tst
		#---------- no corner optimize-------
		#return max(totals[0],totals[1]) + max(totals[2], totals[3])

		pass
	  
    def farthest(self,grid,cell,dirc):
		#gridcopy = grid.clone()
		prv = cell
		cell = (prv[0] + dirc[0],prv[1] + dirc[1])
		while not grid.crossBound(cell) and grid.getCellValue(cell)!=0:
			prv = cell
			cell = (prv[0] + dirc[0],prv[1] + dirc[1])
		return [prv, cell]

		pass
    def cluster(self, grid):
		clusterscore = 0
		for i in range(4):
			for j in range(4):
				if grid.getCellValue((i,j))==0:
				 	continue
				sumn = 0.0
				nN = 0
				nexts = [-1,0,1]
				for k in nexts:
					x = i+k
					if x<0 or x >= 4:
						continue
					for l in nexts:
						y = j+l
						if y<0 or y >= 4:
							continue
						if grid.getCellValue((x,y))>0:
							nN += 1
							sumn += abs(math.log(grid.getCellValue((x,y)),2)\
						         - math.log(grid.getCellValue((i,j)),2))
				clusterscore += sumn / nN
		return clusterscore
    def inBound(self,x, y, m, n):
        return x >= 0 and x < m and y >= 0 and y < n
    
    def numIslands(self, tgrid):
    	def dfs(i, j, m, n, grid,mark):
    	#grid = tgrid.clone()
	        if grid.map[i][j] != 0 and mark[i][j] != 1:
	            mark[i][j] = 1
	            moves = [(1,0), (0,1), (-1,0), (0,-1)]
	            for (movex, movey) in moves:
	                if not grid.crossBound((i + movex, j + movey)):
	                    dfs(i + movex, j + movey, m, n, grid,mark)
    	#tgrid = grid.clone()
        #if not grid: return 0
        #if not grid[0]: return 0
        m, n = 4, 4
        numIslands = 0
        mark = [[0 for i in range(4)] for j in range(4)]
        for i in range(m):
            for j in range(n):
                if tgrid.map[i][j] != 0:
                    dfs(i, j, m, n, tgrid, mark)
                    numIslands += 1
        return numIslands

    def solver(self,Sgrid,turn,alpha,beta,start_time,depth,Mdepth):
		#print depth
		grid =Sgrid.clone()
		valgrid = self.valfun(grid)
		moves = grid.getAvailableMoves()
		if (time.clock() - start_time) > 0.19 or not moves:
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
				if depth > Mdepth:
					move,vals = decision[2],decision[0]
				else:
					move,vals = self.solver(decision[1], False, Maxs[1], beta, start_time, depth +1, Mdepth)
				if vals > Maxs[1]:
					Maxs = [decision, vals]
				if Maxs[1] > alpha:
					alpha = Maxs[1]

				if Maxs[1] >= beta:
					
					return [Maxs[0],beta]
				
			return Maxs
		elif turn == False:
			Mins = [None, beta]
			Worst_Moves = []
			# ----------beta 0.2------------
			cells = grid.getAvailableCells()
			#scores = {2:[],4:[]}
			scores =[2,4]
			mgrid = grid.clone()
			for score in scores:
				for i,epty in enumerate(cells):
					subgrid = mgrid.clone()
					#scores[score].append(0)
					subgrid.setCellValue(epty, score)
					#mgrid.setCellValue(epty, score)
					#-------use modified valfunction-----
					# nislands = self.numIslands(subgrid)
					# tmpval = -self.getsmooth(subgrid)\
					#        + nislands \
					#        - self.cluster(subgrid) * 0.5
					       #- self.monoto(subgrid)
					#------instead of using valfun-------
					tmpval = self.valfun(subgrid)
					#subgrid.setCellValue(epty, 0)
					if not Worst_Moves or tmpval == Worst_Moves[0][0]:
						Worst_Moves.append([tmpval, subgrid])
					elif tmpval < Worst_Moves[0][0]:
						Worst_Moves =[[tmpval, subgrid]]

			if not Worst_Moves:
				return Mins
			for decision in Worst_Moves:
				#newbata = self.valfun(decision[1])
				movee,vals = self.solver(decision[1], True, alpha, Mins[1], start_time, depth, Mdepth)
				if vals < Mins[1]:
					Mins = [decision, vals]
				if Mins[1] < beta:
					beta = Mins[1]
				if Mins[1] <= alpha:
					
					return [Mins[0],alpha]
				
			return Mins
    def idsolver(self,grid,start_time):
		depth = 1
		best = None
		while time.clock() - start_time < 0.19:
			dd = self.solver(grid,True,-float('inf'),float('inf'), start_time, 0, depth)
			if dd:
				best = dd
			depth += 1
		return best
