#!/usr/bin/env bash
set -euo pipefail
echo "Traitement (conversion latin1 vers utf8) des fichiers suivants :"
find . -name *.tex | while read f
do
	if file --mime-encoding "$f" | grep utf ; then
		echo "$f : déjà en utf-8"
	fi

	if file --mime-encoding "$f" | grep iso-8859 ; then
		echo "$f : conversion latin1 vers utf8"
		# if test -f "$f.latin1"
		# then
		# 	cp "$f.latin1" "$f.latin1.bak"
		# fi
		gfile=$(basename "$f" | sed -e 's/(.*)//' -e 's/ //g')
		gdir=$(dirname "$f")
		g="$gdir/$gfile"
		iconv -f latin1 -t utf-8 "$f" > "$g"
		# Change LaTeX inputenc option
		sed -i -e "s:latin1:utf8:" "$g"
	fi
done
echo "Fin du traitement."
