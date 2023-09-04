actual_tea_type = int(input())
answers = list(map(int, input().split()))

correct_count = answers.count(actual_tea_type)


print(correct_count)