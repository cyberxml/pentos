var_accounts_password_warn_age_login_defs="7"
grep -q ^PASS_WARN_DAYS /etc/login.defs && \
  sed -i "s/PASS_WARN_DAYS.*/PASS_WARN_DAYS     $var_accounts_password_warn_age_login_defs/g" /etc/login.defs
if ! [ $? -eq 0 ]; then
    echo "PASS_WARN_DAYS      $var_accounts_password_warn_age_login_defs" >> /etc/login.defs
fi
