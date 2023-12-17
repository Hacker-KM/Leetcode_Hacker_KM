# class FoodRatings:

#     def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
#         self.foods = foods
#         self.cuisines = cuisines
#         self.ratings = ratings
#         self.dic = defaultdict(list)
#         self.store = defaultdict()
#         self.high_rated = defaultdict()
#         for i in range(len(foods)):
#             self.store[foods[i]] = cuisines[i] 
#             self.dic[cuisines[i]].append((foods[i], ratings[i]))

#     def changeRating(self, food: str, newRating: int) -> None:
#         cuisine_find = self.store[food]
#         for i in range(len(self.dic[cuisine_find])):
#             if self.dic[cuisine_find][i][0] == food:
#                 self.dic[cuisine_find][i] = (food, newRating)
        
#     def highestRated(self, cuisine: str) -> str:
#         l = list(self.dic[cuisine])
#         l.sort(key=lambda x: x[1] ,reverse=True)
#         rat = [l[i][1] for i in range(len(l))]
#         ll = []
#         for i in range(len(rat)):
#             if l[i][1]==max(rat):
#                 ll.append(l[i][0])
#         ll.sort()
#         return ll[0]


# TLE




class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.rating = {}
        self.cuisines = defaultdict(list)
        self.food_cuisine = {}
        
        for i in range(len(foods)):
            food, r, cuisine = foods[i], ratings[i], cuisines[i]
            self.rating[food] = -r
            self.food_cuisine[food] = cuisine
            heapq.heappush(self.cuisines[cuisine], (-r, food))
        

    def changeRating(self, food: str, newRating: int) -> None:
        self.rating[food] = -newRating
        cuisine = self.food_cuisine[food]
        heapq.heappush(self.cuisines[cuisine], (-newRating, food))
        

    def highestRated(self, cuisine: str) -> str:
        while self.rating[self.cuisines[cuisine][0][1]] != self.cuisines[cuisine][0][0]:
            heapq.heappop(self.cuisines[cuisine])
            
        return self.cuisines[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)


