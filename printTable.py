tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(stringList):
    colWidths = [0] * len(stringList)
    for w in range(len(colWidths)):
        colWidths[w] = len(max(stringList[w], key=len))

    for i in range(len(stringList[0])):
        for n in range(len(stringList)):
            print(stringList[n][i].rjust(colWidths[n]), end=' ')
        print(' ')

printTable(tableData)
