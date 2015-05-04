import random


def traverse_all_path(city):
    """Traverses with the given city.

    Return all path.
    """
    if len(city) <= 1:
        return [city]

    total_path = []
    for i in range(len(city)):
        remain_city = city[:i] + city[i+1:]
        path = traverse_all_path(remain_city)
        for p in path:
            total_path.append(p + city[i:i+1])

    return total_path


def random_path(city):
    """Generates a path ramdomly with given city."""
    path = []
    temp_city = city[:]
    while len(temp_city):
        random_city = random.choice(temp_city)
        path.append(random_city)
        temp_city.remove(random_city)
    return path


def dist_cal(path, dist):
    """Computes distance with given path."""
    sum_dist = 0
    for i in range(len(path)-1):
        sum_dist += dist[int(path[i])-1][int(path[i+1])-1]
    sum_dist += dist[int(path[len(path)-1])-1][path[0]-1]
    return sum_dist


def traverse_main(city, dist):
    optimal = 10000
    index = -1
    all_path = traverse_all_path(city)
    for i in range(len(all_path)):
        pd = dist_cal(all_path[i], dist)
        if pd < optimal:
            optimal = pd
            index = i
    print 'The length of the optimal path is %d' %optimal
    print 'The optimal path is:'
    print all_path[index]


def random_main(city, dist):
    num = 10
    optimal = 10000
    for i in range(num):
        path = random_path(city)
        pd = dist_cal(path, dist)
        if pd < optimal:
            optimal = pd
            optimal_path = path
    print 'The length of the optimal path is %d' %optimal
    print 'The optimal path is:'
    print optimal_path


if __name__ == '__main__':
    city = [1, 2, 3, 4, 5]

    dist = ((0, 1, 3, 4, 5),
            (1, 0, 1, 2, 3),
            (3, 1, 0, 1, 2),
            (4, 2, 1, 0, 1),
            (5, 3, 2, 1, 0))

    for i in range(0, 5):
        print dist[i][:]

    print '==================='
    traverse_main(city, dist)
    random_main(city, dist)
