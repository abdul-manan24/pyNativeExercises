# __Challenge__

# Slice list into 3 equal chunks and reverse each chunk


sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]

# Getting first chunk.
chunk_1 = slice(3)
# Printing the chunk.
print(f"Chunk one {sample_list[chunk_1]}")
rchunk_1 = []

# iterating through first chunk to append in reversed list.
for num in reversed(sample_list[chunk_1]):
    rchunk_1.append(num)

print(f"After reversing it {rchunk_1}")


# Getting second chunk.
chunk_2 = slice(3,6)
# Printing the chunk.
print(f"Chunk one {sample_list[chunk_2]}")
rchunk_2 = []

# iterating through second chunk to append in reversed list.
for num in reversed(sample_list[chunk_2]):
    rchunk_2.append(num)

print(f"After reversing it {rchunk_2}")


# Getting third chunk.
chunk_3 = slice(6,9)
# Printing the chunk.
print(f"Chunk one {sample_list[chunk_3]}")
rchunk_3 = []

# iterating through first chunk to append in reversed list.
for num in reversed(sample_list[chunk_3]):
    rchunk_3.append(num)

print(f"After reversing it {rchunk_3}")