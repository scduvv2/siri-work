import csv
csv.register_dialect('piper', delimiter='|', quoting=csv.QUOTE_NONE)
def read_file(in_file,out_file):
  with open(in_file, mode='r') as in_file, \
     open(out_file, mode='w') as out_file:
   # A file is iterable
    # We can read each line with a simple for loop
    header = next(in_file)
    out_file.write(header)
    for line in in_file:

        # Tuple unpacking is more Pythonic and readable
        # than using indices
        wite_line = process_line(line)
        out_file.write(wite_line)
      
def process_line(line):

  return "";
read_file('sample.txt','output.txt')