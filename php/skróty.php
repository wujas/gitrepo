<?php
    $data1 = 'Adam Słodowy';
    $data2 = 'Adam Słoowx';
    echo hash('md5', $data);
    echo '
';
    echo hash('sha256', $data2);
    echo hash('md5', $data2);
?>
