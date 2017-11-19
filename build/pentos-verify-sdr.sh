
# -------------------------------------------------
# rtl-sdr
# -------------------------------------------------
# no help or version
# check on error return
rtl_sdr > /dev/null 2>&1
result=$?
if [ $result -eq 1 ]; then
    echo "[P] rtl_sdr"
else
    echo "[F] rtl_sdr"
fi

# -------------------------------------------------
# kalibrate-rtl
# -------------------------------------------------
kal-rtl -h > /dev/null 2>&1
result=$?
if [ $result -eq 255 ]; then
    echo "[P] kal-rtl"
else
    echo "[F] kal-rtl"
fi

# -------------------------------------------------
# hackrf
# -------------------------------------------------
result=$(find /usr/src/kernels -name hackrf | wc -l)
if [ $result -gt 0 ]; then
    echo "[P] hackrf"
else
    echo "[F] hackrf"
fi

# -------------------------------------------------
# airspyone
# -------------------------------------------------
airspy_info > /dev/null 2>&1
result=$?
if [ $result -eq 0 ]; then
    echo "[P] airspyone"
else
    echo "[F] airspyone"
fi

# -------------------------------------------------
# libosmocore
# -------------------------------------------------
osmo-arfcn > /dev/null 2>&1
result=$?
if [ $result -eq 2 ]; then
    echo "[P] libosmocore"
else
    echo "[F] libosmocore"
fi

# -------------------------------------------------
# gnuradio
# -------------------------------------------------
gnuradio-config-info -v > /dev/null 2>&1
result=$?
if [ $result -eq 0 ]; then
    echo "[P] gnuradio"
else
    echo "[F] gnuradio"
fi

# -------------------------------------------------
# grgsm
# -------------------------------------------------
export PYTHONPATH=${PYTHONPATH}:/usr/local/lib64/python2.7/site-packages
grgsm_decode -bv > /dev/null 2>&1
result=$?
if [ $result -eq 0 ]; then
    echo "[P] grgsm"
else
    echo "[F] grgsm"
fi

# -------------------------------------------------
# osmocom
# -------------------------------------------------
osmocom_siggen_nogui -h > /dev/null 2>&1
result=$?
if [ $result -eq 0 ]; then
    echo "[P] osmocom"
else
    echo "[F] osmocom"
fi

# -------------------------------------------------
# gqrx (assumes root runs but cant open display)
# -------------------------------------------------
gqrx -h > /dev/null 2>&1
result=$?
if [ $result -eq 134 ]; then
    echo "[P] gqrx"
else
    echo "[F] gqrx"
fi

# -------------------------------------------------
# dump1090
# -------------------------------------------------
dump1090 -h > /dev/null 2>&1
result=$?
if [ $result -eq 1 ]; then
    echo "[P] dump1090"
else
    echo "[F] dump1090"
fi

# -------------------------------------------------
# rtl-ais
# -------------------------------------------------
rtl_ais -h > /dev/null 2>&1
result=$?
if [ $result -eq 1 ]; then
    echo "[P] rtl_ais"
else
    echo "[F] rtl_ais"
fi

# -------------------------------------------------
# rtl-biast
# -------------------------------------------------
rtl_biast > /dev/null 2>&1
result=$?
if [ $result -eq 1 ]; then
    echo "[P] rtl_biast"
else
    echo "[F] rtl_biast"
fi

# -------------------------------------------------
# gnss-sdr
# -------------------------------------------------
gnss-sdr > /dev/null 2>&1
result=$?
if [ $result -eq 1 ]; then
    echo "[P] gnss-sdr"
else
    echo "[F] gnss-sdr"
fi

# -------------------------------------------------
# xastir
# -------------------------------------------------
xastir -h > /dev/null 2>&1
result=$?
if [ $result -eq 0 ]; then
    echo "[P] xastir"
else
    echo "[F] xastir"
fi

# -------------------------------------------------
# multimon-ng
# -------------------------------------------------
multimon-ng -h > /dev/null 2>&1
result=$?
if [ $result -eq 2 ]; then
    echo "[P] multimon-ng"
else
    echo "[F] multimon-ng"
fi

# -------------------------------------------------
# freqwatch
# -------------------------------------------------
freqwatch.py > /dev/null 2>&1
result=$?
if [ $result -eq 1 ]; then
    echo "[P] freqwatch"
else
    echo "[F] freqwatch"
fi


