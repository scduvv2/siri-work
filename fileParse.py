import csv
# this many columns are always present.
always_present_columns_index=43

# total number of columnns you will need in the target file. this is sum of fixed columns and all the optional columns
# 3 *J1 3*J2+ 1*K4 + 1*L1
# J1=11
# J2 = 19
# K4=6
# L1=5 
total_number_of_columns = 44+(3*11)+(3*19)+(1*6)+(1*5)
segment_sequence = ['J1','J1','J1','J2','J2','J2','K4','L1']
segment_columns={
  "J1": 11,
  "J2":19,
  "K4": 6,
  "L1": 5

}

def process_file(in_file,out_file):
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
        out_file.write('\n')
      
def process_line(line):
  columns = line.split('|')
  write_columns = []
  columnIndex=0
  # as it is always guarnteed that always_present_columns_count are there, adding them first to the write column
  while columnIndex <= always_present_columns_index:
      write_columns.append(columns[columnIndex])
      columnIndex = columnIndex+1

  for segment in segment_sequence:
    if  len(columns)> columnIndex:
      segment_in_file = columns[columnIndex]
      if(segment==segment_in_file):
        # has to do -1 for 0 based index as range function is end inclusive
        for col_to_add_index in range (segment_columns[segment]-1):
          columnIndex = columnIndex + 1
          val = columns[columnIndex]
          write_columns.append(val)
      else:
        write_columns.append(segment)
        for i in range (segment_columns[segment]):
          
          write_columns.append('')
    else :
      write_columns.append(segment)
      for i in range (segment_columns[segment]):                    
        write_columns.append('')
  delim='|'
  return_value = delim.join(write_columns)

  return return_value

process_file('sample.txt','output.txt')