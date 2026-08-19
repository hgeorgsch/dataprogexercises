#!/usr/bin/env bash

set -euo pipefail

usage() {
  printf '%s\n' \
    "Bruk: $0 [--production | --staging]" \
    "" \
    "  --production  Bygg og publiser til /iira2001v2 (standard)" \
    "  --staging     Bygg og publiser til /iira2001v2-staging" \
    "  -h, --help    Vis denne hjelpen"
}

if (( $# > 1 )); then
  usage >&2
  exit 2
fi

case "${1:---production}" in
  --production)
    PUBLISH_DIRECTORY="iira2001v2"
    ;;
  --staging)
    PUBLISH_DIRECTORY="iira2001v2-staging"
    ;;
  -h|--help)
    usage
    exit 0
    ;;
  *)
    printf 'Ukjent argument: %s\n\n' "$1" >&2
    usage >&2
    exit 2
    ;;
esac

# MyST må kjenne publiseringskatalogen når interne lenker bygges.
PUBLISH_BASE_URL="/$PUBLISH_DIRECTORY"
PUBLISH_DESTINATION="login.ansatt.ntnu.no:/home/groupswww/iirevu/$PUBLISH_DIRECTORY/"

# Render Quarto-presentasjonene til statiske, selvstendige HTML-filer.
quarto render slides

# Bygg boken. Publisering skjer bare dersom bygget fullføres uten feil.
BASE_URL="$PUBLISH_BASE_URL" uv run jupyter book build --html

# Synkroniser den ferdige HTML-boken til NTNUs webområde.
printf 'Publiserer til https://iirevu.org.ntnu.no%s/\n' "$PUBLISH_BASE_URL"
rsync -av --delete \
  _build/html/ \
  "$PUBLISH_DESTINATION"
