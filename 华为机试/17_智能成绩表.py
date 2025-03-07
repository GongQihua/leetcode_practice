import sys

class Node:
    def __init__(self, name, scores, total_score):
        self.name = name
        self.scores = scores
        self.total_score = total_score

def main():
    input = sys.stdin.read
    data = input().strip().split()
    
    index = 0

    n = int(data[index])
    index += 1
    m = int(data[index])
    index += 1

    subjects = {}
    for i in range(1, m + 1):
        subjects[data[index]] = 1
        index += 1
    
    students = []

    for i in range(n):
        name = data[index]
        index += 1
        scores = []
        total_score = 0
        for j in range(1, m+1):
            score = int(data[index])
            index += 1
            scores.append(score)
            total_score += score
        
        node = Node(name, scores, total_score)
        students.append(node)

    ranking_subject = data[index]

    if ranking_subject not in subjects:
        students.sort(key=lambda x: (-x.total_score, x.name))
    else:
        k = subjects[ranking_subject] - 1
        students.sort(key=lambda x: (-x.scores[k], x.name))
    
    for student in students:
        print(student.name, end = ' ')

if __name__ == '__main__':
    main()