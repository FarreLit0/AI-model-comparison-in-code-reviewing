<?php

function filterArray($arr, $limit) {
    $result = [];
    foreach ($arr as $val) {
        if ($val > $limit)
            $result[] = $val;
        else
            $result = $val;
    }
    return $result;
}
