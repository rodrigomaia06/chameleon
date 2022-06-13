#/bin/bash
TMP_FILE=".tmpdeck.txt"
DECK="deck.txt"
echo "Reshuffling deck..."
sleep 1
shuf $DECK > $TMP_FILE
cat $TMP_FILE > $DECK
rm -rf $TMP_FILE
