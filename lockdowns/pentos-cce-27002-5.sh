var_accounts_password_minlen_login_defs="14"
grep -q ^PASS_MIN_LEN /etc/login.defs && \
  sed -i "s/PASS_MIN_LEN.*/PASS_MIN_LEN     $var_accounts_password_minlen_login_defs/g" /etc/login.defs
if ! [ $? -eq 0 ]; then
    echo "PASS_MIN_LEN      $var_accounts_password_minlen_login_defs" >> /etc/login.defs
fi

