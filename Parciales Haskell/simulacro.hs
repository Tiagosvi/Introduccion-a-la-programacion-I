
-- [(hola, hola) (chau, adios)] -> false, no repetidos devuelve true



relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = True
relacionesValidas (x:xs) | fst(x) == snd (x) = False
                         | pertenece (fst x) xs = False
                         | pertenece (snd x) xs = False
                         | otherwise = relacionesValidas xs


pertenece :: String -> [(String, String)] -> Bool
pertenece p [] = False
pertenece p (x:xs) | p == fst(x) || p == snd(x) = True
                   | otherwise = pertenece p xs



-- [(Juan, Pedro) (Luis, Juan)] -> [Juan, Pedro, Luis]

personas :: [(String, String)] -> [String]
personas [] = []
personas (x:xs) | (pertenece (fst x) xs) && (pertenece (snd x) xs) = [] ++ personas xs
                | (pertenece (fst x) xs) = [snd x] ++ personas xs
                | (pertenece (snd x) xs) = [fst x] ++ personas xs
                | otherwise = [fst x] ++ [snd x] ++ personas xs




amigosDe :: String -> [(String, String)] -> [String]
amigosDe p [] = []
amigosDe p (x:xs) | p == (fst x) = [snd x] ++ amigosDe p xs
                  | p == (snd x) = [fst x] ++ amigosDe p xs
                  | otherwise = amigosDe p xs









