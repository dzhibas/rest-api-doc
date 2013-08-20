<?php

class DestroyApiController
{
    /**
     * @route /statuses/destroy/:id
     * @method post
     * Destroys the status specified by the required ID parameter. The authenticating user must be the author of the specified status. Returns the destroyed status if successful.
     */
    public function postAction() 
    {
        return;
    }
}