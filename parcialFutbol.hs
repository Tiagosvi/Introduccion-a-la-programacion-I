--Ejercicio:
atajaronSuplentes :: [(String,String)] -> [Int] -> Int -> Int
atajaronSuplentes [] [] 0 = 0
atajaronSuplentes ((x,y):xs) (z:zs) g = g - sumatoria (z:zs)

sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

--Ejercicio 2:

arquerosValidos :: [(String,String)] -> Bool
arquerosValidos [] = True
arquerosValidos ((x,y):xs) | x == y = False
                           | pertenece x xs = False
                           | pertenece y xs = False
                           | otherwise = arquerosValidos xs

pertenece :: String -> [(String,String)] -> Bool
pertenece p [] = False
pertenece p ((x,y):xs) | p == x = True
                       | p == y = True
                       | otherwise = pertenece p xs

--Ejercicio 3:

porcentajeDeGoles :: String -> [(String,String)] -> [Int] -> Float
porcentajeDeGoles a [] [] = 0
porcentajeDeGoles a ((x,y):xs) (z:zs) = division (porcentajeDeGolesAux a ((x,y):xs) (z:zs) * 100) (sumatoria (z:zs))


division :: Int -> Int -> Float
division a b = fromIntegral a / fromIntegral b


porcentajeDeGolesAux :: String -> [(String,String)] -> [Int] -> Int
porcentajeDeGolesAux a [] [] = 0
porcentajeDeGolesAux a ((x,y):xs) (z:zs) | a == y = z
                                         | otherwise = porcentajeDeGolesAux a xs zs 


vallaMenosVencida :: [(String,String)] -> [Int] -> String
vallaMenosVencida [(x,y)]_ = y
vallaMenosVencida ((x,y):(a,b):xs) (z:c:zs) | c > z = vallaMenosVencida ((x,y):xs) (z:zs)
                                            | otherwise = vallaMenosVencida ((a,b):xs) (c:zs)
