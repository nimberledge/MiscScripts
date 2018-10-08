def LNS(L):
	dp = {}
	for i in range(len(L)-1, -1, -1):
		if i == len(L) - 1:
			dp[i] = max(L[i], 0)
			continue
		elif i == len(L) - 1 - 1:
			dp[i] = max(L[i], dp[i+1])
			continue
		dp[i] = max(dp[i+1], dp[i+2], L[i] + dp[i+2])
	return dp[0]

print(LNS([5,1,1,5]))
