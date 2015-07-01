import csv

in_file_handle = open("../Data/NPS_Comments_Data.csv")
out_file_handle = open("../Data/NPS_Comments_Data_new.csv","w")

continue_flag = 0
count=0
start_flag = 0
for line in in_file_handle:
	line = line.strip()
	if line == "":
		continue

	
	if line[0] == "|":
		if len(line) == 1:
			if continue_flag == 1:
				pass
			else:
				continue_flag = 1
				final_line = ""
		else:
			continue_flag = 1
			final_line = ""

	if continue_flag:
		if line[-1] == "|" :
			if len(line) == 1:
				if final_line == "":
					#print line
					#print final_line
					#print continue_flag
					continue_flag = 1
					#continue
				else:
					continue_flag = 0
			else:
				continue_flag = 0
			final_line = (final_line+" "+ line.strip("|")).strip()
		else:
			final_line = (final_line+" "+ line.strip("|")).strip()
			continue
	else:
		final_line = line
	if final_line.strip() != "":
		out_file_handle.write(final_line+"\n")	
		count+=	1
print count

	

in_file_handle.close()
out_file_handle.close()
