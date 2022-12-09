raw = open('data.txt', 'r').readlines()

cur_elf_count = 0
l = []
for line in raw:
    stripped = line.strip()
    if len(stripped) < 1:
        l.append(cur_elf_count)
        cur_elf_count = 0
        continue
    cur_elf_count+=int(stripped)
l.sort(reverse=True)
print(l[0]+l[1]+l[2])