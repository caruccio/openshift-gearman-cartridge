OpenShift Gearman Job Server Cartridge
=================================
This cartridge provides an embedded [Gearman Job Server](http://gearman.org) for your application.

In order to create your application, first you need to register at Getup Cloud.
Go to http://getupcloud.com/#/sign-up and signup for free.
You receive a free 750h trial to test our services.

To add Gearman to your app, run from the terminal:

    rhc cartridge-add --app <app> https://reflector-getupcloud.getup.io/github/getupcloud/openshift-gearman-cartridge

Restart your app so it can see the environment variables from Gearman cartidge:

    rhc app-stop --app <app>
    rhc app-start --app <app>

Gearman address and port is found in the following variables:

    OPENSHIFT_GEARMAN_IP
    OPENSHIFT_GEARMAN_PORT
