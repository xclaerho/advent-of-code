reports = open('input').readlines()
reports = [list(map(int, report.split())) for report in reports]

def is_safe(report):
  increasing = report[0] < report[1]
  for i in range(len(report)-1):
    if not (1<= abs(report[i]-report[i+1]) <= 3 and increasing == (report[i]<report[i+1])):
      return False
  return True

safe = sum(is_safe(report) for report in reports)
print(safe)

def is_any_safe(report):
  for i in range(len(report)):
    if is_safe(report[:i] + report[i+1:]):
      return True
  return False

safe = sum(is_any_safe(report) for report in reports)
print(safe)
