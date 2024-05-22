votosEnBlanco :: [(String, String)] -> [Int] -> Int -> Int
votosEnBlanco (x:xs) (y:ys) t = t -  votosEnBlancoAux (y:ys)

votosEnBlancoAux :: [Int] -> Int
votosEnBlancoAux [] = 0
votosEnBlancoAux (x:xs) = x + votosEnBlancoAux xs


formulasValidas :: [(String, String)] -> Bool
formulasValidas [] = True
formulasValidas (x:xs) | fst(x) == snd (x) = False
                       | (pertenece (fst x)xs ) = False
                       | (pertenece (snd x) xs ) = False
                       | otherwise = formulasValidas xs


pertenece :: String -> [(String, String)] -> Bool
pertenece p [] = False
pertenece p (x:xs) | p == fst(x) = True
                   | p == snd(x) = True
                   | otherwise = pertenece p xs


division :: Int -> Int -> Float
division a b = fromIntegral a / fromIntegral b

porcentajeDeVotos :: String -> [(String, String)] -> [Int] -> Float
porcentajeDeVotos p (x:xs) (y:ys) = division (porcentajeDeVotosAux p (x:xs) (y:ys) * 100) (votosEnBlancoAux (y:ys))


porcentajeDeVotosAux :: String -> [(String, String)] -> [Int] -> Int
porcentajeDeVotosAux p [] [0] = 0
porcentajeDeVotosAux p ((x,y):xs) (z:zs) | y == p = z
                                         | otherwise = porcentajeDeVotosAux p xs zs

proximoPresidente :: [(String, String)] -> [Int] -> String
proximoPresidente [] [0] = x
proximoPresidente ((x,y)xs) (z:zs) | z > porcentajeDeVotosAux (proximoPresidente xs zs) xs zs = z
                                   | otherwise = proximoPresidente xs zs