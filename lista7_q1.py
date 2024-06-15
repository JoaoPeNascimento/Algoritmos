def find_all_groups(n):
    def find_groups(n, last_num, memo):
        if (n, last_num) in memo:
            return memo[(n, last_num)]

        if n == 0:
            groups = [[]]
        else:
            groups = []
            for i in range(last_num, n + 1):
                for group in find_groups(n - i, i, memo):
                    groups.append([i] + group)

        memo[(n, last_num)] = groups
        return groups

    groups = find_groups(n, 1, {})
    return groups[1:]


n = int(input())
groups = find_all_groups(n)
groups.insert(0, [1]*n)  # inclui lista com apenas 1's na primeira posição
print(f"Uma sessão com {n} pessoas pode ter sua audiência nos seguintes subgrupos:")
for group in groups:
    print(group)