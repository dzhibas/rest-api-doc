<?php

class DemoApiController
{
    /**
     * @route /v1/module1/demo-api
     * @method get
     * 
     * this is demo api docblock
     * @urlparam limit int not required limit
     * @returns json item
     */
    public function getAction()
    {
        return "{'success': 'true'}";
    }
}
