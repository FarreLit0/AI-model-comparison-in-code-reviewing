<?php
function check($x) {
    if ($x > 0) {
        if ($x < 100) {
            if ($x % 2 === 0) {
                echo "Even";
            }
        }
    }
}
?>