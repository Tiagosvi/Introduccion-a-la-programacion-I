--Ejercicio:

generarStock :: [String] -> [(String,Int)]
generarStock [] = []
generarStock (x:xs) = (x, cantidadApariciones x (x:xs)): generarStock (eliminarRepetidos (x:xs) x)

cantidadApariciones :: String -> [String] -> Int
cantidadApariciones p [] = 0
cantidadApariciones p (x:xs) | p == x = 1 + cantidadApariciones p xs
                             | otherwise = cantidadApariciones p xs

eliminarRepetidos :: [String] -> String -> [String]
eliminarRepetidos [] _ = []
eliminarRepetidos (x:xs) p | x == p = eliminarRepetidos xs p
                           | otherwise = x: eliminarRepetidos xs p

--Ejercicio 2:

stockDeProducto :: [(String,Int)] -> String -> Int
stockDeProducto [] _ = 0
stockDeProducto ((x,y):xs) p | p == x = y
                             | otherwise = stockDeProducto xs p

--Ejercicio 3:

dineroEnStock :: [(String,Int)] -> [(String,Float)] -> Float
dineroEnStock [] [] = 0
dineroEnStock ((a,b):xs) ((c,d):ys) = unPrecio ((a,b):xs) ((c,d):ys) + dineroEnStock xs ((c,d):ys)


unPrecio :: [(String,Int)] -> [(String,Float)] -> Float
unPrecio [] _ = 0
unPrecio ((a,b):xs) ((c,d):ys) | a == c = d * fromIntegral(b)
                               | otherwise = unPrecio ((a,b):xs) ys

--Ejercicio 4:

aplicarOferta :: [(String,Int)] -> [(String,Float)] -> [(String,Float)]
aplicarOferta [] [] = []
aplicarOferta ((a,b):xs) ((c,d):ys) | (stockDeProducto ((a,b):xs) a) >= 10 = aplicarOfertaAux (c,d) : aplicarOferta xs ys
                                    | otherwise = (c,d) : aplicarOferta xs ys


aplicarOfertaAux :: (String,Float) -> (String,Float)
aplicarOfertaAux ("",0) = ("",0)
aplicarOfertaAux (a,b) = (a,b*0.8)