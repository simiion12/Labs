clear all
# Prima parte a lab 6
res1=integral(@funct1,-0.5,5)
res2=integral(@funct2,-3/2,4)

# A doua parte a lab 6
res3 = integral2(@(x,y)funct3(x,y), 1, 2, 1, 3)

# A treia parte a lab 6
res4 = integral3(@(x,y,m)funct4(m,x,y), 5, 6, 1, 2, 1, 3)

