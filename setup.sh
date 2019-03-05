#!/bin/bash
function setup_proto(){
    echo "Setting up protocol buffer python interfaces in ${PWD##*/}/net/proto"
    cd proto
    python -m grpc_tools.protoc -I. --python_out=../net/proto --grpc_python_out=../net/proto *.proto
    case $(uname -s) in # Need to rewrite imports because Python 3 and GRPC dont like each other
        Darwin*) sed -i -E 's/^\(import.*_pb2\)/from . \1/' ../net/proto/*.py;; #For Mac
        *) sed -i -E 's/^import.*_pb2/from . \0/' ../net/proto/*.py;; #For Linux
    esac
}


if hash protoc 2>/dev/null; then
    setup_proto
else
    echo "---------------"
    echo "    WARNING    "
    echo "---------------"
    echo "You must be in an environment where protoc is installed"
fi
