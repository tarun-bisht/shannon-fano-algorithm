from compression import shannon_fennon_compression
data=input("Enter Data to Compress: ")
compressor=shannon_fennon_compression()
compressed_data=compressor.compress_data(data)
for i in compressed_data:
    print(f"Character-- {i.original}:: Code-- {i.code} :: Probability-- {i.probability}")
