
from collections import Counter

def seq_mining(sequences, proportion, maximum):
	
	patterns = []
	
	for sequence in sequences:
	
		seq_patterns = []
		
		for i in range(1, min(len(sequence), maximum) + 1):
			
			for j in range(len(sequence) + 1 - i):
			
				pattern = sequence[j:j+i]
				
				if pattern not in seq_patterns:
					seq_patterns.append(pattern)
					patterns.append(pattern)
		
	threshold = int(len(sequences) * proportion)
	
	patterns = [pattern for pattern in patterns if patterns.count(pattern) > threshold]
	
	return Counter(patterns)
	
if __name__ == "__main__":

	print(seq_mining(['ABCD', 'ABABC', 'BCAABCD'], 0.34, 10000000))
