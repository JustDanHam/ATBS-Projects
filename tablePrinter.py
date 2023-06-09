tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def printTable(table):

    colWidths = [0] * len(table)

    for i in range(len(table)):
        for j in range(len(table[i])):
            if len(table[i][j]) > colWidths[i]:
                colWidths[i] = len(table[i][j])

    for y in range(len(table[0])):
        for x in range(len(table)):
            print(table[x][y].rjust(colWidths[x]), end = ' ')
        print()

printTable(tableData)
