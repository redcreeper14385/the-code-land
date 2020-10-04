<?php

/**
 * This file is the MOST basic example of OPP in PHP
 */

// The Interface
interface BasicInterface
{
    public function sayHello();
}

// The Class
class BasicOOP implements BasicInterface
{
    function __construct($name)
    {
        $this->name = $name;
    }
    public function sayHello()
    {
        return "Hello " . $this->name;
    }
}


// Generate the Object
$newObject = new BasicOOP("Developer");
echo $newObject->sayHello() . PHP_EOL;
