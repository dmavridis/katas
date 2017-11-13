
def C(n, step, cnt, v):
    if cnt > n or step > n:
        print('1 ...',n, step, cnt, v)
        return
    if cnt == n:
        # if counter cnt reached n print the list
        print('2 ...',n, step, cnt)
        print(v)
        return
    else:
        print('3 ...',n, step, cnt, v)

        # else append the step size to list
        v.append(step)
        # increment the cnt by step and recurse
        C(n, step, cnt + step, v)
        # remove the last step from list
        v.pop()
        # increment the step size and recurse
        print('4 ...',n, step, cnt, v)
        C(n, step + 1, cnt, v)

def find_combinations(n):
    return C(n,1,0,[])


print(find_combinations(5))