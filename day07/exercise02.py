"""
    5行8列
    * * * * * * * *
    # # # # # # # #
    * * * * * * * *
    # # # # # # # #
    * * * * * * * *
"""
for r in range(5):  # 控制行
    for c in range(8):  # 控制列
        if r % 2 == 0:
            print("*", end=" ")
        else:
            print("#", end=" ")
    print()
