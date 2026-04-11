# height = [0,2,0,3,1,0,1,3,2,1]
# max_l. = [0,0,2,2,3,3,3,3,3,3] # parse from left to right
# max_r. = [3,3 ,3,3 ,3,3,2,1,0]  # parse from right to left
# water = [0, 0,0,0,0,0,0,0,0,0]

# water[i] = min(max(h[l]),max(h[r])) - height[i]
# water[i]<0 then water[i]=0

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        water = [0]*n
        max__val_l =0
        max_val_r =0
        max_l = [0]*n
        max_r = [0]*n
        
        for i in range(n):
            if i ==0:
                max_l[i]=0
                max_r[n-1-i]=0
            else:
                max_l[i] = max(max_l[i-1],height[i-1])
                max_r[n-1-i] = max(max_r[n-i],height[n-i])

        
        for i in range(n):
            wtr = min(max_l[i],max_r[i])- height[i]
            if wtr >0:
                water[i]= wtr
            else:
                water[i]= 0
        # print(max_l)
        # print('\n')
        # print(max_r)

        return sum(water)


                

       
        