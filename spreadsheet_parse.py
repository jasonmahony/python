#!/usr/bin/python

# take a comma delimited spreadsheet and output file
# output a column that is the sum of all number values
# and `Total Sum = "total vaule of sums calculated"`

def parse(spreadsheet, outputfile):
    ss_fh = open(spreadsheet)
    o_fh = open(outputfile, 'w')
    sum = 0
    for line in ss_fh:
        row_list = line.strip("\n").split(",")
        row_sum = 0
        for n in row_list:
            if n.isdigit():
                row_sum += int(n)
        row_list.append(row_sum)
        row = ' | '.join(map(str, row_list))
        o_fh.write(row + "\n")
        sum += row_sum
    o_fh.write("Total Sum = " + str(sum) + "\n")
    o_fh.close()

parse("spreadsheet/spreadsheet.csv", "spreadsheet/output.txt")