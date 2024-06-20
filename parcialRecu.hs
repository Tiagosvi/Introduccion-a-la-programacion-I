--Ejercicio: 

aproboMasDeNMaterias :: [(String, [Int])] -> String -> Int -> Bool
aproboMasDeNMaterias [] p n = False
aproboMasDeNMaterias (x:xs) p n | cantAprobadas (encontrarAlumno p (x:xs)) > n = True
                                | otherwise = False


encontrarAlumno :: String -> [(String, [Int])] -> [Int]
encontrarAlumno p [] = []
encontrarAlumno p ((x2,x3):xs) | p == x2 = x3
                               | otherwise = encontrarAlumno p xs

cantAprobadas :: [Int] -> Int
cantAprobadas [] = 0
cantAprobadas (x:xs) | x >= 4 = 1 + cantAprobadas xs
                     | x < 4 = cantAprobadas xs

--Ejercicio 2:

buenosAlumnos :: [(String, [Int])] -> [String]
buenosAlumnos [] = []
buenosAlumnos ((x,y):xs) | buenAlumno y = x: buenosAlumnos xs 
                         | otherwise = buenosAlumnos xs

buenAlumno :: [Int] -> Bool
buenAlumno [] = False
buenAlumno (x:xs) = aplazos (x:xs) && (promedio (x:xs) >= 8)

aplazos :: [Int] -> Bool
aplazos [] = True
aplazos (x:xs) | x < 4 = False
               | otherwise = aplazos xs 

sumatoria :: [Int] -> Int
sumatoria [] = 0
sumatoria (x:xs) = x + sumatoria xs

longitud :: [Int] -> Int
longitud [] = 0
longitud (x:xs) = 1 + longitud xs


promedio :: [Int] -> Float
promedio [] = 0
promedio (x:xs) = fromIntegral(sumatoria (x:xs)) / fromIntegral(longitud (x:xs))


--Ejercicio 3:

mejorPromedio :: [(String, [Int])] -> String
mejorPromedio [] = ""
mejorPromedio ((a,a2):(b,b2):xs) | longitudTuplas ((a,a2):(b,b2):xs) == 2 && promedio a2 >= promedio b2 = a
                                 | longitudTuplas ((a,a2):(b,b2):xs) == 2 && promedio a2 < promedio b2 = b
                                 | promedio a2 > promedio b2 = mejorPromedio ((a,a2):xs)
                                 | otherwise = mejorPromedio ((b,b2):xs)

longitudTuplas :: [(String,[Int])] -> Int
longitudTuplas [] = 0
longitudTuplas (x:xs) = 1 + longitudTuplas xs








