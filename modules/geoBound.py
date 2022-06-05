from shapely.geometry import Point


# def is_arrived(current, destination):

#     # latitude, longitude
#     # (lat_c, lon_c) = current
#     # (lat_d, lon_d) = destination
#     site = Point(destination).buffer(0.0002)
#     user_position = Point(current)
#     value = site.contains(user_position)  # returns True
#     return value


def check_current_lat_lon(current, destination):

    # latitude, longitude
    x = float(10)

    (lat_c, lon_c) = current
    (lat_d, lon_d) = destination
    site = Point(float(lat_d), float(lon_d)).buffer(0.005)
    # site = Point(float(lat_d), float(lon_d)).buffer(0.0002)
    # print(site.area)
    user_position = Point(float(lat_c), float(lon_c))
    value = site.contains(user_position)  # returns True
    return value


def is_arrived(current, sites_list):
    values = None
    j = 0
    for i in sites_list:
        # print(i)
        if check_current_lat_lon(current, i):
            # values.append(j)
            values = j
            break
        j += 1

    return values


# print(check_current_lat_lon(current=(22.5676, 88.387),
#       destination=(22.5676902, 88.3873644)))
# v = is_arrived(current=(10, 10), sites_list=[(22.611111, 88.411111),
#                (22.6112, 88.4112), (22.601439, 88.415494)])
# print(v)
# AE 711 == 22.601439,88.415494
# AE 713 == 22.601831,88.414786
# 22.601479,88.415322
# ('50', '50') [('50', '50'), ('20', '20')]
# print(is_arrived(current=('22.60125', '88.415646'),
#       sites_list=[('50', '50'), ('22.6014977', '88.4112308')]))
