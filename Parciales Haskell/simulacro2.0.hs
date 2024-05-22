relacionesValidas :: [(String, String)] -> Bool
relacionesValidas [] = True
relacionesValidas ((x,y):xs) | x == y = False
                             | pertenece x xs = False
                             | pertenece y xs = False
                             | otherwise = relacionesValidas xs

pertenece :: String -> [(String, String)] -> Bool 
pertenece p [] = False
pertenece p ((x,y):xs) | p == x = True
                       | p == y = True
                       | otherwise = pertenece p xs


personas :: [(String, String)] -> [String]
personas  [] = []
personas ((x,y):xs) | pertenece x xs && pertenece y xs = [] ++ personas xs
                    | pertenece x xs = [y] ++ personas xs
                    | pertenece y xs = [x] ++ personas xs
                    | otherwise = [x] ++ [y] ++ personas xs


amigosDe :: String -> [(String, String)] -> [String]
amigosDe a [] = []
amigosDe a ((x,y):xs) | a == x = [y] ++ amigosDe a xs
                      | a == y = [x] ++ amigosDe a xs
                      | otherwise = amigosDe a xs

