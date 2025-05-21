<?php

class FileManager {
    public static function write($file, $text) {
        $handle = fopen($file, 'w');
        if (!$handle) echo "File opened";
        fwrite($handle, $text);
    }
}
