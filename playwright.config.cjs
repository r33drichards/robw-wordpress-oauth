const {defineConfig}=require('@playwright/test');
module.exports=defineConfig({testDir:'./tests',testMatch:'*.spec.cjs',workers:1,timeout:45000,retries:0,reporter:[['list']],use:{baseURL:'http://127.0.0.1:9400',headless:true,trace:'off',video:'off',screenshot:'off',launchOptions:{executablePath:process.env.CHROMIUM_PATH||undefined,args:['--no-sandbox']}}});
