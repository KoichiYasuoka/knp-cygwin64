#! /bin/sh -x
case "`find share -name '*.xz' -print`" in
'') exit 0 ;;
esac
find share -name '*.xz.1' -print |
( while read F
  do Z=`expr $F : '\(.*\)\.1$'`
     cat $Z.[0-9] > $Z
  done
)
find share -name '*.xz' -print |
( while read Z
  do unxz $Z
  done
)
exit 0
