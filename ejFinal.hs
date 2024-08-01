esSodokuValido :: [[Int]] -> Bool
esSodokuValido [] = True
esSodokuValido (x:xs) | not(esValido x) = False
                      | not(esValidoTranspuesta(transpuesta(x:xs))) = False
                      | otherwise = esSodokuValido xs

                    

esValido :: [Int] -> Bool
esValido [] = True
esValido (x:xs) | cuantasPertenece x (x:xs) > 1 = False
                | otherwise = esValido xs

cuantasPertenece :: Int -> [Int] -> Int
cuantasPertenece n [] = 0
cuantasPertenece n (x:xs) | n == x = 1 + cuantasPertenece n xs
                          | otherwise = cuantasPertenece n xs


transpuesta :: [[Int]] -> [[Int]]
transpuesta [] = []
transpuesta ([]:_) = []
transpuesta (x:xs) = primeros (x:xs) : transpuesta(sacarPrimeros (x:xs))

primeros :: [[Int]] -> [Int]
primeros [] = []
primeros (x:xs) = head (x) : primeros xs

sacarPrimeros :: [[Int]] -> [[Int]]
sacarPrimeros [] = []
sacarPrimeros (x:xs) = tail (x) : sacarPrimeros xs 

esValidoTranspuesta :: [[Int]] -> Bool
esValidoTranspuesta [] = True
esValidoTranspuesta (x:xs) | not(esValido x) = False
                           | otherwise = esValidoTranspuesta xs

    