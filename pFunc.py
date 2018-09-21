#pose関係の関数まとめ

def p1(mas, new):
    mas1x = mas[4][0] - mas[3][0]
    mas1y = mas[4][1] - mas[3][1]
    mas2x = mas[3][0] - mas[2][0]
    mas2y = mas[3][1] - mas[2][1]
    mas3x = mas[7][0] - mas[5][0]
    mas3y = mas[7][1] - mas[5][1]

    new1x = new[4][0] - new[3][0]
    new1y = new[4][1] - new[3][1]
    new2x = new[3][0] - new[2][0]
    new2y = new[3][1] - new[2][1]
    new3x = new[7][0] - new[5][0]
    new3y = new[7][1] - new[5][1]

    # mpans : mas pre ans
    mpans1 = (mas1x * mas2x) + (mas1y * mas2y)  # dot
    mpans2 = (mas2x * mas3y) - (mas2y * mas3x)  # cross

    # npans : new pre ans
    npans1 = (new1x * new2x) + (new1y * new2y)  # dot
    npans2 = (new2x * new3y) - (new2y * new3x)  # cross

    ans = (abs((mpans1 - npans1)) + abs((mpans2 - npans2))) / 2
    print(ans)
    return ans


def p2(mas, new):
    mas1x = mas[7][0] - mas[6][0]
    mas1y = mas[7][1] - mas[6][1]
    mas2x = mas[6][0] - mas[5][0]
    mas2y = mas[6][1] - mas[5][1]
    mas3x = mas[4][0] - mas[2][0]
    mas3y = mas[4][1] - mas[2][1]

    new1x = new[7][0] - new[6][0]
    new1y = new[7][1] - new[6][1]
    new2x = new[6][0] - new[5][0]
    new2y = new[6][1] - new[5][1]
    new3x = new[4][0] - new[2][0]
    new3y = new[4][1] - new[2][1]

    # mpans : mas pre ans
    mpans1 = (mas1x * mas2x) + (mas1y * new2y)  # dot
    mpans2 = (mas2x * mas3y) - (mas2y * mas3x)  # cross

    # npans : new pre ans
    npans1 = (new1x * new2x) + (new1y * new2y)  # dot
    npans2 = (new2x * new3y) - (new2y * new3x)  # cross
    ans = (abs((mpans1 - npans1)) + abs((mpans2 - npans2))) / 2
    print(ans)
    return ans


def p3(mas, new):
    mas1x = mas[4][0] - mas[2][0]
    mas1y = mas[4][1] - mas[2][1]
    mas2x = mas[7][0] - mas[5][0]
    mas2y = mas[7][1] - mas[5][1]
    new1x = new[4][0] - new[2][0]
    new1y = new[4][1] - new[2][1]
    new2x = new[7][0] - new[5][0]
    new2y = new[7][1] - new[5][1]

    # mpans : mas pre ans
    mpans = (mas1x * mas2y) - (mas1y * mas2x)  # cross

    # npans : new pre ans
    npans = (new1x * new2y) - (new1y * new2x)  # cross

    # additional condition determination
    if new[7][1] > new[6][1] and new[3][1] > new[4][1] and new[6][1] > new[3][1]:
        constant = 0
    else:
        constant = 9999

    ans = (abs(mpans + npans) + constant) / 2
    print(ans)
    return ans


def p4(mas, new):
    mas1x = mas[4][0] - mas[3][0]
    mas1y = mas[4][1] - mas[3][1]
    mas2x = mas[3][0] - mas[2][0]
    mas2y = mas[3][1] - mas[2][1]
    mas3x = mas[7][0] - mas[6][0]
    mas3y = mas[7][1] - mas[6][1]
    mas4x = mas[6][0] - mas[5][0]
    mas4y = mas[6][1] - mas[5][1]

    new1x = new[4][0] - new[3][0]
    new1y = new[4][1] - new[3][1]
    new2x = new[3][0] - new[2][0]
    new2y = new[3][1] - new[2][1]
    new3x = new[7][0] - new[6][0]
    new3y = new[7][1] - new[6][1]
    new4x = new[6][0] - new[5][0]
    new4y = new[6][1] - new[5][1]

    # mpans : mas pre ans
    mpans1 = (mas1x * mas2x) + (mas1y * mas2y)  # dot
    mpans2 = (mas3x * mas4x) + (mas3y * mas4y)  # dot

    # npans : new pre ans
    npans1 = (new1x * new2x) + (new1y * new2y)  # dot
    npans2 = (new3x * new4x) + (new3y * new4y)  # dot

    # additional condition determination
    if new[3][1] > new[4][1] and new[6][1] > new[7][1]:
        constant = 0
    else:
        constant = 9999

    ans = (abs((mpans1 - npans1)) + abs((mpans2 - npans2)) + constant) / 2
    print(ans)
    return ans


def p5(mas, new):
    mas1x = mas[4][0] - mas[2][0]
    mas1y = mas[4][1] - mas[2][1]
    mas2x = mas[7][0] - mas[5][0]
    mas2y = mas[7][1] - mas[5][1]
    new1x = new[4][0] - new[2][0]
    new1y = new[4][1] - new[2][1]
    new2x = new[7][0] - new[5][0]
    new2y = new[7][1] - new[5][1]

    # mpans : mas pre ans
    mpans = (mas1x * mas2y) - (mas1y * mas2x)  # cross

    # npans : new pre ans
    npans = (new1x * new2y) - (new1y * new2x)  # cross

    # additional condition determination
    if new[7][1] > new[5][1] and new[4][1] > new[2][1] and new[3][1] > new[5][1]:
        constant = 0
    else:
        constant = 9999

    ans = (abs(mpans + npans) + constant) / 2
    print(ans)
    return ans


def p6(mas, new):
    mas1x = mas[4][0] - mas[2][0]
    mas1y = mas[4][1] - mas[2][1]
    mas2x = mas[7][0] - mas[5][0]
    mas2y = mas[7][1] - mas[5][1]
    new1x = new[4][0] - new[2][0]
    new1y = new[4][1] - new[2][1]
    new2x = new[7][0] - new[5][0]
    new2y = new[7][1] - new[5][1]

    # mpans : mas pre ans
    mpans = (mas1x * mas2y) - (mas1y * mas2x)  # cross

    # npans : new pre ans
    npans = (new1x * new2y) - (new1y * new2x)  # cross

    # additional condition determination
    if new[4][1] > new[3][1] and new[3][1] > new[6][1] and new[6][1] > new[7][1]:
        constant = 0
    else:
        constant = 9999

    ans = (abs(mpans + npans) + constant) / 2
    print(ans)
    return ans


def p7(mas, new):
    mas1x = mas[4][0] - mas[3][0]
    mas1y = mas[4][1] - mas[3][1]
    mas2x = mas[3][0] - mas[2][0]
    mas2y = mas[3][1] - mas[2][1]
    mas3x = mas[7][0] - mas[6][0]
    mas3y = mas[7][1] - mas[6][1]
    mas4x = mas[6][0] - mas[5][0]
    mas4y = mas[6][1] - mas[5][1]

    new1x = new[4][0] - new[3][0]
    new1y = new[4][1] - new[3][1]
    new2x = new[3][0] - new[2][0]
    new2y = new[3][1] - new[2][1]
    new3x = new[7][0] - new[6][0]
    new3y = new[7][1] - new[6][1]
    new4x = new[6][0] - new[5][0]
    new4y = new[6][1] - new[5][1]

    # mpans : mas pre ans
    mpans1 = (mas1x * mas2x) + (mas1y * mas2y)  # dot
    mpans2 = (mas3x * mas4x) + (mas3y * mas4y)  # dot

    # npans : new pre ans
    npans1 = (new1x * new2x) + (new1y * new2y)  # dot
    npans2 = (new3x * new4x) + (new3y * new4y)  # dot

    # additional condition determination
    if new[4][1] > new[3][1] and new[6][1] > new[7][1]:
        constant = 0
    else:
        constant = 9999

    ans = (abs((mpans1 - npans1)) + abs((mpans2 - npans2)) + constant) / 2
    print(ans)
    return ans


def p8(mas, new):
    mas1x = mas[4][0] - mas[3][0]
    mas1y = mas[4][1] - mas[3][1]
    mas2x = mas[3][0] - mas[2][0]
    mas2y = mas[3][1] - mas[2][1]
    mas3x = mas[7][0] - mas[6][0]
    mas3y = mas[7][1] - mas[6][1]
    mas4x = mas[6][0] - mas[5][0]
    mas4y = mas[6][1] - mas[5][1]

    new1x = new[4][0] - new[3][0]
    new1y = new[4][1] - new[3][1]
    new2x = new[3][0] - new[2][0]
    new2y = new[3][1] - new[2][1]
    new3x = new[7][0] - new[6][0]
    new3y = new[7][1] - new[6][1]
    new4x = new[6][0] - new[5][0]
    new4y = new[6][1] - new[5][1]

    # mpans : mas pre ans
    mpans1 = (mas1x * mas2x) + (mas1y * mas2y)  # dot
    mpans2 = (mas3x * mas4x) + (mas3y * mas4y)  # dot

    # npans : new pre ans
    npans1 = (new1x * new2x) + (new1y * new2y)  # dot
    npans2 = (new3x * new4x) + (new3y * new4y)  # dot

    # additional condition determination
    if new[3][1] > new[4][1] and new[6][1] > new[7][1]:
        constant = 0
    else:
        constant = 9999

    ans = (abs((mpans1 - npans1)) + abs((mpans2 - npans2)) + constant) / 2
    print(ans)
    return ans


def p9(mas, new):
    # 判定用ベクトル生成
    mas1x = mas[7][0] - mas[4][0]
    mas1y = mas[7][1] - mas[4][1]
    mas2x = mas[6][0] - mas[3][0]
    mas2y = mas[6][1] - mas[3][1]
    new1x = new[7][0] - new[4][0]
    new1y = new[7][1] - new[4][1]
    new2x = new[6][0] - new[3][0]
    new2y = new[6][1] - new[3][1]
    # 外積計算
    preans1 = (mas1x * new1y) - (mas1y * new1x)
    preans2 = (mas2x * new2y) - (mas2y * new2x)

    ans = (preans1 + preans2) / 2
    print(ans)
    return ans


def selectPose(mas, new, key):
    ans = 0
    if key == 1:
        ans = p1(mas, new)
    elif key == 2:
        ans = p2(mas, new)
    elif key == 3:
        ans = p3(mas, new)
    elif key == 4:
        ans = p4(mas, new)
    elif key == 5:
        ans = p5(mas, new)
    elif key == 6:
        ans = p6(mas, new)
    elif key == 7:
        ans = p7(mas, new)
    elif key == 8:
        ans = p8(mas, new)
    elif key == 9:
        ans = p9(mas, new)

    return ans
