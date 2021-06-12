#!/usr/bin/env bash

# bash 쉘 공부 1일차.
# 무언가 잘 풀리지 않는다.

host="$1"
port="$2"
retry="$3"
attempt_num=1

until pg_isready -h "$host" -p "$port"; do
  (( attempt_num >= retry )) && {
   echo >&2 "connection failed"
   return 1
  }
  echo >&2 "failed"
  attempt_num=$(( attempt_num + 1 ))
  sleep 1
done

echo >&2 "$(date +%Y%m%dt%H%M%S) Postgres is up - executing command"
