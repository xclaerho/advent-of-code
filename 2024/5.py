rules, updates = open('input.txt').read().split('\n\n')
rules = [rule.strip().split('|') for rule in rules.split('\n')]
updates = [update.strip().split(',') for update in updates.split('\n')][:-1] # remove empty line

def check_rule(rule, update):
    before, after = rule
    if before in update and after in update:
      return update.index(before) < update.index(after)
    return True

p1 = 0
p2 = 0
for update in updates:
    if all(check_rule(rule, update) for rule in rules):
      p1 += int(update[len(update)//2])
    else:
      while not all(check_rule(rule, update) for rule in rules):
        for rule in rules:
          if check_rule(rule, update):
            continue
          before, after = rule
          before_index, after_index = update.index(before), update.index(after)
          update[before_index] = after
          update[after_index] = before
      p2 += int(update[len(update)//2])

print(p1)
print(p2)
