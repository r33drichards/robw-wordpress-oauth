<?php
// TEST ONLY: never package/deploy this file. Local disposable Playground fixtures.
if(!defined('ROBW_OAUTH_LOCAL_TEST')||!ROBW_OAUTH_LOCAL_TEST)return;
add_filter('robw_oauth_repository_access',function($allow,$uid,$repo,$write){$u=get_user_by('login','alice');return $u && $uid===$u->ID && $repo==='owned';},10,4);
add_action('template_redirect',function(){if(($_SERVER['REQUEST_URI']??'')==='/__test__/login/alice'||($_SERVER['REQUEST_URI']??'')==='/__test__/login/bob'||($_SERVER['REQUEST_URI']??'')==='/__test__/login/admin'){$name=basename($_SERVER['REQUEST_URI']);$u=get_user_by('login',$name);wp_set_auth_cookie($u->ID);wp_redirect(home_url('/'));exit;}},-200);

add_action('template_redirect',function(){if(wp_parse_url($_SERVER['REQUEST_URI'],PHP_URL_PATH)==='/__test__/runtime'){header('Content-Type: application/json');echo wp_json_encode(['php'=>PHP_VERSION,'wordpress'=>$GLOBALS['wp_version']]);exit;}},-200);
