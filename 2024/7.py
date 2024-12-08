equations = open('input.txt').readlines()

def check_possible(val, nums, part_2 = False):
  if len(nums) == 1:
    return val == nums[0]
  if val % nums[-1] == 0:
    if check_possible(val//nums[-1], nums[:-1], part_2):
      return True
  if check_possible(val-nums[-1], nums[:-1], part_2):
    return True

  if part_2:
    if (val-nums[-1])%10**len(str(nums[-1])) == 0:
      if check_possible((val-nums[-1])//(10**len(str(nums[-1]))), nums[:-1], part_2):
        return True

  return False

possible = []
possible_2 = []
for e in equations:
  val, nums = e.split(': ')
  val = int(val)
  nums = list(map(int, nums.strip().split()))

  if check_possible(val, nums):
    possible.append(val)
  if check_possible(val, nums, True):
    possible_2.append(val)

print(sum(possible))
print(sum(possible_2))
