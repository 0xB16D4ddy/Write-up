#!/usr/bin/php 7.4.27
<?php
    
    $defaultdata = array("showpassword" => "no", "bgcolor"=>"#ffffff");
    function xor_encrypt($in, $key)
    {
        $text = $in;
        $outText = '';
    
        // Iterate through each character
        for($i=0;$i<strlen($text);$i++) {
        $outText .= $text[$i] ^ $key[$i % strlen($key)];
        }
    
        return $outText;
    }

    $ciphertext = hex2bin('0a554b221e00482b02044f2503131a70531957685d555a2d121854250355026852115e2c17115e680c');
    // $key
    $plaintext = json_decode($defaultdata);

    echo(xor_encrypt($ciphertext, $plaintext));
    // phpinfo();
?>