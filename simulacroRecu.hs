relacionesValidas :: [(String,String)] -> Bool
relacionesValidas [] = True
relacionesValidas ((x,y):xs) | x == y = False
                             | pertenece x xs = False
                             | pertenece y xs = False
                             | otherwise = relacionesValidas xs


pertenece :: String -> [(String,String)] -> Bool
pertenece a [] = False
pertenece a ((x,y):xs) | a == x = True
                       | a == y = True
                       | otherwise = pertenece a xs



personas :: [(String,String)] -> [String]
personas [] = []
personas ((x,y):xs) | not(pertenece x xs) && not(pertenece y xs) = x: y: personas xs
                    | not(pertenece y xs) && pertenece x xs = y: personas xs
                    | not(pertenece x xs) && pertenece y xs = x: personas xs
                    | otherwise = personas xs



amigosDe :: String -> [(String,String)] -> [String]
amigosDe a [] = []
amigosDe a ((x,y):xs) | amigosDeAux a x && not(amigosDeAux a y) = y: amigosDe a xs
                      | amigosDeAux a y && not(amigosDeAux a x) = x: amigosDe a xs
                      | otherwise = amigosDe a xs




amigosDeAux :: String -> String -> Bool
amigosDeAux a x = a == x



longitud :: [String] -> Int
longitud [] = 0
longitud (x:xs) = 1 + (longitud xs)


personaConMasAmigos :: [(String,String)] -> String
personaConMasAmigos [] = ""
personaConMasAmigos l = personaConMasAmigosAux (personas l) l 


personaConMasAmigosAux :: [String] -> [(String,String)] -> String
personaConMasAmigosAux [] [] = ""
personaConMasAmigosAux (x:y:xs) (z:zs) | longitud (x:y:xs) == 2 && longitud(amigosDe x (z:zs)) >= longitud(amigosDe y (z:zs)) = x
                                       | longitud (x:y:xs) == 2 && longitud(amigosDe x (z:zs)) < longitud(amigosDe y (z:zs)) = y
                                       | longitud (amigosDe x (z:zs)) > longitud(amigosDe y (z:zs)) = personaConMasAmigosAux (x:xs) (z:zs)
                                       | otherwise = personaConMasAmigosAux (y:xs) (z:zs)



















