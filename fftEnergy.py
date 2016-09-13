import numpy as np
import pandas as pd
'''
the input data is a panda Series, 
this method computes the fft of every 32 points in this data,
and pick the energy of 1Hz, 2Hz, 3Hz,
return a list of tuple,like: [(1ene,2ene,3ene), (), ()...]
'''
fftLength = 32
def fftEnergy(data):
	data = data.values
	length = len(data)
	fftResult = []
	'''
	make sure the data length can be divided by fftLength, if not, cut the 
	last part of the data
	'''
	if(length % fftLength!= 0):
		data = data[:length - length % fftLength]
	
	round = len(data) / fftLength
	
	'''
	only append the energy of 1Hz, 2Hz, 3Hz to fftResult
	'''
	for i in range(round):
		partData = data[0+i*fftLength: (1+i)*fftLength]
		partFft = np.fft.fft(partData)
		fftResult.append((abs(partFft[0]), abs(partFft[1]), abs(partFft[2])))
	
	return fftResult

def main():
	df = pd.read_csv("walk.csv")
	dataProcessed = fftEnergy(df.A)
	writeToCsv("walk_mode.csv", dataProcessed, "walk")
	
	
def writeToCsv(file_name, dataProcessed, mode):
	input = []
	for i in dataProcessed:
		temp = []
		for j in i:
			temp.append(j)
		'''
		append mode to each entry
		'''
		temp.append(mode)
		input.append(temp)
	df = pd.DataFrame(input, columns = ["1Hz","2Hz","3Hz", "mode"])
	df.to_csv(file_name)
	
'''test'''
main()


