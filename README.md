RESTful api documentation generation script
===================

script to generate restful api documentation out of annotated php code. [Output example you can find here](http://htmlpreview.github.io/?https://raw.github.com/dzhibas/rest-api-doc/master/documentation.html)

annotation example

    /**
     * @route /v1/modulename/authentication
     * @method POST
     * @ingroup modulename
     *
     * authentication service example
     *
     * HTTP response code tells about status of login:
     *
     * - 202: Request Accepted
     * - 401: Invalid username/password
     * - 403: Request Denied
     * - 503: Service Unavailable
     *
     * @example input
     *
     * POST /v1/modulename/authentication HTTP/1.1
     * Content-Type: application/json; charset=utf-8
     *
     * {
     *  "username": "demousername",
     *  "passwrod": "demopassword",
     * }
     *
     * @example output
     *
     * {
     *  "message":"Request Accepted",
     *  "id":386
     * }
     *
     * @jsonparam username extranet username required
     * @jsonparam password extranet password required
     *
     * @returns json
     */

Installation
==
pip install -r requirements.txt

Usage
==
$ python parse.py -c

Help
==
    usage: parse.py [-h] [-c] [-d DIR] [--filter FILTER] [-o OUTPUT]

    optional arguments:
      -h, --help            show this help message and exit
      -c, --coverage        ouputs into stdin documentation coverage
      -d DIR, --dir DIR     folder in which we need look for documentation
                            annotation. default: test_src_folder/
      --filter FILTER       gob filter in which files to search. default:
                            *Controler*.php
      -o OUTPUT, --output OUTPUT
                            output filename. default: documentation.html

open generated documentation.html
