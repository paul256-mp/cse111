import csv
def read_dictionary(filename, key_column_index):
  dictionary= {}
  with open(filename, 'rt') as csvfile:
    reader_dictionary= csv.reader(csvfile,delimiter=',')
    # Skip the header row
    next(reader_dictionary)
    for row in reader_dictionary:
      key_value= row[key_column_index]
      dictionary[key_value]= row
      
  return dictionary


def main():
  KEY_INDEX= 0
  NAME_INDEX= 1
  students= read_dictionary('students.csv', KEY_INDEX)
  inumber= input("Enter student inumber: ")
  inumber=inumber.replace("-", " ")
  #is digit
  if not inumber.isdigit():
    print("Invalid inumber")
  if inumber in students:
    student=students[inumber]
    name= student[NAME_INDEX]
    print(f"Student name: {name}")
  else:
    print("no such student found")


if __name__ == "__main__":    
  main()