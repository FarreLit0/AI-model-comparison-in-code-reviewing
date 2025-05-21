<?php
function calculate_average($numbers) {
    if (empty($numbers)) return 0;
    return array_sum($numbers) / count($numbers);
}
?>