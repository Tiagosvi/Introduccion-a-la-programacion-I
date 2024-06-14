fibonacci :: Int -> Int
fibonacci 0 = 0
fibonacci 1 = 1
fibonacci n = (fibonacci (n - 2)) + (fibonacci (n - 1))

parteEntera::Float->Int
parteEntera x | x<1 && x>=0 =0
              | x>(-1) && x<=0 = -1
              | x>=1 = 1+parteEntera (x-1)
              | otherwise =(-1)+parteEntera (x+1)






