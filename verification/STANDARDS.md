# Standards mapping and evidence boundaries

- RFC 6749 §§4.1,5.2: code flow, explicit consent, client/redirect binding, scope checks, token errors, no implicit/password grants.
- RFC 7636 §4 and Appendix B: mandatory S256, official published verifier/challenge vector, missing/malformed/wrong verifier rejection.
- RFC 8252 §7.3: public native-client loopback IP callback with variable port but bound host/path/query.
- RFC 6750 §§2.1,3: Bearer resource authentication/challenges. Git Basic credential transport is an additional RFC 7617 convention, not bearer-token-in-URL support.
- RFC 7009: revocation, unknown-token success, client binding, missing parameter rejection.
- RFC 8414: metadata lists only implemented grants/response types, public-client mode and S256.
- RFC 9700: avoids deprecated grants; exact callback binding, PKCE, replay protection, refresh rotation and family invalidation. This is not a blanket claim that all BCP deployment recommendations have been satisfied.

There is no asserted universal IETF OAuth certification for this implementation. OpenID Foundation OIDC/FAPI suites require profiles not implemented here; no result from those suites is reported. Official WordPress Plugin Check and upstream Git-helper tests are distinct evidence layers.

Final test reports must identify exact code hashes, environment, case outcomes, failures and skipped cases. Changes to protocol/storage code invalidate prior affected PASS. Missing/skipped/blocked tests are not PASS. Native MySQL/production TLS/Wasmer, real Git repository clone/push, full load testing and independent oracle/security authority remain separate gates.
