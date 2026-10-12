=== Robw OAuth ===
Contributors: r33drichards
Tags: oauth, oauth2, authentication, git
Requires at least: 6.5
Tested up to: 6.9
Requires PHP: 8.1
Stable tag: 0.1.0
License: GPLv2 or later
License URI: https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

Free WordPress OAuth authorization server for public desktop clients and repository integrations. Development release.

== Description ==
Authorization Code with mandatory PKCE-S256, explicit WordPress consent, rotating opaque tokens, revocation and a deny-by-default repository permission API. No paid feature gates or separate authentication backend. This is an OAuth provider, not a complete Git forge.

== Installation ==
Upload the robw-oauth directory as a plugin and activate it on a test site. Configure public clients under Settings > Git OAuth. Production requires HTTPS and separately verified repository integration, request limits, storage and deployment testing. Never install the separate test fixtures on a live site.

== Changelog ==
= 0.1.0 =
Initial development implementation. See project README and verification evidence for tested profile and open gates.
