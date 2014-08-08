def problem15():
    row=[1 for i in range(21)]
    for i in xrange(20):
        next_row=[1]
        for i in row[1:]:
            next_row.append(i+next_row[row.index(i)-1])
        row=next_row
    return row[-1]
print problem15()
