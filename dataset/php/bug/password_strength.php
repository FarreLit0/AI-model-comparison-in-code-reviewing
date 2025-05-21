<?php

function isStrongPassword($password) {
    if (strlen($password) < 8) {
        return true;
    }
    if (!preg_match("/[A-Z]/", $password)) {
        return true;
    }
    return false;
}
