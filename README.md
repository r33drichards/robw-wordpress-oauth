# Robw OAuth — free WordPress OAuth server

GPL-2.0-or-later; PHP 8.1+. No paid edition, external auth service, SSH listener, PAT creation, signing-key provisioning, or native PHP subprocess required by the plugin.

**Development release, not a complete Git forge.** This package implements authentication and authorization. Git object storage, smart HTTP clone/push and webhooks are not implemented. The test repository consumer is a deliberately isolated fixture, not Git engine E2E.

## Repository boundary

This repository is **OAuth authentication and authorization only**. It does not contain a Git forge, repository storage, clone/push engine, issue tracker, or webhook delivery implementation.

The separate [Robw WordPress Git Forge](https://github.com/r33drichards/robw-wordpress-forge) plugin owns those features and consumes this provider through `robw_oauth_principal` and the `robw_oauth_repository_access` filter. Install and review each plugin independently; no forge backend is bundled here. Forge development status and transport/storage evidence belong in that repository.

The `repo:read` / `repo:write` scopes and repository-access hook are an integration contract, not an embedded forge. Test consumers here remain fixtures.

## Implemented profile

- Public desktop clients, registered by WordPress administrators (Settings → Git OAuth).
- Authorization Code with mandatory PKCE-S256, nonempty opaque state, and explicit consent tied to a WordPress nonce and a single-use, five-minute ticket.
- Exact HTTPS callback matching. Literal loopback IP HTTP callbacks may vary their port, per RFC 8252; path/query/host remain bound.
- One-use, 60-second authorization codes; five-minute opaque access tokens; rotating refresh tokens bounded by a 24-hour grant lifetime.
- SHA-256 token/code lookup keys; no plaintext authorization codes, access tokens or refresh tokens in persisted OAuth state. No JWTs or private signing keys.
- Database compare-and-swap, not filesystem locks or stale object-cache reads. Refresh/code replay revokes the grant family; expiry, account permissions and client revocation are checked on resource access.
- OAuth error mapping, no-store responses, bounded form input, parameter ambiguity rejection, nonce-protected client management.
- Dependency isolation: namespaced, MIT-licensed bshaffer/oauth2-server-php 1.14.2, exact upstream commit/archive recorded in vendor/manifest.json.

The current pilot store uses one autoload-disabled wp_options row, capped at 8 MiB with expiry cleanup. This is intentionally bounded but serializes mutations; a high-volume installation needs separately reviewed storage and deployment load tests. Configure upstream request limits/rate limiting and trusted HTTPS proxy handling before production. Multisite/subdirectory discovery and native production MySQL/Wasmer acceptance remain outside the tested profile.

## WordPress / Git integration

Endpoints under /robw-oauth/: authorize, token, revoke, resource. Discovery: /.well-known/oauth-authorization-server.

A forge integration calls robw_oauth_principal(authorizationHeader, repositoryID, isWrite), rejects WP_Error, and enforces the returned principal before every Git operation. Register robw_oauth_repository_access to check real repository ACLs: **the default is deny**. This plugin never treats WordPress cookies as sufficient Git API credentials.

Bearer authentication follows RFC 6750. For Git HTTPS credential helpers, Basic username oauth2 / password OAuth access token is also supported. Password grants, client-credentials grants, implicit grants, device flow, OIDC, FAPI and dynamic client registration are not supported or advertised.

Example helper configuration (not a deployed URL):

    git config --global --add credential.helper oauth
    git config --global credential.https://code.example.test.oauthClientId robw-git
    git config --global credential.https://code.example.test.oauthScopes "repo:read repo:write"
    git config --global credential.https://code.example.test.oauthAuthURL /robw-oauth/authorize
    git config --global credential.https://code.example.test.oauthTokenURL /robw-oauth/token

Install git-credential-oauth separately on the client, and configure an OS credential manager before it. Register its loopback callback (default http://127.0.0.1, without a path) in WordPress. Production HTTP OAuth endpoints are rejected; only explicit local-test mode with a loopback canonical WordPress URL permits HTTP.

## Testing

Node >=24.18 and npm >=11.16; npm ci; npm audit --audit-level=moderate; npm test. See tools/test.cjs, tests/blueprint.json, tests/oauth.spec.cjs and verification/ for the final evidence.

Uses the official WordPress Playground distribution, a real Chromium browser, real loopback callbacks, and actual HTTP requests. Concurrent redemption is exercised against two PHP workers. A separate test drives actual git credential fill with pinned upstream git-credential-oauth, browser PKCE consent, authenticated HTTP read/write authorization and revocation. Maintainer Go tests are run separately.

**Tests demonstrate covered properties; they do not prove absence of every vulnerability.** RFC vectors/requirements and upstream tests are not an IETF certificate. This is not OIDC/FAPI-certified. Official WordPress Plugin Check is a separate packaging/static-analysis gate, not an OAuth security certificate. Unrun gates must remain NOT_RUN/BLOCKED, not PASS.

Never deploy tests/mu or define ROBW_OAUTH_LOCAL_TEST on a production site. Test fixtures contain local-only login/state controls and are excluded from the install ZIP. Never enable traces, credential dumps or cookie snapshots during OAuth tests.

### Runtime evidence correction

The historical 53-case run passed, but its WordPress 6.9 / PHP 8.3 labels came from CLI configuration, not runtime assertions. During separate forge development, a supplied Blueprint was observed using default runtime tracks despite the CLI banner. Those old labels are **not verified compatibility evidence**; the report now marks them configured/unverified. The reproduction runner now pins preferred versions inside the Blueprint and checks actual runtime versions. A fresh OAuth-only version-pinned run is still pending; forge integration tests are not substituted for this provider’s own suite.
