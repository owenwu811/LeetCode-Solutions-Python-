
#this is from the grokking course - last question in subsets chapter without solution 

#given a set of n positive integers, find all the possible subsets of integers that sum up to a number k

#example 1: setofintegers = {1, 3, 5, 21, 19, 7, 2}, k = 7, output: {5, 2}, {7}


#my own solution:

def get_k_sum_subsets(set_of_integers, target_sum):
  # Replace this placeholder return statement with your code
  set_of_integers = list(set_of_integers)
  subsets = []  
  def f(i, curset):
    if sum(curset) == target_sum:
      subsets.append(curset.copy())
      return
    if i >= len(set_of_integers):
      return 
    curset.append(set_of_integers[i])
    f(i + 1, curset)
    curset.pop()
    f(i + 1, curset)
  f(0, [])
  return subsets
