# Wojciech Jedrysik
# 06.03.2019

def main():
    pointsCount = int(input("Enter the number of points: "))

    if pointsCount < 0:
        print("Not enough points.")
        exit()

    x_list = []
    y_list = []

    for i in range(pointsCount):
        print("Enter x for a point ", i+1, ":")
        x = int(input())
        print("Enter y for a point ", i+1, ":")
        y = int(input())

        x_list.append(x)
        y_list.append(y)

    point = int(input("Enter the x coordinate of the point at which interpolation is to be performed: "))

    result = interpolation(x_list, y_list, point, pointsCount)
    print("Interpolation result: ", result)


def interpolation(x_list, y_list, point, size):
    result = 0
    for i in range(size):
        tmp = 1.0
        for j in range(size):
            if i != j:
                tmp *= (point - x_list[j]) / (x_list[i] - x_list[j])
        result += tmp * y_list[i]
    return result


if __name__ == "__main__":
    main()