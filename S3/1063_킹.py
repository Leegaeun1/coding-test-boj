dic = {
    "R": (1,0),
    "L": (-1,0),
    "B": (0,1),
    "T": (0,-1),
    "RT": (1,-1),
    "LT": (-1,-1),
    "RB": (1,1),
    "LB": (-1,1)
}

king, stone, n = input().split()
king_x, king_y = ord(king[0])-65 , 8 - int(king[1])
stone_x, stone_y = ord(stone[0])-65 , 8 - int(stone[1])

for _ in range(int(n)):
    move = input()
    dx, dy = dic[move]
    nx, ny = king_x + dx, king_y + dy
    
    if 0 <= nx < 8 and 0 <= ny < 8:  # 킹이 먼저 이동 가능해야 함
        if nx == stone_x and ny == stone_y:  # 돌과 충돌
            sx, sy = stone_x + dx, stone_y + dy
            if 0 <= sx < 8 and 0 <= sy < 8:  # 돌도 이동 가능
                king_x, king_y = nx, ny
                stone_x, stone_y = sx, sy
        else:
            king_x, king_y = nx, ny

print(chr(king_x+65) + str(8-king_y))
print(chr(stone_x+65) + str(8-stone_y))
