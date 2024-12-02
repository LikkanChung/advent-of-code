def part1(input_data):
    safe_reports = [report_is_safe(list(map(int, report.strip().split(' ')))) for report in input_data]

    print(safe_reports.count(True))

def part2(input_data):
    safe = 0
    for line in input_data:
        report = list(map(int, line.strip().split(' ')))
        if (report_is_safe(report)):
            safe += 1
        else:
            for i in range(len(report)):
                if report_is_safe(report[:i] + report[i+1:]):
                    safe += 1
                    break
    print(safe)

    
def report_is_safe(levels: list[int]):
    
    if sorted(levels) != levels and list(reversed(sorted(levels))) != levels:
        return False
    
    previous = None
    for level in levels:
        if previous is None:
            # First level
            previous = level
        else:
            difference = abs(int(previous) - int(level))
            previous = level
            if difference < 1 or difference > 3:
                return False
    return True

