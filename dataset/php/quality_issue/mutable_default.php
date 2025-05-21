<?php
function append_value($value, &$list = null) {
    if ($list === null) $list = array();
    $list[] = $value;
    return $list;
}
?>