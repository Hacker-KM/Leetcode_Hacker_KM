
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for asteroid in asteroids:
            while stack and asteroid < 0 and stack[-1] > 0:
                if abs(asteroid) > stack[-1]:
                    stack.pop()
                elif abs(asteroid) == stack[-1]:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(asteroid)
        return stack

        # for i in range(1,len(asteroids)):
        #     if (asteroids[i-1]>0 and asteroids[i]>0) or (asteroids[i-1]<0 and asteroids[i]<0):
        #         print(asteroids[i-1],asteroids[i],'c')
        #         continue
        #     else:
        #         if abs(asteroids[i-1])==abs(asteroids[i]):
        #             asteroids.remove(asteroids[i])
        #             asteroids.remove(asteroids[i-1])
        #             print(asteroids)
        #         else:

        #             if abs(asteroids[i-1])>abs(asteroids[i]):
        #                 asteroids.remove(asteroids[i])
        #             else:
        #                 asteroids.remove(asteroids[i-1])
        #             # asteroids.remove(asteroids[i])
        #             print(asteroids)
        # return asteroids

