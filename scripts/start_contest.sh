#!/bin/bash
# Usage: ./start_contest.sh Weekly_Contest_400
CONTEST_NAME=$1
if [ -z "$CONTEST_NAME" ]; then
    CONTEST_NAME="Contest_$(date +%Y-%m-%d)"
fi

mkdir -p leetcode/contests/"$CONTEST_NAME"
for prob in Q1 Q2 Q3 Q4; do
    cp templates/base.cpp leetcode/contests/"$CONTEST_NAME"/"$prob".cpp
done

echo "Successfully initialized $CONTEST_NAME with 4 problems."
