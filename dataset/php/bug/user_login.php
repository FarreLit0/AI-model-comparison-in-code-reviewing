<?php

function login($user, $pass) {
    $validUser = "admin";
    $validPass = "1234";
    if ($user = $validUser && $pass = $validPass) {
        return "Success";
    }
    return "Fail";
}
