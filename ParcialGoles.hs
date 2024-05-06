
atajaronSuplentes :: [(String, String)] -> [Int] -> Int -> Int
atajaronSuplentes [] [0] 0 = 0
atajaronSuplentes (x:xs) (y:ys) g = g - atajaronSuplentesAux (y:ys)
                                


atajaronSuplentesAux :: [Int] -> Int
atajaronSuplentesAux [] = 0
atajaronSuplentesAux (x:xs) = x + atajaronSuplentesAux xs



equiposValidos :: [(String, String)] -> Bool
equiposValidos [] = True
equiposValidos (x:xs) | fst (x) == snd (x) = False
                      | (pertenece (fst x) xs) = False
                      | (pertenece (snd x) xs) = False
                      | otherwise = equiposValidos xs


division :: Int -> Int -> Float
division a b = fromIntegral a / fromIntegral b

porcentajeDeGoles :: String -> [(String, String)] -> [Int] -> Float
porcentajeDeGoles a (x:xs) (y:ys) = division (porcentajeDeGolesAux a (x:xs) (y:ys) * 100) (atajaronSuplentesAux (y:ys))

porcentajeDeGolesAux :: String -> [(String, String)] -> [Int] -> Int
porcentajeDeGolesAux a [] [0] = 0
porcentajeDeGolesAux a ((x, y):xs) (z:zs) | a == y = z
                     | otherwise = porcentajeDeGolesAux a xs zs


vallaMenosVencida :: [(String, String)] -> [Int] -> String
vallaMenosVencida [(x,y)] [z] = y
vallaMenosVencida ((x, y):xs) (z:zs) | z < porcentajeDeGolesAux (vallaMenosVencida xs zs) xs zs = y
                                     | otherwise = vallaMenosVencida xs zs


