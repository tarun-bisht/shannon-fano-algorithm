#Compress class for storing different parameters of string
class compress:
	def __init__(self,correspond):
		self.original=correspond
		self.count=0
		self.code=""
		self.probability=0
#Shannon Compression Class for compressing data using shannon fennon encoding
class shannon_fennon_compression:
	def getProbability(self,compressor):
		return compressor.probability
	def compress_data(self,data):
		'''
		1- Process String and find probability of all the unique occurences of characters in String
		2- Using processed list to store elements which are been processed ie... probability is been found
		3- probability list consists of probability of each characters
		'''
		processed=[]
		compressor=[]
		total_length=len(data)
		for i in range(len(data)):
			if data[i] not in processed:
				processed.append(data[i])
				count=data.count(data[i])
				var=count/total_length #Finding probability of unique characters in data
				comp=compress(data[i])
				comp.count=count
				comp.probability=var
				compressor.append(comp)
		# sorting probability in descending order
		sorted_compressor=sorted(compressor,key=self.getProbability,reverse=True)
		split=self.splitter(probability=[i.probability for i in sorted_compressor],pointer=0)
		self.encoder(sorted_compressor,split)
		return sorted_compressor
	#split probabilities in order used in shannon encoding
	def splitter(self,probability,pointer):
		diff=sum(probability[:pointer+1])-sum(probability[pointer+1:len(probability)])
		if diff<0:
			point=self.splitter(probability,pointer+1)
			diff_1=sum(probability[:point])-sum(probability[point:len(probability)])
			diff_2=sum(probability[:point+1])-sum(probability[point+1:len(probability)])
			if abs(diff_1)<abs(diff_2):
				return point-1
			return point
		else:
			return pointer
	#Encode string to compressed version of string data in binary
	def encoder(self,compressor,split):
		if split > 0:
			part_1=compressor[:split+1]
			for i in part_1:
				i.code+='0'
			if len(part_1)<=1:
				return
			self.encoder(part_1,self.splitter(probability=[i.probability for i in part_1],pointer=0))
			part_2=compressor[split+1:len(compressor)]
			for i in part_2:
				i.code+='1'
			if len(part_2)<=1:
				return
			self.encoder(part_2,self.splitter(probability=[i.probability for i in part_2],pointer=0))
		elif split==0:
			part_1=compressor[:split+1]
			for i in part_1:
				i.code+='0'
			part_2=compressor[split+1:len(compressor)]
			for i in part_2:
				i.code+='1'

#Main Function
if __name__=='__main__':
	print("Data--- malyalam madman")
	compressor=shannon_fennon_compression()
	compressed_data=compressor.compress_data("malyalam madman")
	for i in compressed_data:
	    print(f"Character-- {i.original}:: Code-- {i.code} :: Probability-- {i.probability}")
	print("")
	print("Data--- shannon")
	compressed_data=compressor.compress_data("shannon")
	for i in compressed_data:
	    print(f"Character-- {i.original}:: Code-- {i.code} :: Probability-- {i.probability}")
	print("")
	print("Data--- fennon")
	compressed_data=compressor.compress_data("fennon")
	for i in compressed_data:
	    print(f"Character-- {i.original}:: Code-- {i.code} :: Probability-- {i.probability}")
