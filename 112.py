#DFS Recursively
class Solution:
	def hasPathSum(self, root, sum):
		    if not root:
			    return False
		    if not root.left and not root.right and root.val == sum:
			    return True
		    return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)

class Solution:
	def hasPathSum(self, root, sum): #have a function with a path summing up to a sum
	    res = [] #this is the stack that i'll append the results to
	    self.dfs(root, sum, res) #call on the dfs function and pass in the root, the sum and the result array
	    return any(res) #when the dfs fun finishes if there is true in the function
	def dfs(self, root, target, res):
	    if root:
		if not root.left and not root.right and root.val == target: #if root.left and root.left==null and root.val==target 
		    res.append(True) #we can achieve sum and we append true to the array
		if root.left: #The any() function returns True if any element of an iterable is True. If not, any() returns Fals
		    self.dfs(root.left, target-root.val, res)
		if root.right:
		    self.dfs(root.right, target-root.val, res)

# BFS with stack
class Solution:
	# DFS with stack
    def hasPathSum(self, root, sum):
        if not root:
            return False
        stack = [(root, root.val)]
        while stack:
            curr, val = stack.pop()
            if not curr.left and not curr.right and val == sum:
                return True
            if curr.right:
                stack.append((curr.right, val+curr.right.val))
            if curr.left:
                stack.append((curr.left, val+curr.left.val))
        return False
# BFS with queue
class Solution:
	def hasPathSum(self, root, sum):
	    if not root:
		return False
	    queue = [(root, sum-root.val)]
	    while queue:
		curr, val = queue.pop(0)
		if not curr.left and not curr.right and val == 0:
		    return True
		if curr.left:
		    queue.append((curr.left, val-curr.left.val))
		if curr.right:
		    queue.append((curr.right, val-curr.right.val))
	    return False

	
