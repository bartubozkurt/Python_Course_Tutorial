file_counts = {"jpg": 10, "txt": 14,"csv":2,"py":23}
for i in file_counts:
  print(i)
print('-----------------')

for ext, amount in file_counts.items():
  print("There are {} files with the .{} extension".format(ext,amount))
print('-----------------')
print(file_counts.keys())
print(file_counts.values())
