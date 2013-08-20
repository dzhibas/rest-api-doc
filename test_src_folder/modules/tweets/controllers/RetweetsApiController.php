<?php

class RetweetsApiController
{
    /**
     * @route /statuses/retweets/:id
     * @method get
     * @ingroup tweets
     *
     * Returns up to 100 of the first retweets of a given tweet.
     *
     * @urlparam count int not required Specifies the number of records to retrieve. Must be less than or equal to 100. Example: 5
     * @urlparam id int required The numerical ID of the desired status. Example: 123
     * @urlparam trim_user int When set to either true, t or 1, each tweet returned in a timeline will include a user object including only the status authors numerical ID. Omit this parameter to receive the complete user object. Example: true
     *
     * @example request
     * GET https://api.twitter.com/1.1/statuses/retweets/21947795900469248.json
     * {
     *   "errors": [
     *     {
     *       "message": "Bad Authentication data",
     *       "code": 215
     *     }
     *   ]
     * }
     * @returns json
     */
    public function getAction()
    {
        return;
    }
}