#Q-1) Next Greater Element
#Answer:-
def find_next_ele(A):
	for i in range(len(A)):
		next_ele = -1
		for j in range(i+1,len(A)):
			if A[j]>A[i]:
				next_ele = A[j]
				break
		print(next_ele,end =" ")

if __name__ == "__main__":
	A= [2,6,4,7,8,3,5,9] # 0 1 2 3 4 5 6 7 8
	find_next_ele(A)

# t(n) : O(n**2)

