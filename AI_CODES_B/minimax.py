def minimax(values, flag=True):
   new = []
   for i in range(0, len(values) - 1, 2):
      if flag:
         new.append(max(values[i], values[i+1]))
      else:
         new.append(min(values[i], values[i+1]))
      if len(values)%2:
         new.append(values[-1])
   return minimax(new, not flag) if len(new) > 1 else new[0]
         
leaf_values = [3, 6, 9, 4, 7, 3, 4, 5, 2]

print('The root value will be', minimax(leaf_values))