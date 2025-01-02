def reader_gen(file_name):
               
    with open(file_name, 'r') as file:
        for line in file:
            
            yield line.strip()


    


file_read = (reader_gen(r"E:\python\python_ex\generator_ex\python_sorted.txt"))

print(next(file_read))
print(next(file_read))
print(next(file_read))
print(next(file_read))


