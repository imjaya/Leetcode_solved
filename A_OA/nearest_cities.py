#If no cities found, return None instread of string "None" 
from collections import defaultdict
def findNearestCities(numCities: int, cities: List[str], xCoordinates: List[int], yCoordinates: List[int],
                      numOfQueries: int, queries: List[str]) -> List[str]:




    coordinate_to_city_map = {}
    x_cities = defaultdict(list)
    y_cities = defaultdict(list)
    for x, y, city_name in zip(xCoordinates, yCoordinates, cities):
        coordinate_to_city_map[city_name] = (x, y)
        x_cities[x].append((y, city_name))
        y_cities[y].append((x, city_name))
    query_results = []
    for q_city in queries:
        if q_city not in coordinate_to_city_map:
            query_results.append(None)
            print(q_city)
            continue
        min_dist = float('inf')
        closest_city = ""
        qx, qy = coordinate_to_city_map[q_city]
        # print(q_city)
        for y, city in x_cities[qx]:
            dist = abs(y - qy)
            if city != q_city and (dist < min_dist or (dist == min_dist and city < closest_city)):
                # print("x match")
                closest_city = str(city)
                min_dist = dist
        for x, city in y_cities[qy]:
            dist = abs(x - qx)
            if city != q_city and (dist < min_dist or (dist == min_dist and city < closest_city)):
                # print("y match")
                closest_city = str(city)
                min_dist = dist
        query_results.append(closest_city)
        for i in range(0,len(query_results)):
            if query_results[i]=="NONE" or query_results[i]=="" :
                query_results[i]=None
        
    return query_results

