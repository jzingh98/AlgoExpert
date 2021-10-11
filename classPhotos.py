def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort()
	blueShirtHeights.sort()
	blueBack = True
	redBack = True
	# Check if all Blues at i are greated than all Reds at i
	for i in range(len(redShirtHeights)):
		if redShirtHeights[i] >= blueShirtHeights[i]:
			blueBack = False
			break
	# Check if all Reds at i are greater than all Blues at i
	for i in range(len(redShirtHeights)):
		if redShirtHeights[i] <= blueShirtHeights[i]:
			redBack = False
			break
	return blueBack or redBack
