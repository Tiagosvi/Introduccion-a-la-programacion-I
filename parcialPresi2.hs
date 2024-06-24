--Ejercicio:
formulasValidas :: [(String,String)] -> Bool
formulasValidas [] = True
formulasValidas ((x,y):xs) | x == y = False
                           | pertenece x xs = False
                           | pertenece y xs = False
                           | otherwise = formulasValidas xs

pertenece :: String -> [(String,String)] -> Bool
pertenece p [] = False
pertenece p ((x,y):xs) | p == x = True
                       | p == y = True
                       | otherwise = pertenece p xs

--Ejercicio 2:
votosEnBlanco :: [(String,String)] -> [Int] -> Int -> Int
votosEnBlanco (x:xs) (y:ys) n = n - sumatoria (y:ys)

sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs 


--Ejercicio 4:
proximoPresidente :: [(String,String)] -> [Int] -> String
proximoPresidente [(a,b)] _ = a
proximoPresidente ((a,b):(c,d):xs) (y:z:ys) | y > z = proximoPresidente ((a,b):xs) (y:ys)
                                            | otherwise = proximoPresidente ((c,d):xs) (z:ys)


porcentajeDeVotos :: String -> [(String,String)] -> [Int] -> Float
porcentajeDeVotos p (x:xs) (y:ys) = division (buscarVotos p (x:xs) (y:ys) * 100) (sumatoria (y:ys))

buscarVotos :: String -> [(String,String)] -> [Int] -> Int
buscarVotos p [] [] = 0
buscarVotos p ((a,b):xs) (y:ys)| p == a = y
                               | otherwise = buscarVotos p xs ys

division:: Int -> Int -> Float
division a b = (fromIntegral a) / (fromIntegral b)