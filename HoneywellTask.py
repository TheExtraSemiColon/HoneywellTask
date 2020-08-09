


import imageio
import numpy as np
from PIL import Image
import random
import argparse 




def checkval(data, x,y,t):
	
	return data[x-1][y-1][t]+data[x][y][t]+data[x][y+1][t]+data[x][y-1][t]+data[x][y+1][t]+data[x+1][y-1][t]+data[x+1][y][t]+data[x+1][y+1][t]



def initialize(data):


	initState=[[1,0,1,1,0,1],[0,0,0,0,1,1],[1,1,0,0,1,1],[0,1,1,0,0,1],[1,0,1,1,0,1],[1,0,1,1,0,1],[0,0,0,0,1,1],[0,1,1,0,0,1],[1,1,0,0,1,1],[0,0,0,0,1,1],]

	n=len(initState[0])
	m=len(initState)


	

	for i in range(0,n):
			for j in range(0,m):
			
				data[j+1][i+1][0]=initState[j][i]
	return data

def gameOfLife(data,maximumTime):
	time_max=maximumTime
	N=len(data)
	for t in range(0,time_max-1):
		
		for j in range(1,N-1):
			for i in range(1,N-1):
				val=1
				val=checkval(data,i,j,t)
				if val<0 or val>8:
					print("Val value is incorrect")
				elif val<2 or val>=4:
					data[i][j][t+1]=0
				elif val==2 or val==3:
					if data[i][j][t]==0 and val==3:
						data[i][j][t+1]=1
					elif data[i][j][t]==1:
						data[i][j][t+1]=1


	return data

def makeMovie(data, maximumTime):
	filenames=[]
	time_max=maximumTime
	data=np.array(data)
	for ti in range(0,time_max):
		img = Image.fromarray(( data[:,:,ti]*255).astype(np.uint8))
		filename='Frame'+str(ti)+'.png'
		img.save(filename)
		filenames.append(filename)
	images = []
	for filename in filenames:
	    images.append(imageio.imread(filename))
	imageio.mimsave('movie.gif', images)


def main():
	# Command line args are in sys.argv[1], sys.argv[2] .. 
    # sys.argv[0] is the script name itself and can be ignored 
    # parse arguments 
    parser = argparse.ArgumentParser(description="Runs Conway's Game of Life simulation.") 
  
    # add arguments 
    parser.add_argument('--grid-size', dest='N', required=False) 
    #parser.add_argument('--mov-file', dest='movfile', required=False) 
    parser.add_argument('--frames', dest='frame', required=False) 
    parser.add_argument('--glider', action='store_true', required=False)  
    args = parser.parse_args() 
      
    # set grid size 
    N = 100
    if args.N and int(args.N) > 8: 
        N = int(args.N) 
    # set frames 
    timemax=20
    if args.frame and int(args.frame) > 8: 
        timemax = int(args.frame) 
          
   
  
    grid=[]
    # check if "glider" demo flag is specified 
    if args.glider: 
        grid = [[[0 for time in range(timemax)]for row in range(N)] for col in range(N)]
        grid=initialize(grid)   
    else:  
        grid = [[[ 0 if random.random()>=0.05 else 1 for time in range(timemax)]for row in range(N)] for col in range(N)] 

    #Process the data; game of life begins
    grid=gameOfLife(grid,timemax)
  
  
    #make the movie and play it
    makeMovie(grid,timemax)
    # im1 = Image.open('movie.gif')
    # im1.seek()



if __name__ == '__main__': 
    main() 