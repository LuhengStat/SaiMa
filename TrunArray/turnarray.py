while 1:
    n = raw_input()
    if n != "":
        n = int(n)
        array = raw_input()
        array = array.split()
        array = map(float, array)


        def judge(array):
            n1 = len(array)
            sortarray = sorted(array)
            '''
            pos = []
            for i in range(n1):
                if array[i] != sortarray[i]:
                    pos = pos + [i]
            '''
            pos = [i for i in range(n1) if array[i] != sortarray[i]]

            if len(pos) == 1:
                return "yes"
            else:
                temparray = array[:]
                partarray = [array[i] for i in range(pos[0], pos[len(pos) - 1] + 1)]
                partarray = list(reversed(partarray))
                start = pos[0]
                end = pos[len(pos) - 1]
                temparray = array[:start] + partarray + array[end + 1:]
                if temparray == sorted(array):
                    return "yes"
                else:
                    return "no"


        print judge(array)

    else:
        break

