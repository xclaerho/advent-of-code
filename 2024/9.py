from collections import defaultdict

disk_map = open('input.txt').read().splitlines()[0]

def compact_fragmented(disk_map):
  files = list(map(int, disk_map[::2]))
  free = list(map(int, disk_map[1::2]))
  checksum = 0
  block = 0

  for id in range(len(files)):
    if id >= len(files):
      break
    for _ in range(files[id]):
      checksum += id*block
      block += 1
      files[id] -= 1
    if files[-1] == 0:
      break
    for i in range(free[id]):
      checksum += (len(files)-1)*block
      block += 1
      files[-1] -= 1
      if files[-1] == 0:
        files.pop()

  return checksum

def compact_whole(disk_map):
  files = list(map(int, disk_map[::2]))
  free = list(map(int, disk_map[1::2]))

  files_moved_behind_id = defaultdict(list)
  for id in range(len(files)-1,0,-1):
    size = files[id]
    # only want to move left
    for i in range(id):
      if free[i] >= size:
        files_moved_behind_id[i].append((id, size))
        free[i] -= size
        files[id] = -size
        break

  checksum = 0
  block = 0
  for id in range(len(files)):
    for _ in range(abs(files[id])):
      if files[id] > 0:
        checksum += block*id
      block += 1
    for moved_id, size in files_moved_behind_id[id]:
      for _ in range(size):
        checksum += block*moved_id
        block += 1
    if id >= len(free):
      break
    for _ in range(free[id]):
      block += 1
  return checksum

print(compact_fragmented(disk_map), compact_whole(disk_map))
