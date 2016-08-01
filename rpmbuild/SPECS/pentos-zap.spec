Name:           pentos-zap
Version:        2.5.0
Release:        0
Summary:        pentos-zap
Group:          Applications/Other
License:        GPL
URL:            https://github.com/zaproxy/zaproxy/releases/download/2.4.3/ZAP_2.5.0_Linux.tar.gz
Vendor:         OWASP Zed Attack Proxy
Source:         pentos-zap-2.5.0.tar.gz
Prefix:         %{_prefix}
Packager: 	cyberxml
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
The OWASP Zed Attack Proxy (ZAP) is one of the world’s most popular free security tools and is actively maintained by hundreds of international volunteers*. It can help you automatically find security vulnerabilities in your web applications while you are developing and testing your applications. Its also a great tool for experienced pentesters to use for manual security testing.

%prep
%setup -q

%build

%install
mkdir -p "$RPM_BUILD_ROOT/usr/local/pentos/apps/zap"
cp -R * "$RPM_BUILD_ROOT/usr/local/pentos/apps/zap"

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
/usr/local/pentos/apps/zap/README
/usr/local/pentos/apps/zap/db/db.properties
/usr/local/pentos/apps/zap/db/hsqldb.properties
/usr/local/pentos/apps/zap/db/mysql.properties
/usr/local/pentos/apps/zap/db/mysql.schema
/usr/local/pentos/apps/zap/db/zapdb.properties
/usr/local/pentos/apps/zap/db/zapdb.script
/usr/local/pentos/apps/zap/filter/dummy.txt
/usr/local/pentos/apps/zap/lang/Messages.properties
/usr/local/pentos/apps/zap/lang/Messages_ar_SA.properties
/usr/local/pentos/apps/zap/lang/Messages_az_AZ.properties
/usr/local/pentos/apps/zap/lang/Messages_bn_BD.properties
/usr/local/pentos/apps/zap/lang/Messages_bs_BA.properties
/usr/local/pentos/apps/zap/lang/Messages_da_DK.properties
/usr/local/pentos/apps/zap/lang/Messages_de_DE.properties
/usr/local/pentos/apps/zap/lang/Messages_el_GR.properties
/usr/local/pentos/apps/zap/lang/Messages_es_ES.properties
/usr/local/pentos/apps/zap/lang/Messages_fa_IR.properties
/usr/local/pentos/apps/zap/lang/Messages_fil_PH.properties
/usr/local/pentos/apps/zap/lang/Messages_fr_FR.properties
/usr/local/pentos/apps/zap/lang/Messages_hi_IN.properties
/usr/local/pentos/apps/zap/lang/Messages_hr_HR.properties
/usr/local/pentos/apps/zap/lang/Messages_hu_HU.properties
/usr/local/pentos/apps/zap/lang/Messages_id_ID.properties
/usr/local/pentos/apps/zap/lang/Messages_it_IT.properties
/usr/local/pentos/apps/zap/lang/Messages_ja_JP.properties
/usr/local/pentos/apps/zap/lang/Messages_ko_KR.properties
/usr/local/pentos/apps/zap/lang/Messages_mk_MK.properties
/usr/local/pentos/apps/zap/lang/Messages_ms_MY.properties
/usr/local/pentos/apps/zap/lang/Messages_nb_NO.properties
/usr/local/pentos/apps/zap/lang/Messages_nl_NL.properties
/usr/local/pentos/apps/zap/lang/Messages_pl_PL.properties
/usr/local/pentos/apps/zap/lang/Messages_pt_BR.properties
/usr/local/pentos/apps/zap/lang/Messages_ro_RO.properties
/usr/local/pentos/apps/zap/lang/Messages_ru_RU.properties
/usr/local/pentos/apps/zap/lang/Messages_si_LK.properties
/usr/local/pentos/apps/zap/lang/Messages_sk_SK.properties
/usr/local/pentos/apps/zap/lang/Messages_sl_SI.properties
/usr/local/pentos/apps/zap/lang/Messages_sq_AL.properties
/usr/local/pentos/apps/zap/lang/Messages_sr_CS.properties
/usr/local/pentos/apps/zap/lang/Messages_sr_SP.properties
/usr/local/pentos/apps/zap/lang/Messages_tr_TR.properties
/usr/local/pentos/apps/zap/lang/Messages_uk_UA.properties
/usr/local/pentos/apps/zap/lang/Messages_ur_PK.properties
/usr/local/pentos/apps/zap/lang/Messages_zh_CN.properties
/usr/local/pentos/apps/zap/lang/vulnerabilities.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_ar_SA.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_az_AZ.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_bn_BD.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_bs_BA.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_da_DK.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_de_DE.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_el_GR.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_es_ES.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_fa_IR.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_fil_PH.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_fr_FR.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_hi_IN.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_hr_HR.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_hu_HU.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_id_ID.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_it_IT.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_ja_JP.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_ko_KR.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_mk_MK.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_ms_MY.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_nb_NO.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_nl_NL.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_pl_PL.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_pt_BR.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_ro_RO.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_ru_RU.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_si_LK.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_sk_SK.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_sl_SI.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_sq_AL.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_sr_CS.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_sr_SP.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_tr_TR.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_uk_UA.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_ur_PK.xml
/usr/local/pentos/apps/zap/lang/vulnerabilities_zh_CN.xml
/usr/local/pentos/apps/zap/lib/BrowserLauncher2-1_3.jar
/usr/local/pentos/apps/zap/lib/JBroFuzz.jar
/usr/local/pentos/apps/zap/lib/JBroFuzzEncoder.jar
/usr/local/pentos/apps/zap/lib/ant.jar
/usr/local/pentos/apps/zap/lib/bcmail-jdk15on-152.jar
/usr/local/pentos/apps/zap/lib/bcpkix-jdk15on-152.jar
/usr/local/pentos/apps/zap/lib/bcprov-jdk15on-152.jar
/usr/local/pentos/apps/zap/lib/commons-beanutils-1.8.3.jar
/usr/local/pentos/apps/zap/lib/commons-codec-1.9.jar
/usr/local/pentos/apps/zap/lib/commons-collections-3.2.2.jar
/usr/local/pentos/apps/zap/lib/commons-configuration-1.9.jar
/usr/local/pentos/apps/zap/lib/commons-csv-1.1.jar
/usr/local/pentos/apps/zap/lib/commons-httpclient-3.1.jar
/usr/local/pentos/apps/zap/lib/commons-jxpath-1.3.jar
/usr/local/pentos/apps/zap/lib/commons-lang-2.6.jar
/usr/local/pentos/apps/zap/lib/commons-logging-1.2.jar
/usr/local/pentos/apps/zap/lib/commons-logging-api-1.1.1.jar
/usr/local/pentos/apps/zap/lib/diffutils-1.2.1.jar
/usr/local/pentos/apps/zap/lib/ezmorph-1.0.6.jar
/usr/local/pentos/apps/zap/lib/harlib-jackson-1.1.2.jar
/usr/local/pentos/apps/zap/lib/hsqldb.jar
/usr/local/pentos/apps/zap/lib/httpclient-4.5.jar
/usr/local/pentos/apps/zap/lib/httpcore-4.4.1.jar
/usr/local/pentos/apps/zap/lib/java-semver-0.8.0.jar
/usr/local/pentos/apps/zap/lib/jdom.jar
/usr/local/pentos/apps/zap/lib/jericho-html-3.1.jar
/usr/local/pentos/apps/zap/lib/jfreechart-1.0.13.jar
/usr/local/pentos/apps/zap/lib/jfxrt.jar
/usr/local/pentos/apps/zap/lib/jgrapht-core-0.9.0.jar
/usr/local/pentos/apps/zap/lib/jh.jar
/usr/local/pentos/apps/zap/lib/json-lib-2.4-jdk15.jar
/usr/local/pentos/apps/zap/lib/log4j-1.2.17.jar
/usr/local/pentos/apps/zap/lib/rsyntaxtextarea-2.5.8.jar
/usr/local/pentos/apps/zap/lib/sqlite-jdbc-3.8.11.1.jar
/usr/local/pentos/apps/zap/lib/swingx-all-1.6.4.jar
/usr/local/pentos/apps/zap/lib/xom-1.2.10.jar
/usr/local/pentos/apps/zap/license/ApacheLicense-2.0.txt
/usr/local/pentos/apps/zap/license/COPYING
/usr/local/pentos/apps/zap/license/RSyntaxTextArea.License.txt
/usr/local/pentos/apps/zap/license/TheClarifiedArtisticLicense.htm
/usr/local/pentos/apps/zap/license/TheClarifiedArtisticLicense.rtf
/usr/local/pentos/apps/zap/license/gpl-2.0.txt
/usr/local/pentos/apps/zap/license/hsqldb_lic.txt
/usr/local/pentos/apps/zap/license/hypersonic_lic.txt
/usr/local/pentos/apps/zap/license/lgpl-3.0.txt
/usr/local/pentos/apps/zap/log/dummy.txt
/usr/local/pentos/apps/zap/plugin/Readme.txt
/usr/local/pentos/apps/zap/plugin/alertFilters-beta-3.zap
/usr/local/pentos/apps/zap/plugin/ascanrules-release-23.zap
/usr/local/pentos/apps/zap/plugin/bruteforce-beta-5.zap
/usr/local/pentos/apps/zap/plugin/coreLang-release-10.zap
/usr/local/pentos/apps/zap/plugin/diff-beta-6.zap
/usr/local/pentos/apps/zap/plugin/directorylistv1-release-3.zap
/usr/local/pentos/apps/zap/plugin/fuzz-beta-5.zap
/usr/local/pentos/apps/zap/plugin/gettingStarted-release-5.zap
/usr/local/pentos/apps/zap/plugin/help-release-6.zap
/usr/local/pentos/apps/zap/plugin/invoke-beta-3.zap
/usr/local/pentos/apps/zap/plugin/onlineMenu-release-4.zap
/usr/local/pentos/apps/zap/plugin/pscanrules-release-16.zap
/usr/local/pentos/apps/zap/plugin/quickstart-release-18.zap
/usr/local/pentos/apps/zap/plugin/reveal-release-2.zap
/usr/local/pentos/apps/zap/plugin/saverawmessage-release-3.zap
/usr/local/pentos/apps/zap/plugin/scripts-beta-16.zap
/usr/local/pentos/apps/zap/plugin/selenium-release-5.zap
/usr/local/pentos/apps/zap/plugin/spiderAjax-release-15.zap
/usr/local/pentos/apps/zap/plugin/tips-beta-5.zap
/usr/local/pentos/apps/zap/plugin/websocket-release-11.zap
/usr/local/pentos/apps/zap/plugin/zest-beta-21.zap
"/usr/local/pentos/apps/zap/scripts/templates/active/Active default template.js"
"/usr/local/pentos/apps/zap/scripts/templates/authentication/Authentication default template.js"
"/usr/local/pentos/apps/zap/scripts/templates/authentication/BodgeIt Store Authentication.js"
"/usr/local/pentos/apps/zap/scripts/templates/authentication/Simple Form-Based Authentication.js"
"/usr/local/pentos/apps/zap/scripts/templates/authentication/Wordpress Authentication.js"
"/usr/local/pentos/apps/zap/scripts/templates/httpsender/HttpSender default template.js"
"/usr/local/pentos/apps/zap/scripts/templates/passive/Passive default template.js"
"/usr/local/pentos/apps/zap/scripts/templates/proxy/Proxy default template.js"
"/usr/local/pentos/apps/zap/scripts/templates/standalone/Loop through history table.js"
"/usr/local/pentos/apps/zap/scripts/templates/standalone/Standalone default template.js"
"/usr/local/pentos/apps/zap/scripts/templates/standalone/Traverse sites tree.js"
"/usr/local/pentos/apps/zap/scripts/templates/targeted/Find HTML comments.js"
"/usr/local/pentos/apps/zap/scripts/templates/targeted/Targeted default template.js"
"/usr/local/pentos/apps/zap/scripts/templates/variant/Input Vector default template.js"
"/usr/local/pentos/apps/zap/scripts/templates/variant/Input Vector sharp query separator.js"
/usr/local/pentos/apps/zap/session/dummy.txt
/usr/local/pentos/apps/zap/xml/alert.dtd
/usr/local/pentos/apps/zap/xml/alert.xml
/usr/local/pentos/apps/zap/xml/alertDef.dtd
/usr/local/pentos/apps/zap/xml/alertDef.xml
/usr/local/pentos/apps/zap/xml/chrome-user-agents.txt
/usr/local/pentos/apps/zap/xml/common-user-agents.txt
/usr/local/pentos/apps/zap/xml/config.dtd
/usr/local/pentos/apps/zap/xml/config.xml
/usr/local/pentos/apps/zap/xml/drivers.dtd
/usr/local/pentos/apps/zap/xml/drivers.xml
/usr/local/pentos/apps/zap/xml/firefox-user-agents.txt
/usr/local/pentos/apps/zap/xml/internet-explorer-user-agents.txt
/usr/local/pentos/apps/zap/xml/log4j.properties
/usr/local/pentos/apps/zap/xml/report.html.xsl
/usr/local/pentos/apps/zap/xml/report.xml.xsl
/usr/local/pentos/apps/zap/xml/reportCompare.xsl
/usr/local/pentos/apps/zap/xml/safari-user-agents.txt
/usr/local/pentos/apps/zap/xml/scanPolicy.xml
/usr/local/pentos/apps/zap/xml/session.dtd
/usr/local/pentos/apps/zap/xml/session.xml
/usr/local/pentos/apps/zap/xml/test.xml
/usr/local/pentos/apps/zap/xml/untitledsession.xml
/usr/local/pentos/apps/zap/zap-2.5.0.jar
/usr/local/pentos/apps/zap/zap.bat
/usr/local/pentos/apps/zap/zap.ico
/usr/local/pentos/apps/zap/zap.sh

%changelog
