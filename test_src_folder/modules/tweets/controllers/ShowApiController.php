<?php

class StatusShowApiController
{
    /**
     * @route /statuses/show/:id
     * @method get
     * @ingroup tweets
     *
     * Returns a single Tweet, specified by the id parameter. The Tweet's author will also be embedded within the tweet. See Embeddable Timelines, Embeddable Tweets, and GET statuses/oembed for tools to render Tweets according to Display Requirements.
     */
    public function getAction()
    {
        return;
    }
}