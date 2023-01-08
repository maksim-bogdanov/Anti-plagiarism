def levenstein (text_1, text_2):
   F = [[(i + j) if i * j == 0 else 0 for j in range(len(text_2) + 1)] for i in range(len(text_1) + 1)]
   
   for i in range(1, len(text_1) + 1):
      for j in range(1, len(text_2) + 1):
         if text_1[i - 1] == text_2[j - 1]:
            F[i][j] = F[i - 1][j - 1]
         else:
            F[i][j] = 1 + min(F[i - 1][j], F[i][j - 1], F[i - 1][j - 1])
  
   return F[len(text_1)][len(text_2)]
   
            

f_r = open(input(), 'r')
f_w = open(input(), 'w') 
file_names = []
for line in f_r.readlines():
    if line != '\n': 
       file_names.append(line)
       
f_r.close()


for i in range(len(file_names)):
  if file_names[i].find('\n') != -1:
     file_names[i] = file_names[i][ : file_names[i].find('\n')]
         

for i in range(len(file_names)):
   
    first_name = file_names[i][ : file_names[i].find(' ')]   
    last_name = file_names[i][file_names[i].find(' ') + 1 : len(file_names[i])]
    
    f = open(first_name, 'r')
    program_1 = f.read()
    f.close()
    
    f = open(last_name, 'r')
    program_2 = f.read()
    f.close()  
    
    p = 1 - levenstein (program_1, program_2) / max(len(program_1), len(program_2))
    f_w.write(str(round(p, 2)))
    f_w.write('\n')

f_w.close()


    
                   

      