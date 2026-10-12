<?php

namespace RobwOAuthVendor\OAuth2\TokenType;

use RobwOAuthVendor\OAuth2\RequestInterface;
use RobwOAuthVendor\OAuth2\ResponseInterface;

/**
* This is not yet supported!
*/
class Mac implements TokenTypeInterface
{
    public function getTokenType()
    {
        return 'mac';
    }

    public function getAccessTokenParameter(RequestInterface $request, ResponseInterface $response)
    {
        throw new \LogicException("Not supported");
    }
}
