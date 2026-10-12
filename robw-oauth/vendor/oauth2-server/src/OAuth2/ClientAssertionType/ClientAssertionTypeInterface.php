<?php

namespace RobwOAuthVendor\OAuth2\ClientAssertionType;

use RobwOAuthVendor\OAuth2\RequestInterface;
use RobwOAuthVendor\OAuth2\ResponseInterface;

/**
 * Interface for all OAuth2 Client Assertion Types
 */
interface ClientAssertionTypeInterface
{
    /**
     * Validate the OAuth request
     *
     * @param RequestInterface $request
     * @param ResponseInterface $response
     * @return mixed
     */
    public function validateRequest(RequestInterface $request, ResponseInterface $response);

    /**
     * Get the client id
     *
     * @return mixed
     */
    public function getClientId();
}
