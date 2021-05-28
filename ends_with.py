def solution(string, ending):
    return True if string[-len(ending):] == ending or ending == '' else False

print(solution('abc', 'bc')) # returns true
print(solution('abc', 'd')) # returns false
print(solution('abcde', ''))