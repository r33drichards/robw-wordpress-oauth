<?php
/**
 * Plugin Name: Robw OAuth
 * Description: Free OAuth 2.0 authorization server for WordPress integrations. Development release.
 * Version: 0.1.0
 * Requires PHP: 8.1
 * License: GPL-2.0-or-later
 */
defined('ABSPATH') || exit;
spl_autoload_register(function($class){$prefix='RobwOAuthVendor'.chr(92).'OAuth2'.chr(92);if(str_starts_with($class,$prefix)){$path=__DIR__.'/vendor/oauth2-server/src/OAuth2/'.str_replace(chr(92),'/',substr($class,strlen($prefix))).'.php';if(is_file($path))require_once $path;}});
require_once __DIR__.'/src/server.php';
require_once __DIR__.'/src/http.php';
add_action('template_redirect', 'robw_oauth_route', -100);
add_action('admin_menu', function () { add_options_page('Git OAuth','Git OAuth','manage_options','robw-oauth','robw_oauth_admin'); });
