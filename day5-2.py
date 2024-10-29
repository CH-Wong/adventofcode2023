with open("input_day5.txt") as file:
    data = file.read()

chunks = data.split("\n\n")

mappings_list = []
for chunk in chunks[1:]:
    mappings = chunk.split("\n")[1:]

    mappings = [mapping.split() for mapping in mappings]
    for ind, mapping in enumerate(mappings):
        mappings[ind] = [int(val) for val in mappings[ind]]

    mappings_list.append(mappings)

_, seed_ranges = chunks[0].split(": ")
seed_ranges = [int(val) for val in seed_ranges.split()]

seeds = []
for s, r in zip(seed_ranges[::2], seed_ranges[1::2]):
    print(s,r)
    # seeds.extend(range(s,s+r))
print(len(seeds))


# locations = []
# for seed in seeds:
#     for mappings in mappings_list:
#         for target, source, steps in mappings:
#             if source <= seed <= source + steps:
#                 seed += target - source
#                 break

#     locations.append(seed)

# print(min(locations))
