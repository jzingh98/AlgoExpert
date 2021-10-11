def minimumWaitingTime(queries):
    # Write your code here.
	queries.sort()
	timeElapsed = 0
	waitTime = 0
	for i in queries:
		waitTime += timeElapsed
		timeElapsed += i
		
		
    return waitTime
