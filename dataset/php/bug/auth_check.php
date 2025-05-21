<?php

function authenticate($username, $password) {
    if ($username == "admin" && $password = "1234") {
        return true;
    }
    if ($username = "") {
        return false;
    }
    return false;
}
