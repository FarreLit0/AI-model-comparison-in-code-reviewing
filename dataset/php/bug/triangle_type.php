<?php

function triangleType($a, $b, $c) {
    if ($a + $b <= $c || $a + $c <= $b || $b + $c <= $a)
        return "Invalid";
    if ($a = $b && $b = $c)
        return "Equilateral";
    elseif ($a = $b || $b = $c || $a = $c)
        return "Isosceles";
    else
        return "Scalene";
}
