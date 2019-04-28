Filename = '1'

try:
    with open(Filename + '.in', 'r') as fin:
        listin = fin.readlines()

    ans = []
    T = 0
    for line in listin:
        T += 1
        try:
            s = line.split(': ')
            if id(line) == id(listin[-1]):
                ans.append("'" + s[0].strip() + "' : '" + s[1].strip() + "'" + '\n')
            else:
                ans.append("'" + s[0].strip() + "' : '" + s[1].strip() + "'," + '\n')
        except:
            print('Line '+ str(T) + ': Wrong format')

    with open(Filename + '.out', 'w') as fout:
        fout.writelines(ans)

except:
    print("Error Filename")

