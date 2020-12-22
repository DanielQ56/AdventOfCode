
def CountAnswers(groups):
    answers = {}

    for group in groups:
        g = group.replace("\n", "")

        g = set(g)

        for l in g:
            if l in answers:
                answers[l] += 1
            else:
                answers[l] = 1
    
    return sum(a for a in answers.values())

def CountAnswersAll(groups):
    answers = {}

    for group in groups:
        gr = set(group.replace("\n", ""))
        grp = group.split("\n")

        for l in gr:
            if all(l in g for g in grp):
                if l in answers:
                    answers[l] += 1
                else:
                    answers[l] = 1

    return sum(a for a in answers.values())
        


if __name__ == "__main__":

    inputFile = open("Day6Input.txt")

    groups = inputFile.read().split("\n\n")

    print(CountAnswersAll(groups))

    inputFile.close()
