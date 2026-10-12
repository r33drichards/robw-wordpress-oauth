# Security / release gates

No live-site deployment has been performed. Treat 0.1.0 as a reviewed-development candidate, not a production assurance claim.

Production gates include native WordPress/MySQL/Wasmer compatibility, trusted HTTPS termination, request/rate limits, backup/restore and load tests, independent security review, and actual forge ACL/Git transport integration. WordPress Plugin Check findings are recorded separately and must not be silently waived. Official OIDC/FAPI certification is not claimed; those profiles are not implemented.

Only registered callbacks are redirected to. PKCE-S256 and raw redirect binding are mandatory. Secrets are never placed in resource URLs; request/response traces and credential logging must be disabled. Authorize callbacks necessarily carry a short-lived one-use code under the OAuth standard; no-store/no-referrer reduce retention.

WordPress administrators can register/delete public clients. Account sessions and WordPress nonce validation protect consent and administration. A public client identifier is not a secret or proof of user identity. Every resource access uses a valid token, current user status, current client scope policy and the consumer's repository ACL; deny-by-default is intentional.

OAuth database state bypasses WordPress option caches using prepared fresh reads and atomic BINARY compare-and-swap. Access/code/refresh secrets are indexed only by SHA-256; grant-family IDs cannot authenticate on their own. No private keys or OAuth client secrets are needed for the supported profile.

Test-only mu plugins provide controlled local actors and expiry/permission fixtures. They are never part of the plugin artifact. The browser E2E suite uses real consent and callback navigation, not mocked token issuance. The resource consumer is a fixture and is not evidence of actual Git clone/push correctness.
