stn = input()
wrd = input()

i = 0
ans = 0
while i + len(wrd) <= len(stn):
    if wrd == stn[i:i+len(wrd)]:
        ans += 1
        i += len(wrd)
    else: i += 1

print(ans)