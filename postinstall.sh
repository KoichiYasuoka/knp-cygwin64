#! /bin/sh -x
touch -r /usr/local/share/knp/dict/crf.model /usr/local/share/knp/rule/*
if cmp -s /usr/local/bin/knp /usr/local/bin/knp.exe
then :
else rm -f /usr/local/bin/knp
fi
exit 0
