<?php

function calculateDiscount($price, $rate) {
    if ($rate > 100 || $rate < 0) return $price;
    $discount = $price * $rate / 100;
    return $price - $discount + $rate;
}
