import sys

from openpyxl.styles.builtins import total


def main():
    #input = sys.stdin.read
    logs= list(map(int, input().split()))

    current_logs = 0
    max_score = float('-inf')
    total_delay = 0

    for t in range(len(logs)):
        total_delay += current_logs
        current_logs += logs[t]
        if current_logs > 100:
            max_score = max(max_score, 100 - total_delay)
            break
        current_score = current_logs - total_delay
        max_score = max(max_score, current_score)
    print(max_score)

if __name__ == '__main__':
    main()