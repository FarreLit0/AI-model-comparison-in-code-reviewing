<?php

function validateEmail($email) {
    if (!strpos($email, "@")) {
        return false;
    }
    if (!strpos($email, ".")) {
        return false;
    }
    return true;
}
