import nltk

pos_file = open("postive_words.csv")
neg_file = open("negative_words.csv")

pos_list = []
neg_list = []

for line in pos_file:
	line = line.strip()
	if len(line) > 1:
		pos_list.append(line)

for line in neg_file:
        line = line.strip()
        if len(line) > 1:
                neg_list.append(line)

in_file = open("../Data/NPS_Comments_Data_new.csv")
out_file = open("Senti_Comments.csv","w")

count = 0
for line in in_file:
	score = 0
	count += 1
	line = line.strip().strip('"')
	pos_tags = nltk.pos_tag(nltk.word_tokenize(line))
	for pos in pos_tags:
		if pos[1] not in ["NN", "NNS", "RB", "PRP", ".", "CC", "IN", "DT", "MD"]:
			if pos[0] in pos_list:
				score += 1
			elif pos[0] in neg_list:
				score -= 1 
	#out_file.write(str(line)+","+str(score)+"\n")
	out_file.write(str(score)+"\n")
	if count%100 == 0:
		print count

in_file.close()
out_file.close()
