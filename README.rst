!IMPORTANT
==========

The product is broken! It runs on Python 3.8, but it got obsolete with Plone 5.2! It might work with Plone 5.1.

The skin based login has been removed and got replaced by a browser page based login - see `Products.CMFPlone commit 76d03441 <https://github.com/plone/Products.CMFPlone/commit/76d0344187c9d9c039086dad2ee375489ba81915#diff-3c31a803000849eed0e811268665c75c12ba307957800f2242bff775765998de>`_. ``portal_skins/plone_login`` is now gone, see `PLIP #2092 <https://github.com/plone/Products.CMFPlone/issues/2092>`_. The missing ``portal_skins/plone_login`` of course mean the ```login_form_validate`` <https://github.com/plone/Products.CMFPlone/blob/8635459222bbf3bc5401edcc8ba19d8400eada0d/Products/CMFPlone/skins/plone_login/login_form_validate.vpy>`_ is gone too, as a reasult the login portlet produces an error.

Possible solution to provide a layer based override for the login page.


Introduction
============

``collective.pluggablelogin`` overrides the standard Plone login form
with a template using a portlet manager, so that various login
components can be configured.

.. image:: https://github.com/collective/collective.pluggablelogin/raw/master/screenshot.png


Configuration
-------------

Go to the Addons control panel and activate "Pluggable Login Page."

Now if you go to ``/login`` while logged in as a Manager, you'll see a
"Manage portlets" link which you can use to manage the available
login portlets. By default, the standard login portlet and a
registration form portlet are enabled (the latter is only shown
if self registration is enabled for the site).

As well as manual assignment via the web interface, the pluggable login
page can also be assigned portlets via GenericSetup, in the same way
as Plone's other portlet managers can. For example, to register a custom
porlet on the pluggable login page, use this an example within ``portlets.xml``
inside a GenericSetup profile:

.. code:: xml

    <portlets
        xmlns:i18n="http://xml.zope.org/namespaces/i18n"
        i18n:domain="plone">
     <assignment 
        name="navigation"
        category="context"
        key="/"
        manager="collective.pluggablelogin"
        type="my.product.portlets.CustomLoginPortlet"
        insert-before="*"
        visible="True">
        <property name="title">string:Login portlet title</property>
        <property name="description">string:Example property</property>
     </assignment>
    </portlets>


Credits
=======

Developed by David Glick and `Groundwire Consulting
<http://groundwireconsulting.com>`_. Sponsored by the `Innocence Project
<http://www.innocenceproject.org/>`_.


To-do
=====

* Refactor inline styles on the logged in or out views.
