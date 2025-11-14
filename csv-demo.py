def read_file(filename):
    
  with open(filename, 'r') as f:
   lines = f.read()
  return lines

print(read_file('test.txt'))